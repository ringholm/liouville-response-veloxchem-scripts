from mpi4py import MPI
import veloxchem as vlx
import sys
import numpy as np
import random
import copy
import L2
import L3

# Dirac delta fn
def drc(i, j):
	if (i == j):
		return 1
	else:
		return 0
		
# AO to MO basis transformation
def ao2mo(mo, A):
	return np.linalg.multi_dot([mo.T, A, mo])

# Test system setup
molecule_string = """
    O 0 0 0
    H 1.0 0.7 0
    H 1.0 -0.7 0"""

basis_set_label = 'STO-3G'

scf_settings = {'conv_thresh': 1.0e-6}
method_settings = {}

comm = MPI.COMM_WORLD
ostream = vlx.OutputStream(sys.stdout)

molecule = vlx.Molecule.read_str(molecule_string, units='angs')
basis = vlx.MolecularBasis.read(molecule, basis_set_label)

ostream.print_block(molecule.get_string())
ostream.print_block(basis.get_string('Atomic Basis', molecule))
ostream.flush()

# SCF calculation

# Do SCF again with non-custom routine
scfdrv = vlx.ScfRestrictedDriver(comm, ostream)
scfdrv.update_settings(scf_settings, method_settings)
scfdrv.compute(molecule, basis)

MOs = scfdrv.scf_tensors['C']
F = scfdrv.scf_tensors['F'][0]

# AO integrals (pq|rs)
n_ao = MOs.shape[0]
pqrs = np.zeros((n_ao, n_ao, n_ao, n_ao))

eri_drv = vlx.ElectronRepulsionIntegralsDriver(comm)
eri_drv.compute_in_mem(molecule, basis, pqrs)

# MO integrals (tu|vw), chemists' notation
tqrs = np.einsum('pqrs,pt->tqrs', pqrs, MOs, optimize=True)
del pqrs
turs = np.einsum('tqrs,qu->turs', tqrs, MOs, optimize=True)
del tqrs
tuvs = np.einsum('turs,rv->tuvs', turs, MOs, optimize=True)
del turs
tuvw = np.einsum('tuvs,sw->tuvw', tuvs, MOs, optimize=True)
del tuvs


H00 = scfdrv.old_energy

# Setup for linear response to get RHS for integrals
ref_freqs = [0.14]
ref_freqs_str = [str(x) for x in ref_freqs]

# Doing calculation with custom routine, stops at RHS
lr_solver = vlx.LinearResponseSolver(comm, ostream)
lr_solver.update_settings(
{
'frequencies': ','.join(ref_freqs_str),
}, method_settings)


# My RHS
RHS = lr_solver.get_prop_grad('dipole', 'xyz', molecule,
                                   basis, scfdrv.scf_tensors)

# Transition integrals
V0n_x = RHS[0][:RHS[0].shape[0]//2]
V0n_y = RHS[1][:RHS[1].shape[0]//2]
V0n_z = RHS[2][:RHS[2].shape[0]//2]

# "Proper" RHS
RHS_0 = RHS[0]
RHS_1 = RHS[1]
RHS_2 = RHS[2]

# Reference damped response data
damp_param = 0.005

cpp_solver_ref = vlx.ComplexResponse(comm, ostream)
cpp_solver_ref.update_settings(
{
'frequencies': ','.join(ref_freqs_str),
'damping': damp_param}, method_settings)
cpp_ref_dict = cpp_solver_ref.compute(molecule, basis,
                               scfdrv.scf_tensors)


# MO 2-electron integrals (curr. only used to get n_occ, n_virt)
moints_drv = vlx.MOIntegralsDriver(comm, ostream)
ovov = moints_drv.compute_in_mem(molecule, basis, scfdrv.mol_orbs, "OVOV")

n_occ = ovov.shape[0]
n_virt = ovov.shape[1]
n_ex = n_occ * n_virt

# Dipole moment integrals
dipole_drv = vlx.ElectricDipoleIntegralsDriver(comm)
dipole_mats = dipole_drv.compute(molecule, basis)

dipole_x = dipole_mats.x_to_numpy()
dipole_y = dipole_mats.y_to_numpy()
dipole_z = dipole_mats.z_to_numpy()

np.set_printoptions(precision=5, suppress=True, linewidth=132) 

dipole_x_a = np.einsum('pq,pt->tq', dipole_x, MOs, optimize=True)
dipole_x_ab = np.einsum('tq,qu->tu', dipole_x_a, MOs, optimize=True)

dipole_y_a = np.einsum('pq,pt->tq', dipole_y, MOs, optimize=True)
dipole_y_ab = np.einsum('tq,qu->tu', dipole_y_a, MOs, optimize=True)

dipole_z_a = np.einsum('pq,pt->tq', dipole_z, MOs, optimize=True)
dipole_z_ab = np.einsum('tq,qu->tu', dipole_z_a, MOs, optimize=True)

V_mn_x = np.zeros((n_ex, n_ex))
V_mn_y = np.zeros((n_ex, n_ex))
V_mn_z = np.zeros((n_ex, n_ex))

# Ground-state dipole moment components
V_00_x = 2.0 * sum([dipole_x_ab[i,i] for i in range(n_occ)])
V_00_y = 2.0 * sum([dipole_y_ab[i,i] for i in range(n_occ)])
V_00_z = 2.0 * sum([dipole_z_ab[i,i] for i in range(n_occ)])

# Vm|n integrals
for i in range(n_occ):
	for s in range(n_virt):
		
		for j in range(n_occ):
			for t in range(n_virt):
			
				V_mn_x[i*n_virt + s, j*n_virt + t] += 2.0*V_00_x * drc(s,t) * drc(i,j) + 2.0 * dipole_x_ab[n_occ + t, n_occ + s] * drc(i,j) - 2.0 * dipole_x_ab[i, j]*drc(s,t)
				
				V_mn_y[i*n_virt + s, j*n_virt + t] += 2.0*V_00_y * drc(s,t) * drc(i,j) + 2.0 * dipole_y_ab[n_occ + t, n_occ + s] * drc(i,j) - 2.0 * dipole_y_ab[i, j]*drc(s,t)
				
				V_mn_z[i*n_virt + s, j*n_virt + t] += 2.0*V_00_z * drc(s,t) * drc(i,j) + 2.0 * dipole_z_ab[n_occ + t, n_occ + s] * drc(i,j) - 2.0 * dipole_z_ab[i, j]*drc(s,t)


F_mo = ao2mo(MOs, F)
g = tuvw

w = ref_freqs[0]

# E[2] and S[2] matrices
E2 = np.zeros((2 * n_ex, 2 * n_ex))
S2 = np.zeros((2 * n_ex, 2 * n_ex))

r = 0
c = 0
k = 0

# Size includes both m0, 0n elements and mn, nm elements
E2 = L2.L2_f(n_occ, n_virt, F_mo, g)
S2 = np.eye(n_ex*(n_ex + 2), dtype=complex)

RHS = np.zeros((n_ex*(n_ex + 2)), dtype=complex)
RHS[:2*n_ex] = 1.0j*RHS_0

# mu in L-space basis (one application of Q_mn) - NOT EXACTLY SAME AS RHS
M = np.zeros((n_ex*(n_ex + 2)), dtype=complex)
M[:n_ex] = RHS_0[:n_ex]
M[n_ex:2*n_ex] = RHS_0[:n_ex]

X = np.linalg.solve(E2 - 2.*(w + 1.0j * damp_param)*S2, RHS)

rsp = 1.0j*np.dot(M, X)

print('Linear response:', rsp)
print('Difference from reference: ', cpp_ref_dict['response_functions'][('x', 'x', ref_freqs[0])] - rsp)

K_1 = copy.deepcopy(X)

# Now constructing RHS for 2nd order

# V[2] and contraction with K

# Making first without any coefficient, to be handled later
# I assume that integrals of type Vmn|0 are zero

V2 = np.zeros((n_ex*(n_ex + 2)), dtype=complex)

for m in range(n_ex):

	for p in range(n_ex):
	
		V2[m] += 2.0 *(-1.0 * V_mn_x[m, p] + 2.0 * V_00_x * drc(m,p)) * K_1[p]
	

for n in range(n_ex):

	for q in range(n_ex):
	
		V2[n + n_ex] += 2.0 * (1.0*V_mn_x[q, n] - 2.0 * V_00_x * drc(n,q)) * K_1[n_ex + q]

# (no mn contribution to this V[2])

# G[3] and contractions with K

# Determinant-pair damping constants (currently zero)
Gamma = np.zeros((n_ex + 1, n_ex + 1), dtype=complex)

gamma_seed = damp_param

for m in range(n_ex + 1):
	for n in range(n_ex + 1):
	
		if m == 0:
			Gamma[m,n] = gamma_seed
			
		elif n == 0:
			Gamma[m,n] = gamma_seed
			
		else:
			Gamma[m,n] = 0.5*2.0*gamma_seed

G3 = np.zeros((n_ex*(n_ex + 2)), dtype=complex)

for m in range(n_ex):
	for n in range(n_ex):
		G3[2*n_ex + m*n_ex + n] = (Gamma[m + 1,n + 1] - Gamma[m + 1,0] - Gamma[0,n + 1]) * K_1[m] * K_1[n_ex + n]

# From general expression expansion coefficient	
G3 *= -0.5

# E[3] and contractions with K

# Coefficients for E operators not fully settled, other factors I think are handled
# I do for now no regard to "non-integral E operators", review later
# For conjugate Hmn|p integrals Hm|np I do Hpn|m: Can be reviewed later whether it should be H_np|m (maybe they are symmetric)

K_for_L3 = np.zeros((2, 2*n_ex), dtype=complex)
K_for_L3[0,:] = K_1[:2*n_ex]
K_for_L3[1,:] = K_1[:2*n_ex]

L3_arr = L3.L3_f(n_occ, n_virt, H00, F_mo, g, K_for_L3)

# Setting up final projection vector
# Going by an assumed E operator form of this, revisit this point later
V_p = np.zeros((n_ex*(n_ex + 2)), dtype=complex)
V_p[:n_ex] = RHS_0[:n_ex]
V_p[n_ex:2*n_ex] = RHS_0[:n_ex]

for m in range(n_ex):
	for n in range(n_ex):
		V_p[2*n_ex + m*n_ex + n] = -1.0*V_mn_x[n,m]

# Left-hand side of rsp eqn.
# Here 2*w for SHG rsp, adapt this later
LHS = E2 - 2.0*(2.0*w + 1.0j* damp_param)*S2

# Second part: Contraction with K1*K1 part of rho(2) where the resulting state pair was not |0,0>>

rsp_Q2 = 0.0

for m in range(n_ex):
	for n in range(n_ex):
		rsp_Q2 -= 2.0*(V_mn_x[n,m] - 2.0*V_00_x*drc(m,n)) * K_1[m] * K_1[n_ex + n]


E2inv = np.linalg.inv(LHS)

NaT3_L = np.zeros(2*n_ex+ n_ex*n_ex, dtype=complex)

for m in range(2*n_ex + n_ex*n_ex):
	for p in range(2*n_ex+ n_ex*n_ex):
		NaT3_L[p] += E2inv[p,m] *1.0j* L3_arr[m]

rsp_QT3_L = np.dot(V_p, NaT3_L)

NaX2 = np.zeros(2*n_ex+ n_ex*n_ex, dtype=complex)

for m in range(2*n_ex + n_ex*n_ex):
	for p in range(2*n_ex+ n_ex*n_ex):
		NaX2[p] += E2inv[p,m] * V2[m]

rsp_QNa = np.dot(V_p, NaX2)


rsp_Q_all_test = rsp_Q2 + rsp_QNa *1.0j + rsp_QT3_L *1.0j

print('')
print('Quadratic response function', rsp_Q_all_test)
print('')
print('Individual contributions:')
print('')
print('NaX2 with factor', rsp_QNa *1.0j)
print('NxA2 with factor', rsp_Q2)
print('NaT3 with factor', rsp_QT3_L *1.0j)


NaG3 = np.zeros(2*n_ex+ n_ex*n_ex, dtype=complex)

for m in range(2*n_ex + n_ex*n_ex):

	for p in range(2*n_ex+ n_ex*n_ex):
	
		NaG3[p] += E2inv[p,m] *1.0j* G3[m]


rsp_G3 = np.dot(V_p, NaG3)
print('')
print('NaG3 contribution (not counted in above response function)', rsp_G3)



