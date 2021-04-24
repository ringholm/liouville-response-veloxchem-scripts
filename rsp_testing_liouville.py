from mpi4py import MPI
import veloxchem as vlx
import sys
import numpy as np
import random
import copy
import L3

# Dirac delta fn
def drc(i, j):
	if (i == j):
		return 1
	else:
		return 0
		
# Dirac delta fn returning logical
def dlt(i, j):
	if (i == j):
		return True
	else:
		return False

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
rsp_settings = {'conv_thresh': 1.0e-4, 'nstates': 5}

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

MOs = scfdrv.scf_tensors['C'] #str(scfdrv.mol_orbs).splitlines()[2:]
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
ref_freqs = [0.1]
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

# Precalculating g_abpp sums over p
g_pp_occ = np.zeros((n_virt, n_occ))
g_pp_virt = np.zeros((n_virt, n_occ))

for a in range(n_virt):
	aa = n_occ + a
	for b in range(n_occ):
		
		for p in range(n_occ):
			g_pp_occ[a,b] += g[aa, b, p, p]
	
		for p in range(n_virt):
			pp = n_occ + p
			g_pp_virt[a,b] += g[aa, b, pp, pp]



# Transition integrals of H0 between a singly excited determinant and the reference state
H0_single_2_grnd = np.zeros((n_ex))

# Transition integrals of H0 between singly excited determinants
H0_single = np.zeros((n_ex, n_ex))

# Transition integrals of H0 betweeen ground state and doubly excited determinant
H0_dbl_2_grnd = np.zeros((n_ex * n_ex))

k = 0

# Assuming ordering is all from one occ to all virt, then next occ and so on - change this if needed
# Assume orbital transition orderings are from lowest to highest energy in each category occ/virt
for i in range(n_occ):
	for s in range(n_virt):
		
		H0_single_2_grnd[i*n_virt + s] = 2.0 * F_mo[n_occ + s, i] - 1.0* g_pp_occ[s, i] + tuvw[n_occ + s, n_occ + s, n_occ + s, i] + tuvw[n_occ + s, i, i, i]

		for j in range(n_occ):
			for t in range(n_virt):
			
				H0_single[i*n_virt + s, j*n_virt + t] = 2.0 * F_mo[n_occ + s, n_occ + t] * drc(i, j) - 2.0* F_mo[i,j] * drc(s, t) - 2.0*tuvw[n_occ+s, n_occ+t, i, j] + 4.0*tuvw[n_occ+s, i, n_occ+t, j ] + 2.0 * H00 * drc(i, j) * drc(s, t) 
				
				# Sign error?
				H0_dbl_2_grnd[k] = 4.0 * tuvw[n_occ+t, j, n_occ+s, i] - 2.0 * tuvw[n_occ+t, i, n_occ+s, j] 
				
				k += 1

# This block for H0 mn|p matrix elements:

# Transition integrals of H0 betweeen doubly and singly excited determinants
H0_mn_p = np.zeros((n_ex, n_ex, n_ex))



#tuvw[, , , ]



# Adding up contributions to the transition integrals
for i in range(n_occ):
	for s in range(n_virt):
		n = i*n_virt + s
		ss = n_occ + s

		for j in range(n_occ):
			for t in range(n_virt):
				m = j*n_virt + t
				tt = n_occ + t
			
				for k in range(n_occ):
					for v in range(n_virt):
						p = k*n_virt + v
						vv = n_occ + v
						
						pr = False
						if (m==4 and n==4 and p==4):
							pr = True
							
						if (s!=t and i!=j):

							if (dlt(v,s)):# and not (dlt(k,i) or dlt(k,j))):
								H0_mn_p[m,n,p] += 2.0 * g[tt, i, k, j] - 2.0 * g[k, i, tt, j]
							
							if (dlt(v,t)):# and not (dlt(k,i) or dlt(k,j))):
								H0_mn_p[m,n,p] -= 2.0 * g[ss, i, k, j] - 2.0 * g[k, i, ss, j]
								
							if (dlt(k,i)):# and not (dlt(v,s) or dlt(v,t))):
								H0_mn_p[m,n,p] += 2.0 * g[ss, vv, tt, j] - 2.0 * g[tt, vv, ss, j]

							if (dlt(k,j)):# and not (dlt(v,s) or dlt(v,t))):
								H0_mn_p[m,n,p] -= 2.0 * g[ss, vv, tt, i] - 2.0 * g[tt, vv, ss, i]

							if (dlt(v,s) and dlt(k,i)):
								H0_mn_p[m,n,p] += 4.0 * F_mo[tt, j] + 2.0 * g_pp_virt[t, j] - 2.0 * g_pp_occ[t, j]
								H0_mn_p[m,n,p] += 2.0 * g[tt, j, j, j] + 2.0 * g[tt, tt, tt, j] 
							
							if (dlt(v,t) and dlt(k,j)):
								H0_mn_p[m,n,p] += 4.0 * F_mo[ss, i] + 2.0 * g_pp_virt[s, i] - 2.0 * g_pp_occ[s, i]
								H0_mn_p[m,n,p] += 2.0 * g[ss, i, i, i] + 2.0 * g[ss, ss, ss, i]
					
							if (dlt(v,s) and dlt(k,j)):
								H0_mn_p[m,n,p] -= 2.0 * F_mo[tt, i] + 2.0 * g_pp_virt[t, i]
								H0_mn_p[m,n,p] -= g[tt, i, i, i] + g[tt, tt, tt, i]
												
							if (dlt(v,t) and dlt(k,i)):
								H0_mn_p[m,n,p] -= 2.0 * F_mo[ss, j] + 2.0 * g_pp_virt[s, j]
								H0_mn_p[m,n,p] -= g[ss, j, j, j] + g[ss, ss, ss, j]

						else:
						
							if (dlt(v,s) and dlt(k,i)):
								H0_mn_p[m,n,p] += -2.0 * g_pp_occ[t, j]
								H0_mn_p[m,n,p] += 1.0 * g[tt, j, j, j] + 1.0 * g[tt, tt, tt, j] 
							
							if (dlt(v,t) and dlt(k,j)):
								H0_mn_p[m,n,p] += -2.0 * g_pp_occ[s, i]
								H0_mn_p[m,n,p] += 1.0 * g[ss, i, i, i] + 1.0 * g[ss, ss, ss, i]


						if (pr):
							print('contrib a', 2.0 * g[tt, i, k, j] - 2.0 * g[k, i, tt, j])

						if (pr):
							print('contrib b', -2.0 * g[ss, i, k, j] + 2.0 * g[k, i, ss, j])
														
						if (pr):
							print('contrib c', 2.0 * g[ss, vv, tt, j] - 2.0 * g[tt, vv, ss, j])

						if (pr):
							print('contrib d', -2.0 * g[ss, vv, tt, i] + 2.0 * g[tt, vv, ss, i])

						if (pr):
							print('occ contrib only', - 2.0 * g_pp_occ[t, j])
							print('virt contrib only', +2.0 * g_pp_virt[t, j])
							
							print('contrib e1', 4.0 * F_mo[tt, j] + 2.0 * g_pp_virt[t, j] - 2.0 * g_pp_occ[t, j])
							print('contrib e2', 2.0 * g[tt, j, j, j] + 2.0 * g[tt, tt, tt, j] )

						if (pr):	
							print('contrib f1', 4.0 * F_mo[ss, i] + 2.0 * g_pp_virt[s, i] - 2.0 * g_pp_occ[s, i])	
							print('contrib f2', 2.0 * g[ss, i, i, i] + 2.0 * g[ss, ss, ss, i])
					
						if (pr):
							print('contrib g1', -2.0 * F_mo[tt, i] - 2.0 * g_pp_virt[t, i])
							print('contrib g2', -1,0*g[tt, i, i, i] - g[tt, tt, tt, i])

						if (pr):
							print('contrib h', -2.0 * F_mo[ss, j] - 2.0 * g_pp_virt[s, j])
							print('contrib h2', -1.0*g[ss, j, j, j] - g[ss, ss, ss, j])
							print('Hmn p final', H0_mn_p[m,n,p])
							

# Transition integrals of H0 between ground state and up-m, up-n, down-p determinants
H0_0_pDnm = np.zeros((n_ex, n_ex, n_ex))							

for i in range(n_occ):
	for s in range(n_virt):
		m = i*n_virt + s
		ss = n_occ + s

		for j in range(n_occ):
			for t in range(n_virt):
				n = j*n_virt + t
				tt = n_occ + t
			
				for k in range(n_occ):
					for v in range(n_virt):
						p = k*n_virt + v
						vv = n_occ + v


						if (dlt(v,s) and dlt(k,i)):

							H0_0_pDnm[p,n,m] += 2.0*H0_single_2_grnd[n]

						if (dlt(v,t) and dlt(k,j)):
							
							H0_0_pDnm[p,n,m] += 2.0*H0_single_2_grnd[m]
					
						if (dlt(v,s) and dlt(k,j)):
							
							H0_0_pDnm[p,n,m] -= 1.0*H0_single_2_grnd[i*n_virt + t]
													
						if (dlt(v,t) and dlt(k,i)):
							
							H0_0_pDnm[p,n,m] -= 1.0*H0_single_2_grnd[j*n_virt + s]




#H0_mn_p *= 0.0
#H0_single_2_grnd *= 0.0

w = ref_freqs[0]

# E[2] and S[2] matrices
E2 = np.zeros((2 * n_ex, 2 * n_ex))
S2 = np.zeros((2 * n_ex, 2 * n_ex))

r = 0
c = 0
k = 0

# Assuming ordering is all from one occ to all virt, change if needed
for i in range(n_occ):
	for s in range(n_virt):
	
		for j in range(n_occ):
			for t in range(n_virt):

				# Top left block				
				E2[r, c] = H0_single[r, c] - 2.0 * H00 * drc(i, j) * drc(s, t)
				
				# Top right block
				# Should be c.c. between this and next blk, now neglected
				E2[r, c + n_ex] = -1.0 * H0_dbl_2_grnd[k] #* (1 - drc(i,j)) * (1 - drc(s,t))
				
				# Bottom left block
				E2[r + n_ex, c] = -1.0 * H0_dbl_2_grnd[k] #* (1 - drc(i,j)) * (1 - drc(s,t))

				# Bottom right block
				E2[r + n_ex, c + n_ex] = H0_single[c, r] - 2.0 * H00 * drc(i, j) * drc(s, t)
				
				# S[2]
				if (r == c):
					S2[r, c] = 1.0
					S2[r + n_ex, c + n_ex] = -1.0
				
				k += 1
				
				c += 1
			

		c = 0

		r += 1			





# Left-hand side of rsp eqn.
LHS = E2 - (w + 1.0j* damp_param)*S2*2.

print('My RHS', RHS_0)

#RHS_chg_0 = np.zeros((RHS_0.shape[0]))
#RHS_chg_0[:RHS_0.shape[0]//2] = 2*RHS_0[:RHS_0.shape[0]//2]
#print('TEST manipulated RHS:', RHS_chg_0)

# Solving rsp eqn.
X = np.linalg.solve(LHS, RHS_0)

print('H-space params.', X)

# Making expectation value
rsp = -1.0* np.dot(RHS_0, X)


print('My response function component:', rsp)
print('Reference: ', cpp_ref_dict['response_functions'][('x', 'x', ref_freqs[0])])
print('Difference: ', cpp_ref_dict['response_functions'][('x', 'x', ref_freqs[0])] - rsp)


# Liouville section begins

# First trying out first order response, no damping

# Do the mn coefficients automatically come out as zero?


# Switching to excitation indices instead of occ, virt indices

# Size includes both m0, 0n elements and mn, nm elements
E2 = np.zeros((n_ex*(n_ex + 2), n_ex*(n_ex + 2)), dtype=complex)

S2 = np.eye(n_ex*(n_ex + 2), dtype=complex)

# Constructing fully m0, 0n, p0, 0q type elements first

# I do fully explicit now even though there are symmetries, just to be thorough

# (m0, p0)
for m in range(n_ex):
	for p in range(n_ex):
	
		# The factor 2 for H00 comes from the use of E operators, most likely correct but not fully verified
		E2[m, p] = H0_single[m, p] - 2.0 * H00 * drc(m,p)  

# (m0, 0q)
for m in range(n_ex):
	for q in range(n_ex):
		
		E2[m, q + n_ex] = H0_dbl_2_grnd[m * n_ex + q]
		
# (0n, p0)
for n in range(n_ex):
	for p in range(n_ex):

		E2[n + n_ex, p] = -1.0 * H0_dbl_2_grnd[n * n_ex + p]

# (0n, 0q)
for n in range(n_ex):
	for q in range(n_ex):

		# The factor 2 for H00 comes from the use of E operators, most likely correct but not fully verified
		E2[n + n_ex, q + n_ex] = 2.0 * H00 * drc(n,q) - H0_single[q, n]

# (m0, pq)
for m in range(n_ex):
	for p in range(n_ex):
		for q in range(n_ex):
		
			E2[m, p*n_ex + q + 2*n_ex] = -2.0 * H0_single_2_grnd[q] * drc(m,p)

# (0n, pq)
for n in range(n_ex):
	for p in range(n_ex):
		for q in range(n_ex):
		
			E2[n + n_ex, p*n_ex + q + 2*n_ex] = 2.0 * H0_single_2_grnd[p] * drc(n,q)

# (mn, p0) is zero
# (mn, 0q) is zero

# (mn, pq)

for m in range(n_ex):
	for n in range(n_ex):
		for p in range(n_ex):
			for q in range(n_ex):
			
				E2[m * n_ex + n + 2*n_ex, p*n_ex + q + 2*n_ex] = 2.0 * H0_single[m, p] * drc(n,q) - 2.0 * H0_single[q, n] * drc(m,p)


RHS = np.zeros((n_ex*(n_ex + 2)), dtype=complex)
RHS[:2*n_ex] = 1.0j*RHS_0

# mu in L-space basis (one application of Q_mn) - NOT EXACTLY SAME AS RHS
M = np.zeros((n_ex*(n_ex + 2)), dtype=complex)
M[:n_ex] = RHS_0[:n_ex]
M[n_ex:2*n_ex] = RHS_0[:n_ex]

print('L-space RHS:', RHS)

X = np.linalg.solve(E2 - 2.*(w + 1.0j * damp_param)*S2, RHS)

print('L-space params', X)

rsp = 1.0j*np.dot(M, X)

print('Response:', rsp)
print('Difference from refefence: ', cpp_ref_dict['response_functions'][('x', 'x', ref_freqs[0])] - rsp)

K_1 = copy.deepcopy(X)

print('My K1')
print(K_1)


print('One sss: integral block', tuvw[n_occ, n_occ, n_occ, :])

print('First sssi integral', tuvw[n_occ, n_occ, n_occ, 0])
print('First siii integral', tuvw[n_occ, 0, 0, 0])

print('Test: first ssii integral', tuvw[n_occ, n_occ, 0, 0])
print('Test: first siis integral', tuvw[n_occ, 0, 0, n_occ])
print('Test: first issi integral', tuvw[0, n_occ, n_occ, 0])



print('Example sssi cross integral', tuvw[n_occ+1, n_occ, n_occ, 0])
print('Example siii cross integral', tuvw[n_occ, 0, 2, 0])

print('Test: example ssii double cross integral', tuvw[n_occ, n_occ +1, 3, 0])
print('Test: example siis double cross integral', tuvw[n_occ, 0, 3, n_occ + 1])
print('Test: example issi double cross integral', tuvw[0, n_occ+ 1, n_occ, 1])


#tuvw[n_occ + s, n_occ + s, n_occ + s, i] + tuvw[n_occ + s, i, i, i]


# Now constructing RHS for 2nd order

# V[2] and contraction with K

# Making first without any coefficient, to be handled later
# I assume that integrals of type Vmn|0 are zero

V2 = np.zeros((n_ex*(n_ex + 2)), dtype=complex)

for m in range(n_ex):

	for p in range(n_ex):
	
		V2[m] += (-1.0 * V_mn_x[m, p] + 2.0 * V_00_x * drc(m,p)) * K_1[p]
	

for n in range(n_ex):

	for q in range(n_ex):
	
		V2[n + n_ex] += (1.0*V_mn_x[q, n] - 2.0 * V_00_x * drc(n,q)) * K_1[n_ex + q]

# (no mn contribution to this V[2])

# G[3] and contractions with K

# Determinant-pair damping constants (currently zero)
Gamma = np.zeros((n_ex + 1, n_ex + 1), dtype=complex)

gamma_seed = damp_param/2.0

for m in range(n_ex + 1):

	for n in range(n_ex + 1):
	
		if m == 0:
		
			Gamma[m,n] = gamma_seed
			
		elif n == 0:
		
			Gamma[m,n] = gamma_seed
			
		else:
		
			Gamma[m,n] = 0.0*2.0*gamma_seed
		
			
	
		

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


print('My F_mo')
print(F_mo)

print('My V_mn_x')
print(V_mn_x)

print('My H0 single to ground')
print(H0_single_2_grnd)

print('My H0 single mn')
print(H0_single)


print('My first Hmn_p')
print(H0_mn_p[:,:,0])


E3 = np.zeros((n_ex*(n_ex + 2)), dtype=complex)

# (m, 0 part)
for m in range(n_ex):

	for p in range(n_ex):
	
		for s in range(n_ex):
		
			E3[m] += (2.0 * H0_single_2_grnd[s] * drc(m,p) + 2.0 * H0_single_2_grnd[p] * drc(m,s) - 1.0*H0_mn_p[p,s,m]) * K_1[p] * K_1[s]

			if (m==4 and p==4 and s==4):
				print('stg s', 2.0 * H0_single_2_grnd[s] * drc(m,p))
				print('stg p', 2.0 * H0_single_2_grnd[p] * drc(m,s))
				print('h0mnp psm', -1.0*H0_mn_p[p,s,m])
				print('the two Ks',  K_1[p], K_1[s])
				
				print('E3m now p0s0', p, s, E3[m])
				print(' ')
		
		for t in range(n_ex):
		
			E3[m] += (1.0 * H0_0_pDnm[p,t,m] - 1.0 * H0_mn_p[t,m,p]) * K_1[p] * K_1[n_ex + t]

			if (m==4 and p==4 and t==4):

				print('H0_0_pdnm ptm', 1.0 * H0_0_pDnm[p,t,m] )
				print('h0mnp psm', - 1.0*H0_mn_p[t,m,p])
				print('the two Ks',  K_1[p], K_1[n_ex + t])
			
				print('E3m now p00t', p,t, E3[m])	
				print(' ')

		
	for q in range(n_ex):
	
		for s in range(n_ex):		

			E3[m] += (2.0 *H0_single_2_grnd[q] * drc(m,s) + 2.0 *H0_single_2_grnd[m] * drc(s,q) - 1.0 * H0_mn_p[q,m,s]) * K_1[n_ex + q] * K_1[s]

			if (m==4 and q==4 and s==4):

				print('stg q', 2.0 * H0_single_2_grnd[q] * drc(m,s))
				print('stg m', 2.0 * H0_single_2_grnd[m] * drc(s,q))
				print('h0mnp qms', -1.0 * H0_mn_p[q,m,s])
				print('the two Ks',  K_1[n_ex + q], K_1[s])
			
				print('E3m now 0qs0', q,s, E3[m])
				print(' ')

# (0, n part)
for n in range(n_ex):

	for q in range(n_ex):
	
		for t in range(n_ex):
		
			E3[n_ex + n] += (-2.0 *H0_single_2_grnd[t] * drc(n,q) - 2.0 *H0_single_2_grnd[q] * drc(n,t) + 1.0 * H0_mn_p[q,t,n]) * K_1[n_ex + q] * K_1[n_ex + t]


		for s in range(n_ex):
		
			E3[n_ex + n] += (-1.0 * H0_0_pDnm[q,s,n] + 1.0 * H0_mn_p[s,n,q]) * K_1[n_ex + q] * K_1[s]

			
	for p in range(n_ex):
	
		for t in range(n_ex):		

			E3[n_ex + n] += (-2.0 *H0_single_2_grnd[p] * drc(n,t) - 2.0 *H0_single_2_grnd[n] * drc(p,t) + 1.0 * H0_mn_p[p,n,t]) * K_1[p] * K_1[n_ex + t]

# (m, n part is zero)

				
	
# From general expression expansion coefficient	
E3 *= -0.5

print('My E3')
print(E3)


# NEW BLOCK: E3 FROM GENERATED CODE

K_for_L3 = np.zeros((2, 2*n_ex), dtype=complex)

K_for_L3[0,:] = K_1[:2*n_ex]
K_for_L3[1,:] = K_1[:2*n_ex]

L3_arr = L3.L3_f(n_occ, n_virt, H00, F_mo, g, K_for_L3)

tmp_L3 = copy.deepcopy(L3_arr[:n_ex])
L3_arr[:n_ex] = L3_arr[n_ex:2*n_ex]
L3_arr[n_ex:2*n_ex] = tmp_L3



print('My L3')
print(L3_arr)


#END NEW BLOCK



print('My V2')
print(V2)

# Setting up final projection vector
# Going by an assumed E operator form of this, revisit this point later

V_p = np.zeros((n_ex*(n_ex + 2)), dtype=complex)

V_p[:n_ex] = RHS_0[:n_ex]
V_p[n_ex:2*n_ex] = RHS_0[:n_ex]

for m in range(n_ex):

	for n in range(n_ex):

		V_p[2*n_ex + m*n_ex + n] = -1.0*V_mn_x[n,m]# - V_00_x*drc(m,n)


# Quadratic response RHS
RHS_Q = V2 - 1.0j*E3 + G3

# Left-hand side of rsp eqn.
# Here 2*w for SHG rsp, adapt this later
LHS = E2 - 2.0*(2.0*w + 1.0j* damp_param)*S2

print('My 2nd order RHS', RHS_Q)


# Solving rsp eqn.
K2 = np.linalg.solve(LHS, RHS_Q)

print('My K2 coeffs.') 
for m in range(n_ex):

	print(m, ', g:', K2[m])
	
for n in range(n_ex):

	print('g,', n, ':', K2[n_ex + n])

for m in range(n_ex):

	for n in range(n_ex):

		print(m, ',', n, ':', K2[2*n_ex + m*n_ex + n])

#print(K2)

#for m in range(n_ex):
#
#	K2[2*n_ex + m*n_ex + m] = 0.0

# This is only the first part of the final contraction - also contraction with other coeffs.
rsp_Q = 1.0j*np.dot(V_p, K2)

print('My response function after first part', rsp_Q)

# Second part: Contraction with K1*K1 part of rho(2) where the resulting state pair was not |0,0>>

rsp_Q2 = 0.0

for m in range(n_ex):

	for n in range(n_ex):
	
		rsp_Q2 -= (V_mn_x[n,m] - 2.0*V_00_x*drc(m,n)) * K_1[m] * K_1[n_ex + n]




print('Second part contrib to rsp function', rsp_Q2)

rsp_Q += rsp_Q2
print('My response function after second part', rsp_Q)

E2inv = np.linalg.inv(LHS)

NaT3 = np.zeros(2*n_ex+ n_ex*n_ex, dtype=complex)

for m in range(2*n_ex + n_ex*n_ex):

	for p in range(2*n_ex+ n_ex*n_ex):
	
		NaT3[p] += E2inv[p,m] * 1.0j*E3[m]

print('NaT3', NaT3)

rsp_QT3 = np.dot(V_p, NaT3)

print('NaT3 contribution', rsp_QT3)



E2inv = np.linalg.inv(LHS)

NaT3_L = np.zeros(2*n_ex+ n_ex*n_ex, dtype=complex)

for m in range(2*n_ex + n_ex*n_ex):

	for p in range(2*n_ex+ n_ex*n_ex):
	
		NaT3_L[p] += E2inv[p,m] *1.0j* L3_arr[m]

print('NaT3_L', NaT3_L)

rsp_QT3_L = np.dot(V_p, NaT3_L)

print('NaT3_L contribution', rsp_QT3_L)




NaX2 = np.zeros(2*n_ex+ n_ex*n_ex, dtype=complex)

for m in range(2*n_ex + n_ex*n_ex):

	for p in range(2*n_ex+ n_ex*n_ex):
	
		NaX2[p] += E2inv[p,m] * V2[m]



print('NaX2', NaX2)

print('Vp first two', V_p[:2*n_ex])

rsp_QNa = np.dot(V_p, NaX2)

print('NaX2 contribution', rsp_QNa)

print('E2inv first column', E2inv[:,0])


rsp_Q_all_test = rsp_Q2 + rsp_QNa *1.0j + rsp_QT3_L *1.0j

print('rsp Q test', rsp_Q_all_test)
print('2 x rsp Q test', 2.0* rsp_Q_all_test)

print('NaX2 w fact', 2.0* rsp_QNa *1.0j)
print('NxA2 w fact', 2.0* rsp_Q2)
print('NaT3 w fact', 2.0* rsp_QT3_L *1.0j)


NaG3 = np.zeros(2*n_ex+ n_ex*n_ex, dtype=complex)

for m in range(2*n_ex + n_ex*n_ex):

	for p in range(2*n_ex+ n_ex*n_ex):
	
		NaG3[p] += E2inv[p,m] *1.0j* G3[m]

print('NaG3', NaG3)

rsp_G3 = np.dot(V_p, NaG3)

print('NaG3 contribution', rsp_G3)


'''
# Third and last part: Contraction with K1*K1 part of rho(2) where the resulting state pair was |0,0>>


rsp_Q3 = 0.0

for m in range(n_ex):

	# Factor 1/2 is doubled since two combinations lead here, hence the coefficient is 1
	rsp_Q3 += V_00_x * K_1[m] * K_1[n_ex + m]


print('Third part contrib to rsp function', rsp_Q3)

rsp_Q += rsp_Q3

print('My response function after third part', rsp_Q)
'''



