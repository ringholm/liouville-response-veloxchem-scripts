import numpy as np


def L4(n_occ, n_virt, H00, F, g, K): 
 
	n_ex = n_occ * n_virt

	# Current operator combination: {'a': 1, 'b': 1, 'c': 1, 'd': 1}
	# All terms vanished for this combination

	# Current operator combination: {'a': 1, 'b': 1, 'c': 1, 'd': 2}
	for i in range(n_occ):
		for j in range(n_occ):
			for k in range(n_occ):
				for m in range(n_occ):
					for s in range(n_virt):
						for t in range(n_virt):
							for u in range(n_virt):
								for v in range(n_virt):

									if ((j == i) and (k == i) and (m == i)):

										if ((t == s) and (u == s) and (v == s)):

											L4[i*n_virt + s + n_ex] += (-12 * g[i, n_occ + s, i, n_occ + s] ) * K[0, i*n_virt + s] * K[1, i*n_virt + s] * K[2, i*n_virt + s]

										elif ((t == s) and (u == s) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s + n_ex] += (-8 * g[i, n_occ + s, i, n_occ + v] ) * K[0, i*n_virt + s] * K[1, i*n_virt + s] * K[2, i*n_virt + v]

										elif ((t == s) and (u != s) and (u != t) and (v == s)):

											L4[i*n_virt + s + n_ex] += (-8 * g[i, n_occ + s, i, n_occ + u] ) * K[0, i*n_virt + s] * K[1, i*n_virt + u] * K[2, i*n_virt + s]

										elif ((t == s) and (u != s) and (u != t) and (v == u)):

											L4[i*n_virt + s + n_ex] += (-4 * g[i, n_occ + u, i, n_occ + u] ) * K[0, i*n_virt + s] * K[1, i*n_virt + u] * K[2, i*n_virt + u]

										elif ((t == s) and (u != s) and (u != t) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s + n_ex] += (-4 * g[i, n_occ + u, i, n_occ + v] ) * K[0, i*n_virt + s] * K[1, i*n_virt + u] * K[2, i*n_virt + v]

										elif ((t != s) and (u == s) and (v == s)):

											L4[i*n_virt + s + n_ex] += (-8 * g[i, n_occ + s, i, n_occ + t] ) * K[0, i*n_virt + t] * K[1, i*n_virt + s] * K[2, i*n_virt + s]

										elif ((t != s) and (u == s) and (v == t)):

											L4[i*n_virt + s + n_ex] += (-4 * g[i, n_occ + t, i, n_occ + t] ) * K[0, i*n_virt + t] * K[1, i*n_virt + s] * K[2, i*n_virt + t]

										elif ((t != s) and (u == s) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s + n_ex] += (-4 * g[i, n_occ + t, i, n_occ + v] ) * K[0, i*n_virt + t] * K[1, i*n_virt + s] * K[2, i*n_virt + v]

										elif ((t != s) and (u == t) and (v == s)):

											L4[i*n_virt + s + n_ex] += (-4 * g[i, n_occ + t, i, n_occ + t] ) * K[0, i*n_virt + t] * K[1, i*n_virt + t] * K[2, i*n_virt + s]

										elif ((t != s) and (u != s) and (u != t) and (v == s)):

											L4[i*n_virt + s + n_ex] += (-4 * g[i, n_occ + t, i, n_occ + u] ) * K[0, i*n_virt + t] * K[1, i*n_virt + u] * K[2, i*n_virt + s]

									elif ((j == i) and (k == i) and (m != i) and (m != j) and (m != k)):

										if ((t == s) and (u == s) and (v == s)):

											L4[i*n_virt + s + n_ex] += (-8 * g[i, n_occ + s, m, n_occ + s] ) * K[0, i*n_virt + s] * K[1, i*n_virt + s] * K[2, m*n_virt + s]

										elif ((t == s) and (u == s) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s + n_ex] += (-8 * g[i, n_occ + s, m, n_occ + v] + 4 * g[i, n_occ + v, m, n_occ + s] ) * K[0, i*n_virt + s] * K[1, i*n_virt + s] * K[2, m*n_virt + v]

										elif ((t == s) and (u != s) and (u != t) and (v == s)):

											L4[i*n_virt + s + n_ex] += (-6 * g[i, n_occ + u, m, n_occ + s] ) * K[0, i*n_virt + s] * K[1, i*n_virt + u] * K[2, m*n_virt + s]

										elif ((t == s) and (u != s) and (u != t) and (v == u)):

											L4[i*n_virt + s + n_ex] += (-2 * g[i, n_occ + u, m, n_occ + u] ) * K[0, i*n_virt + s] * K[1, i*n_virt + u] * K[2, m*n_virt + u]

										elif ((t == s) and (u != s) and (u != t) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s + n_ex] += (-4 * g[i, n_occ + u, m, n_occ + v] + 2 * g[i, n_occ + v, m, n_occ + u] ) * K[0, i*n_virt + s] * K[1, i*n_virt + u] * K[2, m*n_virt + v]

										elif ((t != s) and (u == s) and (v == s)):

											L4[i*n_virt + s + n_ex] += (-6 * g[i, n_occ + t, m, n_occ + s] ) * K[0, i*n_virt + t] * K[1, i*n_virt + s] * K[2, m*n_virt + s]

										elif ((t != s) and (u == s) and (v == t)):

											L4[i*n_virt + s + n_ex] += (-2 * g[i, n_occ + t, m, n_occ + t] ) * K[0, i*n_virt + t] * K[1, i*n_virt + s] * K[2, m*n_virt + t]

										elif ((t != s) and (u == s) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s + n_ex] += (-4 * g[i, n_occ + t, m, n_occ + v] + 2 * g[i, n_occ + v, m, n_occ + t] ) * K[0, i*n_virt + t] * K[1, i*n_virt + s] * K[2, m*n_virt + v]

										elif ((t != s) and (u == t) and (v == s)):

											L4[i*n_virt + s + n_ex] += (-4 * g[i, n_occ + t, m, n_occ + t] ) * K[0, i*n_virt + t] * K[1, i*n_virt + t] * K[2, m*n_virt + s]

										elif ((t != s) and (u != s) and (u != t) and (v == s)):

											L4[i*n_virt + s + n_ex] += (-2 * g[i, n_occ + t, m, n_occ + u] + -2 * g[i, n_occ + u, m, n_occ + t] ) * K[0, i*n_virt + t] * K[1, i*n_virt + u] * K[2, m*n_virt + s]

									elif ((j == i) and (k != i) and (k != j) and (m == i)):

										if ((t == s) and (u == s) and (v == s)):

											L4[i*n_virt + s + n_ex] += (-8 * g[i, n_occ + s, k, n_occ + s] ) * K[0, i*n_virt + s] * K[1, k*n_virt + s] * K[2, i*n_virt + s]

										elif ((t == s) and (u == s) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s + n_ex] += (-6 * g[i, n_occ + v, k, n_occ + s] ) * K[0, i*n_virt + s] * K[1, k*n_virt + s] * K[2, i*n_virt + v]

										elif ((t == s) and (u != s) and (u != t) and (v == s)):

											L4[i*n_virt + s + n_ex] += (-8 * g[i, n_occ + s, k, n_occ + u] + 4 * g[i, n_occ + u, k, n_occ + s] ) * K[0, i*n_virt + s] * K[1, k*n_virt + u] * K[2, i*n_virt + s]

										elif ((t == s) and (u != s) and (u != t) and (v == u)):

											L4[i*n_virt + s + n_ex] += (-2 * g[i, n_occ + u, k, n_occ + u] ) * K[0, i*n_virt + s] * K[1, k*n_virt + u] * K[2, i*n_virt + u]

										elif ((t == s) and (u != s) and (u != t) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s + n_ex] += (2 * g[i, n_occ + u, k, n_occ + v] + -4 * g[i, n_occ + v, k, n_occ + u] ) * K[0, i*n_virt + s] * K[1, k*n_virt + u] * K[2, i*n_virt + v]

										elif ((t != s) and (u == s) and (v == s)):

											L4[i*n_virt + s + n_ex] += (-6 * g[i, n_occ + t, k, n_occ + s] ) * K[0, i*n_virt + t] * K[1, k*n_virt + s] * K[2, i*n_virt + s]

										elif ((t != s) and (u == s) and (v == t)):

											L4[i*n_virt + s + n_ex] += (-4 * g[i, n_occ + t, k, n_occ + t] ) * K[0, i*n_virt + t] * K[1, k*n_virt + s] * K[2, i*n_virt + t]

										elif ((t != s) and (u == s) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s + n_ex] += (-2 * g[i, n_occ + t, k, n_occ + v] + -2 * g[i, n_occ + v, k, n_occ + t] ) * K[0, i*n_virt + t] * K[1, k*n_virt + s] * K[2, i*n_virt + v]

										elif ((t != s) and (u == t) and (v == s)):

											L4[i*n_virt + s + n_ex] += (-2 * g[i, n_occ + t, k, n_occ + t] ) * K[0, i*n_virt + t] * K[1, k*n_virt + t] * K[2, i*n_virt + s]

										elif ((t != s) and (u != s) and (u != t) and (v == s)):

											L4[i*n_virt + s + n_ex] += (-4 * g[i, n_occ + t, k, n_occ + u] + 2 * g[i, n_occ + u, k, n_occ + t] ) * K[0, i*n_virt + t] * K[1, k*n_virt + u] * K[2, i*n_virt + s]

									elif ((j == i) and (k != i) and (k != j) and (m == k)):

										if ((t == s) and (u == s) and (v == s)):

											L4[i*n_virt + s + n_ex] += (-4 * g[k, n_occ + s, k, n_occ + s] ) * K[0, i*n_virt + s] * K[1, k*n_virt + s] * K[2, k*n_virt + s]

										elif ((t == s) and (u == s) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s + n_ex] += (-2 * g[k, n_occ + s, k, n_occ + v] ) * K[0, i*n_virt + s] * K[1, k*n_virt + s] * K[2, k*n_virt + v]

										elif ((t == s) and (u != s) and (u != t) and (v == s)):

											L4[i*n_virt + s + n_ex] += (-2 * g[k, n_occ + s, k, n_occ + u] ) * K[0, i*n_virt + s] * K[1, k*n_virt + u] * K[2, k*n_virt + s]

										elif ((t != s) and (u == s) and (v == s)):

											L4[i*n_virt + s + n_ex] += (-4 * g[k, n_occ + s, k, n_occ + t] ) * K[0, i*n_virt + t] * K[1, k*n_virt + s] * K[2, k*n_virt + s]

										elif ((t != s) and (u == s) and (v == t)):

											L4[i*n_virt + s + n_ex] += (-2 * g[k, n_occ + t, k, n_occ + t] ) * K[0, i*n_virt + t] * K[1, k*n_virt + s] * K[2, k*n_virt + t]

										elif ((t != s) and (u == s) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s + n_ex] += (-2 * g[k, n_occ + t, k, n_occ + v] ) * K[0, i*n_virt + t] * K[1, k*n_virt + s] * K[2, k*n_virt + v]

										elif ((t != s) and (u == t) and (v == s)):

											L4[i*n_virt + s + n_ex] += (-2 * g[k, n_occ + t, k, n_occ + t] ) * K[0, i*n_virt + t] * K[1, k*n_virt + t] * K[2, k*n_virt + s]

										elif ((t != s) and (u != s) and (u != t) and (v == s)):

											L4[i*n_virt + s + n_ex] += (-2 * g[k, n_occ + t, k, n_occ + u] ) * K[0, i*n_virt + t] * K[1, k*n_virt + u] * K[2, k*n_virt + s]

									elif ((j == i) and (k != i) and (k != j) and (m != i) and (m != j) and (m != k)):

										if ((t == s) and (u == s) and (v == s)):

											L4[i*n_virt + s + n_ex] += (-4 * g[k, n_occ + s, m, n_occ + s] ) * K[0, i*n_virt + s] * K[1, k*n_virt + s] * K[2, m*n_virt + s]

										elif ((t == s) and (u == s) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s + n_ex] += (-4 * g[k, n_occ + s, m, n_occ + v] + 2 * g[k, n_occ + v, m, n_occ + s] ) * K[0, i*n_virt + s] * K[1, k*n_virt + s] * K[2, m*n_virt + v]

										elif ((t == s) and (u != s) and (u != t) and (v == s)):

											L4[i*n_virt + s + n_ex] += (2 * g[k, n_occ + s, m, n_occ + u] + -4 * g[k, n_occ + u, m, n_occ + s] ) * K[0, i*n_virt + s] * K[1, k*n_virt + u] * K[2, m*n_virt + s]

										elif ((t != s) and (u == s) and (v == s)):

											L4[i*n_virt + s + n_ex] += (-2 * g[k, n_occ + s, m, n_occ + t] + -2 * g[k, n_occ + t, m, n_occ + s] ) * K[0, i*n_virt + t] * K[1, k*n_virt + s] * K[2, m*n_virt + s]

										elif ((t != s) and (u == s) and (v == t)):

											L4[i*n_virt + s + n_ex] += (-2 * g[k, n_occ + t, m, n_occ + t] ) * K[0, i*n_virt + t] * K[1, k*n_virt + s] * K[2, m*n_virt + t]

										elif ((t != s) and (u == s) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s + n_ex] += (-4 * g[k, n_occ + t, m, n_occ + v] + 2 * g[k, n_occ + v, m, n_occ + t] ) * K[0, i*n_virt + t] * K[1, k*n_virt + s] * K[2, m*n_virt + v]

										elif ((t != s) and (u == t) and (v == s)):

											L4[i*n_virt + s + n_ex] += (-2 * g[k, n_occ + t, m, n_occ + t] ) * K[0, i*n_virt + t] * K[1, k*n_virt + t] * K[2, m*n_virt + s]

										elif ((t != s) and (u != s) and (u != t) and (v == s)):

											L4[i*n_virt + s + n_ex] += (2 * g[k, n_occ + t, m, n_occ + u] + -4 * g[k, n_occ + u, m, n_occ + t] ) * K[0, i*n_virt + t] * K[1, k*n_virt + u] * K[2, m*n_virt + s]

									elif ((j != i) and (k == i) and (m == i)):

										if ((t == s) and (u == s) and (v == s)):

											L4[i*n_virt + s + n_ex] += (-8 * g[i, n_occ + s, j, n_occ + s] ) * K[0, j*n_virt + s] * K[1, i*n_virt + s] * K[2, i*n_virt + s]

										elif ((t == s) and (u == s) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s + n_ex] += (-6 * g[i, n_occ + v, j, n_occ + s] ) * K[0, j*n_virt + s] * K[1, i*n_virt + s] * K[2, i*n_virt + v]

										elif ((t == s) and (u != s) and (u != t) and (v == s)):

											L4[i*n_virt + s + n_ex] += (-6 * g[i, n_occ + u, j, n_occ + s] ) * K[0, j*n_virt + s] * K[1, i*n_virt + u] * K[2, i*n_virt + s]

										elif ((t == s) and (u != s) and (u != t) and (v == u)):

											L4[i*n_virt + s + n_ex] += (-4 * g[i, n_occ + u, j, n_occ + u] ) * K[0, j*n_virt + s] * K[1, i*n_virt + u] * K[2, i*n_virt + u]

										elif ((t == s) and (u != s) and (u != t) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s + n_ex] += (-2 * g[i, n_occ + u, j, n_occ + v] + -2 * g[i, n_occ + v, j, n_occ + u] ) * K[0, j*n_virt + s] * K[1, i*n_virt + u] * K[2, i*n_virt + v]

										elif ((t != s) and (u == s) and (v == s)):

											L4[i*n_virt + s + n_ex] += (-8 * g[i, n_occ + s, j, n_occ + t] + 4 * g[i, n_occ + t, j, n_occ + s] ) * K[0, j*n_virt + t] * K[1, i*n_virt + s] * K[2, i*n_virt + s]

										elif ((t != s) and (u == s) and (v == t)):

											L4[i*n_virt + s + n_ex] += (-2 * g[i, n_occ + t, j, n_occ + t] ) * K[0, j*n_virt + t] * K[1, i*n_virt + s] * K[2, i*n_virt + t]

										elif ((t != s) and (u == s) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s + n_ex] += (2 * g[i, n_occ + t, j, n_occ + v] + -4 * g[i, n_occ + v, j, n_occ + t] ) * K[0, j*n_virt + t] * K[1, i*n_virt + s] * K[2, i*n_virt + v]

										elif ((t != s) and (u == t) and (v == s)):

											L4[i*n_virt + s + n_ex] += (-2 * g[i, n_occ + t, j, n_occ + t] ) * K[0, j*n_virt + t] * K[1, i*n_virt + t] * K[2, i*n_virt + s]

										elif ((t != s) and (u != s) and (u != t) and (v == s)):

											L4[i*n_virt + s + n_ex] += (2 * g[i, n_occ + t, j, n_occ + u] + -4 * g[i, n_occ + u, j, n_occ + t] ) * K[0, j*n_virt + t] * K[1, i*n_virt + u] * K[2, i*n_virt + s]

									elif ((j != i) and (k == i) and (m == j)):

										if ((t == s) and (u == s) and (v == s)):

											L4[i*n_virt + s + n_ex] += (-4 * g[j, n_occ + s, j, n_occ + s] ) * K[0, j*n_virt + s] * K[1, i*n_virt + s] * K[2, j*n_virt + s]

										elif ((t == s) and (u == s) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s + n_ex] += (-2 * g[j, n_occ + s, j, n_occ + v] ) * K[0, j*n_virt + s] * K[1, i*n_virt + s] * K[2, j*n_virt + v]

										elif ((t == s) and (u != s) and (u != t) and (v == s)):

											L4[i*n_virt + s + n_ex] += (-4 * g[j, n_occ + s, j, n_occ + u] ) * K[0, j*n_virt + s] * K[1, i*n_virt + u] * K[2, j*n_virt + s]

										elif ((t == s) and (u != s) and (u != t) and (v == u)):

											L4[i*n_virt + s + n_ex] += (-2 * g[j, n_occ + u, j, n_occ + u] ) * K[0, j*n_virt + s] * K[1, i*n_virt + u] * K[2, j*n_virt + u]

										elif ((t == s) and (u != s) and (u != t) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s + n_ex] += (-2 * g[j, n_occ + u, j, n_occ + v] ) * K[0, j*n_virt + s] * K[1, i*n_virt + u] * K[2, j*n_virt + v]

										elif ((t != s) and (u == s) and (v == s)):

											L4[i*n_virt + s + n_ex] += (-2 * g[j, n_occ + s, j, n_occ + t] ) * K[0, j*n_virt + t] * K[1, i*n_virt + s] * K[2, j*n_virt + s]

										elif ((t != s) and (u == t) and (v == s)):

											L4[i*n_virt + s + n_ex] += (-2 * g[j, n_occ + t, j, n_occ + t] ) * K[0, j*n_virt + t] * K[1, i*n_virt + t] * K[2, j*n_virt + s]

										elif ((t != s) and (u != s) and (u != t) and (v == s)):

											L4[i*n_virt + s + n_ex] += (-2 * g[j, n_occ + t, j, n_occ + u] ) * K[0, j*n_virt + t] * K[1, i*n_virt + u] * K[2, j*n_virt + s]

									elif ((j != i) and (k == i) and (m != i) and (m != j) and (m != k)):

										if ((t == s) and (u == s) and (v == s)):

											L4[i*n_virt + s + n_ex] += (-4 * g[j, n_occ + s, m, n_occ + s] ) * K[0, j*n_virt + s] * K[1, i*n_virt + s] * K[2, m*n_virt + s]

										elif ((t == s) and (u == s) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s + n_ex] += (-4 * g[j, n_occ + s, m, n_occ + v] + 2 * g[j, n_occ + v, m, n_occ + s] ) * K[0, j*n_virt + s] * K[1, i*n_virt + s] * K[2, m*n_virt + v]

										elif ((t == s) and (u != s) and (u != t) and (v == s)):

											L4[i*n_virt + s + n_ex] += (-2 * g[j, n_occ + s, m, n_occ + u] + -2 * g[j, n_occ + u, m, n_occ + s] ) * K[0, j*n_virt + s] * K[1, i*n_virt + u] * K[2, m*n_virt + s]

										elif ((t == s) and (u != s) and (u != t) and (v == u)):

											L4[i*n_virt + s + n_ex] += (-2 * g[j, n_occ + u, m, n_occ + u] ) * K[0, j*n_virt + s] * K[1, i*n_virt + u] * K[2, m*n_virt + u]

										elif ((t == s) and (u != s) and (u != t) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s + n_ex] += (-4 * g[j, n_occ + u, m, n_occ + v] + 2 * g[j, n_occ + v, m, n_occ + u] ) * K[0, j*n_virt + s] * K[1, i*n_virt + u] * K[2, m*n_virt + v]

										elif ((t != s) and (u == s) and (v == s)):

											L4[i*n_virt + s + n_ex] += (2 * g[j, n_occ + s, m, n_occ + t] + -4 * g[j, n_occ + t, m, n_occ + s] ) * K[0, j*n_virt + t] * K[1, i*n_virt + s] * K[2, m*n_virt + s]

										elif ((t != s) and (u == t) and (v == s)):

											L4[i*n_virt + s + n_ex] += (-2 * g[j, n_occ + t, m, n_occ + t] ) * K[0, j*n_virt + t] * K[1, i*n_virt + t] * K[2, m*n_virt + s]

										elif ((t != s) and (u != s) and (u != t) and (v == s)):

											L4[i*n_virt + s + n_ex] += (-4 * g[j, n_occ + t, m, n_occ + u] + 2 * g[j, n_occ + u, m, n_occ + t] ) * K[0, j*n_virt + t] * K[1, i*n_virt + u] * K[2, m*n_virt + s]

									elif ((j != i) and (k == j) and (m == i)):

										if ((t == s) and (u == s) and (v == s)):

											L4[i*n_virt + s + n_ex] += (-4 * g[j, n_occ + s, j, n_occ + s] ) * K[0, j*n_virt + s] * K[1, j*n_virt + s] * K[2, i*n_virt + s]

										elif ((t == s) and (u == s) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s + n_ex] += (-4 * g[j, n_occ + s, j, n_occ + v] ) * K[0, j*n_virt + s] * K[1, j*n_virt + s] * K[2, i*n_virt + v]

										elif ((t == s) and (u != s) and (u != t) and (v == s)):

											L4[i*n_virt + s + n_ex] += (-2 * g[j, n_occ + s, j, n_occ + u] ) * K[0, j*n_virt + s] * K[1, j*n_virt + u] * K[2, i*n_virt + s]

										elif ((t == s) and (u != s) and (u != t) and (v == u)):

											L4[i*n_virt + s + n_ex] += (-2 * g[j, n_occ + u, j, n_occ + u] ) * K[0, j*n_virt + s] * K[1, j*n_virt + u] * K[2, i*n_virt + u]

										elif ((t == s) and (u != s) and (u != t) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s + n_ex] += (-2 * g[j, n_occ + u, j, n_occ + v] ) * K[0, j*n_virt + s] * K[1, j*n_virt + u] * K[2, i*n_virt + v]

										elif ((t != s) and (u == s) and (v == s)):

											L4[i*n_virt + s + n_ex] += (-2 * g[j, n_occ + s, j, n_occ + t] ) * K[0, j*n_virt + t] * K[1, j*n_virt + s] * K[2, i*n_virt + s]

										elif ((t != s) and (u == s) and (v == t)):

											L4[i*n_virt + s + n_ex] += (-2 * g[j, n_occ + t, j, n_occ + t] ) * K[0, j*n_virt + t] * K[1, j*n_virt + s] * K[2, i*n_virt + t]

										elif ((t != s) and (u == s) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s + n_ex] += (-2 * g[j, n_occ + t, j, n_occ + v] ) * K[0, j*n_virt + t] * K[1, j*n_virt + s] * K[2, i*n_virt + v]

									elif ((j != i) and (k != i) and (k != j) and (m == i)):

										if ((t == s) and (u == s) and (v == s)):

											L4[i*n_virt + s + n_ex] += (-4 * g[j, n_occ + s, k, n_occ + s] ) * K[0, j*n_virt + s] * K[1, k*n_virt + s] * K[2, i*n_virt + s]

										elif ((t == s) and (u == s) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s + n_ex] += (-2 * g[j, n_occ + s, k, n_occ + v] + -2 * g[j, n_occ + v, k, n_occ + s] ) * K[0, j*n_virt + s] * K[1, k*n_virt + s] * K[2, i*n_virt + v]

										elif ((t == s) and (u != s) and (u != t) and (v == s)):

											L4[i*n_virt + s + n_ex] += (-4 * g[j, n_occ + s, k, n_occ + u] + 2 * g[j, n_occ + u, k, n_occ + s] ) * K[0, j*n_virt + s] * K[1, k*n_virt + u] * K[2, i*n_virt + s]

										elif ((t == s) and (u != s) and (u != t) and (v == u)):

											L4[i*n_virt + s + n_ex] += (-2 * g[j, n_occ + u, k, n_occ + u] ) * K[0, j*n_virt + s] * K[1, k*n_virt + u] * K[2, i*n_virt + u]

										elif ((t == s) and (u != s) and (u != t) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s + n_ex] += (2 * g[j, n_occ + u, k, n_occ + v] + -4 * g[j, n_occ + v, k, n_occ + u] ) * K[0, j*n_virt + s] * K[1, k*n_virt + u] * K[2, i*n_virt + v]

										elif ((t != s) and (u == s) and (v == s)):

											L4[i*n_virt + s + n_ex] += (2 * g[j, n_occ + s, k, n_occ + t] + -4 * g[j, n_occ + t, k, n_occ + s] ) * K[0, j*n_virt + t] * K[1, k*n_virt + s] * K[2, i*n_virt + s]

										elif ((t != s) and (u == s) and (v == t)):

											L4[i*n_virt + s + n_ex] += (-2 * g[j, n_occ + t, k, n_occ + t] ) * K[0, j*n_virt + t] * K[1, k*n_virt + s] * K[2, i*n_virt + t]

										elif ((t != s) and (u == s) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s + n_ex] += (-4 * g[j, n_occ + t, k, n_occ + v] + 2 * g[j, n_occ + v, k, n_occ + t] ) * K[0, j*n_virt + t] * K[1, k*n_virt + s] * K[2, i*n_virt + v]

	# Current operator combination: {'a': 1, 'b': 1, 'c': 1, 'd': 3}
	# All terms vanished for this combination

	# Current operator combination: {'a': 1, 'b': 1, 'c': 2, 'd': 1}
	# All terms vanished for this combination

	# Current operator combination: {'a': 1, 'b': 1, 'c': 2, 'd': 2}
	for i in range(n_occ):
		for j in range(n_occ):
			for k in range(n_occ):
				for m in range(n_occ):
					for s in range(n_virt):
						for t in range(n_virt):
							for u in range(n_virt):
								for v in range(n_virt):

									if ((j == i) and (k == i) and (m == i)):

										if ((t == s) and (u == s) and (v == s)):

											L4[i*n_virt + s + n_ex] += (4 * F[i, i] + -4 * F[n_occ + s, n_occ + s] + -4 * g[i, i, n_occ + s, n_occ + s] + -16 * g[i, n_occ + s, i, n_occ + s] + 4 * g[n_occ + s, n_occ + s, n_occ + s, n_occ + s] + 4 * g[i, i, i, i] ) * K[0, i*n_virt + s + n_ex] * K[1, i*n_virt + s] * K[2, i*n_virt + s]

										elif ((t == s) and (u == s) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s + n_ex] += (-2 * F[n_occ + s, n_occ + v] + 4 * g[n_occ + s, n_occ + s, n_occ + s, n_occ + v] + -2 * g[i, i, n_occ + s, n_occ + v] + -8 * g[i, n_occ + s, i, n_occ + v] ) * K[0, i*n_virt + s + n_ex] * K[1, i*n_virt + s] * K[2, i*n_virt + v]

										elif ((t == s) and (u != s) and (u != t) and (v == s)):

											L4[i*n_virt + s + n_ex] += (-2 * F[n_occ + s, n_occ + u] + -2 * g[i, i, n_occ + s, n_occ + u] + -8 * g[i, n_occ + s, i, n_occ + u] + 4 * g[n_occ + s, n_occ + s, n_occ + s, n_occ + u] ) * K[0, i*n_virt + s + n_ex] * K[1, i*n_virt + u] * K[2, i*n_virt + s]

										elif ((t == s) and (u != s) and (u != t) and (v == u)):

											L4[i*n_virt + s + n_ex] += (4 * g[n_occ + s, n_occ + u, n_occ + s, n_occ + u] ) * K[0, i*n_virt + s + n_ex] * K[1, i*n_virt + u] * K[2, i*n_virt + u]

										elif ((t == s) and (u != s) and (u != t) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s + n_ex] += (4 * g[n_occ + s, n_occ + u, n_occ + s, n_occ + v] ) * K[0, i*n_virt + s + n_ex] * K[1, i*n_virt + u] * K[2, i*n_virt + v]

										elif ((t != s) and (u == s) and (v == s)):

											L4[i*n_virt + s + n_ex] += (-4 * F[n_occ + s, n_occ + t] + 4 * g[n_occ + s, n_occ + s, n_occ + s, n_occ + t] + -12 * g[i, n_occ + s, i, n_occ + t] ) * K[0, i*n_virt + t + n_ex] * K[1, i*n_virt + s] * K[2, i*n_virt + s]

										elif ((t != s) and (u == s) and (v == t)):

											L4[i*n_virt + s + n_ex] += (2 * F[i, i] + -2 * F[n_occ + t, n_occ + t] + 2 * g[n_occ + s, n_occ + s, n_occ + t, n_occ + t] + 2 * g[n_occ + s, n_occ + t, n_occ + s, n_occ + t] + -6 * g[i, n_occ + t, i, n_occ + t] + -2 * g[i, i, n_occ + s, n_occ + s] + -2 * g[i, n_occ + s, i, n_occ + s] + 2 * g[i, i, i, i] ) * K[0, i*n_virt + t + n_ex] * K[1, i*n_virt + s] * K[2, i*n_virt + t]

										elif ((t != s) and (u == s) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s + n_ex] += (-2 * F[n_occ + t, n_occ + v] + 2 * g[n_occ + s, n_occ + t, n_occ + s, n_occ + v] + 2 * g[n_occ + s, n_occ + s, n_occ + t, n_occ + v] + -6 * g[i, n_occ + t, i, n_occ + v] ) * K[0, i*n_virt + t + n_ex] * K[1, i*n_virt + s] * K[2, i*n_virt + v]

										elif ((t != s) and (u == t) and (v == s)):

											L4[i*n_virt + s + n_ex] += (2 * F[i, i] + -2 * F[n_occ + t, n_occ + t] + 2 * g[n_occ + s, n_occ + s, n_occ + t, n_occ + t] + 2 * g[n_occ + s, n_occ + t, n_occ + s, n_occ + t] + -6 * g[i, n_occ + t, i, n_occ + t] + -2 * g[i, i, n_occ + s, n_occ + s] + -2 * g[i, n_occ + s, i, n_occ + s] + 2 * g[i, i, i, i] ) * K[0, i*n_virt + t + n_ex] * K[1, i*n_virt + t] * K[2, i*n_virt + s]

										elif ((t != s) and (u == t) and (v == t)):

											L4[i*n_virt + s + n_ex] += (4 * g[n_occ + s, n_occ + t, n_occ + t, n_occ + t] + -4 * g[i, n_occ + s, i, n_occ + t] + -4 * g[i, i, n_occ + s, n_occ + t] ) * K[0, i*n_virt + t + n_ex] * K[1, i*n_virt + t] * K[2, i*n_virt + t]

										elif ((t != s) and (u == t) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s + n_ex] += (2 * g[n_occ + s, n_occ + v, n_occ + t, n_occ + t] + 2 * g[n_occ + s, n_occ + t, n_occ + t, n_occ + v] + -2 * g[i, i, n_occ + s, n_occ + v] + -2 * g[i, n_occ + s, i, n_occ + v] ) * K[0, i*n_virt + t + n_ex] * K[1, i*n_virt + t] * K[2, i*n_virt + v]

										elif ((t != s) and (u != s) and (u != t) and (v == s)):

											L4[i*n_virt + s + n_ex] += (-2 * F[n_occ + t, n_occ + u] + 2 * g[n_occ + s, n_occ + s, n_occ + t, n_occ + u] + 2 * g[n_occ + s, n_occ + t, n_occ + s, n_occ + u] + -6 * g[i, n_occ + t, i, n_occ + u] ) * K[0, i*n_virt + t + n_ex] * K[1, i*n_virt + u] * K[2, i*n_virt + s]

										elif ((t != s) and (u != s) and (u != t) and (v == t)):

											L4[i*n_virt + s + n_ex] += (2 * g[n_occ + s, n_occ + t, n_occ + t, n_occ + u] + 2 * g[n_occ + s, n_occ + u, n_occ + t, n_occ + t] + -2 * g[i, n_occ + s, i, n_occ + u] + -2 * g[i, i, n_occ + s, n_occ + u] ) * K[0, i*n_virt + t + n_ex] * K[1, i*n_virt + u] * K[2, i*n_virt + t]

										elif ((t != s) and (u != s) and (u != t) and (v == u)):

											L4[i*n_virt + s + n_ex] += (4 * g[n_occ + s, n_occ + u, n_occ + t, n_occ + u] ) * K[0, i*n_virt + t + n_ex] * K[1, i*n_virt + u] * K[2, i*n_virt + u]

										elif ((t != s) and (u != s) and (u != t) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s + n_ex] += (2 * g[n_occ + s, n_occ + v, n_occ + t, n_occ + u] + 2 * g[n_occ + s, n_occ + u, n_occ + t, n_occ + v] ) * K[0, i*n_virt + t + n_ex] * K[1, i*n_virt + u] * K[2, i*n_virt + v]

									elif ((j == i) and (k == i) and (m != i) and (m != j) and (m != k)):

										if ((t == s) and (u == s) and (v == s)):

											L4[i*n_virt + s + n_ex] += (2 * F[i, m] + -2 * g[i, m, n_occ + s, n_occ + s] + 4 * g[i, i, i, m] + -8 * g[i, n_occ + s, m, n_occ + s] ) * K[0, i*n_virt + s + n_ex] * K[1, i*n_virt + s] * K[2, m*n_virt + s]

										elif ((t == s) and (u == s) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s + n_ex] += (4 * g[i, m, n_occ + s, n_occ + v] + -8 * g[i, n_occ + s, m, n_occ + v] ) * K[0, i*n_virt + s + n_ex] * K[1, i*n_virt + s] * K[2, m*n_virt + v]

										elif ((t == s) and (u != s) and (u != t) and (v == s)):

											L4[i*n_virt + s + n_ex] += (-6 * g[i, m, n_occ + s, n_occ + u] ) * K[0, i*n_virt + s + n_ex] * K[1, i*n_virt + u] * K[2, m*n_virt + s]

										elif ((t != s) and (u == s) and (v == s)):

											L4[i*n_virt + s + n_ex] += (-6 * g[i, n_occ + t, m, n_occ + s] ) * K[0, i*n_virt + t + n_ex] * K[1, i*n_virt + s] * K[2, m*n_virt + s]

										elif ((t != s) and (u == s) and (v == t)):

											L4[i*n_virt + s + n_ex] += (-4 * g[i, m, n_occ + s, n_occ + s] + 2 * g[i, i, i, m] + -4 * g[i, n_occ + t, m, n_occ + t] + 2 * g[i, m, n_occ + t, n_occ + t] + 2 * g[i, n_occ + s, m, n_occ + s] ) * K[0, i*n_virt + t + n_ex] * K[1, i*n_virt + s] * K[2, m*n_virt + t]

										elif ((t != s) and (u == s) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s + n_ex] += (2 * g[i, m, n_occ + t, n_occ + v] + -4 * g[i, n_occ + t, m, n_occ + v] ) * K[0, i*n_virt + t + n_ex] * K[1, i*n_virt + s] * K[2, m*n_virt + v]

										elif ((t != s) and (u == t) and (v == s)):

											L4[i*n_virt + s + n_ex] += (2 * F[i, m] + -2 * g[i, n_occ + t, m, n_occ + t] + -2 * g[i, m, n_occ + t, n_occ + t] + -4 * g[i, n_occ + s, m, n_occ + s] + 2 * g[i, m, n_occ + s, n_occ + s] + 2 * g[i, i, i, m] ) * K[0, i*n_virt + t + n_ex] * K[1, i*n_virt + t] * K[2, m*n_virt + s]

										elif ((t != s) and (u == t) and (v == t)):

											L4[i*n_virt + s + n_ex] += (-2 * g[i, m, n_occ + s, n_occ + t] + -2 * g[i, n_occ + s, m, n_occ + t] ) * K[0, i*n_virt + t + n_ex] * K[1, i*n_virt + t] * K[2, m*n_virt + t]

										elif ((t != s) and (u == t) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s + n_ex] += (-4 * g[i, n_occ + s, m, n_occ + v] + 2 * g[i, m, n_occ + s, n_occ + v] ) * K[0, i*n_virt + t + n_ex] * K[1, i*n_virt + t] * K[2, m*n_virt + v]

										elif ((t != s) and (u != s) and (u != t) and (v == s)):

											L4[i*n_virt + s + n_ex] += (-2 * g[i, n_occ + t, m, n_occ + u] + -2 * g[i, m, n_occ + t, n_occ + u] ) * K[0, i*n_virt + t + n_ex] * K[1, i*n_virt + u] * K[2, m*n_virt + s]

										elif ((t != s) and (u != s) and (u != t) and (v == t)):

											L4[i*n_virt + s + n_ex] += (-4 * g[i, m, n_occ + s, n_occ + u] + 2 * g[i, n_occ + s, m, n_occ + u] ) * K[0, i*n_virt + t + n_ex] * K[1, i*n_virt + u] * K[2, m*n_virt + t]

									elif ((j == i) and (k != i) and (k != j) and (m == i)):

										if ((t == s) and (u == s) and (v == s)):

											L4[i*n_virt + s + n_ex] += (2 * F[i, k] + -8 * g[i, n_occ + s, k, n_occ + s] + 4 * g[i, i, i, k] + -2 * g[i, k, n_occ + s, n_occ + s] ) * K[0, i*n_virt + s + n_ex] * K[1, k*n_virt + s] * K[2, i*n_virt + s]

										elif ((t == s) and (u == s) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s + n_ex] += (-6 * g[i, k, n_occ + s, n_occ + v] ) * K[0, i*n_virt + s + n_ex] * K[1, k*n_virt + s] * K[2, i*n_virt + v]

										elif ((t == s) and (u != s) and (u != t) and (v == s)):

											L4[i*n_virt + s + n_ex] += (4 * g[i, k, n_occ + s, n_occ + u] + -8 * g[i, n_occ + s, k, n_occ + u] ) * K[0, i*n_virt + s + n_ex] * K[1, k*n_virt + u] * K[2, i*n_virt + s]

										elif ((t != s) and (u == s) and (v == s)):

											L4[i*n_virt + s + n_ex] += (-6 * g[i, n_occ + t, k, n_occ + s] ) * K[0, i*n_virt + t + n_ex] * K[1, k*n_virt + s] * K[2, i*n_virt + s]

										elif ((t != s) and (u == s) and (v == t)):

											L4[i*n_virt + s + n_ex] += (2 * F[i, k] + -2 * g[i, n_occ + t, k, n_occ + t] + -2 * g[i, k, n_occ + t, n_occ + t] + -4 * g[i, n_occ + s, k, n_occ + s] + 2 * g[i, k, n_occ + s, n_occ + s] + 2 * g[i, i, i, k] ) * K[0, i*n_virt + t + n_ex] * K[1, k*n_virt + s] * K[2, i*n_virt + t]

										elif ((t != s) and (u == s) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s + n_ex] += (-2 * g[i, n_occ + t, k, n_occ + v] + -2 * g[i, k, n_occ + t, n_occ + v] ) * K[0, i*n_virt + t + n_ex] * K[1, k*n_virt + s] * K[2, i*n_virt + v]

										elif ((t != s) and (u == t) and (v == s)):

											L4[i*n_virt + s + n_ex] += (-4 * g[i, k, n_occ + s, n_occ + s] + 2 * g[i, i, i, k] + -4 * g[i, n_occ + t, k, n_occ + t] + 2 * g[i, k, n_occ + t, n_occ + t] + 2 * g[i, n_occ + s, k, n_occ + s] ) * K[0, i*n_virt + t + n_ex] * K[1, k*n_virt + t] * K[2, i*n_virt + s]

										elif ((t != s) and (u == t) and (v == t)):

											L4[i*n_virt + s + n_ex] += (-2 * g[i, k, n_occ + s, n_occ + t] + -2 * g[i, n_occ + s, k, n_occ + t] ) * K[0, i*n_virt + t + n_ex] * K[1, k*n_virt + t] * K[2, i*n_virt + t]

										elif ((t != s) and (u == t) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s + n_ex] += (-4 * g[i, k, n_occ + s, n_occ + v] + 2 * g[i, n_occ + s, k, n_occ + v] ) * K[0, i*n_virt + t + n_ex] * K[1, k*n_virt + t] * K[2, i*n_virt + v]

										elif ((t != s) and (u != s) and (u != t) and (v == s)):

											L4[i*n_virt + s + n_ex] += (2 * g[i, k, n_occ + t, n_occ + u] + -4 * g[i, n_occ + t, k, n_occ + u] ) * K[0, i*n_virt + t + n_ex] * K[1, k*n_virt + u] * K[2, i*n_virt + s]

										elif ((t != s) and (u != s) and (u != t) and (v == t)):

											L4[i*n_virt + s + n_ex] += (-4 * g[i, n_occ + s, k, n_occ + u] + 2 * g[i, k, n_occ + s, n_occ + u] ) * K[0, i*n_virt + t + n_ex] * K[1, k*n_virt + u] * K[2, i*n_virt + t]

									elif ((j == i) and (k != i) and (k != j) and (m == k)):

										if ((t == s) and (u == s) and (v == s)):

											L4[i*n_virt + s + n_ex] += (4 * g[i, k, i, k] ) * K[0, i*n_virt + s + n_ex] * K[1, k*n_virt + s] * K[2, k*n_virt + s]

										elif ((t != s) and (u == s) and (v == t)):

											L4[i*n_virt + s + n_ex] += (2 * g[i, k, i, k] ) * K[0, i*n_virt + t + n_ex] * K[1, k*n_virt + s] * K[2, k*n_virt + t]

										elif ((t != s) and (u == t) and (v == s)):

											L4[i*n_virt + s + n_ex] += (2 * g[i, k, i, k] ) * K[0, i*n_virt + t + n_ex] * K[1, k*n_virt + t] * K[2, k*n_virt + s]

									elif ((j == i) and (k != i) and (k != j) and (m != i) and (m != j) and (m != k)):

										if ((t == s) and (u == s) and (v == s)):

											L4[i*n_virt + s + n_ex] += (4 * g[i, k, i, m] ) * K[0, i*n_virt + s + n_ex] * K[1, k*n_virt + s] * K[2, m*n_virt + s]

										elif ((t != s) and (u == s) and (v == t)):

											L4[i*n_virt + s + n_ex] += (2 * g[i, k, i, m] ) * K[0, i*n_virt + t + n_ex] * K[1, k*n_virt + s] * K[2, m*n_virt + t]

										elif ((t != s) and (u == t) and (v == s)):

											L4[i*n_virt + s + n_ex] += (2 * g[i, k, i, m] ) * K[0, i*n_virt + t + n_ex] * K[1, k*n_virt + t] * K[2, m*n_virt + s]

									elif ((j != i) and (k == i) and (m == i)):

										if ((t == s) and (u == s) and (v == s)):

											L4[i*n_virt + s + n_ex] += (4 * F[i, j] + -12 * g[i, n_occ + s, j, n_occ + s] + 4 * g[i, i, i, j] ) * K[0, j*n_virt + s + n_ex] * K[1, i*n_virt + s] * K[2, i*n_virt + s]

										elif ((t == s) and (u == s) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s + n_ex] += (-6 * g[i, n_occ + v, j, n_occ + s] ) * K[0, j*n_virt + s + n_ex] * K[1, i*n_virt + s] * K[2, i*n_virt + v]

										elif ((t == s) and (u != s) and (u != t) and (v == s)):

											L4[i*n_virt + s + n_ex] += (-6 * g[i, n_occ + u, j, n_occ + s] ) * K[0, j*n_virt + s + n_ex] * K[1, i*n_virt + u] * K[2, i*n_virt + s]

										elif ((t != s) and (u == s) and (v == s)):

											L4[i*n_virt + s + n_ex] += (4 * g[i, j, n_occ + s, n_occ + t] + -8 * g[i, n_occ + s, j, n_occ + t] ) * K[0, j*n_virt + t + n_ex] * K[1, i*n_virt + s] * K[2, i*n_virt + s]

										elif ((t != s) and (u == s) and (v == t)):

											L4[i*n_virt + s + n_ex] += (2 * F[i, j] + -2 * g[i, n_occ + s, j, n_occ + s] + -2 * g[i, j, n_occ + s, n_occ + s] + -4 * g[i, n_occ + t, j, n_occ + t] + 2 * g[i, j, n_occ + t, n_occ + t] + 2 * g[i, i, i, j] ) * K[0, j*n_virt + t + n_ex] * K[1, i*n_virt + s] * K[2, i*n_virt + t]

										elif ((t != s) and (u == s) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s + n_ex] += (2 * g[i, j, n_occ + t, n_occ + v] + -4 * g[i, n_occ + v, j, n_occ + t] ) * K[0, j*n_virt + t + n_ex] * K[1, i*n_virt + s] * K[2, i*n_virt + v]

										elif ((t != s) and (u == t) and (v == s)):

											L4[i*n_virt + s + n_ex] += (2 * F[i, j] + -2 * g[i, n_occ + s, j, n_occ + s] + -2 * g[i, j, n_occ + s, n_occ + s] + -4 * g[i, n_occ + t, j, n_occ + t] + 2 * g[i, j, n_occ + t, n_occ + t] + 2 * g[i, i, i, j] ) * K[0, j*n_virt + t + n_ex] * K[1, i*n_virt + t] * K[2, i*n_virt + s]

										elif ((t != s) and (u == t) and (v == t)):

											L4[i*n_virt + s + n_ex] += (-4 * g[i, n_occ + t, j, n_occ + s] + -4 * g[i, j, n_occ + s, n_occ + t] ) * K[0, j*n_virt + t + n_ex] * K[1, i*n_virt + t] * K[2, i*n_virt + t]

										elif ((t != s) and (u == t) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s + n_ex] += (-2 * g[i, n_occ + v, j, n_occ + s] + -2 * g[i, j, n_occ + s, n_occ + v] ) * K[0, j*n_virt + t + n_ex] * K[1, i*n_virt + t] * K[2, i*n_virt + v]

										elif ((t != s) and (u != s) and (u != t) and (v == s)):

											L4[i*n_virt + s + n_ex] += (2 * g[i, j, n_occ + t, n_occ + u] + -4 * g[i, n_occ + u, j, n_occ + t] ) * K[0, j*n_virt + t + n_ex] * K[1, i*n_virt + u] * K[2, i*n_virt + s]

										elif ((t != s) and (u != s) and (u != t) and (v == t)):

											L4[i*n_virt + s + n_ex] += (-2 * g[i, n_occ + u, j, n_occ + s] + -2 * g[i, j, n_occ + s, n_occ + u] ) * K[0, j*n_virt + t + n_ex] * K[1, i*n_virt + u] * K[2, i*n_virt + t]

									elif ((j != i) and (k == i) and (m == j)):

										if ((t == s) and (u == s) and (v == s)):

											L4[i*n_virt + s + n_ex] += (2 * F[j, j] + -2 * F[n_occ + s, n_occ + s] + 2 * g[n_occ + s, n_occ + s, n_occ + s, n_occ + s] + -6 * g[j, n_occ + s, j, n_occ + s] + -2 * g[i, i, n_occ + s, n_occ + s] + 2 * g[i, i, j, j] + 2 * g[i, j, i, j] + -2 * g[i, n_occ + s, i, n_occ + s] ) * K[0, j*n_virt + s + n_ex] * K[1, i*n_virt + s] * K[2, j*n_virt + s]

										elif ((t == s) and (u == s) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s + n_ex] += (2 * g[n_occ + s, n_occ + s, n_occ + s, n_occ + v] + -4 * g[i, i, n_occ + s, n_occ + v] + -4 * g[j, n_occ + s, j, n_occ + v] + 2 * g[i, n_occ + s, i, n_occ + v] + 2 * g[j, j, n_occ + s, n_occ + v] ) * K[0, j*n_virt + s + n_ex] * K[1, i*n_virt + s] * K[2, j*n_virt + v]

										elif ((t == s) and (u != s) and (u != t) and (v == s)):

											L4[i*n_virt + s + n_ex] += (-2 * F[n_occ + s, n_occ + u] + 2 * g[n_occ + s, n_occ + s, n_occ + s, n_occ + u] + -2 * g[j, j, n_occ + s, n_occ + u] + -4 * g[i, n_occ + s, i, n_occ + u] + 2 * g[i, i, n_occ + s, n_occ + u] + -2 * g[j, n_occ + s, j, n_occ + u] ) * K[0, j*n_virt + s + n_ex] * K[1, i*n_virt + u] * K[2, j*n_virt + s]

										elif ((t == s) and (u != s) and (u != t) and (v == u)):

											L4[i*n_virt + s + n_ex] += (2 * g[n_occ + s, n_occ + u, n_occ + s, n_occ + u] ) * K[0, j*n_virt + s + n_ex] * K[1, i*n_virt + u] * K[2, j*n_virt + u]

										elif ((t == s) and (u != s) and (u != t) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s + n_ex] += (2 * g[n_occ + s, n_occ + u, n_occ + s, n_occ + v] ) * K[0, j*n_virt + s + n_ex] * K[1, i*n_virt + u] * K[2, j*n_virt + v]

										elif ((t != s) and (u == s) and (v == s)):

											L4[i*n_virt + s + n_ex] += (-2 * F[n_occ + s, n_occ + t] + 2 * g[n_occ + s, n_occ + s, n_occ + s, n_occ + t] + -2 * g[i, i, n_occ + s, n_occ + t] + 2 * g[j, j, n_occ + s, n_occ + t] + -4 * g[j, n_occ + s, j, n_occ + t] + -2 * g[i, n_occ + s, i, n_occ + t] ) * K[0, j*n_virt + t + n_ex] * K[1, i*n_virt + s] * K[2, j*n_virt + s]

										elif ((t != s) and (u == s) and (v == t)):

											L4[i*n_virt + s + n_ex] += (-2 * g[n_occ + s, n_occ + t, n_occ + s, n_occ + t] + 4 * g[n_occ + s, n_occ + s, n_occ + t, n_occ + t] + 2 * g[i, n_occ + t, i, n_occ + t] + -4 * g[i, i, n_occ + t, n_occ + t] + -4 * g[j, j, n_occ + s, n_occ + s] + 2 * g[j, n_occ + s, j, n_occ + s] + -2 * g[i, j, i, j] + 4 * g[i, i, j, j] ) * K[0, j*n_virt + t + n_ex] * K[1, i*n_virt + s] * K[2, j*n_virt + t]

										elif ((t != s) and (u == s) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s + n_ex] += (-2 * g[n_occ + s, n_occ + t, n_occ + s, n_occ + v] + 4 * g[n_occ + s, n_occ + s, n_occ + t, n_occ + v] + 2 * g[i, n_occ + t, i, n_occ + v] + -4 * g[i, i, n_occ + t, n_occ + v] ) * K[0, j*n_virt + t + n_ex] * K[1, i*n_virt + s] * K[2, j*n_virt + v]

										elif ((t != s) and (u == t) and (v == s)):

											L4[i*n_virt + s + n_ex] += (2 * F[j, j] + -2 * F[n_occ + t, n_occ + t] + 4 * g[n_occ + s, n_occ + t, n_occ + s, n_occ + t] + -2 * g[n_occ + s, n_occ + s, n_occ + t, n_occ + t] + 2 * g[i, i, n_occ + t, n_occ + t] + 2 * g[j, j, n_occ + t, n_occ + t] + -2 * g[i, i, j, j] + -4 * g[i, n_occ + t, i, n_occ + t] + -4 * g[j, n_occ + s, j, n_occ + s] + -4 * g[j, n_occ + t, j, n_occ + t] + 2 * g[j, j, n_occ + s, n_occ + s] + 4 * g[i, j, i, j] ) * K[0, j*n_virt + t + n_ex] * K[1, i*n_virt + t] * K[2, j*n_virt + s]

										elif ((t != s) and (u == t) and (v == t)):

											L4[i*n_virt + s + n_ex] += (2 * g[n_occ + s, n_occ + t, n_occ + t, n_occ + t] + -2 * g[j, n_occ + s, j, n_occ + t] + -2 * g[j, j, n_occ + s, n_occ + t] ) * K[0, j*n_virt + t + n_ex] * K[1, i*n_virt + t] * K[2, j*n_virt + t]

										elif ((t != s) and (u == t) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s + n_ex] += (4 * g[n_occ + s, n_occ + t, n_occ + t, n_occ + v] + -2 * g[n_occ + s, n_occ + v, n_occ + t, n_occ + t] + -4 * g[j, n_occ + s, j, n_occ + v] + 2 * g[j, j, n_occ + s, n_occ + v] ) * K[0, j*n_virt + t + n_ex] * K[1, i*n_virt + t] * K[2, j*n_virt + v]

										elif ((t != s) and (u != s) and (u != t) and (v == s)):

											L4[i*n_virt + s + n_ex] += (-2 * F[n_occ + t, n_occ + u] + 4 * g[n_occ + s, n_occ + t, n_occ + s, n_occ + u] + -2 * g[n_occ + s, n_occ + s, n_occ + t, n_occ + u] + 2 * g[i, i, n_occ + t, n_occ + u] + 2 * g[j, j, n_occ + t, n_occ + u] + -4 * g[i, n_occ + t, i, n_occ + u] + -4 * g[j, n_occ + t, j, n_occ + u] ) * K[0, j*n_virt + t + n_ex] * K[1, i*n_virt + u] * K[2, j*n_virt + s]

										elif ((t != s) and (u != s) and (u != t) and (v == t)):

											L4[i*n_virt + s + n_ex] += (-2 * g[n_occ + s, n_occ + t, n_occ + t, n_occ + u] + 4 * g[n_occ + s, n_occ + u, n_occ + t, n_occ + t] + 2 * g[j, n_occ + s, j, n_occ + u] + -4 * g[j, j, n_occ + s, n_occ + u] ) * K[0, j*n_virt + t + n_ex] * K[1, i*n_virt + u] * K[2, j*n_virt + t]

										elif ((t != s) and (u != s) and (u != t) and (v == u)):

											L4[i*n_virt + s + n_ex] += (2 * g[n_occ + s, n_occ + u, n_occ + t, n_occ + u] ) * K[0, j*n_virt + t + n_ex] * K[1, i*n_virt + u] * K[2, j*n_virt + u]

										elif ((t != s) and (u != s) and (u != t) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s + n_ex] += (4 * g[n_occ + s, n_occ + u, n_occ + t, n_occ + v] + -2 * g[n_occ + s, n_occ + v, n_occ + t, n_occ + u] ) * K[0, j*n_virt + t + n_ex] * K[1, i*n_virt + u] * K[2, j*n_virt + v]

									elif ((j != i) and (k == i) and (m != i) and (m != j) and (m != k)):

										if ((t == s) and (u == s) and (v == s)):

											L4[i*n_virt + s + n_ex] += (2 * F[j, m] + -6 * g[j, n_occ + s, m, n_occ + s] + 2 * g[i, i, j, m] + 2 * g[i, j, i, m] ) * K[0, j*n_virt + s + n_ex] * K[1, i*n_virt + s] * K[2, m*n_virt + s]

										elif ((t == s) and (u == s) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s + n_ex] += (2 * g[j, m, n_occ + s, n_occ + v] + -4 * g[j, n_occ + s, m, n_occ + v] ) * K[0, j*n_virt + s + n_ex] * K[1, i*n_virt + s] * K[2, m*n_virt + v]

										elif ((t == s) and (u != s) and (u != t) and (v == s)):

											L4[i*n_virt + s + n_ex] += (-2 * g[j, n_occ + s, m, n_occ + u] + -2 * g[j, m, n_occ + s, n_occ + u] ) * K[0, j*n_virt + s + n_ex] * K[1, i*n_virt + u] * K[2, m*n_virt + s]

										elif ((t != s) and (u == s) and (v == s)):

											L4[i*n_virt + s + n_ex] += (2 * g[j, m, n_occ + s, n_occ + t] + -4 * g[j, n_occ + t, m, n_occ + s] ) * K[0, j*n_virt + t + n_ex] * K[1, i*n_virt + s] * K[2, m*n_virt + s]

										elif ((t != s) and (u == s) and (v == t)):

											L4[i*n_virt + s + n_ex] += (2 * g[j, n_occ + s, m, n_occ + s] + -4 * g[j, m, n_occ + s, n_occ + s] + -2 * g[i, j, i, m] + 4 * g[i, i, j, m] ) * K[0, j*n_virt + t + n_ex] * K[1, i*n_virt + s] * K[2, m*n_virt + t]

										elif ((t != s) and (u == t) and (v == s)):

											L4[i*n_virt + s + n_ex] += (2 * F[j, m] + -4 * g[j, n_occ + s, m, n_occ + s] + -4 * g[j, n_occ + t, m, n_occ + t] + 2 * g[j, m, n_occ + s, n_occ + s] + 2 * g[j, m, n_occ + t, n_occ + t] + -2 * g[i, i, j, m] + 4 * g[i, j, i, m] ) * K[0, j*n_virt + t + n_ex] * K[1, i*n_virt + t] * K[2, m*n_virt + s]

										elif ((t != s) and (u == t) and (v == t)):

											L4[i*n_virt + s + n_ex] += (-2 * g[j, n_occ + s, m, n_occ + t] + -2 * g[j, m, n_occ + s, n_occ + t] ) * K[0, j*n_virt + t + n_ex] * K[1, i*n_virt + t] * K[2, m*n_virt + t]

										elif ((t != s) and (u == t) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s + n_ex] += (2 * g[j, m, n_occ + s, n_occ + v] + -4 * g[j, n_occ + s, m, n_occ + v] ) * K[0, j*n_virt + t + n_ex] * K[1, i*n_virt + t] * K[2, m*n_virt + v]

										elif ((t != s) and (u != s) and (u != t) and (v == s)):

											L4[i*n_virt + s + n_ex] += (2 * g[j, m, n_occ + t, n_occ + u] + -4 * g[j, n_occ + t, m, n_occ + u] ) * K[0, j*n_virt + t + n_ex] * K[1, i*n_virt + u] * K[2, m*n_virt + s]

										elif ((t != s) and (u != s) and (u != t) and (v == t)):

											L4[i*n_virt + s + n_ex] += (-4 * g[j, m, n_occ + s, n_occ + u] + 2 * g[j, n_occ + s, m, n_occ + u] ) * K[0, j*n_virt + t + n_ex] * K[1, i*n_virt + u] * K[2, m*n_virt + t]

									elif ((j != i) and (k == j) and (m == i)):

										if ((t == s) and (u == s) and (v == s)):

											L4[i*n_virt + s + n_ex] += (2 * F[j, j] + -2 * F[n_occ + s, n_occ + s] + 2 * g[n_occ + s, n_occ + s, n_occ + s, n_occ + s] + -6 * g[j, n_occ + s, j, n_occ + s] + -2 * g[i, i, n_occ + s, n_occ + s] + 2 * g[i, i, j, j] + 2 * g[i, j, i, j] + -2 * g[i, n_occ + s, i, n_occ + s] ) * K[0, j*n_virt + s + n_ex] * K[1, j*n_virt + s] * K[2, i*n_virt + s]

										elif ((t == s) and (u == s) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s + n_ex] += (-2 * F[n_occ + s, n_occ + v] + 2 * g[n_occ + s, n_occ + s, n_occ + s, n_occ + v] + -2 * g[j, j, n_occ + s, n_occ + v] + -4 * g[i, n_occ + s, i, n_occ + v] + 2 * g[i, i, n_occ + s, n_occ + v] + -2 * g[j, n_occ + s, j, n_occ + v] ) * K[0, j*n_virt + s + n_ex] * K[1, j*n_virt + s] * K[2, i*n_virt + v]

										elif ((t == s) and (u != s) and (u != t) and (v == s)):

											L4[i*n_virt + s + n_ex] += (2 * g[n_occ + s, n_occ + s, n_occ + s, n_occ + u] + -4 * g[i, i, n_occ + s, n_occ + u] + -4 * g[j, n_occ + s, j, n_occ + u] + 2 * g[i, n_occ + s, i, n_occ + u] + 2 * g[j, j, n_occ + s, n_occ + u] ) * K[0, j*n_virt + s + n_ex] * K[1, j*n_virt + u] * K[2, i*n_virt + s]

										elif ((t == s) and (u != s) and (u != t) and (v == u)):

											L4[i*n_virt + s + n_ex] += (2 * g[n_occ + s, n_occ + u, n_occ + s, n_occ + u] ) * K[0, j*n_virt + s + n_ex] * K[1, j*n_virt + u] * K[2, i*n_virt + u]

										elif ((t == s) and (u != s) and (u != t) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s + n_ex] += (2 * g[n_occ + s, n_occ + u, n_occ + s, n_occ + v] ) * K[0, j*n_virt + s + n_ex] * K[1, j*n_virt + u] * K[2, i*n_virt + v]

										elif ((t != s) and (u == s) and (v == s)):

											L4[i*n_virt + s + n_ex] += (-2 * F[n_occ + s, n_occ + t] + 2 * g[n_occ + s, n_occ + s, n_occ + s, n_occ + t] + -2 * g[i, i, n_occ + s, n_occ + t] + 2 * g[j, j, n_occ + s, n_occ + t] + -4 * g[j, n_occ + s, j, n_occ + t] + -2 * g[i, n_occ + s, i, n_occ + t] ) * K[0, j*n_virt + t + n_ex] * K[1, j*n_virt + s] * K[2, i*n_virt + s]

										elif ((t != s) and (u == s) and (v == t)):

											L4[i*n_virt + s + n_ex] += (2 * F[j, j] + -2 * F[n_occ + t, n_occ + t] + 4 * g[n_occ + s, n_occ + t, n_occ + s, n_occ + t] + -2 * g[n_occ + s, n_occ + s, n_occ + t, n_occ + t] + 2 * g[i, i, n_occ + t, n_occ + t] + 2 * g[j, j, n_occ + t, n_occ + t] + -2 * g[i, i, j, j] + -4 * g[j, n_occ + s, j, n_occ + s] + -4 * g[i, n_occ + t, i, n_occ + t] + -4 * g[j, n_occ + t, j, n_occ + t] + 2 * g[j, j, n_occ + s, n_occ + s] + 4 * g[i, j, i, j] ) * K[0, j*n_virt + t + n_ex] * K[1, j*n_virt + s] * K[2, i*n_virt + t]

										elif ((t != s) and (u == s) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s + n_ex] += (-2 * F[n_occ + t, n_occ + v] + 4 * g[n_occ + s, n_occ + t, n_occ + s, n_occ + v] + -2 * g[n_occ + s, n_occ + s, n_occ + t, n_occ + v] + 2 * g[i, i, n_occ + t, n_occ + v] + 2 * g[j, j, n_occ + t, n_occ + v] + -4 * g[i, n_occ + t, i, n_occ + v] + -4 * g[j, n_occ + t, j, n_occ + v] ) * K[0, j*n_virt + t + n_ex] * K[1, j*n_virt + s] * K[2, i*n_virt + v]

										elif ((t != s) and (u == t) and (v == s)):

											L4[i*n_virt + s + n_ex] += (-2 * g[n_occ + s, n_occ + t, n_occ + s, n_occ + t] + 4 * g[n_occ + s, n_occ + s, n_occ + t, n_occ + t] + 2 * g[i, n_occ + t, i, n_occ + t] + -4 * g[i, i, n_occ + t, n_occ + t] + -4 * g[j, j, n_occ + s, n_occ + s] + 2 * g[j, n_occ + s, j, n_occ + s] + -2 * g[i, j, i, j] + 4 * g[i, i, j, j] ) * K[0, j*n_virt + t + n_ex] * K[1, j*n_virt + t] * K[2, i*n_virt + s]

										elif ((t != s) and (u == t) and (v == t)):

											L4[i*n_virt + s + n_ex] += (2 * g[n_occ + s, n_occ + t, n_occ + t, n_occ + t] + -2 * g[j, n_occ + s, j, n_occ + t] + -2 * g[j, j, n_occ + s, n_occ + t] ) * K[0, j*n_virt + t + n_ex] * K[1, j*n_virt + t] * K[2, i*n_virt + t]

										elif ((t != s) and (u == t) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s + n_ex] += (-2 * g[n_occ + s, n_occ + t, n_occ + t, n_occ + v] + 4 * g[n_occ + s, n_occ + v, n_occ + t, n_occ + t] + 2 * g[j, n_occ + s, j, n_occ + v] + -4 * g[j, j, n_occ + s, n_occ + v] ) * K[0, j*n_virt + t + n_ex] * K[1, j*n_virt + t] * K[2, i*n_virt + v]

										elif ((t != s) and (u != s) and (u != t) and (v == s)):

											L4[i*n_virt + s + n_ex] += (-2 * g[n_occ + s, n_occ + t, n_occ + s, n_occ + u] + 4 * g[n_occ + s, n_occ + s, n_occ + t, n_occ + u] + 2 * g[i, n_occ + t, i, n_occ + u] + -4 * g[i, i, n_occ + t, n_occ + u] ) * K[0, j*n_virt + t + n_ex] * K[1, j*n_virt + u] * K[2, i*n_virt + s]

										elif ((t != s) and (u != s) and (u != t) and (v == t)):

											L4[i*n_virt + s + n_ex] += (4 * g[n_occ + s, n_occ + t, n_occ + t, n_occ + u] + -2 * g[n_occ + s, n_occ + u, n_occ + t, n_occ + t] + -4 * g[j, n_occ + s, j, n_occ + u] + 2 * g[j, j, n_occ + s, n_occ + u] ) * K[0, j*n_virt + t + n_ex] * K[1, j*n_virt + u] * K[2, i*n_virt + t]

										elif ((t != s) and (u != s) and (u != t) and (v == u)):

											L4[i*n_virt + s + n_ex] += (2 * g[n_occ + s, n_occ + u, n_occ + t, n_occ + u] ) * K[0, j*n_virt + t + n_ex] * K[1, j*n_virt + u] * K[2, i*n_virt + u]

										elif ((t != s) and (u != s) and (u != t) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s + n_ex] += (-2 * g[n_occ + s, n_occ + u, n_occ + t, n_occ + v] + 4 * g[n_occ + s, n_occ + v, n_occ + t, n_occ + u] ) * K[0, j*n_virt + t + n_ex] * K[1, j*n_virt + u] * K[2, i*n_virt + v]

									elif ((j != i) and (k == j) and (m == j)):

										if ((t == s) and (u == s) and (v == s)):

											L4[i*n_virt + s + n_ex] += (-4 * g[i, j, n_occ + s, n_occ + s] + 4 * g[i, j, j, j] + -4 * g[i, n_occ + s, j, n_occ + s] ) * K[0, j*n_virt + s + n_ex] * K[1, j*n_virt + s] * K[2, j*n_virt + s]

										elif ((t == s) and (u == s) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s + n_ex] += (-2 * g[i, j, n_occ + s, n_occ + v] + -2 * g[i, n_occ + s, j, n_occ + v] ) * K[0, j*n_virt + s + n_ex] * K[1, j*n_virt + s] * K[2, j*n_virt + v]

										elif ((t == s) and (u != s) and (u != t) and (v == s)):

											L4[i*n_virt + s + n_ex] += (-2 * g[i, j, n_occ + s, n_occ + u] + -2 * g[i, n_occ + s, j, n_occ + u] ) * K[0, j*n_virt + s + n_ex] * K[1, j*n_virt + u] * K[2, j*n_virt + s]

										elif ((t != s) and (u == s) and (v == s)):

											L4[i*n_virt + s + n_ex] += (-4 * g[i, n_occ + t, j, n_occ + s] + -4 * g[i, j, n_occ + s, n_occ + t] ) * K[0, j*n_virt + t + n_ex] * K[1, j*n_virt + s] * K[2, j*n_virt + s]

										elif ((t != s) and (u == s) and (v == t)):

											L4[i*n_virt + s + n_ex] += (-2 * g[i, n_occ + t, j, n_occ + t] + -2 * g[i, j, n_occ + t, n_occ + t] + 2 * g[i, j, j, j] ) * K[0, j*n_virt + t + n_ex] * K[1, j*n_virt + s] * K[2, j*n_virt + t]

										elif ((t != s) and (u == s) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s + n_ex] += (-2 * g[i, n_occ + t, j, n_occ + v] + -2 * g[i, j, n_occ + t, n_occ + v] ) * K[0, j*n_virt + t + n_ex] * K[1, j*n_virt + s] * K[2, j*n_virt + v]

										elif ((t != s) and (u == t) and (v == s)):

											L4[i*n_virt + s + n_ex] += (-2 * g[i, n_occ + t, j, n_occ + t] + -2 * g[i, j, n_occ + t, n_occ + t] + 2 * g[i, j, j, j] ) * K[0, j*n_virt + t + n_ex] * K[1, j*n_virt + t] * K[2, j*n_virt + s]

										elif ((t != s) and (u != s) and (u != t) and (v == s)):

											L4[i*n_virt + s + n_ex] += (-2 * g[i, n_occ + t, j, n_occ + u] + -2 * g[i, j, n_occ + t, n_occ + u] ) * K[0, j*n_virt + t + n_ex] * K[1, j*n_virt + u] * K[2, j*n_virt + s]

									elif ((j != i) and (k == j) and (m != i) and (m != j) and (m != k)):

										if ((t == s) and (u == s) and (v == s)):

											L4[i*n_virt + s + n_ex] += (2 * g[i, j, j, m] + -2 * g[i, m, n_occ + s, n_occ + s] + -2 * g[i, n_occ + s, m, n_occ + s] + 2 * g[i, m, j, j] ) * K[0, j*n_virt + s + n_ex] * K[1, j*n_virt + s] * K[2, m*n_virt + s]

										elif ((t == s) and (u == s) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s + n_ex] += (-4 * g[i, n_occ + s, m, n_occ + v] + 2 * g[i, m, n_occ + s, n_occ + v] ) * K[0, j*n_virt + s + n_ex] * K[1, j*n_virt + s] * K[2, m*n_virt + v]

										elif ((t == s) and (u != s) and (u != t) and (v == s)):

											L4[i*n_virt + s + n_ex] += (-4 * g[i, m, n_occ + s, n_occ + u] + 2 * g[i, n_occ + s, m, n_occ + u] ) * K[0, j*n_virt + s + n_ex] * K[1, j*n_virt + u] * K[2, m*n_virt + s]

										elif ((t != s) and (u == s) and (v == s)):

											L4[i*n_virt + s + n_ex] += (-2 * g[i, n_occ + t, m, n_occ + s] + -2 * g[i, m, n_occ + s, n_occ + t] ) * K[0, j*n_virt + t + n_ex] * K[1, j*n_virt + s] * K[2, m*n_virt + s]

										elif ((t != s) and (u == s) and (v == t)):

											L4[i*n_virt + s + n_ex] += (-4 * g[i, n_occ + t, m, n_occ + t] + 2 * g[i, m, n_occ + t, n_occ + t] + 4 * g[i, j, j, m] + -2 * g[i, m, j, j] ) * K[0, j*n_virt + t + n_ex] * K[1, j*n_virt + s] * K[2, m*n_virt + t]

										elif ((t != s) and (u == s) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s + n_ex] += (2 * g[i, m, n_occ + t, n_occ + v] + -4 * g[i, n_occ + t, m, n_occ + v] ) * K[0, j*n_virt + t + n_ex] * K[1, j*n_virt + s] * K[2, m*n_virt + v]

										elif ((t != s) and (u == t) and (v == s)):

											L4[i*n_virt + s + n_ex] += (2 * g[i, n_occ + t, m, n_occ + t] + -4 * g[i, m, n_occ + t, n_occ + t] + -2 * g[i, j, j, m] + 4 * g[i, m, j, j] ) * K[0, j*n_virt + t + n_ex] * K[1, j*n_virt + t] * K[2, m*n_virt + s]

										elif ((t != s) and (u != s) and (u != t) and (v == s)):

											L4[i*n_virt + s + n_ex] += (-4 * g[i, m, n_occ + t, n_occ + u] + 2 * g[i, n_occ + t, m, n_occ + u] ) * K[0, j*n_virt + t + n_ex] * K[1, j*n_virt + u] * K[2, m*n_virt + s]

									elif ((j != i) and (k != i) and (k != j) and (m == i)):

										if ((t == s) and (u == s) and (v == s)):

											L4[i*n_virt + s + n_ex] += (2 * F[j, k] + -6 * g[j, n_occ + s, k, n_occ + s] + 2 * g[i, i, j, k] + 2 * g[i, j, i, k] ) * K[0, j*n_virt + s + n_ex] * K[1, k*n_virt + s] * K[2, i*n_virt + s]

										elif ((t == s) and (u == s) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s + n_ex] += (-2 * g[j, n_occ + s, k, n_occ + v] + -2 * g[j, k, n_occ + s, n_occ + v] ) * K[0, j*n_virt + s + n_ex] * K[1, k*n_virt + s] * K[2, i*n_virt + v]

										elif ((t == s) and (u != s) and (u != t) and (v == s)):

											L4[i*n_virt + s + n_ex] += (2 * g[j, k, n_occ + s, n_occ + u] + -4 * g[j, n_occ + s, k, n_occ + u] ) * K[0, j*n_virt + s + n_ex] * K[1, k*n_virt + u] * K[2, i*n_virt + s]

										elif ((t != s) and (u == s) and (v == s)):

											L4[i*n_virt + s + n_ex] += (2 * g[j, k, n_occ + s, n_occ + t] + -4 * g[j, n_occ + t, k, n_occ + s] ) * K[0, j*n_virt + t + n_ex] * K[1, k*n_virt + s] * K[2, i*n_virt + s]

										elif ((t != s) and (u == s) and (v == t)):

											L4[i*n_virt + s + n_ex] += (2 * F[j, k] + -4 * g[j, n_occ + s, k, n_occ + s] + -4 * g[j, n_occ + t, k, n_occ + t] + 2 * g[j, k, n_occ + s, n_occ + s] + 2 * g[j, k, n_occ + t, n_occ + t] + -2 * g[i, i, j, k] + 4 * g[i, j, i, k] ) * K[0, j*n_virt + t + n_ex] * K[1, k*n_virt + s] * K[2, i*n_virt + t]

										elif ((t != s) and (u == s) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s + n_ex] += (2 * g[j, k, n_occ + t, n_occ + v] + -4 * g[j, n_occ + t, k, n_occ + v] ) * K[0, j*n_virt + t + n_ex] * K[1, k*n_virt + s] * K[2, i*n_virt + v]

										elif ((t != s) and (u == t) and (v == s)):

											L4[i*n_virt + s + n_ex] += (2 * g[j, n_occ + s, k, n_occ + s] + -4 * g[j, k, n_occ + s, n_occ + s] + -2 * g[i, j, i, k] + 4 * g[i, i, j, k] ) * K[0, j*n_virt + t + n_ex] * K[1, k*n_virt + t] * K[2, i*n_virt + s]

										elif ((t != s) and (u == t) and (v == t)):

											L4[i*n_virt + s + n_ex] += (-2 * g[j, n_occ + s, k, n_occ + t] + -2 * g[j, k, n_occ + s, n_occ + t] ) * K[0, j*n_virt + t + n_ex] * K[1, k*n_virt + t] * K[2, i*n_virt + t]

										elif ((t != s) and (u == t) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s + n_ex] += (-4 * g[j, k, n_occ + s, n_occ + v] + 2 * g[j, n_occ + s, k, n_occ + v] ) * K[0, j*n_virt + t + n_ex] * K[1, k*n_virt + t] * K[2, i*n_virt + v]

										elif ((t != s) and (u != s) and (u != t) and (v == t)):

											L4[i*n_virt + s + n_ex] += (2 * g[j, k, n_occ + s, n_occ + u] + -4 * g[j, n_occ + s, k, n_occ + u] ) * K[0, j*n_virt + t + n_ex] * K[1, k*n_virt + u] * K[2, i*n_virt + t]

									elif ((j != i) and (k != i) and (k != j) and (m == j)):

										if ((t == s) and (u == s) and (v == s)):

											L4[i*n_virt + s + n_ex] += (2 * g[i, j, j, k] + -2 * g[i, k, n_occ + s, n_occ + s] + -2 * g[i, n_occ + s, k, n_occ + s] + 2 * g[i, k, j, j] ) * K[0, j*n_virt + s + n_ex] * K[1, k*n_virt + s] * K[2, j*n_virt + s]

										elif ((t == s) and (u == s) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s + n_ex] += (-4 * g[i, k, n_occ + s, n_occ + v] + 2 * g[i, n_occ + s, k, n_occ + v] ) * K[0, j*n_virt + s + n_ex] * K[1, k*n_virt + s] * K[2, j*n_virt + v]

										elif ((t == s) and (u != s) and (u != t) and (v == s)):

											L4[i*n_virt + s + n_ex] += (-4 * g[i, n_occ + s, k, n_occ + u] + 2 * g[i, k, n_occ + s, n_occ + u] ) * K[0, j*n_virt + s + n_ex] * K[1, k*n_virt + u] * K[2, j*n_virt + s]

										elif ((t != s) and (u == s) and (v == s)):

											L4[i*n_virt + s + n_ex] += (-2 * g[i, n_occ + t, k, n_occ + s] + -2 * g[i, k, n_occ + s, n_occ + t] ) * K[0, j*n_virt + t + n_ex] * K[1, k*n_virt + s] * K[2, j*n_virt + s]

										elif ((t != s) and (u == s) and (v == t)):

											L4[i*n_virt + s + n_ex] += (2 * g[i, n_occ + t, k, n_occ + t] + -4 * g[i, k, n_occ + t, n_occ + t] + -2 * g[i, j, j, k] + 4 * g[i, k, j, j] ) * K[0, j*n_virt + t + n_ex] * K[1, k*n_virt + s] * K[2, j*n_virt + t]

										elif ((t != s) and (u == s) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s + n_ex] += (-4 * g[i, k, n_occ + t, n_occ + v] + 2 * g[i, n_occ + t, k, n_occ + v] ) * K[0, j*n_virt + t + n_ex] * K[1, k*n_virt + s] * K[2, j*n_virt + v]

										elif ((t != s) and (u == t) and (v == s)):

											L4[i*n_virt + s + n_ex] += (-4 * g[i, n_occ + t, k, n_occ + t] + 2 * g[i, k, n_occ + t, n_occ + t] + 4 * g[i, j, j, k] + -2 * g[i, k, j, j] ) * K[0, j*n_virt + t + n_ex] * K[1, k*n_virt + t] * K[2, j*n_virt + s]

										elif ((t != s) and (u != s) and (u != t) and (v == s)):

											L4[i*n_virt + s + n_ex] += (2 * g[i, k, n_occ + t, n_occ + u] + -4 * g[i, n_occ + t, k, n_occ + u] ) * K[0, j*n_virt + t + n_ex] * K[1, k*n_virt + u] * K[2, j*n_virt + s]

									elif ((j != i) and (k != i) and (k != j) and (m == k)):

										if ((t == s) and (u == s) and (v == s)):

											L4[i*n_virt + s + n_ex] += (4 * g[i, k, j, k] ) * K[0, j*n_virt + s + n_ex] * K[1, k*n_virt + s] * K[2, k*n_virt + s]

										elif ((t != s) and (u == s) and (v == t)):

											L4[i*n_virt + s + n_ex] += (2 * g[i, k, j, k] ) * K[0, j*n_virt + t + n_ex] * K[1, k*n_virt + s] * K[2, k*n_virt + t]

										elif ((t != s) and (u == t) and (v == s)):

											L4[i*n_virt + s + n_ex] += (2 * g[i, k, j, k] ) * K[0, j*n_virt + t + n_ex] * K[1, k*n_virt + t] * K[2, k*n_virt + s]

									elif ((j != i) and (k != i) and (k != j) and (m != i) and (m != j) and (m != k)):

										if ((t == s) and (u == s) and (v == s)):

											L4[i*n_virt + s + n_ex] += (2 * g[i, m, j, k] + 2 * g[i, k, j, m] ) * K[0, j*n_virt + s + n_ex] * K[1, k*n_virt + s] * K[2, m*n_virt + s]

										elif ((t != s) and (u == s) and (v == t)):

											L4[i*n_virt + s + n_ex] += (4 * g[i, k, j, m] + -2 * g[i, m, j, k] ) * K[0, j*n_virt + t + n_ex] * K[1, k*n_virt + s] * K[2, m*n_virt + t]

										elif ((t != s) and (u == t) and (v == s)):

											L4[i*n_virt + s + n_ex] += (-2 * g[i, k, j, m] + 4 * g[i, m, j, k] ) * K[0, j*n_virt + t + n_ex] * K[1, k*n_virt + t] * K[2, m*n_virt + s]

	# Current operator combination: {'a': 1, 'b': 1, 'c': 2, 'd': 3}
	# All terms vanished for this combination

	# Current operator combination: {'a': 1, 'b': 1, 'c': 3, 'd': 1}
	# This combination was excluded by the contr_type_only argument {'a': 1, 'b': 1, 'c': 3, 'd': 1}

	# Current operator combination: {'a': 1, 'b': 1, 'c': 3, 'd': 2}
	# This combination was excluded by the contr_type_only argument {'a': 1, 'b': 1, 'c': 3, 'd': 2}

	# Current operator combination: {'a': 1, 'b': 1, 'c': 3, 'd': 3}
	# This combination was excluded by the contr_type_only argument {'a': 1, 'b': 1, 'c': 3, 'd': 3}

	# Current operator combination: {'a': 1, 'b': 2, 'c': 1, 'd': 1}
	for i in range(n_occ):
		for j in range(n_occ):
			for k in range(n_occ):
				for m in range(n_occ):
					for s in range(n_virt):
						for t in range(n_virt):
							for u in range(n_virt):
								for v in range(n_virt):

									if ((j == i) and (k == i) and (m == i)):

										if ((t == s) and (u == s) and (v == s)):

											L4[i*n_virt + s] += (8 * g[i, n_occ + s, i, n_occ + s] ) * K[0, i*n_virt + s] * K[1, i*n_virt + s + n_ex] * K[2, i*n_virt + s]

										elif ((t == s) and (u == s) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s] += (6 * g[i, n_occ + s, i, n_occ + v] ) * K[0, i*n_virt + s] * K[1, i*n_virt + s + n_ex] * K[2, i*n_virt + v]

										elif ((t == s) and (u != s) and (u != t) and (v == u)):

											L4[i*n_virt + s] += (2 * g[i, n_occ + s, i, n_occ + s] ) * K[0, i*n_virt + s] * K[1, i*n_virt + u + n_ex] * K[2, i*n_virt + u]

										elif ((t != s) and (u == s) and (v == s)):

											L4[i*n_virt + s] += (4 * g[i, n_occ + s, i, n_occ + t] ) * K[0, i*n_virt + t] * K[1, i*n_virt + s + n_ex] * K[2, i*n_virt + s]

										elif ((t != s) and (u == s) and (v == t)):

											L4[i*n_virt + s] += (2 * g[i, n_occ + t, i, n_occ + t] ) * K[0, i*n_virt + t] * K[1, i*n_virt + s + n_ex] * K[2, i*n_virt + t]

										elif ((t != s) and (u == s) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s] += (2 * g[i, n_occ + t, i, n_occ + v] ) * K[0, i*n_virt + t] * K[1, i*n_virt + s + n_ex] * K[2, i*n_virt + v]

										elif ((t != s) and (u == t) and (v == s)):

											L4[i*n_virt + s] += (4 * g[i, n_occ + s, i, n_occ + s] ) * K[0, i*n_virt + t] * K[1, i*n_virt + t + n_ex] * K[2, i*n_virt + s]

										elif ((t != s) and (u == t) and (v == t)):

											L4[i*n_virt + s] += (6 * g[i, n_occ + s, i, n_occ + t] ) * K[0, i*n_virt + t] * K[1, i*n_virt + t + n_ex] * K[2, i*n_virt + t]

										elif ((t != s) and (u == t) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s] += (4 * g[i, n_occ + s, i, n_occ + v] ) * K[0, i*n_virt + t] * K[1, i*n_virt + t + n_ex] * K[2, i*n_virt + v]

										elif ((t != s) and (u != s) and (u != t) and (v == u)):

											L4[i*n_virt + s] += (2 * g[i, n_occ + s, i, n_occ + t] ) * K[0, i*n_virt + t] * K[1, i*n_virt + u + n_ex] * K[2, i*n_virt + u]

									elif ((j == i) and (k == i) and (m != i) and (m != j) and (m != k)):

										if ((t == s) and (u == s) and (v == s)):

											L4[i*n_virt + s] += (6 * g[i, n_occ + s, m, n_occ + s] ) * K[0, i*n_virt + s] * K[1, i*n_virt + s + n_ex] * K[2, m*n_virt + s]

										elif ((t == s) and (u == s) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s] += (8 * g[i, n_occ + s, m, n_occ + v] + -4 * g[i, n_occ + v, m, n_occ + s] ) * K[0, i*n_virt + s] * K[1, i*n_virt + s + n_ex] * K[2, m*n_virt + v]

										elif ((t == s) and (u != s) and (u != t) and (v == u)):

											L4[i*n_virt + s] += (2 * g[i, n_occ + s, m, n_occ + s] ) * K[0, i*n_virt + s] * K[1, i*n_virt + u + n_ex] * K[2, m*n_virt + u]

										elif ((t != s) and (u == s) and (v == s)):

											L4[i*n_virt + s] += (2 * g[i, n_occ + s, m, n_occ + t] + 2 * g[i, n_occ + t, m, n_occ + s] ) * K[0, i*n_virt + t] * K[1, i*n_virt + s + n_ex] * K[2, m*n_virt + s]

										elif ((t != s) and (u == s) and (v == t)):

											L4[i*n_virt + s] += (2 * g[i, n_occ + t, m, n_occ + t] ) * K[0, i*n_virt + t] * K[1, i*n_virt + s + n_ex] * K[2, m*n_virt + t]

										elif ((t != s) and (u == s) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s] += (4 * g[i, n_occ + t, m, n_occ + v] + -2 * g[i, n_occ + v, m, n_occ + t] ) * K[0, i*n_virt + t] * K[1, i*n_virt + s + n_ex] * K[2, m*n_virt + v]

										elif ((t != s) and (u == t) and (v == s)):

											L4[i*n_virt + s] += (2 * g[i, n_occ + s, m, n_occ + s] ) * K[0, i*n_virt + t] * K[1, i*n_virt + t + n_ex] * K[2, m*n_virt + s]

										elif ((t != s) and (u == t) and (v == t)):

											L4[i*n_virt + s] += (8 * g[i, n_occ + s, m, n_occ + t] + -4 * g[i, n_occ + t, m, n_occ + s] ) * K[0, i*n_virt + t] * K[1, i*n_virt + t + n_ex] * K[2, m*n_virt + t]

										elif ((t != s) and (u == t) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s] += (4 * g[i, n_occ + s, m, n_occ + v] + -2 * g[i, n_occ + v, m, n_occ + s] ) * K[0, i*n_virt + t] * K[1, i*n_virt + t + n_ex] * K[2, m*n_virt + v]

										elif ((t != s) and (u != s) and (u != t) and (v == u)):

											L4[i*n_virt + s] += (4 * g[i, n_occ + s, m, n_occ + t] + -2 * g[i, n_occ + t, m, n_occ + s] ) * K[0, i*n_virt + t] * K[1, i*n_virt + u + n_ex] * K[2, m*n_virt + u]

									elif ((j == i) and (k != i) and (k != j) and (m == k)):

										if ((t == s) and (u == s) and (v == s)):

											L4[i*n_virt + s] += (2 * g[i, n_occ + s, i, n_occ + s] ) * K[0, i*n_virt + s] * K[1, k*n_virt + s + n_ex] * K[2, k*n_virt + s]

										elif ((t == s) and (u == s) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s] += (2 * g[i, n_occ + s, i, n_occ + v] ) * K[0, i*n_virt + s] * K[1, k*n_virt + s + n_ex] * K[2, k*n_virt + v]

										elif ((t != s) and (u == t) and (v == s)):

											L4[i*n_virt + s] += (2 * g[i, n_occ + s, i, n_occ + s] ) * K[0, i*n_virt + t] * K[1, k*n_virt + t + n_ex] * K[2, k*n_virt + s]

										elif ((t != s) and (u == t) and (v == t)):

											L4[i*n_virt + s] += (2 * g[i, n_occ + s, i, n_occ + t] ) * K[0, i*n_virt + t] * K[1, k*n_virt + t + n_ex] * K[2, k*n_virt + t]

										elif ((t != s) and (u == t) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s] += (2 * g[i, n_occ + s, i, n_occ + v] ) * K[0, i*n_virt + t] * K[1, k*n_virt + t + n_ex] * K[2, k*n_virt + v]

									elif ((j != i) and (k == i) and (m == i)):

										if ((t == s) and (u == s) and (v == s)):

											L4[i*n_virt + s] += (4 * g[i, n_occ + s, j, n_occ + s] ) * K[0, j*n_virt + s] * K[1, i*n_virt + s + n_ex] * K[2, i*n_virt + s]

										elif ((t == s) and (u == s) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s] += (2 * g[i, n_occ + s, j, n_occ + v] + 2 * g[i, n_occ + v, j, n_occ + s] ) * K[0, j*n_virt + s] * K[1, i*n_virt + s + n_ex] * K[2, i*n_virt + v]

										elif ((t != s) and (u == t) and (v == s)):

											L4[i*n_virt + s] += (4 * g[i, n_occ + s, j, n_occ + s] ) * K[0, j*n_virt + t] * K[1, i*n_virt + t + n_ex] * K[2, i*n_virt + s]

										elif ((t != s) and (u == t) and (v == t)):

											L4[i*n_virt + s] += (2 * g[i, n_occ + t, j, n_occ + s] + 2 * g[i, n_occ + s, j, n_occ + t] ) * K[0, j*n_virt + t] * K[1, i*n_virt + t + n_ex] * K[2, i*n_virt + t]

										elif ((t != s) and (u == t) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s] += (2 * g[i, n_occ + v, j, n_occ + s] + 2 * g[i, n_occ + s, j, n_occ + v] ) * K[0, j*n_virt + t] * K[1, i*n_virt + t + n_ex] * K[2, i*n_virt + v]

									elif ((j != i) and (k == i) and (m == j)):

										if ((t == s) and (u == s) and (v == s)):

											L4[i*n_virt + s] += (2 * g[j, n_occ + s, j, n_occ + s] ) * K[0, j*n_virt + s] * K[1, i*n_virt + s + n_ex] * K[2, j*n_virt + s]

										elif ((t == s) and (u == s) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s] += (2 * g[j, n_occ + s, j, n_occ + v] ) * K[0, j*n_virt + s] * K[1, i*n_virt + s + n_ex] * K[2, j*n_virt + v]

										elif ((t != s) and (u == t) and (v == s)):

											L4[i*n_virt + s] += (2 * g[j, n_occ + s, j, n_occ + s] ) * K[0, j*n_virt + t] * K[1, i*n_virt + t + n_ex] * K[2, j*n_virt + s]

										elif ((t != s) and (u == t) and (v == t)):

											L4[i*n_virt + s] += (2 * g[j, n_occ + s, j, n_occ + t] ) * K[0, j*n_virt + t] * K[1, i*n_virt + t + n_ex] * K[2, j*n_virt + t]

										elif ((t != s) and (u == t) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s] += (2 * g[j, n_occ + s, j, n_occ + v] ) * K[0, j*n_virt + t] * K[1, i*n_virt + t + n_ex] * K[2, j*n_virt + v]

									elif ((j != i) and (k == i) and (m != i) and (m != j) and (m != k)):

										if ((t == s) and (u == s) and (v == s)):

											L4[i*n_virt + s] += (2 * g[j, n_occ + s, m, n_occ + s] ) * K[0, j*n_virt + s] * K[1, i*n_virt + s + n_ex] * K[2, m*n_virt + s]

										elif ((t == s) and (u == s) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s] += (4 * g[j, n_occ + s, m, n_occ + v] + -2 * g[j, n_occ + v, m, n_occ + s] ) * K[0, j*n_virt + s] * K[1, i*n_virt + s + n_ex] * K[2, m*n_virt + v]

										elif ((t != s) and (u == t) and (v == s)):

											L4[i*n_virt + s] += (2 * g[j, n_occ + s, m, n_occ + s] ) * K[0, j*n_virt + t] * K[1, i*n_virt + t + n_ex] * K[2, m*n_virt + s]

										elif ((t != s) and (u == t) and (v == t)):

											L4[i*n_virt + s] += (4 * g[j, n_occ + s, m, n_occ + t] + -2 * g[j, n_occ + t, m, n_occ + s] ) * K[0, j*n_virt + t] * K[1, i*n_virt + t + n_ex] * K[2, m*n_virt + t]

										elif ((t != s) and (u == t) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s] += (4 * g[j, n_occ + s, m, n_occ + v] + -2 * g[j, n_occ + v, m, n_occ + s] ) * K[0, j*n_virt + t] * K[1, i*n_virt + t + n_ex] * K[2, m*n_virt + v]

									elif ((j != i) and (k == j) and (m == i)):

										if ((t == s) and (u == s) and (v == s)):

											L4[i*n_virt + s] += (4 * g[i, n_occ + s, i, n_occ + s] ) * K[0, j*n_virt + s] * K[1, j*n_virt + s + n_ex] * K[2, i*n_virt + s]

										elif ((t == s) and (u == s) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s] += (2 * g[i, n_occ + s, i, n_occ + v] ) * K[0, j*n_virt + s] * K[1, j*n_virt + s + n_ex] * K[2, i*n_virt + v]

										elif ((t == s) and (u != s) and (u != t) and (v == u)):

											L4[i*n_virt + s] += (2 * g[i, n_occ + s, i, n_occ + s] ) * K[0, j*n_virt + s] * K[1, j*n_virt + u + n_ex] * K[2, i*n_virt + u]

										elif ((t != s) and (u == s) and (v == s)):

											L4[i*n_virt + s] += (4 * g[i, n_occ + s, i, n_occ + t] ) * K[0, j*n_virt + t] * K[1, j*n_virt + s + n_ex] * K[2, i*n_virt + s]

										elif ((t != s) and (u == s) and (v == t)):

											L4[i*n_virt + s] += (2 * g[i, n_occ + t, i, n_occ + t] ) * K[0, j*n_virt + t] * K[1, j*n_virt + s + n_ex] * K[2, i*n_virt + t]

										elif ((t != s) and (u == s) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s] += (2 * g[i, n_occ + t, i, n_occ + v] ) * K[0, j*n_virt + t] * K[1, j*n_virt + s + n_ex] * K[2, i*n_virt + v]

										elif ((t != s) and (u == t) and (v == t)):

											L4[i*n_virt + s] += (2 * g[i, n_occ + s, i, n_occ + t] ) * K[0, j*n_virt + t] * K[1, j*n_virt + t + n_ex] * K[2, i*n_virt + t]

										elif ((t != s) and (u != s) and (u != t) and (v == u)):

											L4[i*n_virt + s] += (2 * g[i, n_occ + s, i, n_occ + t] ) * K[0, j*n_virt + t] * K[1, j*n_virt + u + n_ex] * K[2, i*n_virt + u]

									elif ((j != i) and (k == j) and (m == j)):

										if ((t == s) and (u == s) and (v == s)):

											L4[i*n_virt + s] += (6 * g[i, n_occ + s, j, n_occ + s] ) * K[0, j*n_virt + s] * K[1, j*n_virt + s + n_ex] * K[2, j*n_virt + s]

										elif ((t == s) and (u == s) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s] += (8 * g[i, n_occ + s, j, n_occ + v] + -4 * g[i, n_occ + v, j, n_occ + s] ) * K[0, j*n_virt + s] * K[1, j*n_virt + s + n_ex] * K[2, j*n_virt + v]

										elif ((t == s) and (u != s) and (u != t) and (v == u)):

											L4[i*n_virt + s] += (2 * g[i, n_occ + s, j, n_occ + s] ) * K[0, j*n_virt + s] * K[1, j*n_virt + u + n_ex] * K[2, j*n_virt + u]

										elif ((t != s) and (u == s) and (v == s)):

											L4[i*n_virt + s] += (2 * g[i, n_occ + t, j, n_occ + s] + 2 * g[i, n_occ + s, j, n_occ + t] ) * K[0, j*n_virt + t] * K[1, j*n_virt + s + n_ex] * K[2, j*n_virt + s]

										elif ((t != s) and (u == s) and (v == t)):

											L4[i*n_virt + s] += (2 * g[i, n_occ + t, j, n_occ + t] ) * K[0, j*n_virt + t] * K[1, j*n_virt + s + n_ex] * K[2, j*n_virt + t]

										elif ((t != s) and (u == s) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s] += (4 * g[i, n_occ + t, j, n_occ + v] + -2 * g[i, n_occ + v, j, n_occ + t] ) * K[0, j*n_virt + t] * K[1, j*n_virt + s + n_ex] * K[2, j*n_virt + v]

										elif ((t != s) and (u == t) and (v == s)):

											L4[i*n_virt + s] += (2 * g[i, n_occ + s, j, n_occ + s] ) * K[0, j*n_virt + t] * K[1, j*n_virt + t + n_ex] * K[2, j*n_virt + s]

										elif ((t != s) and (u == t) and (v == t)):

											L4[i*n_virt + s] += (8 * g[i, n_occ + s, j, n_occ + t] + -4 * g[i, n_occ + t, j, n_occ + s] ) * K[0, j*n_virt + t] * K[1, j*n_virt + t + n_ex] * K[2, j*n_virt + t]

										elif ((t != s) and (u == t) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s] += (4 * g[i, n_occ + s, j, n_occ + v] + -2 * g[i, n_occ + v, j, n_occ + s] ) * K[0, j*n_virt + t] * K[1, j*n_virt + t + n_ex] * K[2, j*n_virt + v]

										elif ((t != s) and (u != s) and (u != t) and (v == u)):

											L4[i*n_virt + s] += (4 * g[i, n_occ + s, j, n_occ + t] + -2 * g[i, n_occ + t, j, n_occ + s] ) * K[0, j*n_virt + t] * K[1, j*n_virt + u + n_ex] * K[2, j*n_virt + u]

									elif ((j != i) and (k == j) and (m != i) and (m != j) and (m != k)):

										if ((t == s) and (u == s) and (v == s)):

											L4[i*n_virt + s] += (4 * g[i, n_occ + s, m, n_occ + s] ) * K[0, j*n_virt + s] * K[1, j*n_virt + s + n_ex] * K[2, m*n_virt + s]

										elif ((t == s) and (u == s) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s] += (4 * g[i, n_occ + s, m, n_occ + v] + -2 * g[i, n_occ + v, m, n_occ + s] ) * K[0, j*n_virt + s] * K[1, j*n_virt + s + n_ex] * K[2, m*n_virt + v]

										elif ((t == s) and (u != s) and (u != t) and (v == u)):

											L4[i*n_virt + s] += (2 * g[i, n_occ + s, m, n_occ + s] ) * K[0, j*n_virt + s] * K[1, j*n_virt + u + n_ex] * K[2, m*n_virt + u]

										elif ((t != s) and (u == s) and (v == s)):

											L4[i*n_virt + s] += (2 * g[i, n_occ + t, m, n_occ + s] + 2 * g[i, n_occ + s, m, n_occ + t] ) * K[0, j*n_virt + t] * K[1, j*n_virt + s + n_ex] * K[2, m*n_virt + s]

										elif ((t != s) and (u == s) and (v == t)):

											L4[i*n_virt + s] += (2 * g[i, n_occ + t, m, n_occ + t] ) * K[0, j*n_virt + t] * K[1, j*n_virt + s + n_ex] * K[2, m*n_virt + t]

										elif ((t != s) and (u == s) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s] += (4 * g[i, n_occ + t, m, n_occ + v] + -2 * g[i, n_occ + v, m, n_occ + t] ) * K[0, j*n_virt + t] * K[1, j*n_virt + s + n_ex] * K[2, m*n_virt + v]

										elif ((t != s) and (u == t) and (v == t)):

											L4[i*n_virt + s] += (4 * g[i, n_occ + s, m, n_occ + t] + -2 * g[i, n_occ + t, m, n_occ + s] ) * K[0, j*n_virt + t] * K[1, j*n_virt + t + n_ex] * K[2, m*n_virt + t]

										elif ((t != s) and (u != s) and (u != t) and (v == u)):

											L4[i*n_virt + s] += (4 * g[i, n_occ + s, m, n_occ + t] + -2 * g[i, n_occ + t, m, n_occ + s] ) * K[0, j*n_virt + t] * K[1, j*n_virt + u + n_ex] * K[2, m*n_virt + u]

									elif ((j != i) and (k != i) and (k != j) and (m == k)):

										if ((t == s) and (u == s) and (v == s)):

											L4[i*n_virt + s] += (2 * g[i, n_occ + s, j, n_occ + s] ) * K[0, j*n_virt + s] * K[1, k*n_virt + s + n_ex] * K[2, k*n_virt + s]

										elif ((t == s) and (u == s) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s] += (4 * g[i, n_occ + s, j, n_occ + v] + -2 * g[i, n_occ + v, j, n_occ + s] ) * K[0, j*n_virt + s] * K[1, k*n_virt + s + n_ex] * K[2, k*n_virt + v]

										elif ((t != s) and (u == t) and (v == s)):

											L4[i*n_virt + s] += (2 * g[i, n_occ + s, j, n_occ + s] ) * K[0, j*n_virt + t] * K[1, k*n_virt + t + n_ex] * K[2, k*n_virt + s]

										elif ((t != s) and (u == t) and (v == t)):

											L4[i*n_virt + s] += (4 * g[i, n_occ + s, j, n_occ + t] + -2 * g[i, n_occ + t, j, n_occ + s] ) * K[0, j*n_virt + t] * K[1, k*n_virt + t + n_ex] * K[2, k*n_virt + t]

										elif ((t != s) and (u == t) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s] += (4 * g[i, n_occ + s, j, n_occ + v] + -2 * g[i, n_occ + v, j, n_occ + s] ) * K[0, j*n_virt + t] * K[1, k*n_virt + t + n_ex] * K[2, k*n_virt + v]

	# Current operator combination: {'a': 1, 'b': 2, 'c': 1, 'd': 2}
	for i in range(n_occ):
		for j in range(n_occ):
			for k in range(n_occ):
				for m in range(n_occ):
					for s in range(n_virt):
						for t in range(n_virt):
							for u in range(n_virt):
								for v in range(n_virt):

									if ((j == i) and (k == i) and (m == i)):

										if ((t == s) and (u == s) and (v == s)):

											L4[i*n_virt + s + n_ex] += (4 * F[i, i] + -4 * F[n_occ + s, n_occ + s] + -4 * g[i, i, n_occ + s, n_occ + s] + -16 * g[i, n_occ + s, i, n_occ + s] + 4 * g[n_occ + s, n_occ + s, n_occ + s, n_occ + s] + 4 * g[i, i, i, i] ) * K[0, i*n_virt + s] * K[1, i*n_virt + s + n_ex] * K[2, i*n_virt + s]

										elif ((t == s) and (u == s) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s + n_ex] += (4 * g[n_occ + s, n_occ + s, n_occ + s, n_occ + v] + -4 * g[i, i, n_occ + s, n_occ + v] + -4 * g[i, n_occ + s, i, n_occ + v] ) * K[0, i*n_virt + s] * K[1, i*n_virt + s + n_ex] * K[2, i*n_virt + v]

										elif ((t == s) and (u != s) and (u != t) and (v == s)):

											L4[i*n_virt + s + n_ex] += (-2 * F[n_occ + s, n_occ + u] + -2 * g[i, i, n_occ + s, n_occ + u] + -8 * g[i, n_occ + s, i, n_occ + u] + 4 * g[n_occ + s, n_occ + s, n_occ + s, n_occ + u] ) * K[0, i*n_virt + s] * K[1, i*n_virt + u + n_ex] * K[2, i*n_virt + s]

										elif ((t == s) and (u != s) and (u != t) and (v == u)):

											L4[i*n_virt + s + n_ex] += (2 * F[i, i] + -2 * F[n_occ + s, n_occ + s] + 2 * g[n_occ + s, n_occ + s, n_occ + u, n_occ + u] + 2 * g[n_occ + s, n_occ + u, n_occ + s, n_occ + u] + -2 * g[i, i, n_occ + u, n_occ + u] + -2 * g[i, n_occ + u, i, n_occ + u] + -6 * g[i, n_occ + s, i, n_occ + s] + 2 * g[i, i, i, i] ) * K[0, i*n_virt + s] * K[1, i*n_virt + u + n_ex] * K[2, i*n_virt + u]

										elif ((t == s) and (u != s) and (u != t) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s + n_ex] += (2 * g[n_occ + s, n_occ + u, n_occ + s, n_occ + v] + 2 * g[n_occ + s, n_occ + s, n_occ + u, n_occ + v] + -2 * g[i, i, n_occ + u, n_occ + v] + -2 * g[i, n_occ + u, i, n_occ + v] ) * K[0, i*n_virt + s] * K[1, i*n_virt + u + n_ex] * K[2, i*n_virt + v]

										elif ((t != s) and (u == s) and (v == s)):

											L4[i*n_virt + s + n_ex] += (-4 * F[n_occ + s, n_occ + t] + -12 * g[i, n_occ + s, i, n_occ + t] + 4 * g[n_occ + s, n_occ + s, n_occ + s, n_occ + t] ) * K[0, i*n_virt + t] * K[1, i*n_virt + s + n_ex] * K[2, i*n_virt + s]

										elif ((t != s) and (u == s) and (v == t)):

											L4[i*n_virt + s + n_ex] += (4 * g[n_occ + s, n_occ + t, n_occ + s, n_occ + t] ) * K[0, i*n_virt + t] * K[1, i*n_virt + s + n_ex] * K[2, i*n_virt + t]

										elif ((t != s) and (u == s) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s + n_ex] += (4 * g[n_occ + s, n_occ + t, n_occ + s, n_occ + v] ) * K[0, i*n_virt + t] * K[1, i*n_virt + s + n_ex] * K[2, i*n_virt + v]

										elif ((t != s) and (u == t) and (v == s)):

											L4[i*n_virt + s + n_ex] += (2 * F[i, i] + -2 * F[n_occ + t, n_occ + t] + -6 * g[i, n_occ + t, i, n_occ + t] + 2 * g[n_occ + s, n_occ + s, n_occ + t, n_occ + t] + 2 * g[n_occ + s, n_occ + t, n_occ + s, n_occ + t] + -2 * g[i, n_occ + s, i, n_occ + s] + -2 * g[i, i, n_occ + s, n_occ + s] + 2 * g[i, i, i, i] ) * K[0, i*n_virt + t] * K[1, i*n_virt + t + n_ex] * K[2, i*n_virt + s]

										elif ((t != s) and (u == t) and (v == t)):

											L4[i*n_virt + s + n_ex] += (-2 * F[n_occ + s, n_occ + t] + 4 * g[n_occ + s, n_occ + t, n_occ + t, n_occ + t] + -8 * g[i, n_occ + s, i, n_occ + t] + -2 * g[i, i, n_occ + s, n_occ + t] ) * K[0, i*n_virt + t] * K[1, i*n_virt + t + n_ex] * K[2, i*n_virt + t]

										elif ((t != s) and (u == t) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s + n_ex] += (2 * g[n_occ + s, n_occ + v, n_occ + t, n_occ + t] + 2 * g[n_occ + s, n_occ + t, n_occ + t, n_occ + v] + -2 * g[i, n_occ + s, i, n_occ + v] + -2 * g[i, i, n_occ + s, n_occ + v] ) * K[0, i*n_virt + t] * K[1, i*n_virt + t + n_ex] * K[2, i*n_virt + v]

										elif ((t != s) and (u != s) and (u != t) and (v == s)):

											L4[i*n_virt + s + n_ex] += (-2 * F[n_occ + t, n_occ + u] + -6 * g[i, n_occ + t, i, n_occ + u] + 2 * g[n_occ + s, n_occ + s, n_occ + t, n_occ + u] + 2 * g[n_occ + s, n_occ + t, n_occ + s, n_occ + u] ) * K[0, i*n_virt + t] * K[1, i*n_virt + u + n_ex] * K[2, i*n_virt + s]

										elif ((t != s) and (u != s) and (u != t) and (v == t)):

											L4[i*n_virt + s + n_ex] += (4 * g[n_occ + s, n_occ + t, n_occ + t, n_occ + u] ) * K[0, i*n_virt + t] * K[1, i*n_virt + u + n_ex] * K[2, i*n_virt + t]

										elif ((t != s) and (u != s) and (u != t) and (v == u)):

											L4[i*n_virt + s + n_ex] += (-2 * F[n_occ + s, n_occ + t] + 2 * g[n_occ + s, n_occ + u, n_occ + t, n_occ + u] + 2 * g[n_occ + s, n_occ + t, n_occ + u, n_occ + u] + -6 * g[i, n_occ + s, i, n_occ + t] ) * K[0, i*n_virt + t] * K[1, i*n_virt + u + n_ex] * K[2, i*n_virt + u]

										elif ((t != s) and (u != s) and (u != t) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s + n_ex] += (2 * g[n_occ + s, n_occ + v, n_occ + t, n_occ + u] + 2 * g[n_occ + s, n_occ + t, n_occ + u, n_occ + v] ) * K[0, i*n_virt + t] * K[1, i*n_virt + u + n_ex] * K[2, i*n_virt + v]

									elif ((j == i) and (k == i) and (m != i) and (m != j) and (m != k)):

										if ((t == s) and (u == s) and (v == s)):

											L4[i*n_virt + s + n_ex] += (-4 * g[i, m, n_occ + s, n_occ + s] + 4 * g[i, i, i, m] + -4 * g[i, n_occ + s, m, n_occ + s] ) * K[0, i*n_virt + s] * K[1, i*n_virt + s + n_ex] * K[2, m*n_virt + s]

										elif ((t == s) and (u != s) and (u != t) and (v == s)):

											L4[i*n_virt + s + n_ex] += (-2 * g[i, m, n_occ + s, n_occ + u] + -2 * g[i, n_occ + u, m, n_occ + s] ) * K[0, i*n_virt + s] * K[1, i*n_virt + u + n_ex] * K[2, m*n_virt + s]

										elif ((t == s) and (u != s) and (u != t) and (v == u)):

											L4[i*n_virt + s + n_ex] += (-2 * g[i, m, n_occ + s, n_occ + s] + -2 * g[i, n_occ + s, m, n_occ + s] + 2 * g[i, i, i, m] ) * K[0, i*n_virt + s] * K[1, i*n_virt + u + n_ex] * K[2, m*n_virt + u]

										elif ((t != s) and (u == s) and (v == s)):

											L4[i*n_virt + s + n_ex] += (-4 * g[i, n_occ + s, m, n_occ + t] + -4 * g[i, m, n_occ + s, n_occ + t] ) * K[0, i*n_virt + t] * K[1, i*n_virt + s + n_ex] * K[2, m*n_virt + s]

										elif ((t != s) and (u == t) and (v == s)):

											L4[i*n_virt + s + n_ex] += (-2 * g[i, n_occ + t, m, n_occ + t] + -2 * g[i, m, n_occ + t, n_occ + t] + 2 * g[i, i, i, m] ) * K[0, i*n_virt + t] * K[1, i*n_virt + t + n_ex] * K[2, m*n_virt + s]

										elif ((t != s) and (u == t) and (v == t)):

											L4[i*n_virt + s + n_ex] += (-2 * g[i, m, n_occ + s, n_occ + t] + -2 * g[i, n_occ + s, m, n_occ + t] ) * K[0, i*n_virt + t] * K[1, i*n_virt + t + n_ex] * K[2, m*n_virt + t]

										elif ((t != s) and (u != s) and (u != t) and (v == s)):

											L4[i*n_virt + s + n_ex] += (-2 * g[i, n_occ + u, m, n_occ + t] + -2 * g[i, m, n_occ + t, n_occ + u] ) * K[0, i*n_virt + t] * K[1, i*n_virt + u + n_ex] * K[2, m*n_virt + s]

										elif ((t != s) and (u != s) and (u != t) and (v == u)):

											L4[i*n_virt + s + n_ex] += (-2 * g[i, m, n_occ + s, n_occ + t] + -2 * g[i, n_occ + s, m, n_occ + t] ) * K[0, i*n_virt + t] * K[1, i*n_virt + u + n_ex] * K[2, m*n_virt + u]

									elif ((j == i) and (k != i) and (k != j) and (m == i)):

										if ((t == s) and (u == s) and (v == s)):

											L4[i*n_virt + s + n_ex] += (2 * F[i, k] + 4 * g[i, i, i, k] + -2 * g[i, k, n_occ + s, n_occ + s] + -8 * g[i, n_occ + s, k, n_occ + s] ) * K[0, i*n_virt + s] * K[1, k*n_virt + s + n_ex] * K[2, i*n_virt + s]

										elif ((t == s) and (u == s) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s + n_ex] += (-2 * g[i, k, n_occ + s, n_occ + v] + -2 * g[i, n_occ + v, k, n_occ + s] ) * K[0, i*n_virt + s] * K[1, k*n_virt + s + n_ex] * K[2, i*n_virt + v]

										elif ((t == s) and (u != s) and (u != t) and (v == s)):

											L4[i*n_virt + s + n_ex] += (4 * g[i, k, n_occ + s, n_occ + u] + -8 * g[i, n_occ + s, k, n_occ + u] ) * K[0, i*n_virt + s] * K[1, k*n_virt + u + n_ex] * K[2, i*n_virt + s]

										elif ((t == s) and (u != s) and (u != t) and (v == u)):

											L4[i*n_virt + s + n_ex] += (2 * F[i, k] + -2 * g[i, n_occ + s, k, n_occ + s] + -2 * g[i, k, n_occ + s, n_occ + s] + -4 * g[i, n_occ + u, k, n_occ + u] + 2 * g[i, k, n_occ + u, n_occ + u] + 2 * g[i, i, i, k] ) * K[0, i*n_virt + s] * K[1, k*n_virt + u + n_ex] * K[2, i*n_virt + u]

										elif ((t == s) and (u != s) and (u != t) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s + n_ex] += (2 * g[i, k, n_occ + u, n_occ + v] + -4 * g[i, n_occ + v, k, n_occ + u] ) * K[0, i*n_virt + s] * K[1, k*n_virt + u + n_ex] * K[2, i*n_virt + v]

										elif ((t != s) and (u == s) and (v == s)):

											L4[i*n_virt + s + n_ex] += (-6 * g[i, n_occ + t, k, n_occ + s] ) * K[0, i*n_virt + t] * K[1, k*n_virt + s + n_ex] * K[2, i*n_virt + s]

										elif ((t != s) and (u == t) and (v == s)):

											L4[i*n_virt + s + n_ex] += (2 * g[i, n_occ + s, k, n_occ + s] + -4 * g[i, k, n_occ + s, n_occ + s] + -4 * g[i, n_occ + t, k, n_occ + t] + 2 * g[i, k, n_occ + t, n_occ + t] + 2 * g[i, i, i, k] ) * K[0, i*n_virt + t] * K[1, k*n_virt + t + n_ex] * K[2, i*n_virt + s]

										elif ((t != s) and (u == t) and (v == t)):

											L4[i*n_virt + s + n_ex] += (-6 * g[i, k, n_occ + s, n_occ + t] ) * K[0, i*n_virt + t] * K[1, k*n_virt + t + n_ex] * K[2, i*n_virt + t]

										elif ((t != s) and (u == t) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s + n_ex] += (-4 * g[i, k, n_occ + s, n_occ + v] + 2 * g[i, n_occ + v, k, n_occ + s] ) * K[0, i*n_virt + t] * K[1, k*n_virt + t + n_ex] * K[2, i*n_virt + v]

										elif ((t != s) and (u != s) and (u != t) and (v == s)):

											L4[i*n_virt + s + n_ex] += (2 * g[i, k, n_occ + t, n_occ + u] + -4 * g[i, n_occ + t, k, n_occ + u] ) * K[0, i*n_virt + t] * K[1, k*n_virt + u + n_ex] * K[2, i*n_virt + s]

										elif ((t != s) and (u != s) and (u != t) and (v == u)):

											L4[i*n_virt + s + n_ex] += (-2 * g[i, n_occ + t, k, n_occ + s] + -2 * g[i, k, n_occ + s, n_occ + t] ) * K[0, i*n_virt + t] * K[1, k*n_virt + u + n_ex] * K[2, i*n_virt + u]

									elif ((j == i) and (k != i) and (k != j) and (m == k)):

										if ((t == s) and (u == s) and (v == s)):

											L4[i*n_virt + s + n_ex] += (2 * F[i, i] + -2 * F[n_occ + s, n_occ + s] + 2 * g[n_occ + s, n_occ + s, n_occ + s, n_occ + s] + -2 * g[k, k, n_occ + s, n_occ + s] + -6 * g[i, n_occ + s, i, n_occ + s] + 2 * g[i, i, k, k] + 2 * g[i, k, i, k] + -2 * g[k, n_occ + s, k, n_occ + s] ) * K[0, i*n_virt + s] * K[1, k*n_virt + s + n_ex] * K[2, k*n_virt + s]

										elif ((t == s) and (u == s) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s + n_ex] += (-2 * g[i, n_occ + s, i, n_occ + v] + 2 * g[n_occ + s, n_occ + s, n_occ + s, n_occ + v] + -2 * g[i, i, n_occ + s, n_occ + v] ) * K[0, i*n_virt + s] * K[1, k*n_virt + s + n_ex] * K[2, k*n_virt + v]

										elif ((t == s) and (u != s) and (u != t) and (v == s)):

											L4[i*n_virt + s + n_ex] += (-2 * F[n_occ + s, n_occ + u] + 2 * g[n_occ + s, n_occ + s, n_occ + s, n_occ + u] + -2 * g[i, i, n_occ + s, n_occ + u] + 2 * g[k, k, n_occ + s, n_occ + u] + -4 * g[k, n_occ + s, k, n_occ + u] + -2 * g[i, n_occ + s, i, n_occ + u] ) * K[0, i*n_virt + s] * K[1, k*n_virt + u + n_ex] * K[2, k*n_virt + s]

										elif ((t == s) and (u != s) and (u != t) and (v == u)):

											L4[i*n_virt + s + n_ex] += (-2 * g[n_occ + s, n_occ + u, n_occ + s, n_occ + u] + 4 * g[n_occ + s, n_occ + s, n_occ + u, n_occ + u] + 2 * g[i, n_occ + u, i, n_occ + u] + -4 * g[i, i, n_occ + u, n_occ + u] + -4 * g[k, k, n_occ + s, n_occ + s] + 2 * g[k, n_occ + s, k, n_occ + s] + -2 * g[i, k, i, k] + 4 * g[i, i, k, k] ) * K[0, i*n_virt + s] * K[1, k*n_virt + u + n_ex] * K[2, k*n_virt + u]

										elif ((t == s) and (u != s) and (u != t) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s + n_ex] += (-2 * g[n_occ + s, n_occ + u, n_occ + s, n_occ + v] + 4 * g[n_occ + s, n_occ + s, n_occ + u, n_occ + v] + 2 * g[i, n_occ + u, i, n_occ + v] + -4 * g[i, i, n_occ + u, n_occ + v] ) * K[0, i*n_virt + s] * K[1, k*n_virt + u + n_ex] * K[2, k*n_virt + v]

										elif ((t != s) and (u == s) and (v == s)):

											L4[i*n_virt + s + n_ex] += (-2 * F[n_occ + s, n_occ + t] + 2 * g[n_occ + s, n_occ + s, n_occ + s, n_occ + t] + -2 * g[k, k, n_occ + s, n_occ + t] + -4 * g[i, n_occ + s, i, n_occ + t] + 2 * g[i, i, n_occ + s, n_occ + t] + -2 * g[k, n_occ + s, k, n_occ + t] ) * K[0, i*n_virt + t] * K[1, k*n_virt + s + n_ex] * K[2, k*n_virt + s]

										elif ((t != s) and (u == s) and (v == t)):

											L4[i*n_virt + s + n_ex] += (2 * g[n_occ + s, n_occ + t, n_occ + s, n_occ + t] ) * K[0, i*n_virt + t] * K[1, k*n_virt + s + n_ex] * K[2, k*n_virt + t]

										elif ((t != s) and (u == s) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s + n_ex] += (2 * g[n_occ + s, n_occ + t, n_occ + s, n_occ + v] ) * K[0, i*n_virt + t] * K[1, k*n_virt + s + n_ex] * K[2, k*n_virt + v]

										elif ((t != s) and (u == t) and (v == s)):

											L4[i*n_virt + s + n_ex] += (2 * F[i, i] + -2 * F[n_occ + t, n_occ + t] + 2 * g[i, i, n_occ + s, n_occ + s] + -4 * g[i, n_occ + s, i, n_occ + s] + 4 * g[i, k, i, k] + 4 * g[n_occ + s, n_occ + t, n_occ + s, n_occ + t] + -2 * g[n_occ + s, n_occ + s, n_occ + t, n_occ + t] + 2 * g[i, i, n_occ + t, n_occ + t] + 2 * g[k, k, n_occ + t, n_occ + t] + -4 * g[i, n_occ + t, i, n_occ + t] + -4 * g[k, n_occ + t, k, n_occ + t] + -2 * g[i, i, k, k] ) * K[0, i*n_virt + t] * K[1, k*n_virt + t + n_ex] * K[2, k*n_virt + s]

										elif ((t != s) and (u == t) and (v == t)):

											L4[i*n_virt + s + n_ex] += (2 * g[i, i, n_occ + s, n_occ + t] + 2 * g[n_occ + s, n_occ + t, n_occ + t, n_occ + t] + -4 * g[i, n_occ + s, i, n_occ + t] + 2 * g[k, n_occ + s, k, n_occ + t] + -4 * g[k, k, n_occ + s, n_occ + t] ) * K[0, i*n_virt + t] * K[1, k*n_virt + t + n_ex] * K[2, k*n_virt + t]

										elif ((t != s) and (u == t) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s + n_ex] += (-4 * g[i, n_occ + s, i, n_occ + v] + 2 * g[i, i, n_occ + s, n_occ + v] + 4 * g[n_occ + s, n_occ + t, n_occ + t, n_occ + v] + -2 * g[n_occ + s, n_occ + v, n_occ + t, n_occ + t] ) * K[0, i*n_virt + t] * K[1, k*n_virt + t + n_ex] * K[2, k*n_virt + v]

										elif ((t != s) and (u != s) and (u != t) and (v == s)):

											L4[i*n_virt + s + n_ex] += (-2 * F[n_occ + t, n_occ + u] + 4 * g[n_occ + s, n_occ + t, n_occ + s, n_occ + u] + -2 * g[n_occ + s, n_occ + s, n_occ + t, n_occ + u] + 2 * g[i, i, n_occ + t, n_occ + u] + 2 * g[k, k, n_occ + t, n_occ + u] + -4 * g[i, n_occ + t, i, n_occ + u] + -4 * g[k, n_occ + t, k, n_occ + u] ) * K[0, i*n_virt + t] * K[1, k*n_virt + u + n_ex] * K[2, k*n_virt + s]

										elif ((t != s) and (u != s) and (u != t) and (v == t)):

											L4[i*n_virt + s + n_ex] += (2 * g[n_occ + s, n_occ + t, n_occ + t, n_occ + u] ) * K[0, i*n_virt + t] * K[1, k*n_virt + u + n_ex] * K[2, k*n_virt + t]

										elif ((t != s) and (u != s) and (u != t) and (v == u)):

											L4[i*n_virt + s + n_ex] += (-2 * g[n_occ + s, n_occ + u, n_occ + t, n_occ + u] + 4 * g[n_occ + s, n_occ + t, n_occ + u, n_occ + u] + 2 * g[k, n_occ + s, k, n_occ + t] + -4 * g[k, k, n_occ + s, n_occ + t] ) * K[0, i*n_virt + t] * K[1, k*n_virt + u + n_ex] * K[2, k*n_virt + u]

										elif ((t != s) and (u != s) and (u != t) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s + n_ex] += (4 * g[n_occ + s, n_occ + t, n_occ + u, n_occ + v] + -2 * g[n_occ + s, n_occ + v, n_occ + t, n_occ + u] ) * K[0, i*n_virt + t] * K[1, k*n_virt + u + n_ex] * K[2, k*n_virt + v]

									elif ((j == i) and (k != i) and (k != j) and (m != i) and (m != j) and (m != k)):

										if ((t == s) and (u == s) and (v == s)):

											L4[i*n_virt + s + n_ex] += (2 * g[i, k, i, m] + -2 * g[k, m, n_occ + s, n_occ + s] + -2 * g[k, n_occ + s, m, n_occ + s] + 2 * g[i, i, k, m] ) * K[0, i*n_virt + s] * K[1, k*n_virt + s + n_ex] * K[2, m*n_virt + s]

										elif ((t == s) and (u != s) and (u != t) and (v == s)):

											L4[i*n_virt + s + n_ex] += (2 * g[k, m, n_occ + s, n_occ + u] + -4 * g[k, n_occ + u, m, n_occ + s] ) * K[0, i*n_virt + s] * K[1, k*n_virt + u + n_ex] * K[2, m*n_virt + s]

										elif ((t == s) and (u != s) and (u != t) and (v == u)):

											L4[i*n_virt + s + n_ex] += (2 * g[k, n_occ + s, m, n_occ + s] + -4 * g[k, m, n_occ + s, n_occ + s] + -2 * g[i, k, i, m] + 4 * g[i, i, k, m] ) * K[0, i*n_virt + s] * K[1, k*n_virt + u + n_ex] * K[2, m*n_virt + u]

										elif ((t != s) and (u == s) and (v == s)):

											L4[i*n_virt + s + n_ex] += (-2 * g[k, n_occ + s, m, n_occ + t] + -2 * g[k, m, n_occ + s, n_occ + t] ) * K[0, i*n_virt + t] * K[1, k*n_virt + s + n_ex] * K[2, m*n_virt + s]

										elif ((t != s) and (u == t) and (v == s)):

											L4[i*n_virt + s + n_ex] += (4 * g[i, k, i, m] + -2 * g[i, i, k, m] + -4 * g[k, n_occ + t, m, n_occ + t] + 2 * g[k, m, n_occ + t, n_occ + t] ) * K[0, i*n_virt + t] * K[1, k*n_virt + t + n_ex] * K[2, m*n_virt + s]

										elif ((t != s) and (u == t) and (v == t)):

											L4[i*n_virt + s + n_ex] += (-4 * g[k, m, n_occ + s, n_occ + t] + 2 * g[k, n_occ + s, m, n_occ + t] ) * K[0, i*n_virt + t] * K[1, k*n_virt + t + n_ex] * K[2, m*n_virt + t]

										elif ((t != s) and (u != s) and (u != t) and (v == s)):

											L4[i*n_virt + s + n_ex] += (2 * g[k, m, n_occ + t, n_occ + u] + -4 * g[k, n_occ + u, m, n_occ + t] ) * K[0, i*n_virt + t] * K[1, k*n_virt + u + n_ex] * K[2, m*n_virt + s]

										elif ((t != s) and (u != s) and (u != t) and (v == u)):

											L4[i*n_virt + s + n_ex] += (-4 * g[k, m, n_occ + s, n_occ + t] + 2 * g[k, n_occ + s, m, n_occ + t] ) * K[0, i*n_virt + t] * K[1, k*n_virt + u + n_ex] * K[2, m*n_virt + u]

									elif ((j != i) and (k == i) and (m == i)):

										if ((t == s) and (u == s) and (v == s)):

											L4[i*n_virt + s + n_ex] += (4 * F[i, j] + -12 * g[i, n_occ + s, j, n_occ + s] + 4 * g[i, i, i, j] ) * K[0, j*n_virt + s] * K[1, i*n_virt + s + n_ex] * K[2, i*n_virt + s]

										elif ((t == s) and (u == s) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s + n_ex] += (-4 * g[i, n_occ + s, j, n_occ + v] + -4 * g[i, j, n_occ + s, n_occ + v] ) * K[0, j*n_virt + s] * K[1, i*n_virt + s + n_ex] * K[2, i*n_virt + v]

										elif ((t == s) and (u != s) and (u != t) and (v == s)):

											L4[i*n_virt + s + n_ex] += (-6 * g[i, n_occ + u, j, n_occ + s] ) * K[0, j*n_virt + s] * K[1, i*n_virt + u + n_ex] * K[2, i*n_virt + s]

										elif ((t == s) and (u != s) and (u != t) and (v == u)):

											L4[i*n_virt + s + n_ex] += (2 * F[i, j] + -2 * g[i, n_occ + u, j, n_occ + u] + -2 * g[i, j, n_occ + u, n_occ + u] + -4 * g[i, n_occ + s, j, n_occ + s] + 2 * g[i, j, n_occ + s, n_occ + s] + 2 * g[i, i, i, j] ) * K[0, j*n_virt + s] * K[1, i*n_virt + u + n_ex] * K[2, i*n_virt + u]

										elif ((t == s) and (u != s) and (u != t) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s + n_ex] += (-2 * g[i, n_occ + u, j, n_occ + v] + -2 * g[i, j, n_occ + u, n_occ + v] ) * K[0, j*n_virt + s] * K[1, i*n_virt + u + n_ex] * K[2, i*n_virt + v]

										elif ((t != s) and (u == s) and (v == s)):

											L4[i*n_virt + s + n_ex] += (4 * g[i, j, n_occ + s, n_occ + t] + -8 * g[i, n_occ + s, j, n_occ + t] ) * K[0, j*n_virt + t] * K[1, i*n_virt + s + n_ex] * K[2, i*n_virt + s]

										elif ((t != s) and (u == t) and (v == s)):

											L4[i*n_virt + s + n_ex] += (2 * F[i, j] + -4 * g[i, n_occ + t, j, n_occ + t] + 2 * g[i, j, n_occ + t, n_occ + t] + -2 * g[i, j, n_occ + s, n_occ + s] + -2 * g[i, n_occ + s, j, n_occ + s] + 2 * g[i, i, i, j] ) * K[0, j*n_virt + t] * K[1, i*n_virt + t + n_ex] * K[2, i*n_virt + s]

										elif ((t != s) and (u == t) and (v == t)):

											L4[i*n_virt + s + n_ex] += (-6 * g[i, n_occ + s, j, n_occ + t] ) * K[0, j*n_virt + t] * K[1, i*n_virt + t + n_ex] * K[2, i*n_virt + t]

										elif ((t != s) and (u == t) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s + n_ex] += (-2 * g[i, j, n_occ + s, n_occ + v] + -2 * g[i, n_occ + s, j, n_occ + v] ) * K[0, j*n_virt + t] * K[1, i*n_virt + t + n_ex] * K[2, i*n_virt + v]

										elif ((t != s) and (u != s) and (u != t) and (v == s)):

											L4[i*n_virt + s + n_ex] += (2 * g[i, j, n_occ + t, n_occ + u] + -4 * g[i, n_occ + u, j, n_occ + t] ) * K[0, j*n_virt + t] * K[1, i*n_virt + u + n_ex] * K[2, i*n_virt + s]

										elif ((t != s) and (u != s) and (u != t) and (v == u)):

											L4[i*n_virt + s + n_ex] += (-4 * g[i, n_occ + s, j, n_occ + t] + 2 * g[i, j, n_occ + s, n_occ + t] ) * K[0, j*n_virt + t] * K[1, i*n_virt + u + n_ex] * K[2, i*n_virt + u]

									elif ((j != i) and (k == i) and (m == j)):

										if ((t == s) and (u == s) and (v == s)):

											L4[i*n_virt + s + n_ex] += (4 * g[i, j, i, j] ) * K[0, j*n_virt + s] * K[1, i*n_virt + s + n_ex] * K[2, j*n_virt + s]

										elif ((t == s) and (u != s) and (u != t) and (v == u)):

											L4[i*n_virt + s + n_ex] += (2 * g[i, j, i, j] ) * K[0, j*n_virt + s] * K[1, i*n_virt + u + n_ex] * K[2, j*n_virt + u]

										elif ((t != s) and (u == t) and (v == s)):

											L4[i*n_virt + s + n_ex] += (2 * g[i, j, i, j] ) * K[0, j*n_virt + t] * K[1, i*n_virt + t + n_ex] * K[2, j*n_virt + s]

									elif ((j != i) and (k == i) and (m != i) and (m != j) and (m != k)):

										if ((t == s) and (u == s) and (v == s)):

											L4[i*n_virt + s + n_ex] += (4 * g[i, j, i, m] ) * K[0, j*n_virt + s] * K[1, i*n_virt + s + n_ex] * K[2, m*n_virt + s]

										elif ((t == s) and (u != s) and (u != t) and (v == u)):

											L4[i*n_virt + s + n_ex] += (2 * g[i, j, i, m] ) * K[0, j*n_virt + s] * K[1, i*n_virt + u + n_ex] * K[2, m*n_virt + u]

										elif ((t != s) and (u == t) and (v == s)):

											L4[i*n_virt + s + n_ex] += (2 * g[i, j, i, m] ) * K[0, j*n_virt + t] * K[1, i*n_virt + t + n_ex] * K[2, m*n_virt + s]

									elif ((j != i) and (k == j) and (m == i)):

										if ((t == s) and (u == s) and (v == s)):

											L4[i*n_virt + s + n_ex] += (2 * F[j, j] + -2 * F[n_occ + s, n_occ + s] + -6 * g[j, n_occ + s, j, n_occ + s] + -2 * g[i, i, n_occ + s, n_occ + s] + 2 * g[n_occ + s, n_occ + s, n_occ + s, n_occ + s] + 2 * g[i, i, j, j] + 2 * g[i, j, i, j] + -2 * g[i, n_occ + s, i, n_occ + s] ) * K[0, j*n_virt + s] * K[1, j*n_virt + s + n_ex] * K[2, i*n_virt + s]

										elif ((t == s) and (u == s) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s + n_ex] += (-2 * g[j, n_occ + s, j, n_occ + v] + 2 * g[n_occ + s, n_occ + s, n_occ + s, n_occ + v] + -2 * g[j, j, n_occ + s, n_occ + v] ) * K[0, j*n_virt + s] * K[1, j*n_virt + s + n_ex] * K[2, i*n_virt + v]

										elif ((t == s) and (u != s) and (u != t) and (v == s)):

											L4[i*n_virt + s + n_ex] += (2 * g[i, n_occ + s, i, n_occ + u] + -4 * g[j, n_occ + s, j, n_occ + u] + -4 * g[i, i, n_occ + s, n_occ + u] + 2 * g[j, j, n_occ + s, n_occ + u] + 2 * g[n_occ + s, n_occ + s, n_occ + s, n_occ + u] ) * K[0, j*n_virt + s] * K[1, j*n_virt + u + n_ex] * K[2, i*n_virt + s]

										elif ((t == s) and (u != s) and (u != t) and (v == u)):

											L4[i*n_virt + s + n_ex] += (2 * F[j, j] + -2 * F[n_occ + s, n_occ + s] + 2 * g[j, j, n_occ + u, n_occ + u] + -4 * g[j, n_occ + u, j, n_occ + u] + 4 * g[i, j, i, j] + 4 * g[n_occ + s, n_occ + u, n_occ + s, n_occ + u] + -2 * g[n_occ + s, n_occ + s, n_occ + u, n_occ + u] + 2 * g[i, i, n_occ + s, n_occ + s] + 2 * g[j, j, n_occ + s, n_occ + s] + -4 * g[j, n_occ + s, j, n_occ + s] + -4 * g[i, n_occ + s, i, n_occ + s] + -2 * g[i, i, j, j] ) * K[0, j*n_virt + s] * K[1, j*n_virt + u + n_ex] * K[2, i*n_virt + u]

										elif ((t == s) and (u != s) and (u != t) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s + n_ex] += (-4 * g[j, n_occ + u, j, n_occ + v] + 2 * g[j, j, n_occ + u, n_occ + v] + 4 * g[n_occ + s, n_occ + u, n_occ + s, n_occ + v] + -2 * g[n_occ + s, n_occ + s, n_occ + u, n_occ + v] ) * K[0, j*n_virt + s] * K[1, j*n_virt + u + n_ex] * K[2, i*n_virt + v]

										elif ((t != s) and (u == s) and (v == s)):

											L4[i*n_virt + s + n_ex] += (-2 * F[n_occ + s, n_occ + t] + -2 * g[i, i, n_occ + s, n_occ + t] + 2 * g[j, j, n_occ + s, n_occ + t] + -4 * g[j, n_occ + s, j, n_occ + t] + 2 * g[n_occ + s, n_occ + s, n_occ + s, n_occ + t] + -2 * g[i, n_occ + s, i, n_occ + t] ) * K[0, j*n_virt + t] * K[1, j*n_virt + s + n_ex] * K[2, i*n_virt + s]

										elif ((t != s) and (u == s) and (v == t)):

											L4[i*n_virt + s + n_ex] += (2 * g[n_occ + s, n_occ + t, n_occ + s, n_occ + t] ) * K[0, j*n_virt + t] * K[1, j*n_virt + s + n_ex] * K[2, i*n_virt + t]

										elif ((t != s) and (u == s) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s + n_ex] += (2 * g[n_occ + s, n_occ + t, n_occ + s, n_occ + v] ) * K[0, j*n_virt + t] * K[1, j*n_virt + s + n_ex] * K[2, i*n_virt + v]

										elif ((t != s) and (u == t) and (v == s)):

											L4[i*n_virt + s + n_ex] += (-4 * g[i, i, n_occ + t, n_occ + t] + 2 * g[i, n_occ + t, i, n_occ + t] + -2 * g[n_occ + s, n_occ + t, n_occ + s, n_occ + t] + 4 * g[n_occ + s, n_occ + s, n_occ + t, n_occ + t] + -4 * g[j, j, n_occ + s, n_occ + s] + 2 * g[j, n_occ + s, j, n_occ + s] + -2 * g[i, j, i, j] + 4 * g[i, i, j, j] ) * K[0, j*n_virt + t] * K[1, j*n_virt + t + n_ex] * K[2, i*n_virt + s]

										elif ((t != s) and (u == t) and (v == t)):

											L4[i*n_virt + s + n_ex] += (-2 * F[n_occ + s, n_occ + t] + 2 * g[n_occ + s, n_occ + t, n_occ + t, n_occ + t] + -2 * g[j, j, n_occ + s, n_occ + t] + -4 * g[i, n_occ + s, i, n_occ + t] + 2 * g[i, i, n_occ + s, n_occ + t] + -2 * g[j, n_occ + s, j, n_occ + t] ) * K[0, j*n_virt + t] * K[1, j*n_virt + t + n_ex] * K[2, i*n_virt + t]

										elif ((t != s) and (u == t) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s + n_ex] += (-2 * g[n_occ + s, n_occ + t, n_occ + t, n_occ + v] + 4 * g[n_occ + s, n_occ + v, n_occ + t, n_occ + t] + 2 * g[j, n_occ + s, j, n_occ + v] + -4 * g[j, j, n_occ + s, n_occ + v] ) * K[0, j*n_virt + t] * K[1, j*n_virt + t + n_ex] * K[2, i*n_virt + v]

										elif ((t != s) and (u != s) and (u != t) and (v == s)):

											L4[i*n_virt + s + n_ex] += (2 * g[i, n_occ + t, i, n_occ + u] + -4 * g[i, i, n_occ + t, n_occ + u] + -2 * g[n_occ + s, n_occ + t, n_occ + s, n_occ + u] + 4 * g[n_occ + s, n_occ + s, n_occ + t, n_occ + u] ) * K[0, j*n_virt + t] * K[1, j*n_virt + u + n_ex] * K[2, i*n_virt + s]

										elif ((t != s) and (u != s) and (u != t) and (v == t)):

											L4[i*n_virt + s + n_ex] += (2 * g[n_occ + s, n_occ + t, n_occ + t, n_occ + u] ) * K[0, j*n_virt + t] * K[1, j*n_virt + u + n_ex] * K[2, i*n_virt + t]

										elif ((t != s) and (u != s) and (u != t) and (v == u)):

											L4[i*n_virt + s + n_ex] += (-2 * F[n_occ + s, n_occ + t] + 4 * g[n_occ + s, n_occ + u, n_occ + t, n_occ + u] + -2 * g[n_occ + s, n_occ + t, n_occ + u, n_occ + u] + 2 * g[i, i, n_occ + s, n_occ + t] + 2 * g[j, j, n_occ + s, n_occ + t] + -4 * g[j, n_occ + s, j, n_occ + t] + -4 * g[i, n_occ + s, i, n_occ + t] ) * K[0, j*n_virt + t] * K[1, j*n_virt + u + n_ex] * K[2, i*n_virt + u]

										elif ((t != s) and (u != s) and (u != t) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s + n_ex] += (-2 * g[n_occ + s, n_occ + t, n_occ + u, n_occ + v] + 4 * g[n_occ + s, n_occ + v, n_occ + t, n_occ + u] ) * K[0, j*n_virt + t] * K[1, j*n_virt + u + n_ex] * K[2, i*n_virt + v]

									elif ((j != i) and (k == j) and (m == j)):

										if ((t == s) and (u == s) and (v == s)):

											L4[i*n_virt + s + n_ex] += (2 * F[i, j] + -2 * g[i, j, n_occ + s, n_occ + s] + 4 * g[i, j, j, j] + -8 * g[i, n_occ + s, j, n_occ + s] ) * K[0, j*n_virt + s] * K[1, j*n_virt + s + n_ex] * K[2, j*n_virt + s]

										elif ((t == s) and (u == s) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s + n_ex] += (-2 * g[i, j, n_occ + s, n_occ + v] + -2 * g[i, n_occ + s, j, n_occ + v] ) * K[0, j*n_virt + s] * K[1, j*n_virt + s + n_ex] * K[2, j*n_virt + v]

										elif ((t == s) and (u != s) and (u != t) and (v == s)):

											L4[i*n_virt + s + n_ex] += (-6 * g[i, j, n_occ + s, n_occ + u] ) * K[0, j*n_virt + s] * K[1, j*n_virt + u + n_ex] * K[2, j*n_virt + s]

										elif ((t == s) and (u != s) and (u != t) and (v == u)):

											L4[i*n_virt + s + n_ex] += (2 * g[i, n_occ + u, j, n_occ + u] + -4 * g[i, j, n_occ + u, n_occ + u] + -4 * g[i, n_occ + s, j, n_occ + s] + 2 * g[i, j, j, j] + 2 * g[i, j, n_occ + s, n_occ + s] ) * K[0, j*n_virt + s] * K[1, j*n_virt + u + n_ex] * K[2, j*n_virt + u]

										elif ((t == s) and (u != s) and (u != t) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s + n_ex] += (-4 * g[i, j, n_occ + u, n_occ + v] + 2 * g[i, n_occ + u, j, n_occ + v] ) * K[0, j*n_virt + s] * K[1, j*n_virt + u + n_ex] * K[2, j*n_virt + v]

										elif ((t != s) and (u == s) and (v == s)):

											L4[i*n_virt + s + n_ex] += (-6 * g[i, n_occ + s, j, n_occ + t] ) * K[0, j*n_virt + t] * K[1, j*n_virt + s + n_ex] * K[2, j*n_virt + s]

										elif ((t != s) and (u == t) and (v == s)):

											L4[i*n_virt + s + n_ex] += (2 * F[i, j] + -2 * g[i, n_occ + t, j, n_occ + t] + -2 * g[i, j, n_occ + t, n_occ + t] + -4 * g[i, n_occ + s, j, n_occ + s] + 2 * g[i, j, n_occ + s, n_occ + s] + 2 * g[i, j, j, j] ) * K[0, j*n_virt + t] * K[1, j*n_virt + t + n_ex] * K[2, j*n_virt + s]

										elif ((t != s) and (u == t) and (v == t)):

											L4[i*n_virt + s + n_ex] += (4 * g[i, j, n_occ + s, n_occ + t] + -8 * g[i, n_occ + s, j, n_occ + t] ) * K[0, j*n_virt + t] * K[1, j*n_virt + t + n_ex] * K[2, j*n_virt + t]

										elif ((t != s) and (u == t) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s + n_ex] += (-4 * g[i, n_occ + s, j, n_occ + v] + 2 * g[i, j, n_occ + s, n_occ + v] ) * K[0, j*n_virt + t] * K[1, j*n_virt + t + n_ex] * K[2, j*n_virt + v]

										elif ((t != s) and (u != s) and (u != t) and (v == s)):

											L4[i*n_virt + s + n_ex] += (-2 * g[i, n_occ + u, j, n_occ + t] + -2 * g[i, j, n_occ + t, n_occ + u] ) * K[0, j*n_virt + t] * K[1, j*n_virt + u + n_ex] * K[2, j*n_virt + s]

										elif ((t != s) and (u != s) and (u != t) and (v == u)):

											L4[i*n_virt + s + n_ex] += (-4 * g[i, n_occ + s, j, n_occ + t] + 2 * g[i, j, n_occ + s, n_occ + t] ) * K[0, j*n_virt + t] * K[1, j*n_virt + u + n_ex] * K[2, j*n_virt + u]

									elif ((j != i) and (k == j) and (m != i) and (m != j) and (m != k)):

										if ((t == s) and (u == s) and (v == s)):

											L4[i*n_virt + s + n_ex] += (2 * g[i, j, j, m] + -2 * g[i, m, n_occ + s, n_occ + s] + -2 * g[i, n_occ + s, m, n_occ + s] + 2 * g[i, m, j, j] ) * K[0, j*n_virt + s] * K[1, j*n_virt + s + n_ex] * K[2, m*n_virt + s]

										elif ((t == s) and (u != s) and (u != t) and (v == s)):

											L4[i*n_virt + s + n_ex] += (-4 * g[i, m, n_occ + s, n_occ + u] + 2 * g[i, n_occ + u, m, n_occ + s] ) * K[0, j*n_virt + s] * K[1, j*n_virt + u + n_ex] * K[2, m*n_virt + s]

										elif ((t == s) and (u != s) and (u != t) and (v == u)):

											L4[i*n_virt + s + n_ex] += (4 * g[i, j, j, m] + -2 * g[i, m, j, j] + -4 * g[i, n_occ + s, m, n_occ + s] + 2 * g[i, m, n_occ + s, n_occ + s] ) * K[0, j*n_virt + s] * K[1, j*n_virt + u + n_ex] * K[2, m*n_virt + u]

										elif ((t != s) and (u == s) and (v == s)):

											L4[i*n_virt + s + n_ex] += (-2 * g[i, m, n_occ + s, n_occ + t] + -2 * g[i, n_occ + s, m, n_occ + t] ) * K[0, j*n_virt + t] * K[1, j*n_virt + s + n_ex] * K[2, m*n_virt + s]

										elif ((t != s) and (u == t) and (v == s)):

											L4[i*n_virt + s + n_ex] += (2 * g[i, n_occ + t, m, n_occ + t] + -4 * g[i, m, n_occ + t, n_occ + t] + -2 * g[i, j, j, m] + 4 * g[i, m, j, j] ) * K[0, j*n_virt + t] * K[1, j*n_virt + t + n_ex] * K[2, m*n_virt + s]

										elif ((t != s) and (u == t) and (v == t)):

											L4[i*n_virt + s + n_ex] += (-4 * g[i, n_occ + s, m, n_occ + t] + 2 * g[i, m, n_occ + s, n_occ + t] ) * K[0, j*n_virt + t] * K[1, j*n_virt + t + n_ex] * K[2, m*n_virt + t]

										elif ((t != s) and (u != s) and (u != t) and (v == s)):

											L4[i*n_virt + s + n_ex] += (-4 * g[i, m, n_occ + t, n_occ + u] + 2 * g[i, n_occ + u, m, n_occ + t] ) * K[0, j*n_virt + t] * K[1, j*n_virt + u + n_ex] * K[2, m*n_virt + s]

										elif ((t != s) and (u != s) and (u != t) and (v == u)):

											L4[i*n_virt + s + n_ex] += (2 * g[i, m, n_occ + s, n_occ + t] + -4 * g[i, n_occ + s, m, n_occ + t] ) * K[0, j*n_virt + t] * K[1, j*n_virt + u + n_ex] * K[2, m*n_virt + u]

									elif ((j != i) and (k != i) and (k != j) and (m == i)):

										if ((t == s) and (u == s) and (v == s)):

											L4[i*n_virt + s + n_ex] += (2 * F[j, k] + -6 * g[j, n_occ + s, k, n_occ + s] + 2 * g[i, i, j, k] + 2 * g[i, j, i, k] ) * K[0, j*n_virt + s] * K[1, k*n_virt + s + n_ex] * K[2, i*n_virt + s]

										elif ((t == s) and (u == s) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s + n_ex] += (-2 * g[j, n_occ + v, k, n_occ + s] + -2 * g[j, k, n_occ + s, n_occ + v] ) * K[0, j*n_virt + s] * K[1, k*n_virt + s + n_ex] * K[2, i*n_virt + v]

										elif ((t == s) and (u != s) and (u != t) and (v == s)):

											L4[i*n_virt + s + n_ex] += (2 * g[j, k, n_occ + s, n_occ + u] + -4 * g[j, n_occ + s, k, n_occ + u] ) * K[0, j*n_virt + s] * K[1, k*n_virt + u + n_ex] * K[2, i*n_virt + s]

										elif ((t == s) and (u != s) and (u != t) and (v == u)):

											L4[i*n_virt + s + n_ex] += (2 * F[j, k] + -4 * g[j, n_occ + s, k, n_occ + s] + -4 * g[j, n_occ + u, k, n_occ + u] + 2 * g[j, k, n_occ + s, n_occ + s] + 2 * g[j, k, n_occ + u, n_occ + u] + -2 * g[i, i, j, k] + 4 * g[i, j, i, k] ) * K[0, j*n_virt + s] * K[1, k*n_virt + u + n_ex] * K[2, i*n_virt + u]

										elif ((t == s) and (u != s) and (u != t) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s + n_ex] += (2 * g[j, k, n_occ + u, n_occ + v] + -4 * g[j, n_occ + v, k, n_occ + u] ) * K[0, j*n_virt + s] * K[1, k*n_virt + u + n_ex] * K[2, i*n_virt + v]

										elif ((t != s) and (u == s) and (v == s)):

											L4[i*n_virt + s + n_ex] += (2 * g[j, k, n_occ + s, n_occ + t] + -4 * g[j, n_occ + t, k, n_occ + s] ) * K[0, j*n_virt + t] * K[1, k*n_virt + s + n_ex] * K[2, i*n_virt + s]

										elif ((t != s) and (u == t) and (v == s)):

											L4[i*n_virt + s + n_ex] += (-2 * g[i, j, i, k] + 4 * g[i, i, j, k] + 2 * g[j, n_occ + s, k, n_occ + s] + -4 * g[j, k, n_occ + s, n_occ + s] ) * K[0, j*n_virt + t] * K[1, k*n_virt + t + n_ex] * K[2, i*n_virt + s]

										elif ((t != s) and (u == t) and (v == t)):

											L4[i*n_virt + s + n_ex] += (-2 * g[j, n_occ + t, k, n_occ + s] + -2 * g[j, k, n_occ + s, n_occ + t] ) * K[0, j*n_virt + t] * K[1, k*n_virt + t + n_ex] * K[2, i*n_virt + t]

										elif ((t != s) and (u == t) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s + n_ex] += (-4 * g[j, k, n_occ + s, n_occ + v] + 2 * g[j, n_occ + v, k, n_occ + s] ) * K[0, j*n_virt + t] * K[1, k*n_virt + t + n_ex] * K[2, i*n_virt + v]

										elif ((t != s) and (u != s) and (u != t) and (v == u)):

											L4[i*n_virt + s + n_ex] += (2 * g[j, k, n_occ + s, n_occ + t] + -4 * g[j, n_occ + t, k, n_occ + s] ) * K[0, j*n_virt + t] * K[1, k*n_virt + u + n_ex] * K[2, i*n_virt + u]

									elif ((j != i) and (k != i) and (k != j) and (m == j)):

										if ((t == s) and (u == s) and (v == s)):

											L4[i*n_virt + s + n_ex] += (4 * g[i, j, j, k] ) * K[0, j*n_virt + s] * K[1, k*n_virt + s + n_ex] * K[2, j*n_virt + s]

										elif ((t == s) and (u != s) and (u != t) and (v == u)):

											L4[i*n_virt + s + n_ex] += (2 * g[i, j, j, k] ) * K[0, j*n_virt + s] * K[1, k*n_virt + u + n_ex] * K[2, j*n_virt + u]

										elif ((t != s) and (u == t) and (v == s)):

											L4[i*n_virt + s + n_ex] += (2 * g[i, j, j, k] ) * K[0, j*n_virt + t] * K[1, k*n_virt + t + n_ex] * K[2, j*n_virt + s]

									elif ((j != i) and (k != i) and (k != j) and (m == k)):

										if ((t == s) and (u == s) and (v == s)):

											L4[i*n_virt + s + n_ex] += (2 * F[i, j] + -6 * g[i, n_occ + s, j, n_occ + s] + 2 * g[i, j, k, k] + 2 * g[i, k, j, k] ) * K[0, j*n_virt + s] * K[1, k*n_virt + s + n_ex] * K[2, k*n_virt + s]

										elif ((t == s) and (u == s) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s + n_ex] += (-2 * g[i, j, n_occ + s, n_occ + v] + -2 * g[i, n_occ + s, j, n_occ + v] ) * K[0, j*n_virt + s] * K[1, k*n_virt + s + n_ex] * K[2, k*n_virt + v]

										elif ((t == s) and (u != s) and (u != t) and (v == s)):

											L4[i*n_virt + s + n_ex] += (-2 * g[i, n_occ + u, j, n_occ + s] + -2 * g[i, j, n_occ + s, n_occ + u] ) * K[0, j*n_virt + s] * K[1, k*n_virt + u + n_ex] * K[2, k*n_virt + s]

										elif ((t == s) and (u != s) and (u != t) and (v == u)):

											L4[i*n_virt + s + n_ex] += (2 * g[i, n_occ + u, j, n_occ + u] + -4 * g[i, j, n_occ + u, n_occ + u] + -2 * g[i, k, j, k] + 4 * g[i, j, k, k] ) * K[0, j*n_virt + s] * K[1, k*n_virt + u + n_ex] * K[2, k*n_virt + u]

										elif ((t == s) and (u != s) and (u != t) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s + n_ex] += (-4 * g[i, j, n_occ + u, n_occ + v] + 2 * g[i, n_occ + u, j, n_occ + v] ) * K[0, j*n_virt + s] * K[1, k*n_virt + u + n_ex] * K[2, k*n_virt + v]

										elif ((t != s) and (u == s) and (v == s)):

											L4[i*n_virt + s + n_ex] += (-4 * g[i, n_occ + s, j, n_occ + t] + 2 * g[i, j, n_occ + s, n_occ + t] ) * K[0, j*n_virt + t] * K[1, k*n_virt + s + n_ex] * K[2, k*n_virt + s]

										elif ((t != s) and (u == t) and (v == s)):

											L4[i*n_virt + s + n_ex] += (2 * F[i, j] + -4 * g[i, n_occ + s, j, n_occ + s] + -4 * g[i, n_occ + t, j, n_occ + t] + 2 * g[i, j, n_occ + s, n_occ + s] + 2 * g[i, j, n_occ + t, n_occ + t] + -2 * g[i, j, k, k] + 4 * g[i, k, j, k] ) * K[0, j*n_virt + t] * K[1, k*n_virt + t + n_ex] * K[2, k*n_virt + s]

										elif ((t != s) and (u == t) and (v == t)):

											L4[i*n_virt + s + n_ex] += (-4 * g[i, n_occ + s, j, n_occ + t] + 2 * g[i, j, n_occ + s, n_occ + t] ) * K[0, j*n_virt + t] * K[1, k*n_virt + t + n_ex] * K[2, k*n_virt + t]

										elif ((t != s) and (u == t) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s + n_ex] += (2 * g[i, j, n_occ + s, n_occ + v] + -4 * g[i, n_occ + s, j, n_occ + v] ) * K[0, j*n_virt + t] * K[1, k*n_virt + t + n_ex] * K[2, k*n_virt + v]

										elif ((t != s) and (u != s) and (u != t) and (v == s)):

											L4[i*n_virt + s + n_ex] += (2 * g[i, j, n_occ + t, n_occ + u] + -4 * g[i, n_occ + u, j, n_occ + t] ) * K[0, j*n_virt + t] * K[1, k*n_virt + u + n_ex] * K[2, k*n_virt + s]

									elif ((j != i) and (k != i) and (k != j) and (m != i) and (m != j) and (m != k)):

										if ((t == s) and (u == s) and (v == s)):

											L4[i*n_virt + s + n_ex] += (2 * g[i, m, j, k] + 2 * g[i, j, k, m] ) * K[0, j*n_virt + s] * K[1, k*n_virt + s + n_ex] * K[2, m*n_virt + s]

										elif ((t == s) and (u != s) and (u != t) and (v == u)):

											L4[i*n_virt + s + n_ex] += (4 * g[i, j, k, m] + -2 * g[i, m, j, k] ) * K[0, j*n_virt + s] * K[1, k*n_virt + u + n_ex] * K[2, m*n_virt + u]

										elif ((t != s) and (u == t) and (v == s)):

											L4[i*n_virt + s + n_ex] += (-2 * g[i, j, k, m] + 4 * g[i, m, j, k] ) * K[0, j*n_virt + t] * K[1, k*n_virt + t + n_ex] * K[2, m*n_virt + s]

	# Current operator combination: {'a': 1, 'b': 2, 'c': 1, 'd': 3}
	# All terms vanished for this combination

	# Current operator combination: {'a': 1, 'b': 2, 'c': 2, 'd': 1}
	for i in range(n_occ):
		for j in range(n_occ):
			for k in range(n_occ):
				for m in range(n_occ):
					for s in range(n_virt):
						for t in range(n_virt):
							for u in range(n_virt):
								for v in range(n_virt):

									if ((j == i) and (k == i) and (m == i)):

										if ((t == s) and (u == s) and (v == s)):

											L4[i*n_virt + s] += (-4 * g[n_occ + s, n_occ + s, n_occ + s, n_occ + s] + 8 * g[i, i, n_occ + s, n_occ + s] + 8 * g[i, n_occ + s, i, n_occ + s] + -4 * g[i, i, i, i] ) * K[0, i*n_virt + s + n_ex] * K[1, i*n_virt + s + n_ex] * K[2, i*n_virt + s]

										elif ((t == s) and (u == s) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s] += (4 * g[i, i, n_occ + s, n_occ + v] + 4 * g[i, n_occ + s, i, n_occ + v] + -4 * g[n_occ + s, n_occ + s, n_occ + s, n_occ + v] ) * K[0, i*n_virt + s + n_ex] * K[1, i*n_virt + s + n_ex] * K[2, i*n_virt + v]

										elif ((t == s) and (u != s) and (u != t) and (v == s)):

											L4[i*n_virt + s] += (-4 * g[n_occ + s, n_occ + s, n_occ + s, n_occ + u] + 4 * g[i, i, n_occ + s, n_occ + u] + 4 * g[i, n_occ + s, i, n_occ + u] ) * K[0, i*n_virt + s + n_ex] * K[1, i*n_virt + u + n_ex] * K[2, i*n_virt + s]

										elif ((t == s) and (u != s) and (u != t) and (v == u)):

											L4[i*n_virt + s] += (2 * g[i, i, n_occ + u, n_occ + u] + 2 * g[i, n_occ + u, i, n_occ + u] + -2 * g[n_occ + s, n_occ + s, n_occ + u, n_occ + u] + -2 * g[n_occ + s, n_occ + u, n_occ + s, n_occ + u] + 2 * g[i, n_occ + s, i, n_occ + s] + 2 * g[i, i, n_occ + s, n_occ + s] + -2 * g[i, i, i, i] ) * K[0, i*n_virt + s + n_ex] * K[1, i*n_virt + u + n_ex] * K[2, i*n_virt + u]

										elif ((t == s) and (u != s) and (u != t) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s] += (2 * g[i, i, n_occ + u, n_occ + v] + 2 * g[i, n_occ + u, i, n_occ + v] + -2 * g[n_occ + s, n_occ + u, n_occ + s, n_occ + v] + -2 * g[n_occ + s, n_occ + s, n_occ + u, n_occ + v] ) * K[0, i*n_virt + s + n_ex] * K[1, i*n_virt + u + n_ex] * K[2, i*n_virt + v]

										elif ((t != s) and (u == s) and (v == s)):

											L4[i*n_virt + s] += (-4 * g[n_occ + s, n_occ + s, n_occ + s, n_occ + t] + 4 * g[i, i, n_occ + s, n_occ + t] + 4 * g[i, n_occ + s, i, n_occ + t] ) * K[0, i*n_virt + t + n_ex] * K[1, i*n_virt + s + n_ex] * K[2, i*n_virt + s]

										elif ((t != s) and (u == s) and (v == t)):

											L4[i*n_virt + s] += (2 * g[i, i, n_occ + t, n_occ + t] + 2 * g[i, n_occ + t, i, n_occ + t] + -2 * g[n_occ + s, n_occ + s, n_occ + t, n_occ + t] + -2 * g[n_occ + s, n_occ + t, n_occ + s, n_occ + t] + 2 * g[i, n_occ + s, i, n_occ + s] + 2 * g[i, i, n_occ + s, n_occ + s] + -2 * g[i, i, i, i] ) * K[0, i*n_virt + t + n_ex] * K[1, i*n_virt + s + n_ex] * K[2, i*n_virt + t]

										elif ((t != s) and (u == s) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s] += (2 * g[i, n_occ + t, i, n_occ + v] + 2 * g[i, i, n_occ + t, n_occ + v] + -2 * g[n_occ + s, n_occ + s, n_occ + t, n_occ + v] + -2 * g[n_occ + s, n_occ + t, n_occ + s, n_occ + v] ) * K[0, i*n_virt + t + n_ex] * K[1, i*n_virt + s + n_ex] * K[2, i*n_virt + v]

										elif ((t != s) and (u == t) and (v == s)):

											L4[i*n_virt + s] += (-4 * g[n_occ + s, n_occ + t, n_occ + s, n_occ + t] ) * K[0, i*n_virt + t + n_ex] * K[1, i*n_virt + t + n_ex] * K[2, i*n_virt + s]

										elif ((t != s) and (u == t) and (v == t)):

											L4[i*n_virt + s] += (-4 * g[n_occ + s, n_occ + t, n_occ + t, n_occ + t] + 4 * g[i, i, n_occ + s, n_occ + t] + 4 * g[i, n_occ + s, i, n_occ + t] ) * K[0, i*n_virt + t + n_ex] * K[1, i*n_virt + t + n_ex] * K[2, i*n_virt + t]

										elif ((t != s) and (u == t) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s] += (-4 * g[n_occ + s, n_occ + t, n_occ + t, n_occ + v] ) * K[0, i*n_virt + t + n_ex] * K[1, i*n_virt + t + n_ex] * K[2, i*n_virt + v]

										elif ((t != s) and (u != s) and (u != t) and (v == s)):

											L4[i*n_virt + s] += (-4 * g[n_occ + s, n_occ + t, n_occ + s, n_occ + u] ) * K[0, i*n_virt + t + n_ex] * K[1, i*n_virt + u + n_ex] * K[2, i*n_virt + s]

										elif ((t != s) and (u != s) and (u != t) and (v == t)):

											L4[i*n_virt + s] += (-2 * g[n_occ + s, n_occ + u, n_occ + t, n_occ + t] + -2 * g[n_occ + s, n_occ + t, n_occ + t, n_occ + u] + 2 * g[i, n_occ + s, i, n_occ + u] + 2 * g[i, i, n_occ + s, n_occ + u] ) * K[0, i*n_virt + t + n_ex] * K[1, i*n_virt + u + n_ex] * K[2, i*n_virt + t]

										elif ((t != s) and (u != s) and (u != t) and (v == u)):

											L4[i*n_virt + s] += (-2 * g[n_occ + s, n_occ + u, n_occ + t, n_occ + u] + -2 * g[n_occ + s, n_occ + t, n_occ + u, n_occ + u] + 2 * g[i, n_occ + s, i, n_occ + t] + 2 * g[i, i, n_occ + s, n_occ + t] ) * K[0, i*n_virt + t + n_ex] * K[1, i*n_virt + u + n_ex] * K[2, i*n_virt + u]

										elif ((t != s) and (u != s) and (u != t) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s] += (-2 * g[n_occ + s, n_occ + u, n_occ + t, n_occ + v] + -2 * g[n_occ + s, n_occ + t, n_occ + u, n_occ + v] ) * K[0, i*n_virt + t + n_ex] * K[1, i*n_virt + u + n_ex] * K[2, i*n_virt + v]

									elif ((j == i) and (k == i) and (m != i) and (m != j) and (m != k)):

										if ((t == s) and (u == s) and (v == s)):

											L4[i*n_virt + s] += (4 * g[i, n_occ + s, m, n_occ + s] + -4 * g[i, i, i, m] + 4 * g[i, m, n_occ + s, n_occ + s] ) * K[0, i*n_virt + s + n_ex] * K[1, i*n_virt + s + n_ex] * K[2, m*n_virt + s]

										elif ((t == s) and (u == s) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s] += (-4 * g[i, m, n_occ + s, n_occ + v] + 8 * g[i, n_occ + s, m, n_occ + v] ) * K[0, i*n_virt + s + n_ex] * K[1, i*n_virt + s + n_ex] * K[2, m*n_virt + v]

										elif ((t == s) and (u != s) and (u != t) and (v == s)):

											L4[i*n_virt + s] += (2 * g[i, n_occ + u, m, n_occ + s] + 2 * g[i, m, n_occ + s, n_occ + u] ) * K[0, i*n_virt + s + n_ex] * K[1, i*n_virt + u + n_ex] * K[2, m*n_virt + s]

										elif ((t == s) and (u != s) and (u != t) and (v == u)):

											L4[i*n_virt + s] += (-2 * g[i, n_occ + s, m, n_occ + s] + 4 * g[i, m, n_occ + s, n_occ + s] + 4 * g[i, n_occ + u, m, n_occ + u] + -2 * g[i, m, n_occ + u, n_occ + u] + -2 * g[i, i, i, m] ) * K[0, i*n_virt + s + n_ex] * K[1, i*n_virt + u + n_ex] * K[2, m*n_virt + u]

										elif ((t == s) and (u != s) and (u != t) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s] += (-2 * g[i, m, n_occ + u, n_occ + v] + 4 * g[i, n_occ + u, m, n_occ + v] ) * K[0, i*n_virt + s + n_ex] * K[1, i*n_virt + u + n_ex] * K[2, m*n_virt + v]

										elif ((t != s) and (u == s) and (v == s)):

											L4[i*n_virt + s] += (2 * g[i, n_occ + t, m, n_occ + s] + 2 * g[i, m, n_occ + s, n_occ + t] ) * K[0, i*n_virt + t + n_ex] * K[1, i*n_virt + s + n_ex] * K[2, m*n_virt + s]

										elif ((t != s) and (u == s) and (v == t)):

											L4[i*n_virt + s] += (-2 * g[i, n_occ + s, m, n_occ + s] + 4 * g[i, m, n_occ + s, n_occ + s] + 4 * g[i, n_occ + t, m, n_occ + t] + -2 * g[i, m, n_occ + t, n_occ + t] + -2 * g[i, i, i, m] ) * K[0, i*n_virt + t + n_ex] * K[1, i*n_virt + s + n_ex] * K[2, m*n_virt + t]

										elif ((t != s) and (u == s) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s] += (-2 * g[i, m, n_occ + t, n_occ + v] + 4 * g[i, n_occ + t, m, n_occ + v] ) * K[0, i*n_virt + t + n_ex] * K[1, i*n_virt + s + n_ex] * K[2, m*n_virt + v]

										elif ((t != s) and (u == t) and (v == t)):

											L4[i*n_virt + s] += (8 * g[i, m, n_occ + s, n_occ + t] + -4 * g[i, n_occ + t, m, n_occ + s] ) * K[0, i*n_virt + t + n_ex] * K[1, i*n_virt + t + n_ex] * K[2, m*n_virt + t]

										elif ((t != s) and (u != s) and (u != t) and (v == t)):

											L4[i*n_virt + s] += (4 * g[i, m, n_occ + s, n_occ + u] + -2 * g[i, n_occ + u, m, n_occ + s] ) * K[0, i*n_virt + t + n_ex] * K[1, i*n_virt + u + n_ex] * K[2, m*n_virt + t]

										elif ((t != s) and (u != s) and (u != t) and (v == u)):

											L4[i*n_virt + s] += (4 * g[i, m, n_occ + s, n_occ + t] + -2 * g[i, n_occ + t, m, n_occ + s] ) * K[0, i*n_virt + t + n_ex] * K[1, i*n_virt + u + n_ex] * K[2, m*n_virt + u]

									elif ((j == i) and (k != i) and (k != j) and (m == i)):

										if ((t == s) and (u == s) and (v == s)):

											L4[i*n_virt + s] += (4 * g[i, k, n_occ + s, n_occ + s] + -4 * g[i, i, i, k] + 4 * g[i, n_occ + s, k, n_occ + s] ) * K[0, i*n_virt + s + n_ex] * K[1, k*n_virt + s + n_ex] * K[2, i*n_virt + s]

										elif ((t == s) and (u == s) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s] += (2 * g[i, n_occ + v, k, n_occ + s] + 2 * g[i, k, n_occ + s, n_occ + v] ) * K[0, i*n_virt + s + n_ex] * K[1, k*n_virt + s + n_ex] * K[2, i*n_virt + v]

										elif ((t == s) and (u != s) and (u != t) and (v == u)):

											L4[i*n_virt + s] += (-2 * g[i, i, i, k] + 2 * g[i, k, n_occ + s, n_occ + s] + 2 * g[i, n_occ + s, k, n_occ + s] ) * K[0, i*n_virt + s + n_ex] * K[1, k*n_virt + u + n_ex] * K[2, i*n_virt + u]

										elif ((t != s) and (u == s) and (v == s)):

											L4[i*n_virt + s] += (4 * g[i, n_occ + s, k, n_occ + t] + 4 * g[i, k, n_occ + s, n_occ + t] ) * K[0, i*n_virt + t + n_ex] * K[1, k*n_virt + s + n_ex] * K[2, i*n_virt + s]

										elif ((t != s) and (u == s) and (v == t)):

											L4[i*n_virt + s] += (2 * g[i, n_occ + t, k, n_occ + t] + 2 * g[i, k, n_occ + t, n_occ + t] + -2 * g[i, i, i, k] ) * K[0, i*n_virt + t + n_ex] * K[1, k*n_virt + s + n_ex] * K[2, i*n_virt + t]

										elif ((t != s) and (u == s) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s] += (2 * g[i, n_occ + v, k, n_occ + t] + 2 * g[i, k, n_occ + t, n_occ + v] ) * K[0, i*n_virt + t + n_ex] * K[1, k*n_virt + s + n_ex] * K[2, i*n_virt + v]

										elif ((t != s) and (u == t) and (v == t)):

											L4[i*n_virt + s] += (2 * g[i, k, n_occ + s, n_occ + t] + 2 * g[i, n_occ + s, k, n_occ + t] ) * K[0, i*n_virt + t + n_ex] * K[1, k*n_virt + t + n_ex] * K[2, i*n_virt + t]

										elif ((t != s) and (u != s) and (u != t) and (v == u)):

											L4[i*n_virt + s] += (2 * g[i, k, n_occ + s, n_occ + t] + 2 * g[i, n_occ + s, k, n_occ + t] ) * K[0, i*n_virt + t + n_ex] * K[1, k*n_virt + u + n_ex] * K[2, i*n_virt + u]

									elif ((j == i) and (k != i) and (k != j) and (m == k)):

										if ((t == s) and (u == s) and (v == s)):

											L4[i*n_virt + s] += (2 * g[k, n_occ + s, k, n_occ + s] + -2 * g[i, k, i, k] + -2 * g[n_occ + s, n_occ + s, n_occ + s, n_occ + s] + 2 * g[i, n_occ + s, i, n_occ + s] + 2 * g[i, i, n_occ + s, n_occ + s] + -2 * g[i, i, k, k] + 2 * g[k, k, n_occ + s, n_occ + s] ) * K[0, i*n_virt + s + n_ex] * K[1, k*n_virt + s + n_ex] * K[2, k*n_virt + s]

										elif ((t == s) and (u == s) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s] += (4 * g[k, n_occ + s, k, n_occ + v] + -2 * g[i, n_occ + s, i, n_occ + v] + 4 * g[i, i, n_occ + s, n_occ + v] + -2 * g[k, k, n_occ + s, n_occ + v] + -2 * g[n_occ + s, n_occ + s, n_occ + s, n_occ + v] ) * K[0, i*n_virt + s + n_ex] * K[1, k*n_virt + s + n_ex] * K[2, k*n_virt + v]

										elif ((t == s) and (u != s) and (u != t) and (v == s)):

											L4[i*n_virt + s] += (2 * g[i, i, n_occ + s, n_occ + u] + -2 * g[n_occ + s, n_occ + s, n_occ + s, n_occ + u] + 2 * g[i, n_occ + s, i, n_occ + u] ) * K[0, i*n_virt + s + n_ex] * K[1, k*n_virt + u + n_ex] * K[2, k*n_virt + s]

										elif ((t == s) and (u != s) and (u != t) and (v == u)):

											L4[i*n_virt + s] += (-2 * g[i, n_occ + u, i, n_occ + u] + 4 * g[i, i, n_occ + u, n_occ + u] + 2 * g[n_occ + s, n_occ + u, n_occ + s, n_occ + u] + -4 * g[n_occ + s, n_occ + s, n_occ + u, n_occ + u] + 2 * g[i, k, i, k] + -4 * g[i, i, k, k] + 4 * g[k, k, n_occ + s, n_occ + s] + -2 * g[k, n_occ + s, k, n_occ + s] ) * K[0, i*n_virt + s + n_ex] * K[1, k*n_virt + u + n_ex] * K[2, k*n_virt + u]

										elif ((t == s) and (u != s) and (u != t) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s] += (-2 * g[i, n_occ + u, i, n_occ + v] + 4 * g[i, i, n_occ + u, n_occ + v] + 2 * g[n_occ + s, n_occ + u, n_occ + s, n_occ + v] + -4 * g[n_occ + s, n_occ + s, n_occ + u, n_occ + v] ) * K[0, i*n_virt + s + n_ex] * K[1, k*n_virt + u + n_ex] * K[2, k*n_virt + v]

										elif ((t != s) and (u == s) and (v == s)):

											L4[i*n_virt + s] += (2 * g[k, n_occ + s, k, n_occ + t] + -2 * g[n_occ + s, n_occ + s, n_occ + s, n_occ + t] + 2 * g[k, k, n_occ + s, n_occ + t] ) * K[0, i*n_virt + t + n_ex] * K[1, k*n_virt + s + n_ex] * K[2, k*n_virt + s]

										elif ((t != s) and (u == s) and (v == t)):

											L4[i*n_virt + s] += (-4 * g[i, k, i, k] + 2 * g[i, i, k, k] + -2 * g[i, i, n_occ + s, n_occ + s] + 4 * g[i, n_occ + s, i, n_occ + s] + -2 * g[k, k, n_occ + t, n_occ + t] + 4 * g[k, n_occ + t, k, n_occ + t] + -4 * g[n_occ + s, n_occ + t, n_occ + s, n_occ + t] + 2 * g[n_occ + s, n_occ + s, n_occ + t, n_occ + t] ) * K[0, i*n_virt + t + n_ex] * K[1, k*n_virt + s + n_ex] * K[2, k*n_virt + t]

										elif ((t != s) and (u == s) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s] += (4 * g[k, n_occ + t, k, n_occ + v] + -2 * g[k, k, n_occ + t, n_occ + v] + -4 * g[n_occ + s, n_occ + t, n_occ + s, n_occ + v] + 2 * g[n_occ + s, n_occ + s, n_occ + t, n_occ + v] ) * K[0, i*n_virt + t + n_ex] * K[1, k*n_virt + s + n_ex] * K[2, k*n_virt + v]

										elif ((t != s) and (u == t) and (v == s)):

											L4[i*n_virt + s] += (-2 * g[n_occ + s, n_occ + t, n_occ + s, n_occ + t] ) * K[0, i*n_virt + t + n_ex] * K[1, k*n_virt + t + n_ex] * K[2, k*n_virt + s]

										elif ((t != s) and (u == t) and (v == t)):

											L4[i*n_virt + s] += (-2 * g[i, i, n_occ + s, n_occ + t] + -2 * g[n_occ + s, n_occ + t, n_occ + t, n_occ + t] + 4 * g[i, n_occ + s, i, n_occ + t] + -2 * g[k, n_occ + s, k, n_occ + t] + 4 * g[k, k, n_occ + s, n_occ + t] ) * K[0, i*n_virt + t + n_ex] * K[1, k*n_virt + t + n_ex] * K[2, k*n_virt + t]

										elif ((t != s) and (u == t) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s] += (-2 * g[n_occ + s, n_occ + t, n_occ + t, n_occ + v] ) * K[0, i*n_virt + t + n_ex] * K[1, k*n_virt + t + n_ex] * K[2, k*n_virt + v]

										elif ((t != s) and (u != s) and (u != t) and (v == s)):

											L4[i*n_virt + s] += (-2 * g[n_occ + s, n_occ + t, n_occ + s, n_occ + u] ) * K[0, i*n_virt + t + n_ex] * K[1, k*n_virt + u + n_ex] * K[2, k*n_virt + s]

										elif ((t != s) and (u != s) and (u != t) and (v == t)):

											L4[i*n_virt + s] += (4 * g[i, n_occ + s, i, n_occ + u] + -2 * g[i, i, n_occ + s, n_occ + u] + -4 * g[n_occ + s, n_occ + t, n_occ + t, n_occ + u] + 2 * g[n_occ + s, n_occ + u, n_occ + t, n_occ + t] ) * K[0, i*n_virt + t + n_ex] * K[1, k*n_virt + u + n_ex] * K[2, k*n_virt + t]

										elif ((t != s) and (u != s) and (u != t) and (v == u)):

											L4[i*n_virt + s] += (2 * g[n_occ + s, n_occ + u, n_occ + t, n_occ + u] + -4 * g[n_occ + s, n_occ + t, n_occ + u, n_occ + u] + -2 * g[k, n_occ + s, k, n_occ + t] + 4 * g[k, k, n_occ + s, n_occ + t] ) * K[0, i*n_virt + t + n_ex] * K[1, k*n_virt + u + n_ex] * K[2, k*n_virt + u]

										elif ((t != s) and (u != s) and (u != t) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s] += (-4 * g[n_occ + s, n_occ + t, n_occ + u, n_occ + v] + 2 * g[n_occ + s, n_occ + u, n_occ + t, n_occ + v] ) * K[0, i*n_virt + t + n_ex] * K[1, k*n_virt + u + n_ex] * K[2, k*n_virt + v]

									elif ((j == i) and (k != i) and (k != j) and (m != i) and (m != j) and (m != k)):

										if ((t == s) and (u == s) and (v == s)):

											L4[i*n_virt + s] += (2 * g[k, n_occ + s, m, n_occ + s] + -2 * g[i, i, k, m] + -2 * g[i, k, i, m] + 2 * g[k, m, n_occ + s, n_occ + s] ) * K[0, i*n_virt + s + n_ex] * K[1, k*n_virt + s + n_ex] * K[2, m*n_virt + s]

										elif ((t == s) and (u == s) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s] += (-2 * g[k, m, n_occ + s, n_occ + v] + 4 * g[k, n_occ + s, m, n_occ + v] ) * K[0, i*n_virt + s + n_ex] * K[1, k*n_virt + s + n_ex] * K[2, m*n_virt + v]

										elif ((t == s) and (u != s) and (u != t) and (v == u)):

											L4[i*n_virt + s] += (2 * g[i, k, i, m] + -4 * g[i, i, k, m] + -2 * g[k, n_occ + s, m, n_occ + s] + 4 * g[k, m, n_occ + s, n_occ + s] ) * K[0, i*n_virt + s + n_ex] * K[1, k*n_virt + u + n_ex] * K[2, m*n_virt + u]

										elif ((t != s) and (u == s) and (v == s)):

											L4[i*n_virt + s] += (2 * g[k, n_occ + t, m, n_occ + s] + 2 * g[k, m, n_occ + s, n_occ + t] ) * K[0, i*n_virt + t + n_ex] * K[1, k*n_virt + s + n_ex] * K[2, m*n_virt + s]

										elif ((t != s) and (u == s) and (v == t)):

											L4[i*n_virt + s] += (-4 * g[i, k, i, m] + 2 * g[i, i, k, m] + 4 * g[k, n_occ + t, m, n_occ + t] + -2 * g[k, m, n_occ + t, n_occ + t] ) * K[0, i*n_virt + t + n_ex] * K[1, k*n_virt + s + n_ex] * K[2, m*n_virt + t]

										elif ((t != s) and (u == s) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s] += (-2 * g[k, m, n_occ + t, n_occ + v] + 4 * g[k, n_occ + t, m, n_occ + v] ) * K[0, i*n_virt + t + n_ex] * K[1, k*n_virt + s + n_ex] * K[2, m*n_virt + v]

										elif ((t != s) and (u == t) and (v == t)):

											L4[i*n_virt + s] += (4 * g[k, m, n_occ + s, n_occ + t] + -2 * g[k, n_occ + t, m, n_occ + s] ) * K[0, i*n_virt + t + n_ex] * K[1, k*n_virt + t + n_ex] * K[2, m*n_virt + t]

										elif ((t != s) and (u != s) and (u != t) and (v == u)):

											L4[i*n_virt + s] += (4 * g[k, m, n_occ + s, n_occ + t] + -2 * g[k, n_occ + t, m, n_occ + s] ) * K[0, i*n_virt + t + n_ex] * K[1, k*n_virt + u + n_ex] * K[2, m*n_virt + u]

									elif ((j != i) and (k == i) and (m == i)):

										if ((t == s) and (u == s) and (v == s)):

											L4[i*n_virt + s] += (4 * g[i, j, n_occ + s, n_occ + s] + -4 * g[i, i, i, j] + 4 * g[i, n_occ + s, j, n_occ + s] ) * K[0, j*n_virt + s + n_ex] * K[1, i*n_virt + s + n_ex] * K[2, i*n_virt + s]

										elif ((t == s) and (u == s) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s] += (2 * g[i, n_occ + v, j, n_occ + s] + 2 * g[i, j, n_occ + s, n_occ + v] ) * K[0, j*n_virt + s + n_ex] * K[1, i*n_virt + s + n_ex] * K[2, i*n_virt + v]

										elif ((t == s) and (u != s) and (u != t) and (v == s)):

											L4[i*n_virt + s] += (4 * g[i, n_occ + s, j, n_occ + u] + 4 * g[i, j, n_occ + s, n_occ + u] ) * K[0, j*n_virt + s + n_ex] * K[1, i*n_virt + u + n_ex] * K[2, i*n_virt + s]

										elif ((t == s) and (u != s) and (u != t) and (v == u)):

											L4[i*n_virt + s] += (2 * g[i, n_occ + u, j, n_occ + u] + 2 * g[i, j, n_occ + u, n_occ + u] + -2 * g[i, i, i, j] ) * K[0, j*n_virt + s + n_ex] * K[1, i*n_virt + u + n_ex] * K[2, i*n_virt + u]

										elif ((t == s) and (u != s) and (u != t) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s] += (2 * g[i, n_occ + v, j, n_occ + u] + 2 * g[i, j, n_occ + u, n_occ + v] ) * K[0, j*n_virt + s + n_ex] * K[1, i*n_virt + u + n_ex] * K[2, i*n_virt + v]

										elif ((t != s) and (u == s) and (v == t)):

											L4[i*n_virt + s] += (-2 * g[i, i, i, j] + 2 * g[i, j, n_occ + s, n_occ + s] + 2 * g[i, n_occ + s, j, n_occ + s] ) * K[0, j*n_virt + t + n_ex] * K[1, i*n_virt + s + n_ex] * K[2, i*n_virt + t]

										elif ((t != s) and (u == t) and (v == t)):

											L4[i*n_virt + s] += (2 * g[i, j, n_occ + s, n_occ + t] + 2 * g[i, n_occ + s, j, n_occ + t] ) * K[0, j*n_virt + t + n_ex] * K[1, i*n_virt + t + n_ex] * K[2, i*n_virt + t]

										elif ((t != s) and (u != s) and (u != t) and (v == t)):

											L4[i*n_virt + s] += (2 * g[i, j, n_occ + s, n_occ + u] + 2 * g[i, n_occ + s, j, n_occ + u] ) * K[0, j*n_virt + t + n_ex] * K[1, i*n_virt + u + n_ex] * K[2, i*n_virt + t]

									elif ((j != i) and (k == i) and (m == j)):

										if ((t == s) and (u == s) and (v == s)):

											L4[i*n_virt + s] += (2 * g[j, n_occ + s, j, n_occ + s] + -2 * g[i, j, i, j] + -2 * g[n_occ + s, n_occ + s, n_occ + s, n_occ + s] + 2 * g[i, n_occ + s, i, n_occ + s] + 2 * g[i, i, n_occ + s, n_occ + s] + -2 * g[i, i, j, j] + 2 * g[j, j, n_occ + s, n_occ + s] ) * K[0, j*n_virt + s + n_ex] * K[1, i*n_virt + s + n_ex] * K[2, j*n_virt + s]

										elif ((t == s) and (u == s) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s] += (-2 * g[i, n_occ + s, i, n_occ + v] + 4 * g[j, n_occ + s, j, n_occ + v] + 4 * g[i, i, n_occ + s, n_occ + v] + -2 * g[j, j, n_occ + s, n_occ + v] + -2 * g[n_occ + s, n_occ + s, n_occ + s, n_occ + v] ) * K[0, j*n_virt + s + n_ex] * K[1, i*n_virt + s + n_ex] * K[2, j*n_virt + v]

										elif ((t == s) and (u != s) and (u != t) and (v == s)):

											L4[i*n_virt + s] += (2 * g[j, n_occ + s, j, n_occ + u] + -2 * g[n_occ + s, n_occ + s, n_occ + s, n_occ + u] + 2 * g[j, j, n_occ + s, n_occ + u] ) * K[0, j*n_virt + s + n_ex] * K[1, i*n_virt + u + n_ex] * K[2, j*n_virt + s]

										elif ((t == s) and (u != s) and (u != t) and (v == u)):

											L4[i*n_virt + s] += (-4 * g[i, j, i, j] + 2 * g[i, i, j, j] + -2 * g[j, j, n_occ + u, n_occ + u] + 4 * g[j, n_occ + u, j, n_occ + u] + -2 * g[i, i, n_occ + s, n_occ + s] + 4 * g[i, n_occ + s, i, n_occ + s] + -4 * g[n_occ + s, n_occ + u, n_occ + s, n_occ + u] + 2 * g[n_occ + s, n_occ + s, n_occ + u, n_occ + u] ) * K[0, j*n_virt + s + n_ex] * K[1, i*n_virt + u + n_ex] * K[2, j*n_virt + u]

										elif ((t == s) and (u != s) and (u != t) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s] += (4 * g[j, n_occ + u, j, n_occ + v] + -2 * g[j, j, n_occ + u, n_occ + v] + -4 * g[n_occ + s, n_occ + u, n_occ + s, n_occ + v] + 2 * g[n_occ + s, n_occ + s, n_occ + u, n_occ + v] ) * K[0, j*n_virt + s + n_ex] * K[1, i*n_virt + u + n_ex] * K[2, j*n_virt + v]

										elif ((t != s) and (u == s) and (v == s)):

											L4[i*n_virt + s] += (2 * g[i, i, n_occ + s, n_occ + t] + -2 * g[n_occ + s, n_occ + s, n_occ + s, n_occ + t] + 2 * g[i, n_occ + s, i, n_occ + t] ) * K[0, j*n_virt + t + n_ex] * K[1, i*n_virt + s + n_ex] * K[2, j*n_virt + s]

										elif ((t != s) and (u == s) and (v == t)):

											L4[i*n_virt + s] += (4 * g[i, i, n_occ + t, n_occ + t] + -2 * g[i, n_occ + t, i, n_occ + t] + 2 * g[n_occ + s, n_occ + t, n_occ + s, n_occ + t] + -4 * g[n_occ + s, n_occ + s, n_occ + t, n_occ + t] + 2 * g[i, j, i, j] + -4 * g[i, i, j, j] + 4 * g[j, j, n_occ + s, n_occ + s] + -2 * g[j, n_occ + s, j, n_occ + s] ) * K[0, j*n_virt + t + n_ex] * K[1, i*n_virt + s + n_ex] * K[2, j*n_virt + t]

										elif ((t != s) and (u == s) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s] += (-2 * g[i, n_occ + t, i, n_occ + v] + 4 * g[i, i, n_occ + t, n_occ + v] + 2 * g[n_occ + s, n_occ + t, n_occ + s, n_occ + v] + -4 * g[n_occ + s, n_occ + s, n_occ + t, n_occ + v] ) * K[0, j*n_virt + t + n_ex] * K[1, i*n_virt + s + n_ex] * K[2, j*n_virt + v]

										elif ((t != s) and (u == t) and (v == s)):

											L4[i*n_virt + s] += (-2 * g[n_occ + s, n_occ + t, n_occ + s, n_occ + t] ) * K[0, j*n_virt + t + n_ex] * K[1, i*n_virt + t + n_ex] * K[2, j*n_virt + s]

										elif ((t != s) and (u == t) and (v == t)):

											L4[i*n_virt + s] += (-2 * g[i, i, n_occ + s, n_occ + t] + -2 * g[n_occ + s, n_occ + t, n_occ + t, n_occ + t] + 4 * g[i, n_occ + s, i, n_occ + t] + -2 * g[j, n_occ + s, j, n_occ + t] + 4 * g[j, j, n_occ + s, n_occ + t] ) * K[0, j*n_virt + t + n_ex] * K[1, i*n_virt + t + n_ex] * K[2, j*n_virt + t]

										elif ((t != s) and (u == t) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s] += (-2 * g[n_occ + s, n_occ + t, n_occ + t, n_occ + v] ) * K[0, j*n_virt + t + n_ex] * K[1, i*n_virt + t + n_ex] * K[2, j*n_virt + v]

										elif ((t != s) and (u != s) and (u != t) and (v == s)):

											L4[i*n_virt + s] += (-2 * g[n_occ + s, n_occ + t, n_occ + s, n_occ + u] ) * K[0, j*n_virt + t + n_ex] * K[1, i*n_virt + u + n_ex] * K[2, j*n_virt + s]

										elif ((t != s) and (u != s) and (u != t) and (v == t)):

											L4[i*n_virt + s] += (2 * g[n_occ + s, n_occ + t, n_occ + t, n_occ + u] + -4 * g[n_occ + s, n_occ + u, n_occ + t, n_occ + t] + -2 * g[j, n_occ + s, j, n_occ + u] + 4 * g[j, j, n_occ + s, n_occ + u] ) * K[0, j*n_virt + t + n_ex] * K[1, i*n_virt + u + n_ex] * K[2, j*n_virt + t]

										elif ((t != s) and (u != s) and (u != t) and (v == u)):

											L4[i*n_virt + s] += (4 * g[i, n_occ + s, i, n_occ + t] + -2 * g[i, i, n_occ + s, n_occ + t] + -4 * g[n_occ + s, n_occ + u, n_occ + t, n_occ + u] + 2 * g[n_occ + s, n_occ + t, n_occ + u, n_occ + u] ) * K[0, j*n_virt + t + n_ex] * K[1, i*n_virt + u + n_ex] * K[2, j*n_virt + u]

										elif ((t != s) and (u != s) and (u != t) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s] += (2 * g[n_occ + s, n_occ + t, n_occ + u, n_occ + v] + -4 * g[n_occ + s, n_occ + u, n_occ + t, n_occ + v] ) * K[0, j*n_virt + t + n_ex] * K[1, i*n_virt + u + n_ex] * K[2, j*n_virt + v]

									elif ((j != i) and (k == i) and (m != i) and (m != j) and (m != k)):

										if ((t == s) and (u == s) and (v == s)):

											L4[i*n_virt + s] += (2 * g[j, n_occ + s, m, n_occ + s] + -2 * g[i, i, j, m] + -2 * g[i, j, i, m] + 2 * g[j, m, n_occ + s, n_occ + s] ) * K[0, j*n_virt + s + n_ex] * K[1, i*n_virt + s + n_ex] * K[2, m*n_virt + s]

										elif ((t == s) and (u == s) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s] += (-2 * g[j, m, n_occ + s, n_occ + v] + 4 * g[j, n_occ + s, m, n_occ + v] ) * K[0, j*n_virt + s + n_ex] * K[1, i*n_virt + s + n_ex] * K[2, m*n_virt + v]

										elif ((t == s) and (u != s) and (u != t) and (v == s)):

											L4[i*n_virt + s] += (2 * g[j, n_occ + u, m, n_occ + s] + 2 * g[j, m, n_occ + s, n_occ + u] ) * K[0, j*n_virt + s + n_ex] * K[1, i*n_virt + u + n_ex] * K[2, m*n_virt + s]

										elif ((t == s) and (u != s) and (u != t) and (v == u)):

											L4[i*n_virt + s] += (-4 * g[i, j, i, m] + 2 * g[i, i, j, m] + 4 * g[j, n_occ + u, m, n_occ + u] + -2 * g[j, m, n_occ + u, n_occ + u] ) * K[0, j*n_virt + s + n_ex] * K[1, i*n_virt + u + n_ex] * K[2, m*n_virt + u]

										elif ((t == s) and (u != s) and (u != t) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s] += (-2 * g[j, m, n_occ + u, n_occ + v] + 4 * g[j, n_occ + u, m, n_occ + v] ) * K[0, j*n_virt + s + n_ex] * K[1, i*n_virt + u + n_ex] * K[2, m*n_virt + v]

										elif ((t != s) and (u == s) and (v == t)):

											L4[i*n_virt + s] += (2 * g[i, j, i, m] + -4 * g[i, i, j, m] + -2 * g[j, n_occ + s, m, n_occ + s] + 4 * g[j, m, n_occ + s, n_occ + s] ) * K[0, j*n_virt + t + n_ex] * K[1, i*n_virt + s + n_ex] * K[2, m*n_virt + t]

										elif ((t != s) and (u == t) and (v == t)):

											L4[i*n_virt + s] += (4 * g[j, m, n_occ + s, n_occ + t] + -2 * g[j, n_occ + t, m, n_occ + s] ) * K[0, j*n_virt + t + n_ex] * K[1, i*n_virt + t + n_ex] * K[2, m*n_virt + t]

										elif ((t != s) and (u != s) and (u != t) and (v == t)):

											L4[i*n_virt + s] += (4 * g[j, m, n_occ + s, n_occ + u] + -2 * g[j, n_occ + u, m, n_occ + s] ) * K[0, j*n_virt + t + n_ex] * K[1, i*n_virt + u + n_ex] * K[2, m*n_virt + t]

									elif ((j != i) and (k == j) and (m == i)):

										if ((t == s) and (u == s) and (v == s)):

											L4[i*n_virt + s] += (-4 * g[i, j, i, j] ) * K[0, j*n_virt + s + n_ex] * K[1, j*n_virt + s + n_ex] * K[2, i*n_virt + s]

										elif ((t == s) and (u != s) and (u != t) and (v == u)):

											L4[i*n_virt + s] += (-2 * g[i, j, i, j] ) * K[0, j*n_virt + s + n_ex] * K[1, j*n_virt + u + n_ex] * K[2, i*n_virt + u]

										elif ((t != s) and (u == s) and (v == t)):

											L4[i*n_virt + s] += (-2 * g[i, j, i, j] ) * K[0, j*n_virt + t + n_ex] * K[1, j*n_virt + s + n_ex] * K[2, i*n_virt + t]

									elif ((j != i) and (k == j) and (m == j)):

										if ((t == s) and (u == s) and (v == s)):

											L4[i*n_virt + s] += (4 * g[i, j, n_occ + s, n_occ + s] + -4 * g[i, j, j, j] + 4 * g[i, n_occ + s, j, n_occ + s] ) * K[0, j*n_virt + s + n_ex] * K[1, j*n_virt + s + n_ex] * K[2, j*n_virt + s]

										elif ((t == s) and (u == s) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s] += (8 * g[i, j, n_occ + s, n_occ + v] + -4 * g[i, n_occ + v, j, n_occ + s] ) * K[0, j*n_virt + s + n_ex] * K[1, j*n_virt + s + n_ex] * K[2, j*n_virt + v]

										elif ((t == s) and (u != s) and (u != t) and (v == s)):

											L4[i*n_virt + s] += (2 * g[i, j, n_occ + s, n_occ + u] + 2 * g[i, n_occ + s, j, n_occ + u] ) * K[0, j*n_virt + s + n_ex] * K[1, j*n_virt + u + n_ex] * K[2, j*n_virt + s]

										elif ((t == s) and (u != s) and (u != t) and (v == u)):

											L4[i*n_virt + s] += (-2 * g[i, n_occ + u, j, n_occ + u] + 4 * g[i, j, n_occ + u, n_occ + u] + 4 * g[i, n_occ + s, j, n_occ + s] + -2 * g[i, j, j, j] + -2 * g[i, j, n_occ + s, n_occ + s] ) * K[0, j*n_virt + s + n_ex] * K[1, j*n_virt + u + n_ex] * K[2, j*n_virt + u]

										elif ((t == s) and (u != s) and (u != t) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s] += (4 * g[i, j, n_occ + u, n_occ + v] + -2 * g[i, n_occ + v, j, n_occ + u] ) * K[0, j*n_virt + s + n_ex] * K[1, j*n_virt + u + n_ex] * K[2, j*n_virt + v]

										elif ((t != s) and (u == s) and (v == s)):

											L4[i*n_virt + s] += (2 * g[i, j, n_occ + s, n_occ + t] + 2 * g[i, n_occ + s, j, n_occ + t] ) * K[0, j*n_virt + t + n_ex] * K[1, j*n_virt + s + n_ex] * K[2, j*n_virt + s]

										elif ((t != s) and (u == s) and (v == t)):

											L4[i*n_virt + s] += (-2 * g[i, n_occ + t, j, n_occ + t] + 4 * g[i, j, n_occ + t, n_occ + t] + 4 * g[i, n_occ + s, j, n_occ + s] + -2 * g[i, j, j, j] + -2 * g[i, j, n_occ + s, n_occ + s] ) * K[0, j*n_virt + t + n_ex] * K[1, j*n_virt + s + n_ex] * K[2, j*n_virt + t]

										elif ((t != s) and (u == s) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s] += (4 * g[i, j, n_occ + t, n_occ + v] + -2 * g[i, n_occ + v, j, n_occ + t] ) * K[0, j*n_virt + t + n_ex] * K[1, j*n_virt + s + n_ex] * K[2, j*n_virt + v]

										elif ((t != s) and (u == t) and (v == t)):

											L4[i*n_virt + s] += (-4 * g[i, j, n_occ + s, n_occ + t] + 8 * g[i, n_occ + s, j, n_occ + t] ) * K[0, j*n_virt + t + n_ex] * K[1, j*n_virt + t + n_ex] * K[2, j*n_virt + t]

										elif ((t != s) and (u != s) and (u != t) and (v == t)):

											L4[i*n_virt + s] += (4 * g[i, n_occ + s, j, n_occ + u] + -2 * g[i, j, n_occ + s, n_occ + u] ) * K[0, j*n_virt + t + n_ex] * K[1, j*n_virt + u + n_ex] * K[2, j*n_virt + t]

										elif ((t != s) and (u != s) and (u != t) and (v == u)):

											L4[i*n_virt + s] += (4 * g[i, n_occ + s, j, n_occ + t] + -2 * g[i, j, n_occ + s, n_occ + t] ) * K[0, j*n_virt + t + n_ex] * K[1, j*n_virt + u + n_ex] * K[2, j*n_virt + u]

									elif ((j != i) and (k == j) and (m != i) and (m != j) and (m != k)):

										if ((t == s) and (u == s) and (v == s)):

											L4[i*n_virt + s] += (-4 * g[i, j, j, m] ) * K[0, j*n_virt + s + n_ex] * K[1, j*n_virt + s + n_ex] * K[2, m*n_virt + s]

										elif ((t == s) and (u != s) and (u != t) and (v == u)):

											L4[i*n_virt + s] += (-2 * g[i, j, j, m] ) * K[0, j*n_virt + s + n_ex] * K[1, j*n_virt + u + n_ex] * K[2, m*n_virt + u]

										elif ((t != s) and (u == s) and (v == t)):

											L4[i*n_virt + s] += (-2 * g[i, j, j, m] ) * K[0, j*n_virt + t + n_ex] * K[1, j*n_virt + s + n_ex] * K[2, m*n_virt + t]

									elif ((j != i) and (k != i) and (k != j) and (m == i)):

										if ((t == s) and (u == s) and (v == s)):

											L4[i*n_virt + s] += (-4 * g[i, j, i, k] ) * K[0, j*n_virt + s + n_ex] * K[1, k*n_virt + s + n_ex] * K[2, i*n_virt + s]

										elif ((t == s) and (u != s) and (u != t) and (v == u)):

											L4[i*n_virt + s] += (-2 * g[i, j, i, k] ) * K[0, j*n_virt + s + n_ex] * K[1, k*n_virt + u + n_ex] * K[2, i*n_virt + u]

										elif ((t != s) and (u == s) and (v == t)):

											L4[i*n_virt + s] += (-2 * g[i, j, i, k] ) * K[0, j*n_virt + t + n_ex] * K[1, k*n_virt + s + n_ex] * K[2, i*n_virt + t]

									elif ((j != i) and (k != i) and (k != j) and (m == j)):

										if ((t == s) and (u == s) and (v == s)):

											L4[i*n_virt + s] += (-2 * g[i, j, j, k] + 2 * g[i, k, n_occ + s, n_occ + s] + 2 * g[i, n_occ + s, k, n_occ + s] + -2 * g[i, k, j, j] ) * K[0, j*n_virt + s + n_ex] * K[1, k*n_virt + s + n_ex] * K[2, j*n_virt + s]

										elif ((t == s) and (u == s) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s] += (4 * g[i, k, n_occ + s, n_occ + v] + -2 * g[i, n_occ + v, k, n_occ + s] ) * K[0, j*n_virt + s + n_ex] * K[1, k*n_virt + s + n_ex] * K[2, j*n_virt + v]

										elif ((t == s) and (u != s) and (u != t) and (v == u)):

											L4[i*n_virt + s] += (-4 * g[i, j, j, k] + 2 * g[i, k, j, j] + 4 * g[i, n_occ + s, k, n_occ + s] + -2 * g[i, k, n_occ + s, n_occ + s] ) * K[0, j*n_virt + s + n_ex] * K[1, k*n_virt + u + n_ex] * K[2, j*n_virt + u]

										elif ((t != s) and (u == s) and (v == s)):

											L4[i*n_virt + s] += (2 * g[i, k, n_occ + s, n_occ + t] + 2 * g[i, n_occ + s, k, n_occ + t] ) * K[0, j*n_virt + t + n_ex] * K[1, k*n_virt + s + n_ex] * K[2, j*n_virt + s]

										elif ((t != s) and (u == s) and (v == t)):

											L4[i*n_virt + s] += (-2 * g[i, n_occ + t, k, n_occ + t] + 4 * g[i, k, n_occ + t, n_occ + t] + 2 * g[i, j, j, k] + -4 * g[i, k, j, j] ) * K[0, j*n_virt + t + n_ex] * K[1, k*n_virt + s + n_ex] * K[2, j*n_virt + t]

										elif ((t != s) and (u == s) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s] += (4 * g[i, k, n_occ + t, n_occ + v] + -2 * g[i, n_occ + v, k, n_occ + t] ) * K[0, j*n_virt + t + n_ex] * K[1, k*n_virt + s + n_ex] * K[2, j*n_virt + v]

										elif ((t != s) and (u == t) and (v == t)):

											L4[i*n_virt + s] += (4 * g[i, n_occ + s, k, n_occ + t] + -2 * g[i, k, n_occ + s, n_occ + t] ) * K[0, j*n_virt + t + n_ex] * K[1, k*n_virt + t + n_ex] * K[2, j*n_virt + t]

										elif ((t != s) and (u != s) and (u != t) and (v == u)):

											L4[i*n_virt + s] += (-2 * g[i, k, n_occ + s, n_occ + t] + 4 * g[i, n_occ + s, k, n_occ + t] ) * K[0, j*n_virt + t + n_ex] * K[1, k*n_virt + u + n_ex] * K[2, j*n_virt + u]

									elif ((j != i) and (k != i) and (k != j) and (m == k)):

										if ((t == s) and (u == s) and (v == s)):

											L4[i*n_virt + s] += (-2 * g[i, k, j, k] + 2 * g[i, j, n_occ + s, n_occ + s] + 2 * g[i, n_occ + s, j, n_occ + s] + -2 * g[i, j, k, k] ) * K[0, j*n_virt + s + n_ex] * K[1, k*n_virt + s + n_ex] * K[2, k*n_virt + s]

										elif ((t == s) and (u == s) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s] += (4 * g[i, j, n_occ + s, n_occ + v] + -2 * g[i, n_occ + v, j, n_occ + s] ) * K[0, j*n_virt + s + n_ex] * K[1, k*n_virt + s + n_ex] * K[2, k*n_virt + v]

										elif ((t == s) and (u != s) and (u != t) and (v == s)):

											L4[i*n_virt + s] += (2 * g[i, j, n_occ + s, n_occ + u] + 2 * g[i, n_occ + s, j, n_occ + u] ) * K[0, j*n_virt + s + n_ex] * K[1, k*n_virt + u + n_ex] * K[2, k*n_virt + s]

										elif ((t == s) and (u != s) and (u != t) and (v == u)):

											L4[i*n_virt + s] += (-2 * g[i, n_occ + u, j, n_occ + u] + 4 * g[i, j, n_occ + u, n_occ + u] + 2 * g[i, k, j, k] + -4 * g[i, j, k, k] ) * K[0, j*n_virt + s + n_ex] * K[1, k*n_virt + u + n_ex] * K[2, k*n_virt + u]

										elif ((t == s) and (u != s) and (u != t) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s] += (4 * g[i, j, n_occ + u, n_occ + v] + -2 * g[i, n_occ + v, j, n_occ + u] ) * K[0, j*n_virt + s + n_ex] * K[1, k*n_virt + u + n_ex] * K[2, k*n_virt + v]

										elif ((t != s) and (u == s) and (v == t)):

											L4[i*n_virt + s] += (-4 * g[i, k, j, k] + 2 * g[i, j, k, k] + 4 * g[i, n_occ + s, j, n_occ + s] + -2 * g[i, j, n_occ + s, n_occ + s] ) * K[0, j*n_virt + t + n_ex] * K[1, k*n_virt + s + n_ex] * K[2, k*n_virt + t]

										elif ((t != s) and (u == t) and (v == t)):

											L4[i*n_virt + s] += (4 * g[i, n_occ + s, j, n_occ + t] + -2 * g[i, j, n_occ + s, n_occ + t] ) * K[0, j*n_virt + t + n_ex] * K[1, k*n_virt + t + n_ex] * K[2, k*n_virt + t]

										elif ((t != s) and (u != s) and (u != t) and (v == t)):

											L4[i*n_virt + s] += (-2 * g[i, j, n_occ + s, n_occ + u] + 4 * g[i, n_occ + s, j, n_occ + u] ) * K[0, j*n_virt + t + n_ex] * K[1, k*n_virt + u + n_ex] * K[2, k*n_virt + t]

									elif ((j != i) and (k != i) and (k != j) and (m != i) and (m != j) and (m != k)):

										if ((t == s) and (u == s) and (v == s)):

											L4[i*n_virt + s] += (-2 * g[i, k, j, m] + -2 * g[i, j, k, m] ) * K[0, j*n_virt + s + n_ex] * K[1, k*n_virt + s + n_ex] * K[2, m*n_virt + s]

										elif ((t == s) and (u != s) and (u != t) and (v == u)):

											L4[i*n_virt + s] += (-4 * g[i, j, k, m] + 2 * g[i, k, j, m] ) * K[0, j*n_virt + s + n_ex] * K[1, k*n_virt + u + n_ex] * K[2, m*n_virt + u]

										elif ((t != s) and (u == s) and (v == t)):

											L4[i*n_virt + s] += (2 * g[i, j, k, m] + -4 * g[i, k, j, m] ) * K[0, j*n_virt + t + n_ex] * K[1, k*n_virt + s + n_ex] * K[2, m*n_virt + t]

	# Current operator combination: {'a': 1, 'b': 2, 'c': 2, 'd': 2}
	for i in range(n_occ):
		for j in range(n_occ):
			for k in range(n_occ):
				for m in range(n_occ):
					for s in range(n_virt):
						for t in range(n_virt):
							for u in range(n_virt):
								for v in range(n_virt):

									if ((j == i) and (k == i) and (m == i)):

										if ((t == s) and (u == s) and (v == s)):

											L4[i*n_virt + s + n_ex] += (-12 * g[i, n_occ + s, i, n_occ + s] ) * K[0, i*n_virt + s + n_ex] * K[1, i*n_virt + s + n_ex] * K[2, i*n_virt + s]

										elif ((t == s) and (u != s) and (u != t) and (v == s)):

											L4[i*n_virt + s + n_ex] += (-8 * g[i, n_occ + s, i, n_occ + u] ) * K[0, i*n_virt + s + n_ex] * K[1, i*n_virt + u + n_ex] * K[2, i*n_virt + s]

										elif ((t == s) and (u != s) and (u != t) and (v == u)):

											L4[i*n_virt + s + n_ex] += (-4 * g[i, n_occ + s, i, n_occ + s] ) * K[0, i*n_virt + s + n_ex] * K[1, i*n_virt + u + n_ex] * K[2, i*n_virt + u]

										elif ((t != s) and (u == s) and (v == s)):

											L4[i*n_virt + s + n_ex] += (-8 * g[i, n_occ + s, i, n_occ + t] ) * K[0, i*n_virt + t + n_ex] * K[1, i*n_virt + s + n_ex] * K[2, i*n_virt + s]

										elif ((t != s) and (u == s) and (v == t)):

											L4[i*n_virt + s + n_ex] += (-4 * g[i, n_occ + s, i, n_occ + s] ) * K[0, i*n_virt + t + n_ex] * K[1, i*n_virt + s + n_ex] * K[2, i*n_virt + t]

										elif ((t != s) and (u == t) and (v == s)):

											L4[i*n_virt + s + n_ex] += (-4 * g[i, n_occ + t, i, n_occ + t] ) * K[0, i*n_virt + t + n_ex] * K[1, i*n_virt + t + n_ex] * K[2, i*n_virt + s]

										elif ((t != s) and (u == t) and (v == t)):

											L4[i*n_virt + s + n_ex] += (-8 * g[i, n_occ + s, i, n_occ + t] ) * K[0, i*n_virt + t + n_ex] * K[1, i*n_virt + t + n_ex] * K[2, i*n_virt + t]

										elif ((t != s) and (u != s) and (u != t) and (v == s)):

											L4[i*n_virt + s + n_ex] += (-4 * g[i, n_occ + t, i, n_occ + u] ) * K[0, i*n_virt + t + n_ex] * K[1, i*n_virt + u + n_ex] * K[2, i*n_virt + s]

										elif ((t != s) and (u != s) and (u != t) and (v == t)):

											L4[i*n_virt + s + n_ex] += (-4 * g[i, n_occ + s, i, n_occ + u] ) * K[0, i*n_virt + t + n_ex] * K[1, i*n_virt + u + n_ex] * K[2, i*n_virt + t]

										elif ((t != s) and (u != s) and (u != t) and (v == u)):

											L4[i*n_virt + s + n_ex] += (-4 * g[i, n_occ + s, i, n_occ + t] ) * K[0, i*n_virt + t + n_ex] * K[1, i*n_virt + u + n_ex] * K[2, i*n_virt + u]

									elif ((j == i) and (k != i) and (k != j) and (m == i)):

										if ((t == s) and (u == s) and (v == s)):

											L4[i*n_virt + s + n_ex] += (-8 * g[i, n_occ + s, k, n_occ + s] ) * K[0, i*n_virt + s + n_ex] * K[1, k*n_virt + s + n_ex] * K[2, i*n_virt + s]

										elif ((t == s) and (u != s) and (u != t) and (v == s)):

											L4[i*n_virt + s + n_ex] += (-8 * g[i, n_occ + s, k, n_occ + u] + 4 * g[i, n_occ + u, k, n_occ + s] ) * K[0, i*n_virt + s + n_ex] * K[1, k*n_virt + u + n_ex] * K[2, i*n_virt + s]

										elif ((t == s) and (u != s) and (u != t) and (v == u)):

											L4[i*n_virt + s + n_ex] += (-4 * g[i, n_occ + s, k, n_occ + s] ) * K[0, i*n_virt + s + n_ex] * K[1, k*n_virt + u + n_ex] * K[2, i*n_virt + u]

										elif ((t != s) and (u == s) and (v == s)):

											L4[i*n_virt + s + n_ex] += (-6 * g[i, n_occ + t, k, n_occ + s] ) * K[0, i*n_virt + t + n_ex] * K[1, k*n_virt + s + n_ex] * K[2, i*n_virt + s]

										elif ((t != s) and (u == s) and (v == t)):

											L4[i*n_virt + s + n_ex] += (-2 * g[i, n_occ + s, k, n_occ + s] ) * K[0, i*n_virt + t + n_ex] * K[1, k*n_virt + s + n_ex] * K[2, i*n_virt + t]

										elif ((t != s) and (u == t) and (v == s)):

											L4[i*n_virt + s + n_ex] += (-2 * g[i, n_occ + t, k, n_occ + t] ) * K[0, i*n_virt + t + n_ex] * K[1, k*n_virt + t + n_ex] * K[2, i*n_virt + s]

										elif ((t != s) and (u == t) and (v == t)):

											L4[i*n_virt + s + n_ex] += (-6 * g[i, n_occ + s, k, n_occ + t] ) * K[0, i*n_virt + t + n_ex] * K[1, k*n_virt + t + n_ex] * K[2, i*n_virt + t]

										elif ((t != s) and (u != s) and (u != t) and (v == s)):

											L4[i*n_virt + s + n_ex] += (-4 * g[i, n_occ + t, k, n_occ + u] + 2 * g[i, n_occ + u, k, n_occ + t] ) * K[0, i*n_virt + t + n_ex] * K[1, k*n_virt + u + n_ex] * K[2, i*n_virt + s]

										elif ((t != s) and (u != s) and (u != t) and (v == t)):

											L4[i*n_virt + s + n_ex] += (-4 * g[i, n_occ + s, k, n_occ + u] + 2 * g[i, n_occ + u, k, n_occ + s] ) * K[0, i*n_virt + t + n_ex] * K[1, k*n_virt + u + n_ex] * K[2, i*n_virt + t]

										elif ((t != s) and (u != s) and (u != t) and (v == u)):

											L4[i*n_virt + s + n_ex] += (-2 * g[i, n_occ + t, k, n_occ + s] + -2 * g[i, n_occ + s, k, n_occ + t] ) * K[0, i*n_virt + t + n_ex] * K[1, k*n_virt + u + n_ex] * K[2, i*n_virt + u]

									elif ((j == i) and (k != i) and (k != j) and (m == k)):

										if ((t == s) and (u == s) and (v == s)):

											L4[i*n_virt + s + n_ex] += (-4 * g[i, n_occ + s, i, n_occ + s] ) * K[0, i*n_virt + s + n_ex] * K[1, k*n_virt + s + n_ex] * K[2, k*n_virt + s]

										elif ((t == s) and (u != s) and (u != t) and (v == s)):

											L4[i*n_virt + s + n_ex] += (-4 * g[i, n_occ + s, i, n_occ + u] ) * K[0, i*n_virt + s + n_ex] * K[1, k*n_virt + u + n_ex] * K[2, k*n_virt + s]

										elif ((t != s) and (u == s) and (v == s)):

											L4[i*n_virt + s + n_ex] += (-2 * g[i, n_occ + s, i, n_occ + t] ) * K[0, i*n_virt + t + n_ex] * K[1, k*n_virt + s + n_ex] * K[2, k*n_virt + s]

										elif ((t != s) and (u == s) and (v == t)):

											L4[i*n_virt + s + n_ex] += (-2 * g[i, n_occ + s, i, n_occ + s] ) * K[0, i*n_virt + t + n_ex] * K[1, k*n_virt + s + n_ex] * K[2, k*n_virt + t]

										elif ((t != s) and (u == t) and (v == s)):

											L4[i*n_virt + s + n_ex] += (-2 * g[i, n_occ + t, i, n_occ + t] ) * K[0, i*n_virt + t + n_ex] * K[1, k*n_virt + t + n_ex] * K[2, k*n_virt + s]

										elif ((t != s) and (u == t) and (v == t)):

											L4[i*n_virt + s + n_ex] += (-2 * g[i, n_occ + s, i, n_occ + t] ) * K[0, i*n_virt + t + n_ex] * K[1, k*n_virt + t + n_ex] * K[2, k*n_virt + t]

										elif ((t != s) and (u != s) and (u != t) and (v == s)):

											L4[i*n_virt + s + n_ex] += (-2 * g[i, n_occ + t, i, n_occ + u] ) * K[0, i*n_virt + t + n_ex] * K[1, k*n_virt + u + n_ex] * K[2, k*n_virt + s]

										elif ((t != s) and (u != s) and (u != t) and (v == t)):

											L4[i*n_virt + s + n_ex] += (-2 * g[i, n_occ + s, i, n_occ + u] ) * K[0, i*n_virt + t + n_ex] * K[1, k*n_virt + u + n_ex] * K[2, k*n_virt + t]

									elif ((j != i) and (k == i) and (m == i)):

										if ((t == s) and (u == s) and (v == s)):

											L4[i*n_virt + s + n_ex] += (-8 * g[i, n_occ + s, j, n_occ + s] ) * K[0, j*n_virt + s + n_ex] * K[1, i*n_virt + s + n_ex] * K[2, i*n_virt + s]

										elif ((t == s) and (u != s) and (u != t) and (v == s)):

											L4[i*n_virt + s + n_ex] += (-6 * g[i, n_occ + u, j, n_occ + s] ) * K[0, j*n_virt + s + n_ex] * K[1, i*n_virt + u + n_ex] * K[2, i*n_virt + s]

										elif ((t == s) and (u != s) and (u != t) and (v == u)):

											L4[i*n_virt + s + n_ex] += (-2 * g[i, n_occ + s, j, n_occ + s] ) * K[0, j*n_virt + s + n_ex] * K[1, i*n_virt + u + n_ex] * K[2, i*n_virt + u]

										elif ((t != s) and (u == s) and (v == s)):

											L4[i*n_virt + s + n_ex] += (-8 * g[i, n_occ + s, j, n_occ + t] + 4 * g[i, n_occ + t, j, n_occ + s] ) * K[0, j*n_virt + t + n_ex] * K[1, i*n_virt + s + n_ex] * K[2, i*n_virt + s]

										elif ((t != s) and (u == s) and (v == t)):

											L4[i*n_virt + s + n_ex] += (-4 * g[i, n_occ + s, j, n_occ + s] ) * K[0, j*n_virt + t + n_ex] * K[1, i*n_virt + s + n_ex] * K[2, i*n_virt + t]

										elif ((t != s) and (u == t) and (v == s)):

											L4[i*n_virt + s + n_ex] += (-2 * g[i, n_occ + t, j, n_occ + t] ) * K[0, j*n_virt + t + n_ex] * K[1, i*n_virt + t + n_ex] * K[2, i*n_virt + s]

										elif ((t != s) and (u == t) and (v == t)):

											L4[i*n_virt + s + n_ex] += (-6 * g[i, n_occ + s, j, n_occ + t] ) * K[0, j*n_virt + t + n_ex] * K[1, i*n_virt + t + n_ex] * K[2, i*n_virt + t]

										elif ((t != s) and (u != s) and (u != t) and (v == s)):

											L4[i*n_virt + s + n_ex] += (2 * g[i, n_occ + t, j, n_occ + u] + -4 * g[i, n_occ + u, j, n_occ + t] ) * K[0, j*n_virt + t + n_ex] * K[1, i*n_virt + u + n_ex] * K[2, i*n_virt + s]

										elif ((t != s) and (u != s) and (u != t) and (v == t)):

											L4[i*n_virt + s + n_ex] += (-2 * g[i, n_occ + u, j, n_occ + s] + -2 * g[i, n_occ + s, j, n_occ + u] ) * K[0, j*n_virt + t + n_ex] * K[1, i*n_virt + u + n_ex] * K[2, i*n_virt + t]

										elif ((t != s) and (u != s) and (u != t) and (v == u)):

											L4[i*n_virt + s + n_ex] += (-4 * g[i, n_occ + s, j, n_occ + t] + 2 * g[i, n_occ + t, j, n_occ + s] ) * K[0, j*n_virt + t + n_ex] * K[1, i*n_virt + u + n_ex] * K[2, i*n_virt + u]

									elif ((j != i) and (k == i) and (m == j)):

										if ((t == s) and (u == s) and (v == s)):

											L4[i*n_virt + s + n_ex] += (-4 * g[i, n_occ + s, i, n_occ + s] ) * K[0, j*n_virt + s + n_ex] * K[1, i*n_virt + s + n_ex] * K[2, j*n_virt + s]

										elif ((t == s) and (u != s) and (u != t) and (v == s)):

											L4[i*n_virt + s + n_ex] += (-2 * g[i, n_occ + s, i, n_occ + u] ) * K[0, j*n_virt + s + n_ex] * K[1, i*n_virt + u + n_ex] * K[2, j*n_virt + s]

										elif ((t == s) and (u != s) and (u != t) and (v == u)):

											L4[i*n_virt + s + n_ex] += (-2 * g[i, n_occ + s, i, n_occ + s] ) * K[0, j*n_virt + s + n_ex] * K[1, i*n_virt + u + n_ex] * K[2, j*n_virt + u]

										elif ((t != s) and (u == s) and (v == s)):

											L4[i*n_virt + s + n_ex] += (-4 * g[i, n_occ + s, i, n_occ + t] ) * K[0, j*n_virt + t + n_ex] * K[1, i*n_virt + s + n_ex] * K[2, j*n_virt + s]

										elif ((t != s) and (u == t) and (v == s)):

											L4[i*n_virt + s + n_ex] += (-2 * g[i, n_occ + t, i, n_occ + t] ) * K[0, j*n_virt + t + n_ex] * K[1, i*n_virt + t + n_ex] * K[2, j*n_virt + s]

										elif ((t != s) and (u == t) and (v == t)):

											L4[i*n_virt + s + n_ex] += (-2 * g[i, n_occ + s, i, n_occ + t] ) * K[0, j*n_virt + t + n_ex] * K[1, i*n_virt + t + n_ex] * K[2, j*n_virt + t]

										elif ((t != s) and (u != s) and (u != t) and (v == s)):

											L4[i*n_virt + s + n_ex] += (-2 * g[i, n_occ + t, i, n_occ + u] ) * K[0, j*n_virt + t + n_ex] * K[1, i*n_virt + u + n_ex] * K[2, j*n_virt + s]

										elif ((t != s) and (u != s) and (u != t) and (v == u)):

											L4[i*n_virt + s + n_ex] += (-2 * g[i, n_occ + s, i, n_occ + t] ) * K[0, j*n_virt + t + n_ex] * K[1, i*n_virt + u + n_ex] * K[2, j*n_virt + u]

									elif ((j != i) and (k == j) and (m == i)):

										if ((t == s) and (u == s) and (v == s)):

											L4[i*n_virt + s + n_ex] += (-4 * g[j, n_occ + s, j, n_occ + s] ) * K[0, j*n_virt + s + n_ex] * K[1, j*n_virt + s + n_ex] * K[2, i*n_virt + s]

										elif ((t == s) and (u != s) and (u != t) and (v == s)):

											L4[i*n_virt + s + n_ex] += (-2 * g[j, n_occ + s, j, n_occ + u] ) * K[0, j*n_virt + s + n_ex] * K[1, j*n_virt + u + n_ex] * K[2, i*n_virt + s]

										elif ((t == s) and (u != s) and (u != t) and (v == u)):

											L4[i*n_virt + s + n_ex] += (-2 * g[j, n_occ + s, j, n_occ + s] ) * K[0, j*n_virt + s + n_ex] * K[1, j*n_virt + u + n_ex] * K[2, i*n_virt + u]

										elif ((t != s) and (u == s) and (v == s)):

											L4[i*n_virt + s + n_ex] += (-2 * g[j, n_occ + s, j, n_occ + t] ) * K[0, j*n_virt + t + n_ex] * K[1, j*n_virt + s + n_ex] * K[2, i*n_virt + s]

										elif ((t != s) and (u == s) and (v == t)):

											L4[i*n_virt + s + n_ex] += (-2 * g[j, n_occ + s, j, n_occ + s] ) * K[0, j*n_virt + t + n_ex] * K[1, j*n_virt + s + n_ex] * K[2, i*n_virt + t]

										elif ((t != s) and (u == t) and (v == t)):

											L4[i*n_virt + s + n_ex] += (-4 * g[j, n_occ + s, j, n_occ + t] ) * K[0, j*n_virt + t + n_ex] * K[1, j*n_virt + t + n_ex] * K[2, i*n_virt + t]

										elif ((t != s) and (u != s) and (u != t) and (v == t)):

											L4[i*n_virt + s + n_ex] += (-2 * g[j, n_occ + s, j, n_occ + u] ) * K[0, j*n_virt + t + n_ex] * K[1, j*n_virt + u + n_ex] * K[2, i*n_virt + t]

										elif ((t != s) and (u != s) and (u != t) and (v == u)):

											L4[i*n_virt + s + n_ex] += (-2 * g[j, n_occ + s, j, n_occ + t] ) * K[0, j*n_virt + t + n_ex] * K[1, j*n_virt + u + n_ex] * K[2, i*n_virt + u]

									elif ((j != i) and (k == j) and (m == j)):

										if ((t == s) and (u == s) and (v == s)):

											L4[i*n_virt + s + n_ex] += (-8 * g[i, n_occ + s, j, n_occ + s] ) * K[0, j*n_virt + s + n_ex] * K[1, j*n_virt + s + n_ex] * K[2, j*n_virt + s]

										elif ((t == s) and (u != s) and (u != t) and (v == s)):

											L4[i*n_virt + s + n_ex] += (-6 * g[i, n_occ + s, j, n_occ + u] ) * K[0, j*n_virt + s + n_ex] * K[1, j*n_virt + u + n_ex] * K[2, j*n_virt + s]

										elif ((t == s) and (u != s) and (u != t) and (v == u)):

											L4[i*n_virt + s + n_ex] += (-2 * g[i, n_occ + s, j, n_occ + s] ) * K[0, j*n_virt + s + n_ex] * K[1, j*n_virt + u + n_ex] * K[2, j*n_virt + u]

										elif ((t != s) and (u == s) and (v == s)):

											L4[i*n_virt + s + n_ex] += (-6 * g[i, n_occ + s, j, n_occ + t] ) * K[0, j*n_virt + t + n_ex] * K[1, j*n_virt + s + n_ex] * K[2, j*n_virt + s]

										elif ((t != s) and (u == s) and (v == t)):

											L4[i*n_virt + s + n_ex] += (-2 * g[i, n_occ + s, j, n_occ + s] ) * K[0, j*n_virt + t + n_ex] * K[1, j*n_virt + s + n_ex] * K[2, j*n_virt + t]

										elif ((t != s) and (u == t) and (v == s)):

											L4[i*n_virt + s + n_ex] += (-4 * g[i, n_occ + t, j, n_occ + t] ) * K[0, j*n_virt + t + n_ex] * K[1, j*n_virt + t + n_ex] * K[2, j*n_virt + s]

										elif ((t != s) and (u == t) and (v == t)):

											L4[i*n_virt + s + n_ex] += (-8 * g[i, n_occ + s, j, n_occ + t] + 4 * g[i, n_occ + t, j, n_occ + s] ) * K[0, j*n_virt + t + n_ex] * K[1, j*n_virt + t + n_ex] * K[2, j*n_virt + t]

										elif ((t != s) and (u != s) and (u != t) and (v == s)):

											L4[i*n_virt + s + n_ex] += (-2 * g[i, n_occ + u, j, n_occ + t] + -2 * g[i, n_occ + t, j, n_occ + u] ) * K[0, j*n_virt + t + n_ex] * K[1, j*n_virt + u + n_ex] * K[2, j*n_virt + s]

										elif ((t != s) and (u != s) and (u != t) and (v == t)):

											L4[i*n_virt + s + n_ex] += (-4 * g[i, n_occ + s, j, n_occ + u] + 2 * g[i, n_occ + u, j, n_occ + s] ) * K[0, j*n_virt + t + n_ex] * K[1, j*n_virt + u + n_ex] * K[2, j*n_virt + t]

										elif ((t != s) and (u != s) and (u != t) and (v == u)):

											L4[i*n_virt + s + n_ex] += (-4 * g[i, n_occ + s, j, n_occ + t] + 2 * g[i, n_occ + t, j, n_occ + s] ) * K[0, j*n_virt + t + n_ex] * K[1, j*n_virt + u + n_ex] * K[2, j*n_virt + u]

									elif ((j != i) and (k != i) and (k != j) and (m == i)):

										if ((t == s) and (u == s) and (v == s)):

											L4[i*n_virt + s + n_ex] += (-4 * g[j, n_occ + s, k, n_occ + s] ) * K[0, j*n_virt + s + n_ex] * K[1, k*n_virt + s + n_ex] * K[2, i*n_virt + s]

										elif ((t == s) and (u != s) and (u != t) and (v == s)):

											L4[i*n_virt + s + n_ex] += (-4 * g[j, n_occ + s, k, n_occ + u] + 2 * g[j, n_occ + u, k, n_occ + s] ) * K[0, j*n_virt + s + n_ex] * K[1, k*n_virt + u + n_ex] * K[2, i*n_virt + s]

										elif ((t == s) and (u != s) and (u != t) and (v == u)):

											L4[i*n_virt + s + n_ex] += (-2 * g[j, n_occ + s, k, n_occ + s] ) * K[0, j*n_virt + s + n_ex] * K[1, k*n_virt + u + n_ex] * K[2, i*n_virt + u]

										elif ((t != s) and (u == s) and (v == s)):

											L4[i*n_virt + s + n_ex] += (2 * g[j, n_occ + s, k, n_occ + t] + -4 * g[j, n_occ + t, k, n_occ + s] ) * K[0, j*n_virt + t + n_ex] * K[1, k*n_virt + s + n_ex] * K[2, i*n_virt + s]

										elif ((t != s) and (u == s) and (v == t)):

											L4[i*n_virt + s + n_ex] += (-2 * g[j, n_occ + s, k, n_occ + s] ) * K[0, j*n_virt + t + n_ex] * K[1, k*n_virt + s + n_ex] * K[2, i*n_virt + t]

										elif ((t != s) and (u == t) and (v == t)):

											L4[i*n_virt + s + n_ex] += (-2 * g[j, n_occ + t, k, n_occ + s] + -2 * g[j, n_occ + s, k, n_occ + t] ) * K[0, j*n_virt + t + n_ex] * K[1, k*n_virt + t + n_ex] * K[2, i*n_virt + t]

										elif ((t != s) and (u != s) and (u != t) and (v == t)):

											L4[i*n_virt + s + n_ex] += (-4 * g[j, n_occ + s, k, n_occ + u] + 2 * g[j, n_occ + u, k, n_occ + s] ) * K[0, j*n_virt + t + n_ex] * K[1, k*n_virt + u + n_ex] * K[2, i*n_virt + t]

										elif ((t != s) and (u != s) and (u != t) and (v == u)):

											L4[i*n_virt + s + n_ex] += (2 * g[j, n_occ + s, k, n_occ + t] + -4 * g[j, n_occ + t, k, n_occ + s] ) * K[0, j*n_virt + t + n_ex] * K[1, k*n_virt + u + n_ex] * K[2, i*n_virt + u]

									elif ((j != i) and (k != i) and (k != j) and (m == j)):

										if ((t == s) and (u == s) and (v == s)):

											L4[i*n_virt + s + n_ex] += (-4 * g[i, n_occ + s, k, n_occ + s] ) * K[0, j*n_virt + s + n_ex] * K[1, k*n_virt + s + n_ex] * K[2, j*n_virt + s]

										elif ((t == s) and (u != s) and (u != t) and (v == s)):

											L4[i*n_virt + s + n_ex] += (-4 * g[i, n_occ + s, k, n_occ + u] + 2 * g[i, n_occ + u, k, n_occ + s] ) * K[0, j*n_virt + s + n_ex] * K[1, k*n_virt + u + n_ex] * K[2, j*n_virt + s]

										elif ((t == s) and (u != s) and (u != t) and (v == u)):

											L4[i*n_virt + s + n_ex] += (-2 * g[i, n_occ + s, k, n_occ + s] ) * K[0, j*n_virt + s + n_ex] * K[1, k*n_virt + u + n_ex] * K[2, j*n_virt + u]

										elif ((t != s) and (u == s) and (v == s)):

											L4[i*n_virt + s + n_ex] += (-2 * g[i, n_occ + t, k, n_occ + s] + -2 * g[i, n_occ + s, k, n_occ + t] ) * K[0, j*n_virt + t + n_ex] * K[1, k*n_virt + s + n_ex] * K[2, j*n_virt + s]

										elif ((t != s) and (u == t) and (v == s)):

											L4[i*n_virt + s + n_ex] += (-2 * g[i, n_occ + t, k, n_occ + t] ) * K[0, j*n_virt + t + n_ex] * K[1, k*n_virt + t + n_ex] * K[2, j*n_virt + s]

										elif ((t != s) and (u == t) and (v == t)):

											L4[i*n_virt + s + n_ex] += (-4 * g[i, n_occ + s, k, n_occ + t] + 2 * g[i, n_occ + t, k, n_occ + s] ) * K[0, j*n_virt + t + n_ex] * K[1, k*n_virt + t + n_ex] * K[2, j*n_virt + t]

										elif ((t != s) and (u != s) and (u != t) and (v == s)):

											L4[i*n_virt + s + n_ex] += (-4 * g[i, n_occ + t, k, n_occ + u] + 2 * g[i, n_occ + u, k, n_occ + t] ) * K[0, j*n_virt + t + n_ex] * K[1, k*n_virt + u + n_ex] * K[2, j*n_virt + s]

										elif ((t != s) and (u != s) and (u != t) and (v == u)):

											L4[i*n_virt + s + n_ex] += (-4 * g[i, n_occ + s, k, n_occ + t] + 2 * g[i, n_occ + t, k, n_occ + s] ) * K[0, j*n_virt + t + n_ex] * K[1, k*n_virt + u + n_ex] * K[2, j*n_virt + u]

									elif ((j != i) and (k != i) and (k != j) and (m == k)):

										if ((t == s) and (u == s) and (v == s)):

											L4[i*n_virt + s + n_ex] += (-4 * g[i, n_occ + s, j, n_occ + s] ) * K[0, j*n_virt + s + n_ex] * K[1, k*n_virt + s + n_ex] * K[2, k*n_virt + s]

										elif ((t == s) and (u != s) and (u != t) and (v == s)):

											L4[i*n_virt + s + n_ex] += (-2 * g[i, n_occ + u, j, n_occ + s] + -2 * g[i, n_occ + s, j, n_occ + u] ) * K[0, j*n_virt + s + n_ex] * K[1, k*n_virt + u + n_ex] * K[2, k*n_virt + s]

										elif ((t != s) and (u == s) and (v == s)):

											L4[i*n_virt + s + n_ex] += (-4 * g[i, n_occ + s, j, n_occ + t] + 2 * g[i, n_occ + t, j, n_occ + s] ) * K[0, j*n_virt + t + n_ex] * K[1, k*n_virt + s + n_ex] * K[2, k*n_virt + s]

										elif ((t != s) and (u == s) and (v == t)):

											L4[i*n_virt + s + n_ex] += (-2 * g[i, n_occ + s, j, n_occ + s] ) * K[0, j*n_virt + t + n_ex] * K[1, k*n_virt + s + n_ex] * K[2, k*n_virt + t]

										elif ((t != s) and (u == t) and (v == s)):

											L4[i*n_virt + s + n_ex] += (-2 * g[i, n_occ + t, j, n_occ + t] ) * K[0, j*n_virt + t + n_ex] * K[1, k*n_virt + t + n_ex] * K[2, k*n_virt + s]

										elif ((t != s) and (u == t) and (v == t)):

											L4[i*n_virt + s + n_ex] += (-4 * g[i, n_occ + s, j, n_occ + t] + 2 * g[i, n_occ + t, j, n_occ + s] ) * K[0, j*n_virt + t + n_ex] * K[1, k*n_virt + t + n_ex] * K[2, k*n_virt + t]

										elif ((t != s) and (u != s) and (u != t) and (v == s)):

											L4[i*n_virt + s + n_ex] += (2 * g[i, n_occ + t, j, n_occ + u] + -4 * g[i, n_occ + u, j, n_occ + t] ) * K[0, j*n_virt + t + n_ex] * K[1, k*n_virt + u + n_ex] * K[2, k*n_virt + s]

										elif ((t != s) and (u != s) and (u != t) and (v == t)):

											L4[i*n_virt + s + n_ex] += (-4 * g[i, n_occ + s, j, n_occ + u] + 2 * g[i, n_occ + u, j, n_occ + s] ) * K[0, j*n_virt + t + n_ex] * K[1, k*n_virt + u + n_ex] * K[2, k*n_virt + t]

	# Current operator combination: {'a': 1, 'b': 2, 'c': 2, 'd': 3}
	# All terms vanished for this combination

	# Current operator combination: {'a': 1, 'b': 2, 'c': 3, 'd': 1}
	# This combination was excluded by the contr_type_only argument {'a': 1, 'b': 2, 'c': 3, 'd': 1}

	# Current operator combination: {'a': 1, 'b': 2, 'c': 3, 'd': 2}
	# This combination was excluded by the contr_type_only argument {'a': 1, 'b': 2, 'c': 3, 'd': 2}

	# Current operator combination: {'a': 1, 'b': 2, 'c': 3, 'd': 3}
	# This combination was excluded by the contr_type_only argument {'a': 1, 'b': 2, 'c': 3, 'd': 3}

	# Current operator combination: {'a': 1, 'b': 3, 'c': 1, 'd': 1}
	# This combination was excluded by the contr_type_only argument {'a': 1, 'b': 3, 'c': 1, 'd': 1}

	# Current operator combination: {'a': 1, 'b': 3, 'c': 1, 'd': 2}
	# This combination was excluded by the contr_type_only argument {'a': 1, 'b': 3, 'c': 1, 'd': 2}

	# Current operator combination: {'a': 1, 'b': 3, 'c': 1, 'd': 3}
	# This combination was excluded by the contr_type_only argument {'a': 1, 'b': 3, 'c': 1, 'd': 3}

	# Current operator combination: {'a': 1, 'b': 3, 'c': 2, 'd': 1}
	# This combination was excluded by the contr_type_only argument {'a': 1, 'b': 3, 'c': 2, 'd': 1}

	# Current operator combination: {'a': 1, 'b': 3, 'c': 2, 'd': 2}
	# This combination was excluded by the contr_type_only argument {'a': 1, 'b': 3, 'c': 2, 'd': 2}

	# Current operator combination: {'a': 1, 'b': 3, 'c': 2, 'd': 3}
	# This combination was excluded by the contr_type_only argument {'a': 1, 'b': 3, 'c': 2, 'd': 3}

	# Current operator combination: {'a': 1, 'b': 3, 'c': 3, 'd': 1}
	# This combination was excluded by the contr_type_only argument {'a': 1, 'b': 3, 'c': 3, 'd': 1}

	# Current operator combination: {'a': 1, 'b': 3, 'c': 3, 'd': 2}
	# This combination was excluded by the contr_type_only argument {'a': 1, 'b': 3, 'c': 3, 'd': 2}

	# Current operator combination: {'a': 1, 'b': 3, 'c': 3, 'd': 3}
	# This combination was excluded by the contr_type_only argument {'a': 1, 'b': 3, 'c': 3, 'd': 3}

	# Current operator combination: {'a': 2, 'b': 1, 'c': 1, 'd': 1}
	for i in range(n_occ):
		for j in range(n_occ):
			for k in range(n_occ):
				for m in range(n_occ):
					for s in range(n_virt):
						for t in range(n_virt):
							for u in range(n_virt):
								for v in range(n_virt):

									if ((j == i) and (k == i) and (m == i)):

										if ((t == s) and (u == s) and (v == s)):

											L4[i*n_virt + s] += (12 * g[i, n_occ + s, i, n_occ + s] ) * K[0, i*n_virt + s] * K[1, i*n_virt + s] * K[2, i*n_virt + s + n_ex]

										elif ((t == s) and (u != s) and (u != t) and (v == s)):

											L4[i*n_virt + s] += (8 * g[i, n_occ + s, i, n_occ + u] ) * K[0, i*n_virt + s] * K[1, i*n_virt + u] * K[2, i*n_virt + s + n_ex]

										elif ((t == s) and (u != s) and (u != t) and (v == u)):

											L4[i*n_virt + s] += (4 * g[i, n_occ + s, i, n_occ + s] ) * K[0, i*n_virt + s] * K[1, i*n_virt + u] * K[2, i*n_virt + u + n_ex]

										elif ((t != s) and (u == s) and (v == s)):

											L4[i*n_virt + s] += (8 * g[i, n_occ + s, i, n_occ + t] ) * K[0, i*n_virt + t] * K[1, i*n_virt + s] * K[2, i*n_virt + s + n_ex]

										elif ((t != s) and (u == s) and (v == t)):

											L4[i*n_virt + s] += (4 * g[i, n_occ + s, i, n_occ + s] ) * K[0, i*n_virt + t] * K[1, i*n_virt + s] * K[2, i*n_virt + t + n_ex]

										elif ((t != s) and (u == t) and (v == s)):

											L4[i*n_virt + s] += (4 * g[i, n_occ + t, i, n_occ + t] ) * K[0, i*n_virt + t] * K[1, i*n_virt + t] * K[2, i*n_virt + s + n_ex]

										elif ((t != s) and (u == t) and (v == t)):

											L4[i*n_virt + s] += (8 * g[i, n_occ + s, i, n_occ + t] ) * K[0, i*n_virt + t] * K[1, i*n_virt + t] * K[2, i*n_virt + t + n_ex]

										elif ((t != s) and (u != s) and (u != t) and (v == s)):

											L4[i*n_virt + s] += (4 * g[i, n_occ + t, i, n_occ + u] ) * K[0, i*n_virt + t] * K[1, i*n_virt + u] * K[2, i*n_virt + s + n_ex]

										elif ((t != s) and (u != s) and (u != t) and (v == t)):

											L4[i*n_virt + s] += (4 * g[i, n_occ + s, i, n_occ + u] ) * K[0, i*n_virt + t] * K[1, i*n_virt + u] * K[2, i*n_virt + t + n_ex]

										elif ((t != s) and (u != s) and (u != t) and (v == u)):

											L4[i*n_virt + s] += (4 * g[i, n_occ + s, i, n_occ + t] ) * K[0, i*n_virt + t] * K[1, i*n_virt + u] * K[2, i*n_virt + u + n_ex]

									elif ((j == i) and (k != i) and (k != j) and (m == i)):

										if ((t == s) and (u == s) and (v == s)):

											L4[i*n_virt + s] += (8 * g[i, n_occ + s, k, n_occ + s] ) * K[0, i*n_virt + s] * K[1, k*n_virt + s] * K[2, i*n_virt + s + n_ex]

										elif ((t == s) and (u != s) and (u != t) and (v == s)):

											L4[i*n_virt + s] += (8 * g[i, n_occ + s, k, n_occ + u] + -4 * g[i, n_occ + u, k, n_occ + s] ) * K[0, i*n_virt + s] * K[1, k*n_virt + u] * K[2, i*n_virt + s + n_ex]

										elif ((t == s) and (u != s) and (u != t) and (v == u)):

											L4[i*n_virt + s] += (4 * g[i, n_occ + s, k, n_occ + s] ) * K[0, i*n_virt + s] * K[1, k*n_virt + u] * K[2, i*n_virt + u + n_ex]

										elif ((t != s) and (u == s) and (v == s)):

											L4[i*n_virt + s] += (6 * g[i, n_occ + t, k, n_occ + s] ) * K[0, i*n_virt + t] * K[1, k*n_virt + s] * K[2, i*n_virt + s + n_ex]

										elif ((t != s) and (u == s) and (v == t)):

											L4[i*n_virt + s] += (2 * g[i, n_occ + s, k, n_occ + s] ) * K[0, i*n_virt + t] * K[1, k*n_virt + s] * K[2, i*n_virt + t + n_ex]

										elif ((t != s) and (u == t) and (v == s)):

											L4[i*n_virt + s] += (2 * g[i, n_occ + t, k, n_occ + t] ) * K[0, i*n_virt + t] * K[1, k*n_virt + t] * K[2, i*n_virt + s + n_ex]

										elif ((t != s) and (u == t) and (v == t)):

											L4[i*n_virt + s] += (6 * g[i, n_occ + s, k, n_occ + t] ) * K[0, i*n_virt + t] * K[1, k*n_virt + t] * K[2, i*n_virt + t + n_ex]

										elif ((t != s) and (u != s) and (u != t) and (v == s)):

											L4[i*n_virt + s] += (4 * g[i, n_occ + t, k, n_occ + u] + -2 * g[i, n_occ + u, k, n_occ + t] ) * K[0, i*n_virt + t] * K[1, k*n_virt + u] * K[2, i*n_virt + s + n_ex]

										elif ((t != s) and (u != s) and (u != t) and (v == t)):

											L4[i*n_virt + s] += (4 * g[i, n_occ + s, k, n_occ + u] + -2 * g[i, n_occ + u, k, n_occ + s] ) * K[0, i*n_virt + t] * K[1, k*n_virt + u] * K[2, i*n_virt + t + n_ex]

										elif ((t != s) and (u != s) and (u != t) and (v == u)):

											L4[i*n_virt + s] += (2 * g[i, n_occ + t, k, n_occ + s] + 2 * g[i, n_occ + s, k, n_occ + t] ) * K[0, i*n_virt + t] * K[1, k*n_virt + u] * K[2, i*n_virt + u + n_ex]

									elif ((j == i) and (k != i) and (k != j) and (m == k)):

										if ((t == s) and (u == s) and (v == s)):

											L4[i*n_virt + s] += (4 * g[i, n_occ + s, i, n_occ + s] ) * K[0, i*n_virt + s] * K[1, k*n_virt + s] * K[2, k*n_virt + s + n_ex]

										elif ((t == s) and (u != s) and (u != t) and (v == s)):

											L4[i*n_virt + s] += (4 * g[i, n_occ + s, i, n_occ + u] ) * K[0, i*n_virt + s] * K[1, k*n_virt + u] * K[2, k*n_virt + s + n_ex]

										elif ((t != s) and (u == s) and (v == s)):

											L4[i*n_virt + s] += (2 * g[i, n_occ + s, i, n_occ + t] ) * K[0, i*n_virt + t] * K[1, k*n_virt + s] * K[2, k*n_virt + s + n_ex]

										elif ((t != s) and (u == s) and (v == t)):

											L4[i*n_virt + s] += (2 * g[i, n_occ + s, i, n_occ + s] ) * K[0, i*n_virt + t] * K[1, k*n_virt + s] * K[2, k*n_virt + t + n_ex]

										elif ((t != s) and (u == t) and (v == s)):

											L4[i*n_virt + s] += (2 * g[i, n_occ + t, i, n_occ + t] ) * K[0, i*n_virt + t] * K[1, k*n_virt + t] * K[2, k*n_virt + s + n_ex]

										elif ((t != s) and (u == t) and (v == t)):

											L4[i*n_virt + s] += (2 * g[i, n_occ + s, i, n_occ + t] ) * K[0, i*n_virt + t] * K[1, k*n_virt + t] * K[2, k*n_virt + t + n_ex]

										elif ((t != s) and (u != s) and (u != t) and (v == s)):

											L4[i*n_virt + s] += (2 * g[i, n_occ + t, i, n_occ + u] ) * K[0, i*n_virt + t] * K[1, k*n_virt + u] * K[2, k*n_virt + s + n_ex]

										elif ((t != s) and (u != s) and (u != t) and (v == t)):

											L4[i*n_virt + s] += (2 * g[i, n_occ + s, i, n_occ + u] ) * K[0, i*n_virt + t] * K[1, k*n_virt + u] * K[2, k*n_virt + t + n_ex]

									elif ((j != i) and (k == i) and (m == i)):

										if ((t == s) and (u == s) and (v == s)):

											L4[i*n_virt + s] += (8 * g[i, n_occ + s, j, n_occ + s] ) * K[0, j*n_virt + s] * K[1, i*n_virt + s] * K[2, i*n_virt + s + n_ex]

										elif ((t == s) and (u != s) and (u != t) and (v == s)):

											L4[i*n_virt + s] += (6 * g[i, n_occ + u, j, n_occ + s] ) * K[0, j*n_virt + s] * K[1, i*n_virt + u] * K[2, i*n_virt + s + n_ex]

										elif ((t == s) and (u != s) and (u != t) and (v == u)):

											L4[i*n_virt + s] += (2 * g[i, n_occ + s, j, n_occ + s] ) * K[0, j*n_virt + s] * K[1, i*n_virt + u] * K[2, i*n_virt + u + n_ex]

										elif ((t != s) and (u == s) and (v == s)):

											L4[i*n_virt + s] += (8 * g[i, n_occ + s, j, n_occ + t] + -4 * g[i, n_occ + t, j, n_occ + s] ) * K[0, j*n_virt + t] * K[1, i*n_virt + s] * K[2, i*n_virt + s + n_ex]

										elif ((t != s) and (u == s) and (v == t)):

											L4[i*n_virt + s] += (4 * g[i, n_occ + s, j, n_occ + s] ) * K[0, j*n_virt + t] * K[1, i*n_virt + s] * K[2, i*n_virt + t + n_ex]

										elif ((t != s) and (u == t) and (v == s)):

											L4[i*n_virt + s] += (2 * g[i, n_occ + t, j, n_occ + t] ) * K[0, j*n_virt + t] * K[1, i*n_virt + t] * K[2, i*n_virt + s + n_ex]

										elif ((t != s) and (u == t) and (v == t)):

											L4[i*n_virt + s] += (6 * g[i, n_occ + s, j, n_occ + t] ) * K[0, j*n_virt + t] * K[1, i*n_virt + t] * K[2, i*n_virt + t + n_ex]

										elif ((t != s) and (u != s) and (u != t) and (v == s)):

											L4[i*n_virt + s] += (-2 * g[i, n_occ + t, j, n_occ + u] + 4 * g[i, n_occ + u, j, n_occ + t] ) * K[0, j*n_virt + t] * K[1, i*n_virt + u] * K[2, i*n_virt + s + n_ex]

										elif ((t != s) and (u != s) and (u != t) and (v == t)):

											L4[i*n_virt + s] += (2 * g[i, n_occ + u, j, n_occ + s] + 2 * g[i, n_occ + s, j, n_occ + u] ) * K[0, j*n_virt + t] * K[1, i*n_virt + u] * K[2, i*n_virt + t + n_ex]

										elif ((t != s) and (u != s) and (u != t) and (v == u)):

											L4[i*n_virt + s] += (4 * g[i, n_occ + s, j, n_occ + t] + -2 * g[i, n_occ + t, j, n_occ + s] ) * K[0, j*n_virt + t] * K[1, i*n_virt + u] * K[2, i*n_virt + u + n_ex]

									elif ((j != i) and (k == i) and (m == j)):

										if ((t == s) and (u == s) and (v == s)):

											L4[i*n_virt + s] += (4 * g[i, n_occ + s, i, n_occ + s] ) * K[0, j*n_virt + s] * K[1, i*n_virt + s] * K[2, j*n_virt + s + n_ex]

										elif ((t == s) and (u != s) and (u != t) and (v == s)):

											L4[i*n_virt + s] += (2 * g[i, n_occ + s, i, n_occ + u] ) * K[0, j*n_virt + s] * K[1, i*n_virt + u] * K[2, j*n_virt + s + n_ex]

										elif ((t == s) and (u != s) and (u != t) and (v == u)):

											L4[i*n_virt + s] += (2 * g[i, n_occ + s, i, n_occ + s] ) * K[0, j*n_virt + s] * K[1, i*n_virt + u] * K[2, j*n_virt + u + n_ex]

										elif ((t != s) and (u == s) and (v == s)):

											L4[i*n_virt + s] += (4 * g[i, n_occ + s, i, n_occ + t] ) * K[0, j*n_virt + t] * K[1, i*n_virt + s] * K[2, j*n_virt + s + n_ex]

										elif ((t != s) and (u == t) and (v == s)):

											L4[i*n_virt + s] += (2 * g[i, n_occ + t, i, n_occ + t] ) * K[0, j*n_virt + t] * K[1, i*n_virt + t] * K[2, j*n_virt + s + n_ex]

										elif ((t != s) and (u == t) and (v == t)):

											L4[i*n_virt + s] += (2 * g[i, n_occ + s, i, n_occ + t] ) * K[0, j*n_virt + t] * K[1, i*n_virt + t] * K[2, j*n_virt + t + n_ex]

										elif ((t != s) and (u != s) and (u != t) and (v == s)):

											L4[i*n_virt + s] += (2 * g[i, n_occ + t, i, n_occ + u] ) * K[0, j*n_virt + t] * K[1, i*n_virt + u] * K[2, j*n_virt + s + n_ex]

										elif ((t != s) and (u != s) and (u != t) and (v == u)):

											L4[i*n_virt + s] += (2 * g[i, n_occ + s, i, n_occ + t] ) * K[0, j*n_virt + t] * K[1, i*n_virt + u] * K[2, j*n_virt + u + n_ex]

									elif ((j != i) and (k == j) and (m == i)):

										if ((t == s) and (u == s) and (v == s)):

											L4[i*n_virt + s] += (4 * g[j, n_occ + s, j, n_occ + s] ) * K[0, j*n_virt + s] * K[1, j*n_virt + s] * K[2, i*n_virt + s + n_ex]

										elif ((t == s) and (u != s) and (u != t) and (v == s)):

											L4[i*n_virt + s] += (2 * g[j, n_occ + s, j, n_occ + u] ) * K[0, j*n_virt + s] * K[1, j*n_virt + u] * K[2, i*n_virt + s + n_ex]

										elif ((t == s) and (u != s) and (u != t) and (v == u)):

											L4[i*n_virt + s] += (2 * g[j, n_occ + s, j, n_occ + s] ) * K[0, j*n_virt + s] * K[1, j*n_virt + u] * K[2, i*n_virt + u + n_ex]

										elif ((t != s) and (u == s) and (v == s)):

											L4[i*n_virt + s] += (2 * g[j, n_occ + s, j, n_occ + t] ) * K[0, j*n_virt + t] * K[1, j*n_virt + s] * K[2, i*n_virt + s + n_ex]

										elif ((t != s) and (u == s) and (v == t)):

											L4[i*n_virt + s] += (2 * g[j, n_occ + s, j, n_occ + s] ) * K[0, j*n_virt + t] * K[1, j*n_virt + s] * K[2, i*n_virt + t + n_ex]

										elif ((t != s) and (u == t) and (v == t)):

											L4[i*n_virt + s] += (4 * g[j, n_occ + s, j, n_occ + t] ) * K[0, j*n_virt + t] * K[1, j*n_virt + t] * K[2, i*n_virt + t + n_ex]

										elif ((t != s) and (u != s) and (u != t) and (v == t)):

											L4[i*n_virt + s] += (2 * g[j, n_occ + s, j, n_occ + u] ) * K[0, j*n_virt + t] * K[1, j*n_virt + u] * K[2, i*n_virt + t + n_ex]

										elif ((t != s) and (u != s) and (u != t) and (v == u)):

											L4[i*n_virt + s] += (2 * g[j, n_occ + s, j, n_occ + t] ) * K[0, j*n_virt + t] * K[1, j*n_virt + u] * K[2, i*n_virt + u + n_ex]

									elif ((j != i) and (k == j) and (m == j)):

										if ((t == s) and (u == s) and (v == s)):

											L4[i*n_virt + s] += (8 * g[i, n_occ + s, j, n_occ + s] ) * K[0, j*n_virt + s] * K[1, j*n_virt + s] * K[2, j*n_virt + s + n_ex]

										elif ((t == s) and (u != s) and (u != t) and (v == s)):

											L4[i*n_virt + s] += (6 * g[i, n_occ + s, j, n_occ + u] ) * K[0, j*n_virt + s] * K[1, j*n_virt + u] * K[2, j*n_virt + s + n_ex]

										elif ((t == s) and (u != s) and (u != t) and (v == u)):

											L4[i*n_virt + s] += (2 * g[i, n_occ + s, j, n_occ + s] ) * K[0, j*n_virt + s] * K[1, j*n_virt + u] * K[2, j*n_virt + u + n_ex]

										elif ((t != s) and (u == s) and (v == s)):

											L4[i*n_virt + s] += (6 * g[i, n_occ + s, j, n_occ + t] ) * K[0, j*n_virt + t] * K[1, j*n_virt + s] * K[2, j*n_virt + s + n_ex]

										elif ((t != s) and (u == s) and (v == t)):

											L4[i*n_virt + s] += (2 * g[i, n_occ + s, j, n_occ + s] ) * K[0, j*n_virt + t] * K[1, j*n_virt + s] * K[2, j*n_virt + t + n_ex]

										elif ((t != s) and (u == t) and (v == s)):

											L4[i*n_virt + s] += (4 * g[i, n_occ + t, j, n_occ + t] ) * K[0, j*n_virt + t] * K[1, j*n_virt + t] * K[2, j*n_virt + s + n_ex]

										elif ((t != s) and (u == t) and (v == t)):

											L4[i*n_virt + s] += (8 * g[i, n_occ + s, j, n_occ + t] + -4 * g[i, n_occ + t, j, n_occ + s] ) * K[0, j*n_virt + t] * K[1, j*n_virt + t] * K[2, j*n_virt + t + n_ex]

										elif ((t != s) and (u != s) and (u != t) and (v == s)):

											L4[i*n_virt + s] += (2 * g[i, n_occ + u, j, n_occ + t] + 2 * g[i, n_occ + t, j, n_occ + u] ) * K[0, j*n_virt + t] * K[1, j*n_virt + u] * K[2, j*n_virt + s + n_ex]

										elif ((t != s) and (u != s) and (u != t) and (v == t)):

											L4[i*n_virt + s] += (4 * g[i, n_occ + s, j, n_occ + u] + -2 * g[i, n_occ + u, j, n_occ + s] ) * K[0, j*n_virt + t] * K[1, j*n_virt + u] * K[2, j*n_virt + t + n_ex]

										elif ((t != s) and (u != s) and (u != t) and (v == u)):

											L4[i*n_virt + s] += (4 * g[i, n_occ + s, j, n_occ + t] + -2 * g[i, n_occ + t, j, n_occ + s] ) * K[0, j*n_virt + t] * K[1, j*n_virt + u] * K[2, j*n_virt + u + n_ex]

									elif ((j != i) and (k != i) and (k != j) and (m == i)):

										if ((t == s) and (u == s) and (v == s)):

											L4[i*n_virt + s] += (4 * g[j, n_occ + s, k, n_occ + s] ) * K[0, j*n_virt + s] * K[1, k*n_virt + s] * K[2, i*n_virt + s + n_ex]

										elif ((t == s) and (u != s) and (u != t) and (v == s)):

											L4[i*n_virt + s] += (4 * g[j, n_occ + s, k, n_occ + u] + -2 * g[j, n_occ + u, k, n_occ + s] ) * K[0, j*n_virt + s] * K[1, k*n_virt + u] * K[2, i*n_virt + s + n_ex]

										elif ((t == s) and (u != s) and (u != t) and (v == u)):

											L4[i*n_virt + s] += (2 * g[j, n_occ + s, k, n_occ + s] ) * K[0, j*n_virt + s] * K[1, k*n_virt + u] * K[2, i*n_virt + u + n_ex]

										elif ((t != s) and (u == s) and (v == s)):

											L4[i*n_virt + s] += (-2 * g[j, n_occ + s, k, n_occ + t] + 4 * g[j, n_occ + t, k, n_occ + s] ) * K[0, j*n_virt + t] * K[1, k*n_virt + s] * K[2, i*n_virt + s + n_ex]

										elif ((t != s) and (u == s) and (v == t)):

											L4[i*n_virt + s] += (2 * g[j, n_occ + s, k, n_occ + s] ) * K[0, j*n_virt + t] * K[1, k*n_virt + s] * K[2, i*n_virt + t + n_ex]

										elif ((t != s) and (u == t) and (v == t)):

											L4[i*n_virt + s] += (2 * g[j, n_occ + t, k, n_occ + s] + 2 * g[j, n_occ + s, k, n_occ + t] ) * K[0, j*n_virt + t] * K[1, k*n_virt + t] * K[2, i*n_virt + t + n_ex]

										elif ((t != s) and (u != s) and (u != t) and (v == t)):

											L4[i*n_virt + s] += (4 * g[j, n_occ + s, k, n_occ + u] + -2 * g[j, n_occ + u, k, n_occ + s] ) * K[0, j*n_virt + t] * K[1, k*n_virt + u] * K[2, i*n_virt + t + n_ex]

										elif ((t != s) and (u != s) and (u != t) and (v == u)):

											L4[i*n_virt + s] += (-2 * g[j, n_occ + s, k, n_occ + t] + 4 * g[j, n_occ + t, k, n_occ + s] ) * K[0, j*n_virt + t] * K[1, k*n_virt + u] * K[2, i*n_virt + u + n_ex]

									elif ((j != i) and (k != i) and (k != j) and (m == j)):

										if ((t == s) and (u == s) and (v == s)):

											L4[i*n_virt + s] += (4 * g[i, n_occ + s, k, n_occ + s] ) * K[0, j*n_virt + s] * K[1, k*n_virt + s] * K[2, j*n_virt + s + n_ex]

										elif ((t == s) and (u != s) and (u != t) and (v == s)):

											L4[i*n_virt + s] += (4 * g[i, n_occ + s, k, n_occ + u] + -2 * g[i, n_occ + u, k, n_occ + s] ) * K[0, j*n_virt + s] * K[1, k*n_virt + u] * K[2, j*n_virt + s + n_ex]

										elif ((t == s) and (u != s) and (u != t) and (v == u)):

											L4[i*n_virt + s] += (2 * g[i, n_occ + s, k, n_occ + s] ) * K[0, j*n_virt + s] * K[1, k*n_virt + u] * K[2, j*n_virt + u + n_ex]

										elif ((t != s) and (u == s) and (v == s)):

											L4[i*n_virt + s] += (2 * g[i, n_occ + t, k, n_occ + s] + 2 * g[i, n_occ + s, k, n_occ + t] ) * K[0, j*n_virt + t] * K[1, k*n_virt + s] * K[2, j*n_virt + s + n_ex]

										elif ((t != s) and (u == t) and (v == s)):

											L4[i*n_virt + s] += (2 * g[i, n_occ + t, k, n_occ + t] ) * K[0, j*n_virt + t] * K[1, k*n_virt + t] * K[2, j*n_virt + s + n_ex]

										elif ((t != s) and (u == t) and (v == t)):

											L4[i*n_virt + s] += (4 * g[i, n_occ + s, k, n_occ + t] + -2 * g[i, n_occ + t, k, n_occ + s] ) * K[0, j*n_virt + t] * K[1, k*n_virt + t] * K[2, j*n_virt + t + n_ex]

										elif ((t != s) and (u != s) and (u != t) and (v == s)):

											L4[i*n_virt + s] += (4 * g[i, n_occ + t, k, n_occ + u] + -2 * g[i, n_occ + u, k, n_occ + t] ) * K[0, j*n_virt + t] * K[1, k*n_virt + u] * K[2, j*n_virt + s + n_ex]

										elif ((t != s) and (u != s) and (u != t) and (v == u)):

											L4[i*n_virt + s] += (4 * g[i, n_occ + s, k, n_occ + t] + -2 * g[i, n_occ + t, k, n_occ + s] ) * K[0, j*n_virt + t] * K[1, k*n_virt + u] * K[2, j*n_virt + u + n_ex]

									elif ((j != i) and (k != i) and (k != j) and (m == k)):

										if ((t == s) and (u == s) and (v == s)):

											L4[i*n_virt + s] += (4 * g[i, n_occ + s, j, n_occ + s] ) * K[0, j*n_virt + s] * K[1, k*n_virt + s] * K[2, k*n_virt + s + n_ex]

										elif ((t == s) and (u != s) and (u != t) and (v == s)):

											L4[i*n_virt + s] += (2 * g[i, n_occ + u, j, n_occ + s] + 2 * g[i, n_occ + s, j, n_occ + u] ) * K[0, j*n_virt + s] * K[1, k*n_virt + u] * K[2, k*n_virt + s + n_ex]

										elif ((t != s) and (u == s) and (v == s)):

											L4[i*n_virt + s] += (4 * g[i, n_occ + s, j, n_occ + t] + -2 * g[i, n_occ + t, j, n_occ + s] ) * K[0, j*n_virt + t] * K[1, k*n_virt + s] * K[2, k*n_virt + s + n_ex]

										elif ((t != s) and (u == s) and (v == t)):

											L4[i*n_virt + s] += (2 * g[i, n_occ + s, j, n_occ + s] ) * K[0, j*n_virt + t] * K[1, k*n_virt + s] * K[2, k*n_virt + t + n_ex]

										elif ((t != s) and (u == t) and (v == s)):

											L4[i*n_virt + s] += (2 * g[i, n_occ + t, j, n_occ + t] ) * K[0, j*n_virt + t] * K[1, k*n_virt + t] * K[2, k*n_virt + s + n_ex]

										elif ((t != s) and (u == t) and (v == t)):

											L4[i*n_virt + s] += (4 * g[i, n_occ + s, j, n_occ + t] + -2 * g[i, n_occ + t, j, n_occ + s] ) * K[0, j*n_virt + t] * K[1, k*n_virt + t] * K[2, k*n_virt + t + n_ex]

										elif ((t != s) and (u != s) and (u != t) and (v == s)):

											L4[i*n_virt + s] += (-2 * g[i, n_occ + t, j, n_occ + u] + 4 * g[i, n_occ + u, j, n_occ + t] ) * K[0, j*n_virt + t] * K[1, k*n_virt + u] * K[2, k*n_virt + s + n_ex]

										elif ((t != s) and (u != s) and (u != t) and (v == t)):

											L4[i*n_virt + s] += (4 * g[i, n_occ + s, j, n_occ + u] + -2 * g[i, n_occ + u, j, n_occ + s] ) * K[0, j*n_virt + t] * K[1, k*n_virt + u] * K[2, k*n_virt + t + n_ex]

	# Current operator combination: {'a': 2, 'b': 1, 'c': 1, 'd': 2}
	for i in range(n_occ):
		for j in range(n_occ):
			for k in range(n_occ):
				for m in range(n_occ):
					for s in range(n_virt):
						for t in range(n_virt):
							for u in range(n_virt):
								for v in range(n_virt):

									if ((j == i) and (k == i) and (m == i)):

										if ((t == s) and (u == s) and (v == s)):

											L4[i*n_virt + s + n_ex] += (4 * g[n_occ + s, n_occ + s, n_occ + s, n_occ + s] + -8 * g[i, i, n_occ + s, n_occ + s] + -8 * g[i, n_occ + s, i, n_occ + s] + 4 * g[i, i, i, i] ) * K[0, i*n_virt + s] * K[1, i*n_virt + s] * K[2, i*n_virt + s + n_ex]

										elif ((t == s) and (u == s) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s + n_ex] += (-4 * g[i, i, n_occ + s, n_occ + v] + -4 * g[i, n_occ + s, i, n_occ + v] + 4 * g[n_occ + s, n_occ + s, n_occ + s, n_occ + v] ) * K[0, i*n_virt + s] * K[1, i*n_virt + s] * K[2, i*n_virt + v + n_ex]

										elif ((t == s) and (u != s) and (u != t) and (v == s)):

											L4[i*n_virt + s + n_ex] += (4 * g[n_occ + s, n_occ + s, n_occ + s, n_occ + u] + -4 * g[i, i, n_occ + s, n_occ + u] + -4 * g[i, n_occ + s, i, n_occ + u] ) * K[0, i*n_virt + s] * K[1, i*n_virt + u] * K[2, i*n_virt + s + n_ex]

										elif ((t == s) and (u != s) and (u != t) and (v == u)):

											L4[i*n_virt + s + n_ex] += (-2 * g[i, i, n_occ + u, n_occ + u] + -2 * g[i, n_occ + u, i, n_occ + u] + 2 * g[n_occ + s, n_occ + s, n_occ + u, n_occ + u] + 2 * g[n_occ + s, n_occ + u, n_occ + s, n_occ + u] + -2 * g[i, n_occ + s, i, n_occ + s] + -2 * g[i, i, n_occ + s, n_occ + s] + 2 * g[i, i, i, i] ) * K[0, i*n_virt + s] * K[1, i*n_virt + u] * K[2, i*n_virt + u + n_ex]

										elif ((t == s) and (u != s) and (u != t) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s + n_ex] += (-2 * g[i, i, n_occ + u, n_occ + v] + -2 * g[i, n_occ + u, i, n_occ + v] + 2 * g[n_occ + s, n_occ + u, n_occ + s, n_occ + v] + 2 * g[n_occ + s, n_occ + s, n_occ + u, n_occ + v] ) * K[0, i*n_virt + s] * K[1, i*n_virt + u] * K[2, i*n_virt + v + n_ex]

										elif ((t != s) and (u == s) and (v == s)):

											L4[i*n_virt + s + n_ex] += (4 * g[n_occ + s, n_occ + s, n_occ + s, n_occ + t] + -4 * g[i, i, n_occ + s, n_occ + t] + -4 * g[i, n_occ + s, i, n_occ + t] ) * K[0, i*n_virt + t] * K[1, i*n_virt + s] * K[2, i*n_virt + s + n_ex]

										elif ((t != s) and (u == s) and (v == t)):

											L4[i*n_virt + s + n_ex] += (-2 * g[i, i, n_occ + t, n_occ + t] + -2 * g[i, n_occ + t, i, n_occ + t] + 2 * g[n_occ + s, n_occ + s, n_occ + t, n_occ + t] + 2 * g[n_occ + s, n_occ + t, n_occ + s, n_occ + t] + -2 * g[i, n_occ + s, i, n_occ + s] + -2 * g[i, i, n_occ + s, n_occ + s] + 2 * g[i, i, i, i] ) * K[0, i*n_virt + t] * K[1, i*n_virt + s] * K[2, i*n_virt + t + n_ex]

										elif ((t != s) and (u == s) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s + n_ex] += (-2 * g[i, n_occ + t, i, n_occ + v] + -2 * g[i, i, n_occ + t, n_occ + v] + 2 * g[n_occ + s, n_occ + s, n_occ + t, n_occ + v] + 2 * g[n_occ + s, n_occ + t, n_occ + s, n_occ + v] ) * K[0, i*n_virt + t] * K[1, i*n_virt + s] * K[2, i*n_virt + v + n_ex]

										elif ((t != s) and (u == t) and (v == s)):

											L4[i*n_virt + s + n_ex] += (4 * g[n_occ + s, n_occ + t, n_occ + s, n_occ + t] ) * K[0, i*n_virt + t] * K[1, i*n_virt + t] * K[2, i*n_virt + s + n_ex]

										elif ((t != s) and (u == t) and (v == t)):

											L4[i*n_virt + s + n_ex] += (4 * g[n_occ + s, n_occ + t, n_occ + t, n_occ + t] + -4 * g[i, i, n_occ + s, n_occ + t] + -4 * g[i, n_occ + s, i, n_occ + t] ) * K[0, i*n_virt + t] * K[1, i*n_virt + t] * K[2, i*n_virt + t + n_ex]

										elif ((t != s) and (u == t) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s + n_ex] += (4 * g[n_occ + s, n_occ + t, n_occ + t, n_occ + v] ) * K[0, i*n_virt + t] * K[1, i*n_virt + t] * K[2, i*n_virt + v + n_ex]

										elif ((t != s) and (u != s) and (u != t) and (v == s)):

											L4[i*n_virt + s + n_ex] += (4 * g[n_occ + s, n_occ + t, n_occ + s, n_occ + u] ) * K[0, i*n_virt + t] * K[1, i*n_virt + u] * K[2, i*n_virt + s + n_ex]

										elif ((t != s) and (u != s) and (u != t) and (v == t)):

											L4[i*n_virt + s + n_ex] += (2 * g[n_occ + s, n_occ + u, n_occ + t, n_occ + t] + 2 * g[n_occ + s, n_occ + t, n_occ + t, n_occ + u] + -2 * g[i, n_occ + s, i, n_occ + u] + -2 * g[i, i, n_occ + s, n_occ + u] ) * K[0, i*n_virt + t] * K[1, i*n_virt + u] * K[2, i*n_virt + t + n_ex]

										elif ((t != s) and (u != s) and (u != t) and (v == u)):

											L4[i*n_virt + s + n_ex] += (2 * g[n_occ + s, n_occ + u, n_occ + t, n_occ + u] + 2 * g[n_occ + s, n_occ + t, n_occ + u, n_occ + u] + -2 * g[i, n_occ + s, i, n_occ + t] + -2 * g[i, i, n_occ + s, n_occ + t] ) * K[0, i*n_virt + t] * K[1, i*n_virt + u] * K[2, i*n_virt + u + n_ex]

										elif ((t != s) and (u != s) and (u != t) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s + n_ex] += (2 * g[n_occ + s, n_occ + u, n_occ + t, n_occ + v] + 2 * g[n_occ + s, n_occ + t, n_occ + u, n_occ + v] ) * K[0, i*n_virt + t] * K[1, i*n_virt + u] * K[2, i*n_virt + v + n_ex]

									elif ((j == i) and (k == i) and (m != i) and (m != j) and (m != k)):

										if ((t == s) and (u == s) and (v == s)):

											L4[i*n_virt + s + n_ex] += (-4 * g[i, n_occ + s, m, n_occ + s] + 4 * g[i, i, i, m] + -4 * g[i, m, n_occ + s, n_occ + s] ) * K[0, i*n_virt + s] * K[1, i*n_virt + s] * K[2, m*n_virt + s + n_ex]

										elif ((t == s) and (u == s) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s + n_ex] += (4 * g[i, m, n_occ + s, n_occ + v] + -8 * g[i, n_occ + s, m, n_occ + v] ) * K[0, i*n_virt + s] * K[1, i*n_virt + s] * K[2, m*n_virt + v + n_ex]

										elif ((t == s) and (u != s) and (u != t) and (v == s)):

											L4[i*n_virt + s + n_ex] += (-2 * g[i, n_occ + u, m, n_occ + s] + -2 * g[i, m, n_occ + s, n_occ + u] ) * K[0, i*n_virt + s] * K[1, i*n_virt + u] * K[2, m*n_virt + s + n_ex]

										elif ((t == s) and (u != s) and (u != t) and (v == u)):

											L4[i*n_virt + s + n_ex] += (2 * g[i, n_occ + s, m, n_occ + s] + -4 * g[i, m, n_occ + s, n_occ + s] + -4 * g[i, n_occ + u, m, n_occ + u] + 2 * g[i, m, n_occ + u, n_occ + u] + 2 * g[i, i, i, m] ) * K[0, i*n_virt + s] * K[1, i*n_virt + u] * K[2, m*n_virt + u + n_ex]

										elif ((t == s) and (u != s) and (u != t) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s + n_ex] += (2 * g[i, m, n_occ + u, n_occ + v] + -4 * g[i, n_occ + u, m, n_occ + v] ) * K[0, i*n_virt + s] * K[1, i*n_virt + u] * K[2, m*n_virt + v + n_ex]

										elif ((t != s) and (u == s) and (v == s)):

											L4[i*n_virt + s + n_ex] += (-2 * g[i, n_occ + t, m, n_occ + s] + -2 * g[i, m, n_occ + s, n_occ + t] ) * K[0, i*n_virt + t] * K[1, i*n_virt + s] * K[2, m*n_virt + s + n_ex]

										elif ((t != s) and (u == s) and (v == t)):

											L4[i*n_virt + s + n_ex] += (2 * g[i, n_occ + s, m, n_occ + s] + -4 * g[i, m, n_occ + s, n_occ + s] + -4 * g[i, n_occ + t, m, n_occ + t] + 2 * g[i, m, n_occ + t, n_occ + t] + 2 * g[i, i, i, m] ) * K[0, i*n_virt + t] * K[1, i*n_virt + s] * K[2, m*n_virt + t + n_ex]

										elif ((t != s) and (u == s) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s + n_ex] += (2 * g[i, m, n_occ + t, n_occ + v] + -4 * g[i, n_occ + t, m, n_occ + v] ) * K[0, i*n_virt + t] * K[1, i*n_virt + s] * K[2, m*n_virt + v + n_ex]

										elif ((t != s) and (u == t) and (v == t)):

											L4[i*n_virt + s + n_ex] += (-8 * g[i, m, n_occ + s, n_occ + t] + 4 * g[i, n_occ + t, m, n_occ + s] ) * K[0, i*n_virt + t] * K[1, i*n_virt + t] * K[2, m*n_virt + t + n_ex]

										elif ((t != s) and (u != s) and (u != t) and (v == t)):

											L4[i*n_virt + s + n_ex] += (-4 * g[i, m, n_occ + s, n_occ + u] + 2 * g[i, n_occ + u, m, n_occ + s] ) * K[0, i*n_virt + t] * K[1, i*n_virt + u] * K[2, m*n_virt + t + n_ex]

										elif ((t != s) and (u != s) and (u != t) and (v == u)):

											L4[i*n_virt + s + n_ex] += (-4 * g[i, m, n_occ + s, n_occ + t] + 2 * g[i, n_occ + t, m, n_occ + s] ) * K[0, i*n_virt + t] * K[1, i*n_virt + u] * K[2, m*n_virt + u + n_ex]

									elif ((j == i) and (k != i) and (k != j) and (m == i)):

										if ((t == s) and (u == s) and (v == s)):

											L4[i*n_virt + s + n_ex] += (-4 * g[i, k, n_occ + s, n_occ + s] + 4 * g[i, i, i, k] + -4 * g[i, n_occ + s, k, n_occ + s] ) * K[0, i*n_virt + s] * K[1, k*n_virt + s] * K[2, i*n_virt + s + n_ex]

										elif ((t == s) and (u == s) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s + n_ex] += (-2 * g[i, n_occ + v, k, n_occ + s] + -2 * g[i, k, n_occ + s, n_occ + v] ) * K[0, i*n_virt + s] * K[1, k*n_virt + s] * K[2, i*n_virt + v + n_ex]

										elif ((t == s) and (u != s) and (u != t) and (v == u)):

											L4[i*n_virt + s + n_ex] += (2 * g[i, i, i, k] + -2 * g[i, k, n_occ + s, n_occ + s] + -2 * g[i, n_occ + s, k, n_occ + s] ) * K[0, i*n_virt + s] * K[1, k*n_virt + u] * K[2, i*n_virt + u + n_ex]

										elif ((t != s) and (u == s) and (v == s)):

											L4[i*n_virt + s + n_ex] += (-4 * g[i, n_occ + s, k, n_occ + t] + -4 * g[i, k, n_occ + s, n_occ + t] ) * K[0, i*n_virt + t] * K[1, k*n_virt + s] * K[2, i*n_virt + s + n_ex]

										elif ((t != s) and (u == s) and (v == t)):

											L4[i*n_virt + s + n_ex] += (-2 * g[i, n_occ + t, k, n_occ + t] + -2 * g[i, k, n_occ + t, n_occ + t] + 2 * g[i, i, i, k] ) * K[0, i*n_virt + t] * K[1, k*n_virt + s] * K[2, i*n_virt + t + n_ex]

										elif ((t != s) and (u == s) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s + n_ex] += (-2 * g[i, n_occ + v, k, n_occ + t] + -2 * g[i, k, n_occ + t, n_occ + v] ) * K[0, i*n_virt + t] * K[1, k*n_virt + s] * K[2, i*n_virt + v + n_ex]

										elif ((t != s) and (u == t) and (v == t)):

											L4[i*n_virt + s + n_ex] += (-2 * g[i, k, n_occ + s, n_occ + t] + -2 * g[i, n_occ + s, k, n_occ + t] ) * K[0, i*n_virt + t] * K[1, k*n_virt + t] * K[2, i*n_virt + t + n_ex]

										elif ((t != s) and (u != s) and (u != t) and (v == u)):

											L4[i*n_virt + s + n_ex] += (-2 * g[i, k, n_occ + s, n_occ + t] + -2 * g[i, n_occ + s, k, n_occ + t] ) * K[0, i*n_virt + t] * K[1, k*n_virt + u] * K[2, i*n_virt + u + n_ex]

									elif ((j == i) and (k != i) and (k != j) and (m == k)):

										if ((t == s) and (u == s) and (v == s)):

											L4[i*n_virt + s + n_ex] += (-2 * g[k, n_occ + s, k, n_occ + s] + 2 * g[i, k, i, k] + 2 * g[n_occ + s, n_occ + s, n_occ + s, n_occ + s] + -2 * g[i, n_occ + s, i, n_occ + s] + -2 * g[i, i, n_occ + s, n_occ + s] + -2 * g[k, k, n_occ + s, n_occ + s] + 2 * g[i, i, k, k] ) * K[0, i*n_virt + s] * K[1, k*n_virt + s] * K[2, k*n_virt + s + n_ex]

										elif ((t == s) and (u == s) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s + n_ex] += (-4 * g[k, n_occ + s, k, n_occ + v] + 2 * g[i, n_occ + s, i, n_occ + v] + -4 * g[i, i, n_occ + s, n_occ + v] + 2 * g[k, k, n_occ + s, n_occ + v] + 2 * g[n_occ + s, n_occ + s, n_occ + s, n_occ + v] ) * K[0, i*n_virt + s] * K[1, k*n_virt + s] * K[2, k*n_virt + v + n_ex]

										elif ((t == s) and (u != s) and (u != t) and (v == s)):

											L4[i*n_virt + s + n_ex] += (-2 * g[i, i, n_occ + s, n_occ + u] + 2 * g[n_occ + s, n_occ + s, n_occ + s, n_occ + u] + -2 * g[i, n_occ + s, i, n_occ + u] ) * K[0, i*n_virt + s] * K[1, k*n_virt + u] * K[2, k*n_virt + s + n_ex]

										elif ((t == s) and (u != s) and (u != t) and (v == u)):

											L4[i*n_virt + s + n_ex] += (2 * g[i, n_occ + u, i, n_occ + u] + -4 * g[i, i, n_occ + u, n_occ + u] + -2 * g[n_occ + s, n_occ + u, n_occ + s, n_occ + u] + 4 * g[n_occ + s, n_occ + s, n_occ + u, n_occ + u] + -4 * g[k, k, n_occ + s, n_occ + s] + 2 * g[k, n_occ + s, k, n_occ + s] + -2 * g[i, k, i, k] + 4 * g[i, i, k, k] ) * K[0, i*n_virt + s] * K[1, k*n_virt + u] * K[2, k*n_virt + u + n_ex]

										elif ((t == s) and (u != s) and (u != t) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s + n_ex] += (2 * g[i, n_occ + u, i, n_occ + v] + -4 * g[i, i, n_occ + u, n_occ + v] + -2 * g[n_occ + s, n_occ + u, n_occ + s, n_occ + v] + 4 * g[n_occ + s, n_occ + s, n_occ + u, n_occ + v] ) * K[0, i*n_virt + s] * K[1, k*n_virt + u] * K[2, k*n_virt + v + n_ex]

										elif ((t != s) and (u == s) and (v == s)):

											L4[i*n_virt + s + n_ex] += (-2 * g[k, n_occ + s, k, n_occ + t] + 2 * g[n_occ + s, n_occ + s, n_occ + s, n_occ + t] + -2 * g[k, k, n_occ + s, n_occ + t] ) * K[0, i*n_virt + t] * K[1, k*n_virt + s] * K[2, k*n_virt + s + n_ex]

										elif ((t != s) and (u == s) and (v == t)):

											L4[i*n_virt + s + n_ex] += (2 * g[i, i, n_occ + s, n_occ + s] + -4 * g[i, n_occ + s, i, n_occ + s] + 4 * g[i, k, i, k] + -2 * g[i, i, k, k] + 2 * g[k, k, n_occ + t, n_occ + t] + -4 * g[k, n_occ + t, k, n_occ + t] + 4 * g[n_occ + s, n_occ + t, n_occ + s, n_occ + t] + -2 * g[n_occ + s, n_occ + s, n_occ + t, n_occ + t] ) * K[0, i*n_virt + t] * K[1, k*n_virt + s] * K[2, k*n_virt + t + n_ex]

										elif ((t != s) and (u == s) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s + n_ex] += (-4 * g[k, n_occ + t, k, n_occ + v] + 2 * g[k, k, n_occ + t, n_occ + v] + 4 * g[n_occ + s, n_occ + t, n_occ + s, n_occ + v] + -2 * g[n_occ + s, n_occ + s, n_occ + t, n_occ + v] ) * K[0, i*n_virt + t] * K[1, k*n_virt + s] * K[2, k*n_virt + v + n_ex]

										elif ((t != s) and (u == t) and (v == s)):

											L4[i*n_virt + s + n_ex] += (2 * g[n_occ + s, n_occ + t, n_occ + s, n_occ + t] ) * K[0, i*n_virt + t] * K[1, k*n_virt + t] * K[2, k*n_virt + s + n_ex]

										elif ((t != s) and (u == t) and (v == t)):

											L4[i*n_virt + s + n_ex] += (2 * g[i, i, n_occ + s, n_occ + t] + 2 * g[n_occ + s, n_occ + t, n_occ + t, n_occ + t] + -4 * g[i, n_occ + s, i, n_occ + t] + 2 * g[k, n_occ + s, k, n_occ + t] + -4 * g[k, k, n_occ + s, n_occ + t] ) * K[0, i*n_virt + t] * K[1, k*n_virt + t] * K[2, k*n_virt + t + n_ex]

										elif ((t != s) and (u == t) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s + n_ex] += (2 * g[n_occ + s, n_occ + t, n_occ + t, n_occ + v] ) * K[0, i*n_virt + t] * K[1, k*n_virt + t] * K[2, k*n_virt + v + n_ex]

										elif ((t != s) and (u != s) and (u != t) and (v == s)):

											L4[i*n_virt + s + n_ex] += (2 * g[n_occ + s, n_occ + t, n_occ + s, n_occ + u] ) * K[0, i*n_virt + t] * K[1, k*n_virt + u] * K[2, k*n_virt + s + n_ex]

										elif ((t != s) and (u != s) and (u != t) and (v == t)):

											L4[i*n_virt + s + n_ex] += (-4 * g[i, n_occ + s, i, n_occ + u] + 2 * g[i, i, n_occ + s, n_occ + u] + 4 * g[n_occ + s, n_occ + t, n_occ + t, n_occ + u] + -2 * g[n_occ + s, n_occ + u, n_occ + t, n_occ + t] ) * K[0, i*n_virt + t] * K[1, k*n_virt + u] * K[2, k*n_virt + t + n_ex]

										elif ((t != s) and (u != s) and (u != t) and (v == u)):

											L4[i*n_virt + s + n_ex] += (-2 * g[n_occ + s, n_occ + u, n_occ + t, n_occ + u] + 4 * g[n_occ + s, n_occ + t, n_occ + u, n_occ + u] + 2 * g[k, n_occ + s, k, n_occ + t] + -4 * g[k, k, n_occ + s, n_occ + t] ) * K[0, i*n_virt + t] * K[1, k*n_virt + u] * K[2, k*n_virt + u + n_ex]

										elif ((t != s) and (u != s) and (u != t) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s + n_ex] += (4 * g[n_occ + s, n_occ + t, n_occ + u, n_occ + v] + -2 * g[n_occ + s, n_occ + u, n_occ + t, n_occ + v] ) * K[0, i*n_virt + t] * K[1, k*n_virt + u] * K[2, k*n_virt + v + n_ex]

									elif ((j == i) and (k != i) and (k != j) and (m != i) and (m != j) and (m != k)):

										if ((t == s) and (u == s) and (v == s)):

											L4[i*n_virt + s + n_ex] += (-2 * g[k, n_occ + s, m, n_occ + s] + 2 * g[i, i, k, m] + 2 * g[i, k, i, m] + -2 * g[k, m, n_occ + s, n_occ + s] ) * K[0, i*n_virt + s] * K[1, k*n_virt + s] * K[2, m*n_virt + s + n_ex]

										elif ((t == s) and (u == s) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s + n_ex] += (2 * g[k, m, n_occ + s, n_occ + v] + -4 * g[k, n_occ + s, m, n_occ + v] ) * K[0, i*n_virt + s] * K[1, k*n_virt + s] * K[2, m*n_virt + v + n_ex]

										elif ((t == s) and (u != s) and (u != t) and (v == u)):

											L4[i*n_virt + s + n_ex] += (-2 * g[i, k, i, m] + 4 * g[i, i, k, m] + 2 * g[k, n_occ + s, m, n_occ + s] + -4 * g[k, m, n_occ + s, n_occ + s] ) * K[0, i*n_virt + s] * K[1, k*n_virt + u] * K[2, m*n_virt + u + n_ex]

										elif ((t != s) and (u == s) and (v == s)):

											L4[i*n_virt + s + n_ex] += (-2 * g[k, n_occ + t, m, n_occ + s] + -2 * g[k, m, n_occ + s, n_occ + t] ) * K[0, i*n_virt + t] * K[1, k*n_virt + s] * K[2, m*n_virt + s + n_ex]

										elif ((t != s) and (u == s) and (v == t)):

											L4[i*n_virt + s + n_ex] += (4 * g[i, k, i, m] + -2 * g[i, i, k, m] + -4 * g[k, n_occ + t, m, n_occ + t] + 2 * g[k, m, n_occ + t, n_occ + t] ) * K[0, i*n_virt + t] * K[1, k*n_virt + s] * K[2, m*n_virt + t + n_ex]

										elif ((t != s) and (u == s) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s + n_ex] += (2 * g[k, m, n_occ + t, n_occ + v] + -4 * g[k, n_occ + t, m, n_occ + v] ) * K[0, i*n_virt + t] * K[1, k*n_virt + s] * K[2, m*n_virt + v + n_ex]

										elif ((t != s) and (u == t) and (v == t)):

											L4[i*n_virt + s + n_ex] += (-4 * g[k, m, n_occ + s, n_occ + t] + 2 * g[k, n_occ + t, m, n_occ + s] ) * K[0, i*n_virt + t] * K[1, k*n_virt + t] * K[2, m*n_virt + t + n_ex]

										elif ((t != s) and (u != s) and (u != t) and (v == u)):

											L4[i*n_virt + s + n_ex] += (-4 * g[k, m, n_occ + s, n_occ + t] + 2 * g[k, n_occ + t, m, n_occ + s] ) * K[0, i*n_virt + t] * K[1, k*n_virt + u] * K[2, m*n_virt + u + n_ex]

									elif ((j != i) and (k == i) and (m == i)):

										if ((t == s) and (u == s) and (v == s)):

											L4[i*n_virt + s + n_ex] += (-4 * g[i, j, n_occ + s, n_occ + s] + 4 * g[i, i, i, j] + -4 * g[i, n_occ + s, j, n_occ + s] ) * K[0, j*n_virt + s] * K[1, i*n_virt + s] * K[2, i*n_virt + s + n_ex]

										elif ((t == s) and (u == s) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s + n_ex] += (-2 * g[i, n_occ + v, j, n_occ + s] + -2 * g[i, j, n_occ + s, n_occ + v] ) * K[0, j*n_virt + s] * K[1, i*n_virt + s] * K[2, i*n_virt + v + n_ex]

										elif ((t == s) and (u != s) and (u != t) and (v == s)):

											L4[i*n_virt + s + n_ex] += (-4 * g[i, n_occ + s, j, n_occ + u] + -4 * g[i, j, n_occ + s, n_occ + u] ) * K[0, j*n_virt + s] * K[1, i*n_virt + u] * K[2, i*n_virt + s + n_ex]

										elif ((t == s) and (u != s) and (u != t) and (v == u)):

											L4[i*n_virt + s + n_ex] += (-2 * g[i, n_occ + u, j, n_occ + u] + -2 * g[i, j, n_occ + u, n_occ + u] + 2 * g[i, i, i, j] ) * K[0, j*n_virt + s] * K[1, i*n_virt + u] * K[2, i*n_virt + u + n_ex]

										elif ((t == s) and (u != s) and (u != t) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s + n_ex] += (-2 * g[i, n_occ + v, j, n_occ + u] + -2 * g[i, j, n_occ + u, n_occ + v] ) * K[0, j*n_virt + s] * K[1, i*n_virt + u] * K[2, i*n_virt + v + n_ex]

										elif ((t != s) and (u == s) and (v == t)):

											L4[i*n_virt + s + n_ex] += (2 * g[i, i, i, j] + -2 * g[i, j, n_occ + s, n_occ + s] + -2 * g[i, n_occ + s, j, n_occ + s] ) * K[0, j*n_virt + t] * K[1, i*n_virt + s] * K[2, i*n_virt + t + n_ex]

										elif ((t != s) and (u == t) and (v == t)):

											L4[i*n_virt + s + n_ex] += (-2 * g[i, j, n_occ + s, n_occ + t] + -2 * g[i, n_occ + s, j, n_occ + t] ) * K[0, j*n_virt + t] * K[1, i*n_virt + t] * K[2, i*n_virt + t + n_ex]

										elif ((t != s) and (u != s) and (u != t) and (v == t)):

											L4[i*n_virt + s + n_ex] += (-2 * g[i, j, n_occ + s, n_occ + u] + -2 * g[i, n_occ + s, j, n_occ + u] ) * K[0, j*n_virt + t] * K[1, i*n_virt + u] * K[2, i*n_virt + t + n_ex]

									elif ((j != i) and (k == i) and (m == j)):

										if ((t == s) and (u == s) and (v == s)):

											L4[i*n_virt + s + n_ex] += (-2 * g[j, n_occ + s, j, n_occ + s] + 2 * g[i, j, i, j] + 2 * g[n_occ + s, n_occ + s, n_occ + s, n_occ + s] + -2 * g[i, n_occ + s, i, n_occ + s] + -2 * g[i, i, n_occ + s, n_occ + s] + -2 * g[j, j, n_occ + s, n_occ + s] + 2 * g[i, i, j, j] ) * K[0, j*n_virt + s] * K[1, i*n_virt + s] * K[2, j*n_virt + s + n_ex]

										elif ((t == s) and (u == s) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s + n_ex] += (2 * g[i, n_occ + s, i, n_occ + v] + -4 * g[j, n_occ + s, j, n_occ + v] + -4 * g[i, i, n_occ + s, n_occ + v] + 2 * g[j, j, n_occ + s, n_occ + v] + 2 * g[n_occ + s, n_occ + s, n_occ + s, n_occ + v] ) * K[0, j*n_virt + s] * K[1, i*n_virt + s] * K[2, j*n_virt + v + n_ex]

										elif ((t == s) and (u != s) and (u != t) and (v == s)):

											L4[i*n_virt + s + n_ex] += (-2 * g[j, n_occ + s, j, n_occ + u] + 2 * g[n_occ + s, n_occ + s, n_occ + s, n_occ + u] + -2 * g[j, j, n_occ + s, n_occ + u] ) * K[0, j*n_virt + s] * K[1, i*n_virt + u] * K[2, j*n_virt + s + n_ex]

										elif ((t == s) and (u != s) and (u != t) and (v == u)):

											L4[i*n_virt + s + n_ex] += (2 * g[j, j, n_occ + u, n_occ + u] + -4 * g[j, n_occ + u, j, n_occ + u] + 4 * g[i, j, i, j] + -2 * g[i, i, j, j] + 2 * g[i, i, n_occ + s, n_occ + s] + -4 * g[i, n_occ + s, i, n_occ + s] + 4 * g[n_occ + s, n_occ + u, n_occ + s, n_occ + u] + -2 * g[n_occ + s, n_occ + s, n_occ + u, n_occ + u] ) * K[0, j*n_virt + s] * K[1, i*n_virt + u] * K[2, j*n_virt + u + n_ex]

										elif ((t == s) and (u != s) and (u != t) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s + n_ex] += (-4 * g[j, n_occ + u, j, n_occ + v] + 2 * g[j, j, n_occ + u, n_occ + v] + 4 * g[n_occ + s, n_occ + u, n_occ + s, n_occ + v] + -2 * g[n_occ + s, n_occ + s, n_occ + u, n_occ + v] ) * K[0, j*n_virt + s] * K[1, i*n_virt + u] * K[2, j*n_virt + v + n_ex]

										elif ((t != s) and (u == s) and (v == s)):

											L4[i*n_virt + s + n_ex] += (-2 * g[i, i, n_occ + s, n_occ + t] + 2 * g[n_occ + s, n_occ + s, n_occ + s, n_occ + t] + -2 * g[i, n_occ + s, i, n_occ + t] ) * K[0, j*n_virt + t] * K[1, i*n_virt + s] * K[2, j*n_virt + s + n_ex]

										elif ((t != s) and (u == s) and (v == t)):

											L4[i*n_virt + s + n_ex] += (-4 * g[i, i, n_occ + t, n_occ + t] + 2 * g[i, n_occ + t, i, n_occ + t] + -2 * g[n_occ + s, n_occ + t, n_occ + s, n_occ + t] + 4 * g[n_occ + s, n_occ + s, n_occ + t, n_occ + t] + -4 * g[j, j, n_occ + s, n_occ + s] + 2 * g[j, n_occ + s, j, n_occ + s] + -2 * g[i, j, i, j] + 4 * g[i, i, j, j] ) * K[0, j*n_virt + t] * K[1, i*n_virt + s] * K[2, j*n_virt + t + n_ex]

										elif ((t != s) and (u == s) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s + n_ex] += (2 * g[i, n_occ + t, i, n_occ + v] + -4 * g[i, i, n_occ + t, n_occ + v] + -2 * g[n_occ + s, n_occ + t, n_occ + s, n_occ + v] + 4 * g[n_occ + s, n_occ + s, n_occ + t, n_occ + v] ) * K[0, j*n_virt + t] * K[1, i*n_virt + s] * K[2, j*n_virt + v + n_ex]

										elif ((t != s) and (u == t) and (v == s)):

											L4[i*n_virt + s + n_ex] += (2 * g[n_occ + s, n_occ + t, n_occ + s, n_occ + t] ) * K[0, j*n_virt + t] * K[1, i*n_virt + t] * K[2, j*n_virt + s + n_ex]

										elif ((t != s) and (u == t) and (v == t)):

											L4[i*n_virt + s + n_ex] += (2 * g[i, i, n_occ + s, n_occ + t] + 2 * g[n_occ + s, n_occ + t, n_occ + t, n_occ + t] + -4 * g[i, n_occ + s, i, n_occ + t] + 2 * g[j, n_occ + s, j, n_occ + t] + -4 * g[j, j, n_occ + s, n_occ + t] ) * K[0, j*n_virt + t] * K[1, i*n_virt + t] * K[2, j*n_virt + t + n_ex]

										elif ((t != s) and (u == t) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s + n_ex] += (2 * g[n_occ + s, n_occ + t, n_occ + t, n_occ + v] ) * K[0, j*n_virt + t] * K[1, i*n_virt + t] * K[2, j*n_virt + v + n_ex]

										elif ((t != s) and (u != s) and (u != t) and (v == s)):

											L4[i*n_virt + s + n_ex] += (2 * g[n_occ + s, n_occ + t, n_occ + s, n_occ + u] ) * K[0, j*n_virt + t] * K[1, i*n_virt + u] * K[2, j*n_virt + s + n_ex]

										elif ((t != s) and (u != s) and (u != t) and (v == t)):

											L4[i*n_virt + s + n_ex] += (-2 * g[n_occ + s, n_occ + t, n_occ + t, n_occ + u] + 4 * g[n_occ + s, n_occ + u, n_occ + t, n_occ + t] + 2 * g[j, n_occ + s, j, n_occ + u] + -4 * g[j, j, n_occ + s, n_occ + u] ) * K[0, j*n_virt + t] * K[1, i*n_virt + u] * K[2, j*n_virt + t + n_ex]

										elif ((t != s) and (u != s) and (u != t) and (v == u)):

											L4[i*n_virt + s + n_ex] += (-4 * g[i, n_occ + s, i, n_occ + t] + 2 * g[i, i, n_occ + s, n_occ + t] + 4 * g[n_occ + s, n_occ + u, n_occ + t, n_occ + u] + -2 * g[n_occ + s, n_occ + t, n_occ + u, n_occ + u] ) * K[0, j*n_virt + t] * K[1, i*n_virt + u] * K[2, j*n_virt + u + n_ex]

										elif ((t != s) and (u != s) and (u != t) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s + n_ex] += (-2 * g[n_occ + s, n_occ + t, n_occ + u, n_occ + v] + 4 * g[n_occ + s, n_occ + u, n_occ + t, n_occ + v] ) * K[0, j*n_virt + t] * K[1, i*n_virt + u] * K[2, j*n_virt + v + n_ex]

									elif ((j != i) and (k == i) and (m != i) and (m != j) and (m != k)):

										if ((t == s) and (u == s) and (v == s)):

											L4[i*n_virt + s + n_ex] += (-2 * g[j, n_occ + s, m, n_occ + s] + 2 * g[i, i, j, m] + 2 * g[i, j, i, m] + -2 * g[j, m, n_occ + s, n_occ + s] ) * K[0, j*n_virt + s] * K[1, i*n_virt + s] * K[2, m*n_virt + s + n_ex]

										elif ((t == s) and (u == s) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s + n_ex] += (2 * g[j, m, n_occ + s, n_occ + v] + -4 * g[j, n_occ + s, m, n_occ + v] ) * K[0, j*n_virt + s] * K[1, i*n_virt + s] * K[2, m*n_virt + v + n_ex]

										elif ((t == s) and (u != s) and (u != t) and (v == s)):

											L4[i*n_virt + s + n_ex] += (-2 * g[j, n_occ + u, m, n_occ + s] + -2 * g[j, m, n_occ + s, n_occ + u] ) * K[0, j*n_virt + s] * K[1, i*n_virt + u] * K[2, m*n_virt + s + n_ex]

										elif ((t == s) and (u != s) and (u != t) and (v == u)):

											L4[i*n_virt + s + n_ex] += (4 * g[i, j, i, m] + -2 * g[i, i, j, m] + -4 * g[j, n_occ + u, m, n_occ + u] + 2 * g[j, m, n_occ + u, n_occ + u] ) * K[0, j*n_virt + s] * K[1, i*n_virt + u] * K[2, m*n_virt + u + n_ex]

										elif ((t == s) and (u != s) and (u != t) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s + n_ex] += (2 * g[j, m, n_occ + u, n_occ + v] + -4 * g[j, n_occ + u, m, n_occ + v] ) * K[0, j*n_virt + s] * K[1, i*n_virt + u] * K[2, m*n_virt + v + n_ex]

										elif ((t != s) and (u == s) and (v == t)):

											L4[i*n_virt + s + n_ex] += (-2 * g[i, j, i, m] + 4 * g[i, i, j, m] + 2 * g[j, n_occ + s, m, n_occ + s] + -4 * g[j, m, n_occ + s, n_occ + s] ) * K[0, j*n_virt + t] * K[1, i*n_virt + s] * K[2, m*n_virt + t + n_ex]

										elif ((t != s) and (u == t) and (v == t)):

											L4[i*n_virt + s + n_ex] += (-4 * g[j, m, n_occ + s, n_occ + t] + 2 * g[j, n_occ + t, m, n_occ + s] ) * K[0, j*n_virt + t] * K[1, i*n_virt + t] * K[2, m*n_virt + t + n_ex]

										elif ((t != s) and (u != s) and (u != t) and (v == t)):

											L4[i*n_virt + s + n_ex] += (-4 * g[j, m, n_occ + s, n_occ + u] + 2 * g[j, n_occ + u, m, n_occ + s] ) * K[0, j*n_virt + t] * K[1, i*n_virt + u] * K[2, m*n_virt + t + n_ex]

									elif ((j != i) and (k == j) and (m == i)):

										if ((t == s) and (u == s) and (v == s)):

											L4[i*n_virt + s + n_ex] += (4 * g[i, j, i, j] ) * K[0, j*n_virt + s] * K[1, j*n_virt + s] * K[2, i*n_virt + s + n_ex]

										elif ((t == s) and (u != s) and (u != t) and (v == u)):

											L4[i*n_virt + s + n_ex] += (2 * g[i, j, i, j] ) * K[0, j*n_virt + s] * K[1, j*n_virt + u] * K[2, i*n_virt + u + n_ex]

										elif ((t != s) and (u == s) and (v == t)):

											L4[i*n_virt + s + n_ex] += (2 * g[i, j, i, j] ) * K[0, j*n_virt + t] * K[1, j*n_virt + s] * K[2, i*n_virt + t + n_ex]

									elif ((j != i) and (k == j) and (m == j)):

										if ((t == s) and (u == s) and (v == s)):

											L4[i*n_virt + s + n_ex] += (-4 * g[i, j, n_occ + s, n_occ + s] + 4 * g[i, j, j, j] + -4 * g[i, n_occ + s, j, n_occ + s] ) * K[0, j*n_virt + s] * K[1, j*n_virt + s] * K[2, j*n_virt + s + n_ex]

										elif ((t == s) and (u == s) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s + n_ex] += (-8 * g[i, j, n_occ + s, n_occ + v] + 4 * g[i, n_occ + v, j, n_occ + s] ) * K[0, j*n_virt + s] * K[1, j*n_virt + s] * K[2, j*n_virt + v + n_ex]

										elif ((t == s) and (u != s) and (u != t) and (v == s)):

											L4[i*n_virt + s + n_ex] += (-2 * g[i, j, n_occ + s, n_occ + u] + -2 * g[i, n_occ + s, j, n_occ + u] ) * K[0, j*n_virt + s] * K[1, j*n_virt + u] * K[2, j*n_virt + s + n_ex]

										elif ((t == s) and (u != s) and (u != t) and (v == u)):

											L4[i*n_virt + s + n_ex] += (2 * g[i, n_occ + u, j, n_occ + u] + -4 * g[i, j, n_occ + u, n_occ + u] + -4 * g[i, n_occ + s, j, n_occ + s] + 2 * g[i, j, j, j] + 2 * g[i, j, n_occ + s, n_occ + s] ) * K[0, j*n_virt + s] * K[1, j*n_virt + u] * K[2, j*n_virt + u + n_ex]

										elif ((t == s) and (u != s) and (u != t) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s + n_ex] += (-4 * g[i, j, n_occ + u, n_occ + v] + 2 * g[i, n_occ + v, j, n_occ + u] ) * K[0, j*n_virt + s] * K[1, j*n_virt + u] * K[2, j*n_virt + v + n_ex]

										elif ((t != s) and (u == s) and (v == s)):

											L4[i*n_virt + s + n_ex] += (-2 * g[i, j, n_occ + s, n_occ + t] + -2 * g[i, n_occ + s, j, n_occ + t] ) * K[0, j*n_virt + t] * K[1, j*n_virt + s] * K[2, j*n_virt + s + n_ex]

										elif ((t != s) and (u == s) and (v == t)):

											L4[i*n_virt + s + n_ex] += (2 * g[i, n_occ + t, j, n_occ + t] + -4 * g[i, j, n_occ + t, n_occ + t] + -4 * g[i, n_occ + s, j, n_occ + s] + 2 * g[i, j, j, j] + 2 * g[i, j, n_occ + s, n_occ + s] ) * K[0, j*n_virt + t] * K[1, j*n_virt + s] * K[2, j*n_virt + t + n_ex]

										elif ((t != s) and (u == s) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s + n_ex] += (-4 * g[i, j, n_occ + t, n_occ + v] + 2 * g[i, n_occ + v, j, n_occ + t] ) * K[0, j*n_virt + t] * K[1, j*n_virt + s] * K[2, j*n_virt + v + n_ex]

										elif ((t != s) and (u == t) and (v == t)):

											L4[i*n_virt + s + n_ex] += (4 * g[i, j, n_occ + s, n_occ + t] + -8 * g[i, n_occ + s, j, n_occ + t] ) * K[0, j*n_virt + t] * K[1, j*n_virt + t] * K[2, j*n_virt + t + n_ex]

										elif ((t != s) and (u != s) and (u != t) and (v == t)):

											L4[i*n_virt + s + n_ex] += (-4 * g[i, n_occ + s, j, n_occ + u] + 2 * g[i, j, n_occ + s, n_occ + u] ) * K[0, j*n_virt + t] * K[1, j*n_virt + u] * K[2, j*n_virt + t + n_ex]

										elif ((t != s) and (u != s) and (u != t) and (v == u)):

											L4[i*n_virt + s + n_ex] += (-4 * g[i, n_occ + s, j, n_occ + t] + 2 * g[i, j, n_occ + s, n_occ + t] ) * K[0, j*n_virt + t] * K[1, j*n_virt + u] * K[2, j*n_virt + u + n_ex]

									elif ((j != i) and (k == j) and (m != i) and (m != j) and (m != k)):

										if ((t == s) and (u == s) and (v == s)):

											L4[i*n_virt + s + n_ex] += (4 * g[i, j, j, m] ) * K[0, j*n_virt + s] * K[1, j*n_virt + s] * K[2, m*n_virt + s + n_ex]

										elif ((t == s) and (u != s) and (u != t) and (v == u)):

											L4[i*n_virt + s + n_ex] += (2 * g[i, j, j, m] ) * K[0, j*n_virt + s] * K[1, j*n_virt + u] * K[2, m*n_virt + u + n_ex]

										elif ((t != s) and (u == s) and (v == t)):

											L4[i*n_virt + s + n_ex] += (2 * g[i, j, j, m] ) * K[0, j*n_virt + t] * K[1, j*n_virt + s] * K[2, m*n_virt + t + n_ex]

									elif ((j != i) and (k != i) and (k != j) and (m == i)):

										if ((t == s) and (u == s) and (v == s)):

											L4[i*n_virt + s + n_ex] += (4 * g[i, j, i, k] ) * K[0, j*n_virt + s] * K[1, k*n_virt + s] * K[2, i*n_virt + s + n_ex]

										elif ((t == s) and (u != s) and (u != t) and (v == u)):

											L4[i*n_virt + s + n_ex] += (2 * g[i, j, i, k] ) * K[0, j*n_virt + s] * K[1, k*n_virt + u] * K[2, i*n_virt + u + n_ex]

										elif ((t != s) and (u == s) and (v == t)):

											L4[i*n_virt + s + n_ex] += (2 * g[i, j, i, k] ) * K[0, j*n_virt + t] * K[1, k*n_virt + s] * K[2, i*n_virt + t + n_ex]

									elif ((j != i) and (k != i) and (k != j) and (m == j)):

										if ((t == s) and (u == s) and (v == s)):

											L4[i*n_virt + s + n_ex] += (2 * g[i, j, j, k] + -2 * g[i, k, n_occ + s, n_occ + s] + -2 * g[i, n_occ + s, k, n_occ + s] + 2 * g[i, k, j, j] ) * K[0, j*n_virt + s] * K[1, k*n_virt + s] * K[2, j*n_virt + s + n_ex]

										elif ((t == s) and (u == s) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s + n_ex] += (-4 * g[i, k, n_occ + s, n_occ + v] + 2 * g[i, n_occ + v, k, n_occ + s] ) * K[0, j*n_virt + s] * K[1, k*n_virt + s] * K[2, j*n_virt + v + n_ex]

										elif ((t == s) and (u != s) and (u != t) and (v == u)):

											L4[i*n_virt + s + n_ex] += (4 * g[i, j, j, k] + -2 * g[i, k, j, j] + -4 * g[i, n_occ + s, k, n_occ + s] + 2 * g[i, k, n_occ + s, n_occ + s] ) * K[0, j*n_virt + s] * K[1, k*n_virt + u] * K[2, j*n_virt + u + n_ex]

										elif ((t != s) and (u == s) and (v == s)):

											L4[i*n_virt + s + n_ex] += (-2 * g[i, k, n_occ + s, n_occ + t] + -2 * g[i, n_occ + s, k, n_occ + t] ) * K[0, j*n_virt + t] * K[1, k*n_virt + s] * K[2, j*n_virt + s + n_ex]

										elif ((t != s) and (u == s) and (v == t)):

											L4[i*n_virt + s + n_ex] += (2 * g[i, n_occ + t, k, n_occ + t] + -4 * g[i, k, n_occ + t, n_occ + t] + -2 * g[i, j, j, k] + 4 * g[i, k, j, j] ) * K[0, j*n_virt + t] * K[1, k*n_virt + s] * K[2, j*n_virt + t + n_ex]

										elif ((t != s) and (u == s) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s + n_ex] += (-4 * g[i, k, n_occ + t, n_occ + v] + 2 * g[i, n_occ + v, k, n_occ + t] ) * K[0, j*n_virt + t] * K[1, k*n_virt + s] * K[2, j*n_virt + v + n_ex]

										elif ((t != s) and (u == t) and (v == t)):

											L4[i*n_virt + s + n_ex] += (-4 * g[i, n_occ + s, k, n_occ + t] + 2 * g[i, k, n_occ + s, n_occ + t] ) * K[0, j*n_virt + t] * K[1, k*n_virt + t] * K[2, j*n_virt + t + n_ex]

										elif ((t != s) and (u != s) and (u != t) and (v == u)):

											L4[i*n_virt + s + n_ex] += (2 * g[i, k, n_occ + s, n_occ + t] + -4 * g[i, n_occ + s, k, n_occ + t] ) * K[0, j*n_virt + t] * K[1, k*n_virt + u] * K[2, j*n_virt + u + n_ex]

									elif ((j != i) and (k != i) and (k != j) and (m == k)):

										if ((t == s) and (u == s) and (v == s)):

											L4[i*n_virt + s + n_ex] += (2 * g[i, k, j, k] + -2 * g[i, j, n_occ + s, n_occ + s] + -2 * g[i, n_occ + s, j, n_occ + s] + 2 * g[i, j, k, k] ) * K[0, j*n_virt + s] * K[1, k*n_virt + s] * K[2, k*n_virt + s + n_ex]

										elif ((t == s) and (u == s) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s + n_ex] += (-4 * g[i, j, n_occ + s, n_occ + v] + 2 * g[i, n_occ + v, j, n_occ + s] ) * K[0, j*n_virt + s] * K[1, k*n_virt + s] * K[2, k*n_virt + v + n_ex]

										elif ((t == s) and (u != s) and (u != t) and (v == s)):

											L4[i*n_virt + s + n_ex] += (-2 * g[i, j, n_occ + s, n_occ + u] + -2 * g[i, n_occ + s, j, n_occ + u] ) * K[0, j*n_virt + s] * K[1, k*n_virt + u] * K[2, k*n_virt + s + n_ex]

										elif ((t == s) and (u != s) and (u != t) and (v == u)):

											L4[i*n_virt + s + n_ex] += (2 * g[i, n_occ + u, j, n_occ + u] + -4 * g[i, j, n_occ + u, n_occ + u] + -2 * g[i, k, j, k] + 4 * g[i, j, k, k] ) * K[0, j*n_virt + s] * K[1, k*n_virt + u] * K[2, k*n_virt + u + n_ex]

										elif ((t == s) and (u != s) and (u != t) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s + n_ex] += (-4 * g[i, j, n_occ + u, n_occ + v] + 2 * g[i, n_occ + v, j, n_occ + u] ) * K[0, j*n_virt + s] * K[1, k*n_virt + u] * K[2, k*n_virt + v + n_ex]

										elif ((t != s) and (u == s) and (v == t)):

											L4[i*n_virt + s + n_ex] += (4 * g[i, k, j, k] + -2 * g[i, j, k, k] + -4 * g[i, n_occ + s, j, n_occ + s] + 2 * g[i, j, n_occ + s, n_occ + s] ) * K[0, j*n_virt + t] * K[1, k*n_virt + s] * K[2, k*n_virt + t + n_ex]

										elif ((t != s) and (u == t) and (v == t)):

											L4[i*n_virt + s + n_ex] += (-4 * g[i, n_occ + s, j, n_occ + t] + 2 * g[i, j, n_occ + s, n_occ + t] ) * K[0, j*n_virt + t] * K[1, k*n_virt + t] * K[2, k*n_virt + t + n_ex]

										elif ((t != s) and (u != s) and (u != t) and (v == t)):

											L4[i*n_virt + s + n_ex] += (2 * g[i, j, n_occ + s, n_occ + u] + -4 * g[i, n_occ + s, j, n_occ + u] ) * K[0, j*n_virt + t] * K[1, k*n_virt + u] * K[2, k*n_virt + t + n_ex]

									elif ((j != i) and (k != i) and (k != j) and (m != i) and (m != j) and (m != k)):

										if ((t == s) and (u == s) and (v == s)):

											L4[i*n_virt + s + n_ex] += (2 * g[i, k, j, m] + 2 * g[i, j, k, m] ) * K[0, j*n_virt + s] * K[1, k*n_virt + s] * K[2, m*n_virt + s + n_ex]

										elif ((t == s) and (u != s) and (u != t) and (v == u)):

											L4[i*n_virt + s + n_ex] += (4 * g[i, j, k, m] + -2 * g[i, k, j, m] ) * K[0, j*n_virt + s] * K[1, k*n_virt + u] * K[2, m*n_virt + u + n_ex]

										elif ((t != s) and (u == s) and (v == t)):

											L4[i*n_virt + s + n_ex] += (-2 * g[i, j, k, m] + 4 * g[i, k, j, m] ) * K[0, j*n_virt + t] * K[1, k*n_virt + s] * K[2, m*n_virt + t + n_ex]

	# Current operator combination: {'a': 2, 'b': 1, 'c': 1, 'd': 3}
	# All terms vanished for this combination

	# Current operator combination: {'a': 2, 'b': 1, 'c': 2, 'd': 1}
	for i in range(n_occ):
		for j in range(n_occ):
			for k in range(n_occ):
				for m in range(n_occ):
					for s in range(n_virt):
						for t in range(n_virt):
							for u in range(n_virt):
								for v in range(n_virt):

									if ((j == i) and (k == i) and (m == i)):

										if ((t == s) and (u == s) and (v == s)):

											L4[i*n_virt + s] += (4 * F[n_occ + s, n_occ + s] + -4 * F[i, i] + 4 * g[i, i, n_occ + s, n_occ + s] + 16 * g[i, n_occ + s, i, n_occ + s] + -4 * g[n_occ + s, n_occ + s, n_occ + s, n_occ + s] + -4 * g[i, i, i, i] ) * K[0, i*n_virt + s + n_ex] * K[1, i*n_virt + s] * K[2, i*n_virt + s + n_ex]

										elif ((t == s) and (u == s) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s] += (-4 * g[n_occ + s, n_occ + s, n_occ + s, n_occ + v] + 4 * g[i, i, n_occ + s, n_occ + v] + 4 * g[i, n_occ + s, i, n_occ + v] ) * K[0, i*n_virt + s + n_ex] * K[1, i*n_virt + s] * K[2, i*n_virt + v + n_ex]

										elif ((t == s) and (u != s) and (u != t) and (v == s)):

											L4[i*n_virt + s] += (2 * F[n_occ + s, n_occ + u] + 2 * g[i, i, n_occ + s, n_occ + u] + 8 * g[i, n_occ + s, i, n_occ + u] + -4 * g[n_occ + s, n_occ + s, n_occ + s, n_occ + u] ) * K[0, i*n_virt + s + n_ex] * K[1, i*n_virt + u] * K[2, i*n_virt + s + n_ex]

										elif ((t == s) and (u != s) and (u != t) and (v == u)):

											L4[i*n_virt + s] += (2 * F[n_occ + s, n_occ + s] + -2 * F[i, i] + -2 * g[n_occ + s, n_occ + s, n_occ + u, n_occ + u] + -2 * g[n_occ + s, n_occ + u, n_occ + s, n_occ + u] + 2 * g[i, i, n_occ + u, n_occ + u] + 2 * g[i, n_occ + u, i, n_occ + u] + 6 * g[i, n_occ + s, i, n_occ + s] + -2 * g[i, i, i, i] ) * K[0, i*n_virt + s + n_ex] * K[1, i*n_virt + u] * K[2, i*n_virt + u + n_ex]

										elif ((t == s) and (u != s) and (u != t) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s] += (-2 * g[n_occ + s, n_occ + u, n_occ + s, n_occ + v] + -2 * g[n_occ + s, n_occ + s, n_occ + u, n_occ + v] + 2 * g[i, i, n_occ + u, n_occ + v] + 2 * g[i, n_occ + u, i, n_occ + v] ) * K[0, i*n_virt + s + n_ex] * K[1, i*n_virt + u] * K[2, i*n_virt + v + n_ex]

										elif ((t != s) and (u == s) and (v == s)):

											L4[i*n_virt + s] += (4 * F[n_occ + s, n_occ + t] + 12 * g[i, n_occ + s, i, n_occ + t] + -4 * g[n_occ + s, n_occ + s, n_occ + s, n_occ + t] ) * K[0, i*n_virt + t + n_ex] * K[1, i*n_virt + s] * K[2, i*n_virt + s + n_ex]

										elif ((t != s) and (u == s) and (v == t)):

											L4[i*n_virt + s] += (-4 * g[n_occ + s, n_occ + t, n_occ + s, n_occ + t] ) * K[0, i*n_virt + t + n_ex] * K[1, i*n_virt + s] * K[2, i*n_virt + t + n_ex]

										elif ((t != s) and (u == s) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s] += (-4 * g[n_occ + s, n_occ + t, n_occ + s, n_occ + v] ) * K[0, i*n_virt + t + n_ex] * K[1, i*n_virt + s] * K[2, i*n_virt + v + n_ex]

										elif ((t != s) and (u == t) and (v == s)):

											L4[i*n_virt + s] += (-2 * F[i, i] + 2 * F[n_occ + t, n_occ + t] + 6 * g[i, n_occ + t, i, n_occ + t] + -2 * g[n_occ + s, n_occ + s, n_occ + t, n_occ + t] + -2 * g[n_occ + s, n_occ + t, n_occ + s, n_occ + t] + 2 * g[i, n_occ + s, i, n_occ + s] + 2 * g[i, i, n_occ + s, n_occ + s] + -2 * g[i, i, i, i] ) * K[0, i*n_virt + t + n_ex] * K[1, i*n_virt + t] * K[2, i*n_virt + s + n_ex]

										elif ((t != s) and (u == t) and (v == t)):

											L4[i*n_virt + s] += (2 * F[n_occ + s, n_occ + t] + -4 * g[n_occ + s, n_occ + t, n_occ + t, n_occ + t] + 8 * g[i, n_occ + s, i, n_occ + t] + 2 * g[i, i, n_occ + s, n_occ + t] ) * K[0, i*n_virt + t + n_ex] * K[1, i*n_virt + t] * K[2, i*n_virt + t + n_ex]

										elif ((t != s) and (u == t) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s] += (-2 * g[n_occ + s, n_occ + v, n_occ + t, n_occ + t] + -2 * g[n_occ + s, n_occ + t, n_occ + t, n_occ + v] + 2 * g[i, n_occ + s, i, n_occ + v] + 2 * g[i, i, n_occ + s, n_occ + v] ) * K[0, i*n_virt + t + n_ex] * K[1, i*n_virt + t] * K[2, i*n_virt + v + n_ex]

										elif ((t != s) and (u != s) and (u != t) and (v == s)):

											L4[i*n_virt + s] += (2 * F[n_occ + t, n_occ + u] + 6 * g[i, n_occ + t, i, n_occ + u] + -2 * g[n_occ + s, n_occ + s, n_occ + t, n_occ + u] + -2 * g[n_occ + s, n_occ + t, n_occ + s, n_occ + u] ) * K[0, i*n_virt + t + n_ex] * K[1, i*n_virt + u] * K[2, i*n_virt + s + n_ex]

										elif ((t != s) and (u != s) and (u != t) and (v == t)):

											L4[i*n_virt + s] += (-4 * g[n_occ + s, n_occ + t, n_occ + t, n_occ + u] ) * K[0, i*n_virt + t + n_ex] * K[1, i*n_virt + u] * K[2, i*n_virt + t + n_ex]

										elif ((t != s) and (u != s) and (u != t) and (v == u)):

											L4[i*n_virt + s] += (2 * F[n_occ + s, n_occ + t] + -2 * g[n_occ + s, n_occ + u, n_occ + t, n_occ + u] + -2 * g[n_occ + s, n_occ + t, n_occ + u, n_occ + u] + 6 * g[i, n_occ + s, i, n_occ + t] ) * K[0, i*n_virt + t + n_ex] * K[1, i*n_virt + u] * K[2, i*n_virt + u + n_ex]

										elif ((t != s) and (u != s) and (u != t) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s] += (-2 * g[n_occ + s, n_occ + v, n_occ + t, n_occ + u] + -2 * g[n_occ + s, n_occ + t, n_occ + u, n_occ + v] ) * K[0, i*n_virt + t + n_ex] * K[1, i*n_virt + u] * K[2, i*n_virt + v + n_ex]

									elif ((j == i) and (k == i) and (m != i) and (m != j) and (m != k)):

										if ((t == s) and (u == s) and (v == s)):

											L4[i*n_virt + s] += (4 * g[i, m, n_occ + s, n_occ + s] + -4 * g[i, i, i, m] + 4 * g[i, n_occ + s, m, n_occ + s] ) * K[0, i*n_virt + s + n_ex] * K[1, i*n_virt + s] * K[2, m*n_virt + s + n_ex]

										elif ((t == s) and (u != s) and (u != t) and (v == s)):

											L4[i*n_virt + s] += (2 * g[i, m, n_occ + s, n_occ + u] + 2 * g[i, n_occ + u, m, n_occ + s] ) * K[0, i*n_virt + s + n_ex] * K[1, i*n_virt + u] * K[2, m*n_virt + s + n_ex]

										elif ((t == s) and (u != s) and (u != t) and (v == u)):

											L4[i*n_virt + s] += (2 * g[i, m, n_occ + s, n_occ + s] + 2 * g[i, n_occ + s, m, n_occ + s] + -2 * g[i, i, i, m] ) * K[0, i*n_virt + s + n_ex] * K[1, i*n_virt + u] * K[2, m*n_virt + u + n_ex]

										elif ((t != s) and (u == s) and (v == s)):

											L4[i*n_virt + s] += (4 * g[i, n_occ + s, m, n_occ + t] + 4 * g[i, m, n_occ + s, n_occ + t] ) * K[0, i*n_virt + t + n_ex] * K[1, i*n_virt + s] * K[2, m*n_virt + s + n_ex]

										elif ((t != s) and (u == t) and (v == s)):

											L4[i*n_virt + s] += (2 * g[i, n_occ + t, m, n_occ + t] + 2 * g[i, m, n_occ + t, n_occ + t] + -2 * g[i, i, i, m] ) * K[0, i*n_virt + t + n_ex] * K[1, i*n_virt + t] * K[2, m*n_virt + s + n_ex]

										elif ((t != s) and (u == t) and (v == t)):

											L4[i*n_virt + s] += (2 * g[i, m, n_occ + s, n_occ + t] + 2 * g[i, n_occ + s, m, n_occ + t] ) * K[0, i*n_virt + t + n_ex] * K[1, i*n_virt + t] * K[2, m*n_virt + t + n_ex]

										elif ((t != s) and (u != s) and (u != t) and (v == s)):

											L4[i*n_virt + s] += (2 * g[i, n_occ + u, m, n_occ + t] + 2 * g[i, m, n_occ + t, n_occ + u] ) * K[0, i*n_virt + t + n_ex] * K[1, i*n_virt + u] * K[2, m*n_virt + s + n_ex]

										elif ((t != s) and (u != s) and (u != t) and (v == u)):

											L4[i*n_virt + s] += (2 * g[i, m, n_occ + s, n_occ + t] + 2 * g[i, n_occ + s, m, n_occ + t] ) * K[0, i*n_virt + t + n_ex] * K[1, i*n_virt + u] * K[2, m*n_virt + u + n_ex]

									elif ((j == i) and (k != i) and (k != j) and (m == i)):

										if ((t == s) and (u == s) and (v == s)):

											L4[i*n_virt + s] += (-2 * F[i, k] + -4 * g[i, i, i, k] + 2 * g[i, k, n_occ + s, n_occ + s] + 8 * g[i, n_occ + s, k, n_occ + s] ) * K[0, i*n_virt + s + n_ex] * K[1, k*n_virt + s] * K[2, i*n_virt + s + n_ex]

										elif ((t == s) and (u == s) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s] += (2 * g[i, k, n_occ + s, n_occ + v] + 2 * g[i, n_occ + v, k, n_occ + s] ) * K[0, i*n_virt + s + n_ex] * K[1, k*n_virt + s] * K[2, i*n_virt + v + n_ex]

										elif ((t == s) and (u != s) and (u != t) and (v == s)):

											L4[i*n_virt + s] += (-4 * g[i, k, n_occ + s, n_occ + u] + 8 * g[i, n_occ + s, k, n_occ + u] ) * K[0, i*n_virt + s + n_ex] * K[1, k*n_virt + u] * K[2, i*n_virt + s + n_ex]

										elif ((t == s) and (u != s) and (u != t) and (v == u)):

											L4[i*n_virt + s] += (-2 * F[i, k] + 2 * g[i, n_occ + s, k, n_occ + s] + 2 * g[i, k, n_occ + s, n_occ + s] + 4 * g[i, n_occ + u, k, n_occ + u] + -2 * g[i, k, n_occ + u, n_occ + u] + -2 * g[i, i, i, k] ) * K[0, i*n_virt + s + n_ex] * K[1, k*n_virt + u] * K[2, i*n_virt + u + n_ex]

										elif ((t == s) and (u != s) and (u != t) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s] += (-2 * g[i, k, n_occ + u, n_occ + v] + 4 * g[i, n_occ + v, k, n_occ + u] ) * K[0, i*n_virt + s + n_ex] * K[1, k*n_virt + u] * K[2, i*n_virt + v + n_ex]

										elif ((t != s) and (u == s) and (v == s)):

											L4[i*n_virt + s] += (6 * g[i, n_occ + t, k, n_occ + s] ) * K[0, i*n_virt + t + n_ex] * K[1, k*n_virt + s] * K[2, i*n_virt + s + n_ex]

										elif ((t != s) and (u == t) and (v == s)):

											L4[i*n_virt + s] += (-2 * g[i, n_occ + s, k, n_occ + s] + 4 * g[i, k, n_occ + s, n_occ + s] + 4 * g[i, n_occ + t, k, n_occ + t] + -2 * g[i, k, n_occ + t, n_occ + t] + -2 * g[i, i, i, k] ) * K[0, i*n_virt + t + n_ex] * K[1, k*n_virt + t] * K[2, i*n_virt + s + n_ex]

										elif ((t != s) and (u == t) and (v == t)):

											L4[i*n_virt + s] += (6 * g[i, k, n_occ + s, n_occ + t] ) * K[0, i*n_virt + t + n_ex] * K[1, k*n_virt + t] * K[2, i*n_virt + t + n_ex]

										elif ((t != s) and (u == t) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s] += (4 * g[i, k, n_occ + s, n_occ + v] + -2 * g[i, n_occ + v, k, n_occ + s] ) * K[0, i*n_virt + t + n_ex] * K[1, k*n_virt + t] * K[2, i*n_virt + v + n_ex]

										elif ((t != s) and (u != s) and (u != t) and (v == s)):

											L4[i*n_virt + s] += (-2 * g[i, k, n_occ + t, n_occ + u] + 4 * g[i, n_occ + t, k, n_occ + u] ) * K[0, i*n_virt + t + n_ex] * K[1, k*n_virt + u] * K[2, i*n_virt + s + n_ex]

										elif ((t != s) and (u != s) and (u != t) and (v == u)):

											L4[i*n_virt + s] += (2 * g[i, n_occ + t, k, n_occ + s] + 2 * g[i, k, n_occ + s, n_occ + t] ) * K[0, i*n_virt + t + n_ex] * K[1, k*n_virt + u] * K[2, i*n_virt + u + n_ex]

									elif ((j == i) and (k != i) and (k != j) and (m == k)):

										if ((t == s) and (u == s) and (v == s)):

											L4[i*n_virt + s] += (2 * F[n_occ + s, n_occ + s] + -2 * F[i, i] + -2 * g[n_occ + s, n_occ + s, n_occ + s, n_occ + s] + -2 * g[i, i, k, k] + 2 * g[k, k, n_occ + s, n_occ + s] + 6 * g[i, n_occ + s, i, n_occ + s] + 2 * g[k, n_occ + s, k, n_occ + s] + -2 * g[i, k, i, k] ) * K[0, i*n_virt + s + n_ex] * K[1, k*n_virt + s] * K[2, k*n_virt + s + n_ex]

										elif ((t == s) and (u == s) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s] += (2 * g[i, n_occ + s, i, n_occ + v] + -2 * g[n_occ + s, n_occ + s, n_occ + s, n_occ + v] + 2 * g[i, i, n_occ + s, n_occ + v] ) * K[0, i*n_virt + s + n_ex] * K[1, k*n_virt + s] * K[2, k*n_virt + v + n_ex]

										elif ((t == s) and (u != s) and (u != t) and (v == s)):

											L4[i*n_virt + s] += (2 * F[n_occ + s, n_occ + u] + -2 * g[n_occ + s, n_occ + s, n_occ + s, n_occ + u] + 2 * g[i, i, n_occ + s, n_occ + u] + -2 * g[k, k, n_occ + s, n_occ + u] + 4 * g[k, n_occ + s, k, n_occ + u] + 2 * g[i, n_occ + s, i, n_occ + u] ) * K[0, i*n_virt + s + n_ex] * K[1, k*n_virt + u] * K[2, k*n_virt + s + n_ex]

										elif ((t == s) and (u != s) and (u != t) and (v == u)):

											L4[i*n_virt + s] += (2 * g[n_occ + s, n_occ + u, n_occ + s, n_occ + u] + -4 * g[n_occ + s, n_occ + s, n_occ + u, n_occ + u] + -2 * g[i, n_occ + u, i, n_occ + u] + 4 * g[i, i, n_occ + u, n_occ + u] + 2 * g[i, k, i, k] + -4 * g[i, i, k, k] + 4 * g[k, k, n_occ + s, n_occ + s] + -2 * g[k, n_occ + s, k, n_occ + s] ) * K[0, i*n_virt + s + n_ex] * K[1, k*n_virt + u] * K[2, k*n_virt + u + n_ex]

										elif ((t == s) and (u != s) and (u != t) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s] += (2 * g[n_occ + s, n_occ + u, n_occ + s, n_occ + v] + -4 * g[n_occ + s, n_occ + s, n_occ + u, n_occ + v] + -2 * g[i, n_occ + u, i, n_occ + v] + 4 * g[i, i, n_occ + u, n_occ + v] ) * K[0, i*n_virt + s + n_ex] * K[1, k*n_virt + u] * K[2, k*n_virt + v + n_ex]

										elif ((t != s) and (u == s) and (v == s)):

											L4[i*n_virt + s] += (2 * F[n_occ + s, n_occ + t] + -2 * g[n_occ + s, n_occ + s, n_occ + s, n_occ + t] + 2 * g[k, k, n_occ + s, n_occ + t] + 4 * g[i, n_occ + s, i, n_occ + t] + -2 * g[i, i, n_occ + s, n_occ + t] + 2 * g[k, n_occ + s, k, n_occ + t] ) * K[0, i*n_virt + t + n_ex] * K[1, k*n_virt + s] * K[2, k*n_virt + s + n_ex]

										elif ((t != s) and (u == s) and (v == t)):

											L4[i*n_virt + s] += (-2 * g[n_occ + s, n_occ + t, n_occ + s, n_occ + t] ) * K[0, i*n_virt + t + n_ex] * K[1, k*n_virt + s] * K[2, k*n_virt + t + n_ex]

										elif ((t != s) and (u == s) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s] += (-2 * g[n_occ + s, n_occ + t, n_occ + s, n_occ + v] ) * K[0, i*n_virt + t + n_ex] * K[1, k*n_virt + s] * K[2, k*n_virt + v + n_ex]

										elif ((t != s) and (u == t) and (v == s)):

											L4[i*n_virt + s] += (2 * F[n_occ + t, n_occ + t] + -2 * F[i, i] + -2 * g[i, i, n_occ + s, n_occ + s] + 4 * g[i, n_occ + s, i, n_occ + s] + -4 * g[n_occ + s, n_occ + t, n_occ + s, n_occ + t] + -4 * g[i, k, i, k] + 2 * g[n_occ + s, n_occ + s, n_occ + t, n_occ + t] + -2 * g[i, i, n_occ + t, n_occ + t] + -2 * g[k, k, n_occ + t, n_occ + t] + 4 * g[i, n_occ + t, i, n_occ + t] + 4 * g[k, n_occ + t, k, n_occ + t] + 2 * g[i, i, k, k] ) * K[0, i*n_virt + t + n_ex] * K[1, k*n_virt + t] * K[2, k*n_virt + s + n_ex]

										elif ((t != s) and (u == t) and (v == t)):

											L4[i*n_virt + s] += (-2 * g[i, i, n_occ + s, n_occ + t] + -2 * g[n_occ + s, n_occ + t, n_occ + t, n_occ + t] + 4 * g[i, n_occ + s, i, n_occ + t] + -2 * g[k, n_occ + s, k, n_occ + t] + 4 * g[k, k, n_occ + s, n_occ + t] ) * K[0, i*n_virt + t + n_ex] * K[1, k*n_virt + t] * K[2, k*n_virt + t + n_ex]

										elif ((t != s) and (u == t) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s] += (4 * g[i, n_occ + s, i, n_occ + v] + -2 * g[i, i, n_occ + s, n_occ + v] + -4 * g[n_occ + s, n_occ + t, n_occ + t, n_occ + v] + 2 * g[n_occ + s, n_occ + v, n_occ + t, n_occ + t] ) * K[0, i*n_virt + t + n_ex] * K[1, k*n_virt + t] * K[2, k*n_virt + v + n_ex]

										elif ((t != s) and (u != s) and (u != t) and (v == s)):

											L4[i*n_virt + s] += (2 * F[n_occ + t, n_occ + u] + -4 * g[n_occ + s, n_occ + t, n_occ + s, n_occ + u] + 2 * g[n_occ + s, n_occ + s, n_occ + t, n_occ + u] + -2 * g[i, i, n_occ + t, n_occ + u] + -2 * g[k, k, n_occ + t, n_occ + u] + 4 * g[i, n_occ + t, i, n_occ + u] + 4 * g[k, n_occ + t, k, n_occ + u] ) * K[0, i*n_virt + t + n_ex] * K[1, k*n_virt + u] * K[2, k*n_virt + s + n_ex]

										elif ((t != s) and (u != s) and (u != t) and (v == t)):

											L4[i*n_virt + s] += (-2 * g[n_occ + s, n_occ + t, n_occ + t, n_occ + u] ) * K[0, i*n_virt + t + n_ex] * K[1, k*n_virt + u] * K[2, k*n_virt + t + n_ex]

										elif ((t != s) and (u != s) and (u != t) and (v == u)):

											L4[i*n_virt + s] += (2 * g[n_occ + s, n_occ + u, n_occ + t, n_occ + u] + -4 * g[n_occ + s, n_occ + t, n_occ + u, n_occ + u] + -2 * g[k, n_occ + s, k, n_occ + t] + 4 * g[k, k, n_occ + s, n_occ + t] ) * K[0, i*n_virt + t + n_ex] * K[1, k*n_virt + u] * K[2, k*n_virt + u + n_ex]

										elif ((t != s) and (u != s) and (u != t) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s] += (-4 * g[n_occ + s, n_occ + t, n_occ + u, n_occ + v] + 2 * g[n_occ + s, n_occ + v, n_occ + t, n_occ + u] ) * K[0, i*n_virt + t + n_ex] * K[1, k*n_virt + u] * K[2, k*n_virt + v + n_ex]

									elif ((j == i) and (k != i) and (k != j) and (m != i) and (m != j) and (m != k)):

										if ((t == s) and (u == s) and (v == s)):

											L4[i*n_virt + s] += (-2 * g[i, k, i, m] + 2 * g[k, m, n_occ + s, n_occ + s] + 2 * g[k, n_occ + s, m, n_occ + s] + -2 * g[i, i, k, m] ) * K[0, i*n_virt + s + n_ex] * K[1, k*n_virt + s] * K[2, m*n_virt + s + n_ex]

										elif ((t == s) and (u != s) and (u != t) and (v == s)):

											L4[i*n_virt + s] += (-2 * g[k, m, n_occ + s, n_occ + u] + 4 * g[k, n_occ + u, m, n_occ + s] ) * K[0, i*n_virt + s + n_ex] * K[1, k*n_virt + u] * K[2, m*n_virt + s + n_ex]

										elif ((t == s) and (u != s) and (u != t) and (v == u)):

											L4[i*n_virt + s] += (-2 * g[k, n_occ + s, m, n_occ + s] + 4 * g[k, m, n_occ + s, n_occ + s] + 2 * g[i, k, i, m] + -4 * g[i, i, k, m] ) * K[0, i*n_virt + s + n_ex] * K[1, k*n_virt + u] * K[2, m*n_virt + u + n_ex]

										elif ((t != s) and (u == s) and (v == s)):

											L4[i*n_virt + s] += (2 * g[k, n_occ + s, m, n_occ + t] + 2 * g[k, m, n_occ + s, n_occ + t] ) * K[0, i*n_virt + t + n_ex] * K[1, k*n_virt + s] * K[2, m*n_virt + s + n_ex]

										elif ((t != s) and (u == t) and (v == s)):

											L4[i*n_virt + s] += (-4 * g[i, k, i, m] + 2 * g[i, i, k, m] + 4 * g[k, n_occ + t, m, n_occ + t] + -2 * g[k, m, n_occ + t, n_occ + t] ) * K[0, i*n_virt + t + n_ex] * K[1, k*n_virt + t] * K[2, m*n_virt + s + n_ex]

										elif ((t != s) and (u == t) and (v == t)):

											L4[i*n_virt + s] += (4 * g[k, m, n_occ + s, n_occ + t] + -2 * g[k, n_occ + s, m, n_occ + t] ) * K[0, i*n_virt + t + n_ex] * K[1, k*n_virt + t] * K[2, m*n_virt + t + n_ex]

										elif ((t != s) and (u != s) and (u != t) and (v == s)):

											L4[i*n_virt + s] += (-2 * g[k, m, n_occ + t, n_occ + u] + 4 * g[k, n_occ + u, m, n_occ + t] ) * K[0, i*n_virt + t + n_ex] * K[1, k*n_virt + u] * K[2, m*n_virt + s + n_ex]

										elif ((t != s) and (u != s) and (u != t) and (v == u)):

											L4[i*n_virt + s] += (4 * g[k, m, n_occ + s, n_occ + t] + -2 * g[k, n_occ + s, m, n_occ + t] ) * K[0, i*n_virt + t + n_ex] * K[1, k*n_virt + u] * K[2, m*n_virt + u + n_ex]

									elif ((j != i) and (k == i) and (m == i)):

										if ((t == s) and (u == s) and (v == s)):

											L4[i*n_virt + s] += (-4 * F[i, j] + 12 * g[i, n_occ + s, j, n_occ + s] + -4 * g[i, i, i, j] ) * K[0, j*n_virt + s + n_ex] * K[1, i*n_virt + s] * K[2, i*n_virt + s + n_ex]

										elif ((t == s) and (u == s) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s] += (4 * g[i, n_occ + s, j, n_occ + v] + 4 * g[i, j, n_occ + s, n_occ + v] ) * K[0, j*n_virt + s + n_ex] * K[1, i*n_virt + s] * K[2, i*n_virt + v + n_ex]

										elif ((t == s) and (u != s) and (u != t) and (v == s)):

											L4[i*n_virt + s] += (6 * g[i, n_occ + u, j, n_occ + s] ) * K[0, j*n_virt + s + n_ex] * K[1, i*n_virt + u] * K[2, i*n_virt + s + n_ex]

										elif ((t == s) and (u != s) and (u != t) and (v == u)):

											L4[i*n_virt + s] += (-2 * F[i, j] + 2 * g[i, n_occ + u, j, n_occ + u] + 2 * g[i, j, n_occ + u, n_occ + u] + 4 * g[i, n_occ + s, j, n_occ + s] + -2 * g[i, j, n_occ + s, n_occ + s] + -2 * g[i, i, i, j] ) * K[0, j*n_virt + s + n_ex] * K[1, i*n_virt + u] * K[2, i*n_virt + u + n_ex]

										elif ((t == s) and (u != s) and (u != t) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s] += (2 * g[i, n_occ + u, j, n_occ + v] + 2 * g[i, j, n_occ + u, n_occ + v] ) * K[0, j*n_virt + s + n_ex] * K[1, i*n_virt + u] * K[2, i*n_virt + v + n_ex]

										elif ((t != s) and (u == s) and (v == s)):

											L4[i*n_virt + s] += (-4 * g[i, j, n_occ + s, n_occ + t] + 8 * g[i, n_occ + s, j, n_occ + t] ) * K[0, j*n_virt + t + n_ex] * K[1, i*n_virt + s] * K[2, i*n_virt + s + n_ex]

										elif ((t != s) and (u == t) and (v == s)):

											L4[i*n_virt + s] += (-2 * F[i, j] + 4 * g[i, n_occ + t, j, n_occ + t] + -2 * g[i, j, n_occ + t, n_occ + t] + 2 * g[i, j, n_occ + s, n_occ + s] + 2 * g[i, n_occ + s, j, n_occ + s] + -2 * g[i, i, i, j] ) * K[0, j*n_virt + t + n_ex] * K[1, i*n_virt + t] * K[2, i*n_virt + s + n_ex]

										elif ((t != s) and (u == t) and (v == t)):

											L4[i*n_virt + s] += (6 * g[i, n_occ + s, j, n_occ + t] ) * K[0, j*n_virt + t + n_ex] * K[1, i*n_virt + t] * K[2, i*n_virt + t + n_ex]

										elif ((t != s) and (u == t) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s] += (2 * g[i, j, n_occ + s, n_occ + v] + 2 * g[i, n_occ + s, j, n_occ + v] ) * K[0, j*n_virt + t + n_ex] * K[1, i*n_virt + t] * K[2, i*n_virt + v + n_ex]

										elif ((t != s) and (u != s) and (u != t) and (v == s)):

											L4[i*n_virt + s] += (-2 * g[i, j, n_occ + t, n_occ + u] + 4 * g[i, n_occ + u, j, n_occ + t] ) * K[0, j*n_virt + t + n_ex] * K[1, i*n_virt + u] * K[2, i*n_virt + s + n_ex]

										elif ((t != s) and (u != s) and (u != t) and (v == u)):

											L4[i*n_virt + s] += (4 * g[i, n_occ + s, j, n_occ + t] + -2 * g[i, j, n_occ + s, n_occ + t] ) * K[0, j*n_virt + t + n_ex] * K[1, i*n_virt + u] * K[2, i*n_virt + u + n_ex]

									elif ((j != i) and (k == i) and (m == j)):

										if ((t == s) and (u == s) and (v == s)):

											L4[i*n_virt + s] += (-4 * g[i, j, i, j] ) * K[0, j*n_virt + s + n_ex] * K[1, i*n_virt + s] * K[2, j*n_virt + s + n_ex]

										elif ((t == s) and (u != s) and (u != t) and (v == u)):

											L4[i*n_virt + s] += (-2 * g[i, j, i, j] ) * K[0, j*n_virt + s + n_ex] * K[1, i*n_virt + u] * K[2, j*n_virt + u + n_ex]

										elif ((t != s) and (u == t) and (v == s)):

											L4[i*n_virt + s] += (-2 * g[i, j, i, j] ) * K[0, j*n_virt + t + n_ex] * K[1, i*n_virt + t] * K[2, j*n_virt + s + n_ex]

									elif ((j != i) and (k == i) and (m != i) and (m != j) and (m != k)):

										if ((t == s) and (u == s) and (v == s)):

											L4[i*n_virt + s] += (-4 * g[i, j, i, m] ) * K[0, j*n_virt + s + n_ex] * K[1, i*n_virt + s] * K[2, m*n_virt + s + n_ex]

										elif ((t == s) and (u != s) and (u != t) and (v == u)):

											L4[i*n_virt + s] += (-2 * g[i, j, i, m] ) * K[0, j*n_virt + s + n_ex] * K[1, i*n_virt + u] * K[2, m*n_virt + u + n_ex]

										elif ((t != s) and (u == t) and (v == s)):

											L4[i*n_virt + s] += (-2 * g[i, j, i, m] ) * K[0, j*n_virt + t + n_ex] * K[1, i*n_virt + t] * K[2, m*n_virt + s + n_ex]

									elif ((j != i) and (k == j) and (m == i)):

										if ((t == s) and (u == s) and (v == s)):

											L4[i*n_virt + s] += (2 * F[n_occ + s, n_occ + s] + -2 * F[j, j] + 6 * g[j, n_occ + s, j, n_occ + s] + 2 * g[i, i, n_occ + s, n_occ + s] + -2 * g[n_occ + s, n_occ + s, n_occ + s, n_occ + s] + -2 * g[i, i, j, j] + 2 * g[i, n_occ + s, i, n_occ + s] + -2 * g[i, j, i, j] ) * K[0, j*n_virt + s + n_ex] * K[1, j*n_virt + s] * K[2, i*n_virt + s + n_ex]

										elif ((t == s) and (u == s) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s] += (2 * g[j, n_occ + s, j, n_occ + v] + -2 * g[n_occ + s, n_occ + s, n_occ + s, n_occ + v] + 2 * g[j, j, n_occ + s, n_occ + v] ) * K[0, j*n_virt + s + n_ex] * K[1, j*n_virt + s] * K[2, i*n_virt + v + n_ex]

										elif ((t == s) and (u != s) and (u != t) and (v == s)):

											L4[i*n_virt + s] += (-2 * g[i, n_occ + s, i, n_occ + u] + 4 * g[j, n_occ + s, j, n_occ + u] + 4 * g[i, i, n_occ + s, n_occ + u] + -2 * g[j, j, n_occ + s, n_occ + u] + -2 * g[n_occ + s, n_occ + s, n_occ + s, n_occ + u] ) * K[0, j*n_virt + s + n_ex] * K[1, j*n_virt + u] * K[2, i*n_virt + s + n_ex]

										elif ((t == s) and (u != s) and (u != t) and (v == u)):

											L4[i*n_virt + s] += (2 * F[n_occ + s, n_occ + s] + -2 * F[j, j] + -2 * g[j, j, n_occ + u, n_occ + u] + 4 * g[j, n_occ + u, j, n_occ + u] + -4 * g[n_occ + s, n_occ + u, n_occ + s, n_occ + u] + -4 * g[i, j, i, j] + 2 * g[n_occ + s, n_occ + s, n_occ + u, n_occ + u] + -2 * g[i, i, n_occ + s, n_occ + s] + -2 * g[j, j, n_occ + s, n_occ + s] + 4 * g[j, n_occ + s, j, n_occ + s] + 4 * g[i, n_occ + s, i, n_occ + s] + 2 * g[i, i, j, j] ) * K[0, j*n_virt + s + n_ex] * K[1, j*n_virt + u] * K[2, i*n_virt + u + n_ex]

										elif ((t == s) and (u != s) and (u != t) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s] += (4 * g[j, n_occ + u, j, n_occ + v] + -2 * g[j, j, n_occ + u, n_occ + v] + -4 * g[n_occ + s, n_occ + u, n_occ + s, n_occ + v] + 2 * g[n_occ + s, n_occ + s, n_occ + u, n_occ + v] ) * K[0, j*n_virt + s + n_ex] * K[1, j*n_virt + u] * K[2, i*n_virt + v + n_ex]

										elif ((t != s) and (u == s) and (v == s)):

											L4[i*n_virt + s] += (2 * F[n_occ + s, n_occ + t] + 2 * g[i, i, n_occ + s, n_occ + t] + -2 * g[j, j, n_occ + s, n_occ + t] + 4 * g[j, n_occ + s, j, n_occ + t] + -2 * g[n_occ + s, n_occ + s, n_occ + s, n_occ + t] + 2 * g[i, n_occ + s, i, n_occ + t] ) * K[0, j*n_virt + t + n_ex] * K[1, j*n_virt + s] * K[2, i*n_virt + s + n_ex]

										elif ((t != s) and (u == s) and (v == t)):

											L4[i*n_virt + s] += (-2 * g[n_occ + s, n_occ + t, n_occ + s, n_occ + t] ) * K[0, j*n_virt + t + n_ex] * K[1, j*n_virt + s] * K[2, i*n_virt + t + n_ex]

										elif ((t != s) and (u == s) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s] += (-2 * g[n_occ + s, n_occ + t, n_occ + s, n_occ + v] ) * K[0, j*n_virt + t + n_ex] * K[1, j*n_virt + s] * K[2, i*n_virt + v + n_ex]

										elif ((t != s) and (u == t) and (v == s)):

											L4[i*n_virt + s] += (4 * g[i, i, n_occ + t, n_occ + t] + -2 * g[i, n_occ + t, i, n_occ + t] + 2 * g[n_occ + s, n_occ + t, n_occ + s, n_occ + t] + -4 * g[n_occ + s, n_occ + s, n_occ + t, n_occ + t] + 2 * g[i, j, i, j] + -4 * g[i, i, j, j] + 4 * g[j, j, n_occ + s, n_occ + s] + -2 * g[j, n_occ + s, j, n_occ + s] ) * K[0, j*n_virt + t + n_ex] * K[1, j*n_virt + t] * K[2, i*n_virt + s + n_ex]

										elif ((t != s) and (u == t) and (v == t)):

											L4[i*n_virt + s] += (2 * F[n_occ + s, n_occ + t] + -2 * g[n_occ + s, n_occ + t, n_occ + t, n_occ + t] + 2 * g[j, j, n_occ + s, n_occ + t] + 4 * g[i, n_occ + s, i, n_occ + t] + -2 * g[i, i, n_occ + s, n_occ + t] + 2 * g[j, n_occ + s, j, n_occ + t] ) * K[0, j*n_virt + t + n_ex] * K[1, j*n_virt + t] * K[2, i*n_virt + t + n_ex]

										elif ((t != s) and (u == t) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s] += (2 * g[n_occ + s, n_occ + t, n_occ + t, n_occ + v] + -4 * g[n_occ + s, n_occ + v, n_occ + t, n_occ + t] + -2 * g[j, n_occ + s, j, n_occ + v] + 4 * g[j, j, n_occ + s, n_occ + v] ) * K[0, j*n_virt + t + n_ex] * K[1, j*n_virt + t] * K[2, i*n_virt + v + n_ex]

										elif ((t != s) and (u != s) and (u != t) and (v == s)):

											L4[i*n_virt + s] += (-2 * g[i, n_occ + t, i, n_occ + u] + 4 * g[i, i, n_occ + t, n_occ + u] + 2 * g[n_occ + s, n_occ + t, n_occ + s, n_occ + u] + -4 * g[n_occ + s, n_occ + s, n_occ + t, n_occ + u] ) * K[0, j*n_virt + t + n_ex] * K[1, j*n_virt + u] * K[2, i*n_virt + s + n_ex]

										elif ((t != s) and (u != s) and (u != t) and (v == t)):

											L4[i*n_virt + s] += (-2 * g[n_occ + s, n_occ + t, n_occ + t, n_occ + u] ) * K[0, j*n_virt + t + n_ex] * K[1, j*n_virt + u] * K[2, i*n_virt + t + n_ex]

										elif ((t != s) and (u != s) and (u != t) and (v == u)):

											L4[i*n_virt + s] += (2 * F[n_occ + s, n_occ + t] + -4 * g[n_occ + s, n_occ + u, n_occ + t, n_occ + u] + 2 * g[n_occ + s, n_occ + t, n_occ + u, n_occ + u] + -2 * g[i, i, n_occ + s, n_occ + t] + -2 * g[j, j, n_occ + s, n_occ + t] + 4 * g[j, n_occ + s, j, n_occ + t] + 4 * g[i, n_occ + s, i, n_occ + t] ) * K[0, j*n_virt + t + n_ex] * K[1, j*n_virt + u] * K[2, i*n_virt + u + n_ex]

										elif ((t != s) and (u != s) and (u != t) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s] += (2 * g[n_occ + s, n_occ + t, n_occ + u, n_occ + v] + -4 * g[n_occ + s, n_occ + v, n_occ + t, n_occ + u] ) * K[0, j*n_virt + t + n_ex] * K[1, j*n_virt + u] * K[2, i*n_virt + v + n_ex]

									elif ((j != i) and (k == j) and (m == j)):

										if ((t == s) and (u == s) and (v == s)):

											L4[i*n_virt + s] += (-2 * F[i, j] + 2 * g[i, j, n_occ + s, n_occ + s] + -4 * g[i, j, j, j] + 8 * g[i, n_occ + s, j, n_occ + s] ) * K[0, j*n_virt + s + n_ex] * K[1, j*n_virt + s] * K[2, j*n_virt + s + n_ex]

										elif ((t == s) and (u == s) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s] += (2 * g[i, j, n_occ + s, n_occ + v] + 2 * g[i, n_occ + s, j, n_occ + v] ) * K[0, j*n_virt + s + n_ex] * K[1, j*n_virt + s] * K[2, j*n_virt + v + n_ex]

										elif ((t == s) and (u != s) and (u != t) and (v == s)):

											L4[i*n_virt + s] += (6 * g[i, j, n_occ + s, n_occ + u] ) * K[0, j*n_virt + s + n_ex] * K[1, j*n_virt + u] * K[2, j*n_virt + s + n_ex]

										elif ((t == s) and (u != s) and (u != t) and (v == u)):

											L4[i*n_virt + s] += (-2 * g[i, n_occ + u, j, n_occ + u] + 4 * g[i, j, n_occ + u, n_occ + u] + 4 * g[i, n_occ + s, j, n_occ + s] + -2 * g[i, j, j, j] + -2 * g[i, j, n_occ + s, n_occ + s] ) * K[0, j*n_virt + s + n_ex] * K[1, j*n_virt + u] * K[2, j*n_virt + u + n_ex]

										elif ((t == s) and (u != s) and (u != t) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s] += (4 * g[i, j, n_occ + u, n_occ + v] + -2 * g[i, n_occ + u, j, n_occ + v] ) * K[0, j*n_virt + s + n_ex] * K[1, j*n_virt + u] * K[2, j*n_virt + v + n_ex]

										elif ((t != s) and (u == s) and (v == s)):

											L4[i*n_virt + s] += (6 * g[i, n_occ + s, j, n_occ + t] ) * K[0, j*n_virt + t + n_ex] * K[1, j*n_virt + s] * K[2, j*n_virt + s + n_ex]

										elif ((t != s) and (u == t) and (v == s)):

											L4[i*n_virt + s] += (-2 * F[i, j] + 2 * g[i, n_occ + t, j, n_occ + t] + 2 * g[i, j, n_occ + t, n_occ + t] + 4 * g[i, n_occ + s, j, n_occ + s] + -2 * g[i, j, n_occ + s, n_occ + s] + -2 * g[i, j, j, j] ) * K[0, j*n_virt + t + n_ex] * K[1, j*n_virt + t] * K[2, j*n_virt + s + n_ex]

										elif ((t != s) and (u == t) and (v == t)):

											L4[i*n_virt + s] += (-4 * g[i, j, n_occ + s, n_occ + t] + 8 * g[i, n_occ + s, j, n_occ + t] ) * K[0, j*n_virt + t + n_ex] * K[1, j*n_virt + t] * K[2, j*n_virt + t + n_ex]

										elif ((t != s) and (u == t) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s] += (4 * g[i, n_occ + s, j, n_occ + v] + -2 * g[i, j, n_occ + s, n_occ + v] ) * K[0, j*n_virt + t + n_ex] * K[1, j*n_virt + t] * K[2, j*n_virt + v + n_ex]

										elif ((t != s) and (u != s) and (u != t) and (v == s)):

											L4[i*n_virt + s] += (2 * g[i, n_occ + u, j, n_occ + t] + 2 * g[i, j, n_occ + t, n_occ + u] ) * K[0, j*n_virt + t + n_ex] * K[1, j*n_virt + u] * K[2, j*n_virt + s + n_ex]

										elif ((t != s) and (u != s) and (u != t) and (v == u)):

											L4[i*n_virt + s] += (4 * g[i, n_occ + s, j, n_occ + t] + -2 * g[i, j, n_occ + s, n_occ + t] ) * K[0, j*n_virt + t + n_ex] * K[1, j*n_virt + u] * K[2, j*n_virt + u + n_ex]

									elif ((j != i) and (k == j) and (m != i) and (m != j) and (m != k)):

										if ((t == s) and (u == s) and (v == s)):

											L4[i*n_virt + s] += (-2 * g[i, j, j, m] + 2 * g[i, m, n_occ + s, n_occ + s] + 2 * g[i, n_occ + s, m, n_occ + s] + -2 * g[i, m, j, j] ) * K[0, j*n_virt + s + n_ex] * K[1, j*n_virt + s] * K[2, m*n_virt + s + n_ex]

										elif ((t == s) and (u != s) and (u != t) and (v == s)):

											L4[i*n_virt + s] += (4 * g[i, m, n_occ + s, n_occ + u] + -2 * g[i, n_occ + u, m, n_occ + s] ) * K[0, j*n_virt + s + n_ex] * K[1, j*n_virt + u] * K[2, m*n_virt + s + n_ex]

										elif ((t == s) and (u != s) and (u != t) and (v == u)):

											L4[i*n_virt + s] += (-4 * g[i, j, j, m] + 2 * g[i, m, j, j] + 4 * g[i, n_occ + s, m, n_occ + s] + -2 * g[i, m, n_occ + s, n_occ + s] ) * K[0, j*n_virt + s + n_ex] * K[1, j*n_virt + u] * K[2, m*n_virt + u + n_ex]

										elif ((t != s) and (u == s) and (v == s)):

											L4[i*n_virt + s] += (2 * g[i, m, n_occ + s, n_occ + t] + 2 * g[i, n_occ + s, m, n_occ + t] ) * K[0, j*n_virt + t + n_ex] * K[1, j*n_virt + s] * K[2, m*n_virt + s + n_ex]

										elif ((t != s) and (u == t) and (v == s)):

											L4[i*n_virt + s] += (-2 * g[i, n_occ + t, m, n_occ + t] + 4 * g[i, m, n_occ + t, n_occ + t] + 2 * g[i, j, j, m] + -4 * g[i, m, j, j] ) * K[0, j*n_virt + t + n_ex] * K[1, j*n_virt + t] * K[2, m*n_virt + s + n_ex]

										elif ((t != s) and (u == t) and (v == t)):

											L4[i*n_virt + s] += (4 * g[i, n_occ + s, m, n_occ + t] + -2 * g[i, m, n_occ + s, n_occ + t] ) * K[0, j*n_virt + t + n_ex] * K[1, j*n_virt + t] * K[2, m*n_virt + t + n_ex]

										elif ((t != s) and (u != s) and (u != t) and (v == s)):

											L4[i*n_virt + s] += (4 * g[i, m, n_occ + t, n_occ + u] + -2 * g[i, n_occ + u, m, n_occ + t] ) * K[0, j*n_virt + t + n_ex] * K[1, j*n_virt + u] * K[2, m*n_virt + s + n_ex]

										elif ((t != s) and (u != s) and (u != t) and (v == u)):

											L4[i*n_virt + s] += (-2 * g[i, m, n_occ + s, n_occ + t] + 4 * g[i, n_occ + s, m, n_occ + t] ) * K[0, j*n_virt + t + n_ex] * K[1, j*n_virt + u] * K[2, m*n_virt + u + n_ex]

									elif ((j != i) and (k != i) and (k != j) and (m == i)):

										if ((t == s) and (u == s) and (v == s)):

											L4[i*n_virt + s] += (-2 * F[j, k] + 6 * g[j, n_occ + s, k, n_occ + s] + -2 * g[i, i, j, k] + -2 * g[i, j, i, k] ) * K[0, j*n_virt + s + n_ex] * K[1, k*n_virt + s] * K[2, i*n_virt + s + n_ex]

										elif ((t == s) and (u == s) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s] += (2 * g[j, n_occ + v, k, n_occ + s] + 2 * g[j, k, n_occ + s, n_occ + v] ) * K[0, j*n_virt + s + n_ex] * K[1, k*n_virt + s] * K[2, i*n_virt + v + n_ex]

										elif ((t == s) and (u != s) and (u != t) and (v == s)):

											L4[i*n_virt + s] += (-2 * g[j, k, n_occ + s, n_occ + u] + 4 * g[j, n_occ + s, k, n_occ + u] ) * K[0, j*n_virt + s + n_ex] * K[1, k*n_virt + u] * K[2, i*n_virt + s + n_ex]

										elif ((t == s) and (u != s) and (u != t) and (v == u)):

											L4[i*n_virt + s] += (-2 * F[j, k] + 4 * g[j, n_occ + s, k, n_occ + s] + 4 * g[j, n_occ + u, k, n_occ + u] + -2 * g[j, k, n_occ + s, n_occ + s] + -2 * g[j, k, n_occ + u, n_occ + u] + 2 * g[i, i, j, k] + -4 * g[i, j, i, k] ) * K[0, j*n_virt + s + n_ex] * K[1, k*n_virt + u] * K[2, i*n_virt + u + n_ex]

										elif ((t == s) and (u != s) and (u != t) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s] += (-2 * g[j, k, n_occ + u, n_occ + v] + 4 * g[j, n_occ + v, k, n_occ + u] ) * K[0, j*n_virt + s + n_ex] * K[1, k*n_virt + u] * K[2, i*n_virt + v + n_ex]

										elif ((t != s) and (u == s) and (v == s)):

											L4[i*n_virt + s] += (-2 * g[j, k, n_occ + s, n_occ + t] + 4 * g[j, n_occ + t, k, n_occ + s] ) * K[0, j*n_virt + t + n_ex] * K[1, k*n_virt + s] * K[2, i*n_virt + s + n_ex]

										elif ((t != s) and (u == t) and (v == s)):

											L4[i*n_virt + s] += (2 * g[i, j, i, k] + -4 * g[i, i, j, k] + -2 * g[j, n_occ + s, k, n_occ + s] + 4 * g[j, k, n_occ + s, n_occ + s] ) * K[0, j*n_virt + t + n_ex] * K[1, k*n_virt + t] * K[2, i*n_virt + s + n_ex]

										elif ((t != s) and (u == t) and (v == t)):

											L4[i*n_virt + s] += (2 * g[j, n_occ + t, k, n_occ + s] + 2 * g[j, k, n_occ + s, n_occ + t] ) * K[0, j*n_virt + t + n_ex] * K[1, k*n_virt + t] * K[2, i*n_virt + t + n_ex]

										elif ((t != s) and (u == t) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s] += (4 * g[j, k, n_occ + s, n_occ + v] + -2 * g[j, n_occ + v, k, n_occ + s] ) * K[0, j*n_virt + t + n_ex] * K[1, k*n_virt + t] * K[2, i*n_virt + v + n_ex]

										elif ((t != s) and (u != s) and (u != t) and (v == u)):

											L4[i*n_virt + s] += (-2 * g[j, k, n_occ + s, n_occ + t] + 4 * g[j, n_occ + t, k, n_occ + s] ) * K[0, j*n_virt + t + n_ex] * K[1, k*n_virt + u] * K[2, i*n_virt + u + n_ex]

									elif ((j != i) and (k != i) and (k != j) and (m == j)):

										if ((t == s) and (u == s) and (v == s)):

											L4[i*n_virt + s] += (-4 * g[i, j, j, k] ) * K[0, j*n_virt + s + n_ex] * K[1, k*n_virt + s] * K[2, j*n_virt + s + n_ex]

										elif ((t == s) and (u != s) and (u != t) and (v == u)):

											L4[i*n_virt + s] += (-2 * g[i, j, j, k] ) * K[0, j*n_virt + s + n_ex] * K[1, k*n_virt + u] * K[2, j*n_virt + u + n_ex]

										elif ((t != s) and (u == t) and (v == s)):

											L4[i*n_virt + s] += (-2 * g[i, j, j, k] ) * K[0, j*n_virt + t + n_ex] * K[1, k*n_virt + t] * K[2, j*n_virt + s + n_ex]

									elif ((j != i) and (k != i) and (k != j) and (m == k)):

										if ((t == s) and (u == s) and (v == s)):

											L4[i*n_virt + s] += (-2 * F[i, j] + 6 * g[i, n_occ + s, j, n_occ + s] + -2 * g[i, j, k, k] + -2 * g[i, k, j, k] ) * K[0, j*n_virt + s + n_ex] * K[1, k*n_virt + s] * K[2, k*n_virt + s + n_ex]

										elif ((t == s) and (u == s) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s] += (2 * g[i, j, n_occ + s, n_occ + v] + 2 * g[i, n_occ + s, j, n_occ + v] ) * K[0, j*n_virt + s + n_ex] * K[1, k*n_virt + s] * K[2, k*n_virt + v + n_ex]

										elif ((t == s) and (u != s) and (u != t) and (v == s)):

											L4[i*n_virt + s] += (2 * g[i, n_occ + u, j, n_occ + s] + 2 * g[i, j, n_occ + s, n_occ + u] ) * K[0, j*n_virt + s + n_ex] * K[1, k*n_virt + u] * K[2, k*n_virt + s + n_ex]

										elif ((t == s) and (u != s) and (u != t) and (v == u)):

											L4[i*n_virt + s] += (-2 * g[i, n_occ + u, j, n_occ + u] + 4 * g[i, j, n_occ + u, n_occ + u] + 2 * g[i, k, j, k] + -4 * g[i, j, k, k] ) * K[0, j*n_virt + s + n_ex] * K[1, k*n_virt + u] * K[2, k*n_virt + u + n_ex]

										elif ((t == s) and (u != s) and (u != t) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s] += (4 * g[i, j, n_occ + u, n_occ + v] + -2 * g[i, n_occ + u, j, n_occ + v] ) * K[0, j*n_virt + s + n_ex] * K[1, k*n_virt + u] * K[2, k*n_virt + v + n_ex]

										elif ((t != s) and (u == s) and (v == s)):

											L4[i*n_virt + s] += (4 * g[i, n_occ + s, j, n_occ + t] + -2 * g[i, j, n_occ + s, n_occ + t] ) * K[0, j*n_virt + t + n_ex] * K[1, k*n_virt + s] * K[2, k*n_virt + s + n_ex]

										elif ((t != s) and (u == t) and (v == s)):

											L4[i*n_virt + s] += (-2 * F[i, j] + 4 * g[i, n_occ + s, j, n_occ + s] + 4 * g[i, n_occ + t, j, n_occ + t] + -2 * g[i, j, n_occ + s, n_occ + s] + -2 * g[i, j, n_occ + t, n_occ + t] + 2 * g[i, j, k, k] + -4 * g[i, k, j, k] ) * K[0, j*n_virt + t + n_ex] * K[1, k*n_virt + t] * K[2, k*n_virt + s + n_ex]

										elif ((t != s) and (u == t) and (v == t)):

											L4[i*n_virt + s] += (4 * g[i, n_occ + s, j, n_occ + t] + -2 * g[i, j, n_occ + s, n_occ + t] ) * K[0, j*n_virt + t + n_ex] * K[1, k*n_virt + t] * K[2, k*n_virt + t + n_ex]

										elif ((t != s) and (u == t) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s] += (-2 * g[i, j, n_occ + s, n_occ + v] + 4 * g[i, n_occ + s, j, n_occ + v] ) * K[0, j*n_virt + t + n_ex] * K[1, k*n_virt + t] * K[2, k*n_virt + v + n_ex]

										elif ((t != s) and (u != s) and (u != t) and (v == s)):

											L4[i*n_virt + s] += (-2 * g[i, j, n_occ + t, n_occ + u] + 4 * g[i, n_occ + u, j, n_occ + t] ) * K[0, j*n_virt + t + n_ex] * K[1, k*n_virt + u] * K[2, k*n_virt + s + n_ex]

									elif ((j != i) and (k != i) and (k != j) and (m != i) and (m != j) and (m != k)):

										if ((t == s) and (u == s) and (v == s)):

											L4[i*n_virt + s] += (-2 * g[i, m, j, k] + -2 * g[i, j, k, m] ) * K[0, j*n_virt + s + n_ex] * K[1, k*n_virt + s] * K[2, m*n_virt + s + n_ex]

										elif ((t == s) and (u != s) and (u != t) and (v == u)):

											L4[i*n_virt + s] += (-4 * g[i, j, k, m] + 2 * g[i, m, j, k] ) * K[0, j*n_virt + s + n_ex] * K[1, k*n_virt + u] * K[2, m*n_virt + u + n_ex]

										elif ((t != s) and (u == t) and (v == s)):

											L4[i*n_virt + s] += (2 * g[i, j, k, m] + -4 * g[i, m, j, k] ) * K[0, j*n_virt + t + n_ex] * K[1, k*n_virt + t] * K[2, m*n_virt + s + n_ex]

	# Current operator combination: {'a': 2, 'b': 1, 'c': 2, 'd': 2}
	for i in range(n_occ):
		for j in range(n_occ):
			for k in range(n_occ):
				for m in range(n_occ):
					for s in range(n_virt):
						for t in range(n_virt):
							for u in range(n_virt):
								for v in range(n_virt):

									if ((j == i) and (k == i) and (m == i)):

										if ((t == s) and (u == s) and (v == s)):

											L4[i*n_virt + s + n_ex] += (-8 * g[i, n_occ + s, i, n_occ + s] ) * K[0, i*n_virt + s + n_ex] * K[1, i*n_virt + s] * K[2, i*n_virt + s + n_ex]

										elif ((t == s) and (u == s) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s + n_ex] += (-6 * g[i, n_occ + s, i, n_occ + v] ) * K[0, i*n_virt + s + n_ex] * K[1, i*n_virt + s] * K[2, i*n_virt + v + n_ex]

										elif ((t == s) and (u != s) and (u != t) and (v == u)):

											L4[i*n_virt + s + n_ex] += (-2 * g[i, n_occ + s, i, n_occ + s] ) * K[0, i*n_virt + s + n_ex] * K[1, i*n_virt + u] * K[2, i*n_virt + u + n_ex]

										elif ((t != s) and (u == s) and (v == s)):

											L4[i*n_virt + s + n_ex] += (-4 * g[i, n_occ + s, i, n_occ + t] ) * K[0, i*n_virt + t + n_ex] * K[1, i*n_virt + s] * K[2, i*n_virt + s + n_ex]

										elif ((t != s) and (u == s) and (v == t)):

											L4[i*n_virt + s + n_ex] += (-2 * g[i, n_occ + t, i, n_occ + t] ) * K[0, i*n_virt + t + n_ex] * K[1, i*n_virt + s] * K[2, i*n_virt + t + n_ex]

										elif ((t != s) and (u == s) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s + n_ex] += (-2 * g[i, n_occ + t, i, n_occ + v] ) * K[0, i*n_virt + t + n_ex] * K[1, i*n_virt + s] * K[2, i*n_virt + v + n_ex]

										elif ((t != s) and (u == t) and (v == s)):

											L4[i*n_virt + s + n_ex] += (-4 * g[i, n_occ + s, i, n_occ + s] ) * K[0, i*n_virt + t + n_ex] * K[1, i*n_virt + t] * K[2, i*n_virt + s + n_ex]

										elif ((t != s) and (u == t) and (v == t)):

											L4[i*n_virt + s + n_ex] += (-6 * g[i, n_occ + s, i, n_occ + t] ) * K[0, i*n_virt + t + n_ex] * K[1, i*n_virt + t] * K[2, i*n_virt + t + n_ex]

										elif ((t != s) and (u == t) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s + n_ex] += (-4 * g[i, n_occ + s, i, n_occ + v] ) * K[0, i*n_virt + t + n_ex] * K[1, i*n_virt + t] * K[2, i*n_virt + v + n_ex]

										elif ((t != s) and (u != s) and (u != t) and (v == u)):

											L4[i*n_virt + s + n_ex] += (-2 * g[i, n_occ + s, i, n_occ + t] ) * K[0, i*n_virt + t + n_ex] * K[1, i*n_virt + u] * K[2, i*n_virt + u + n_ex]

									elif ((j == i) and (k == i) and (m != i) and (m != j) and (m != k)):

										if ((t == s) and (u == s) and (v == s)):

											L4[i*n_virt + s + n_ex] += (-6 * g[i, n_occ + s, m, n_occ + s] ) * K[0, i*n_virt + s + n_ex] * K[1, i*n_virt + s] * K[2, m*n_virt + s + n_ex]

										elif ((t == s) and (u == s) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s + n_ex] += (-8 * g[i, n_occ + s, m, n_occ + v] + 4 * g[i, n_occ + v, m, n_occ + s] ) * K[0, i*n_virt + s + n_ex] * K[1, i*n_virt + s] * K[2, m*n_virt + v + n_ex]

										elif ((t == s) and (u != s) and (u != t) and (v == u)):

											L4[i*n_virt + s + n_ex] += (-2 * g[i, n_occ + s, m, n_occ + s] ) * K[0, i*n_virt + s + n_ex] * K[1, i*n_virt + u] * K[2, m*n_virt + u + n_ex]

										elif ((t != s) and (u == s) and (v == s)):

											L4[i*n_virt + s + n_ex] += (-2 * g[i, n_occ + s, m, n_occ + t] + -2 * g[i, n_occ + t, m, n_occ + s] ) * K[0, i*n_virt + t + n_ex] * K[1, i*n_virt + s] * K[2, m*n_virt + s + n_ex]

										elif ((t != s) and (u == s) and (v == t)):

											L4[i*n_virt + s + n_ex] += (-2 * g[i, n_occ + t, m, n_occ + t] ) * K[0, i*n_virt + t + n_ex] * K[1, i*n_virt + s] * K[2, m*n_virt + t + n_ex]

										elif ((t != s) and (u == s) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s + n_ex] += (-4 * g[i, n_occ + t, m, n_occ + v] + 2 * g[i, n_occ + v, m, n_occ + t] ) * K[0, i*n_virt + t + n_ex] * K[1, i*n_virt + s] * K[2, m*n_virt + v + n_ex]

										elif ((t != s) and (u == t) and (v == s)):

											L4[i*n_virt + s + n_ex] += (-2 * g[i, n_occ + s, m, n_occ + s] ) * K[0, i*n_virt + t + n_ex] * K[1, i*n_virt + t] * K[2, m*n_virt + s + n_ex]

										elif ((t != s) and (u == t) and (v == t)):

											L4[i*n_virt + s + n_ex] += (-8 * g[i, n_occ + s, m, n_occ + t] + 4 * g[i, n_occ + t, m, n_occ + s] ) * K[0, i*n_virt + t + n_ex] * K[1, i*n_virt + t] * K[2, m*n_virt + t + n_ex]

										elif ((t != s) and (u == t) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s + n_ex] += (-4 * g[i, n_occ + s, m, n_occ + v] + 2 * g[i, n_occ + v, m, n_occ + s] ) * K[0, i*n_virt + t + n_ex] * K[1, i*n_virt + t] * K[2, m*n_virt + v + n_ex]

										elif ((t != s) and (u != s) and (u != t) and (v == u)):

											L4[i*n_virt + s + n_ex] += (-4 * g[i, n_occ + s, m, n_occ + t] + 2 * g[i, n_occ + t, m, n_occ + s] ) * K[0, i*n_virt + t + n_ex] * K[1, i*n_virt + u] * K[2, m*n_virt + u + n_ex]

									elif ((j == i) and (k != i) and (k != j) and (m == k)):

										if ((t == s) and (u == s) and (v == s)):

											L4[i*n_virt + s + n_ex] += (-2 * g[i, n_occ + s, i, n_occ + s] ) * K[0, i*n_virt + s + n_ex] * K[1, k*n_virt + s] * K[2, k*n_virt + s + n_ex]

										elif ((t == s) and (u == s) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s + n_ex] += (-2 * g[i, n_occ + s, i, n_occ + v] ) * K[0, i*n_virt + s + n_ex] * K[1, k*n_virt + s] * K[2, k*n_virt + v + n_ex]

										elif ((t != s) and (u == t) and (v == s)):

											L4[i*n_virt + s + n_ex] += (-2 * g[i, n_occ + s, i, n_occ + s] ) * K[0, i*n_virt + t + n_ex] * K[1, k*n_virt + t] * K[2, k*n_virt + s + n_ex]

										elif ((t != s) and (u == t) and (v == t)):

											L4[i*n_virt + s + n_ex] += (-2 * g[i, n_occ + s, i, n_occ + t] ) * K[0, i*n_virt + t + n_ex] * K[1, k*n_virt + t] * K[2, k*n_virt + t + n_ex]

										elif ((t != s) and (u == t) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s + n_ex] += (-2 * g[i, n_occ + s, i, n_occ + v] ) * K[0, i*n_virt + t + n_ex] * K[1, k*n_virt + t] * K[2, k*n_virt + v + n_ex]

									elif ((j != i) and (k == i) and (m == i)):

										if ((t == s) and (u == s) and (v == s)):

											L4[i*n_virt + s + n_ex] += (-4 * g[i, n_occ + s, j, n_occ + s] ) * K[0, j*n_virt + s + n_ex] * K[1, i*n_virt + s] * K[2, i*n_virt + s + n_ex]

										elif ((t == s) and (u == s) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s + n_ex] += (-2 * g[i, n_occ + s, j, n_occ + v] + -2 * g[i, n_occ + v, j, n_occ + s] ) * K[0, j*n_virt + s + n_ex] * K[1, i*n_virt + s] * K[2, i*n_virt + v + n_ex]

										elif ((t != s) and (u == t) and (v == s)):

											L4[i*n_virt + s + n_ex] += (-4 * g[i, n_occ + s, j, n_occ + s] ) * K[0, j*n_virt + t + n_ex] * K[1, i*n_virt + t] * K[2, i*n_virt + s + n_ex]

										elif ((t != s) and (u == t) and (v == t)):

											L4[i*n_virt + s + n_ex] += (-2 * g[i, n_occ + t, j, n_occ + s] + -2 * g[i, n_occ + s, j, n_occ + t] ) * K[0, j*n_virt + t + n_ex] * K[1, i*n_virt + t] * K[2, i*n_virt + t + n_ex]

										elif ((t != s) and (u == t) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s + n_ex] += (-2 * g[i, n_occ + v, j, n_occ + s] + -2 * g[i, n_occ + s, j, n_occ + v] ) * K[0, j*n_virt + t + n_ex] * K[1, i*n_virt + t] * K[2, i*n_virt + v + n_ex]

									elif ((j != i) and (k == i) and (m == j)):

										if ((t == s) and (u == s) and (v == s)):

											L4[i*n_virt + s + n_ex] += (-2 * g[j, n_occ + s, j, n_occ + s] ) * K[0, j*n_virt + s + n_ex] * K[1, i*n_virt + s] * K[2, j*n_virt + s + n_ex]

										elif ((t == s) and (u == s) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s + n_ex] += (-2 * g[j, n_occ + s, j, n_occ + v] ) * K[0, j*n_virt + s + n_ex] * K[1, i*n_virt + s] * K[2, j*n_virt + v + n_ex]

										elif ((t != s) and (u == t) and (v == s)):

											L4[i*n_virt + s + n_ex] += (-2 * g[j, n_occ + s, j, n_occ + s] ) * K[0, j*n_virt + t + n_ex] * K[1, i*n_virt + t] * K[2, j*n_virt + s + n_ex]

										elif ((t != s) and (u == t) and (v == t)):

											L4[i*n_virt + s + n_ex] += (-2 * g[j, n_occ + s, j, n_occ + t] ) * K[0, j*n_virt + t + n_ex] * K[1, i*n_virt + t] * K[2, j*n_virt + t + n_ex]

										elif ((t != s) and (u == t) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s + n_ex] += (-2 * g[j, n_occ + s, j, n_occ + v] ) * K[0, j*n_virt + t + n_ex] * K[1, i*n_virt + t] * K[2, j*n_virt + v + n_ex]

									elif ((j != i) and (k == i) and (m != i) and (m != j) and (m != k)):

										if ((t == s) and (u == s) and (v == s)):

											L4[i*n_virt + s + n_ex] += (-2 * g[j, n_occ + s, m, n_occ + s] ) * K[0, j*n_virt + s + n_ex] * K[1, i*n_virt + s] * K[2, m*n_virt + s + n_ex]

										elif ((t == s) and (u == s) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s + n_ex] += (-4 * g[j, n_occ + s, m, n_occ + v] + 2 * g[j, n_occ + v, m, n_occ + s] ) * K[0, j*n_virt + s + n_ex] * K[1, i*n_virt + s] * K[2, m*n_virt + v + n_ex]

										elif ((t != s) and (u == t) and (v == s)):

											L4[i*n_virt + s + n_ex] += (-2 * g[j, n_occ + s, m, n_occ + s] ) * K[0, j*n_virt + t + n_ex] * K[1, i*n_virt + t] * K[2, m*n_virt + s + n_ex]

										elif ((t != s) and (u == t) and (v == t)):

											L4[i*n_virt + s + n_ex] += (-4 * g[j, n_occ + s, m, n_occ + t] + 2 * g[j, n_occ + t, m, n_occ + s] ) * K[0, j*n_virt + t + n_ex] * K[1, i*n_virt + t] * K[2, m*n_virt + t + n_ex]

										elif ((t != s) and (u == t) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s + n_ex] += (-4 * g[j, n_occ + s, m, n_occ + v] + 2 * g[j, n_occ + v, m, n_occ + s] ) * K[0, j*n_virt + t + n_ex] * K[1, i*n_virt + t] * K[2, m*n_virt + v + n_ex]

									elif ((j != i) and (k == j) and (m == i)):

										if ((t == s) and (u == s) and (v == s)):

											L4[i*n_virt + s + n_ex] += (-4 * g[i, n_occ + s, i, n_occ + s] ) * K[0, j*n_virt + s + n_ex] * K[1, j*n_virt + s] * K[2, i*n_virt + s + n_ex]

										elif ((t == s) and (u == s) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s + n_ex] += (-2 * g[i, n_occ + s, i, n_occ + v] ) * K[0, j*n_virt + s + n_ex] * K[1, j*n_virt + s] * K[2, i*n_virt + v + n_ex]

										elif ((t == s) and (u != s) and (u != t) and (v == u)):

											L4[i*n_virt + s + n_ex] += (-2 * g[i, n_occ + s, i, n_occ + s] ) * K[0, j*n_virt + s + n_ex] * K[1, j*n_virt + u] * K[2, i*n_virt + u + n_ex]

										elif ((t != s) and (u == s) and (v == s)):

											L4[i*n_virt + s + n_ex] += (-4 * g[i, n_occ + s, i, n_occ + t] ) * K[0, j*n_virt + t + n_ex] * K[1, j*n_virt + s] * K[2, i*n_virt + s + n_ex]

										elif ((t != s) and (u == s) and (v == t)):

											L4[i*n_virt + s + n_ex] += (-2 * g[i, n_occ + t, i, n_occ + t] ) * K[0, j*n_virt + t + n_ex] * K[1, j*n_virt + s] * K[2, i*n_virt + t + n_ex]

										elif ((t != s) and (u == s) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s + n_ex] += (-2 * g[i, n_occ + t, i, n_occ + v] ) * K[0, j*n_virt + t + n_ex] * K[1, j*n_virt + s] * K[2, i*n_virt + v + n_ex]

										elif ((t != s) and (u == t) and (v == t)):

											L4[i*n_virt + s + n_ex] += (-2 * g[i, n_occ + s, i, n_occ + t] ) * K[0, j*n_virt + t + n_ex] * K[1, j*n_virt + t] * K[2, i*n_virt + t + n_ex]

										elif ((t != s) and (u != s) and (u != t) and (v == u)):

											L4[i*n_virt + s + n_ex] += (-2 * g[i, n_occ + s, i, n_occ + t] ) * K[0, j*n_virt + t + n_ex] * K[1, j*n_virt + u] * K[2, i*n_virt + u + n_ex]

									elif ((j != i) and (k == j) and (m == j)):

										if ((t == s) and (u == s) and (v == s)):

											L4[i*n_virt + s + n_ex] += (-6 * g[i, n_occ + s, j, n_occ + s] ) * K[0, j*n_virt + s + n_ex] * K[1, j*n_virt + s] * K[2, j*n_virt + s + n_ex]

										elif ((t == s) and (u == s) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s + n_ex] += (-8 * g[i, n_occ + s, j, n_occ + v] + 4 * g[i, n_occ + v, j, n_occ + s] ) * K[0, j*n_virt + s + n_ex] * K[1, j*n_virt + s] * K[2, j*n_virt + v + n_ex]

										elif ((t == s) and (u != s) and (u != t) and (v == u)):

											L4[i*n_virt + s + n_ex] += (-2 * g[i, n_occ + s, j, n_occ + s] ) * K[0, j*n_virt + s + n_ex] * K[1, j*n_virt + u] * K[2, j*n_virt + u + n_ex]

										elif ((t != s) and (u == s) and (v == s)):

											L4[i*n_virt + s + n_ex] += (-2 * g[i, n_occ + t, j, n_occ + s] + -2 * g[i, n_occ + s, j, n_occ + t] ) * K[0, j*n_virt + t + n_ex] * K[1, j*n_virt + s] * K[2, j*n_virt + s + n_ex]

										elif ((t != s) and (u == s) and (v == t)):

											L4[i*n_virt + s + n_ex] += (-2 * g[i, n_occ + t, j, n_occ + t] ) * K[0, j*n_virt + t + n_ex] * K[1, j*n_virt + s] * K[2, j*n_virt + t + n_ex]

										elif ((t != s) and (u == s) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s + n_ex] += (-4 * g[i, n_occ + t, j, n_occ + v] + 2 * g[i, n_occ + v, j, n_occ + t] ) * K[0, j*n_virt + t + n_ex] * K[1, j*n_virt + s] * K[2, j*n_virt + v + n_ex]

										elif ((t != s) and (u == t) and (v == s)):

											L4[i*n_virt + s + n_ex] += (-2 * g[i, n_occ + s, j, n_occ + s] ) * K[0, j*n_virt + t + n_ex] * K[1, j*n_virt + t] * K[2, j*n_virt + s + n_ex]

										elif ((t != s) and (u == t) and (v == t)):

											L4[i*n_virt + s + n_ex] += (-8 * g[i, n_occ + s, j, n_occ + t] + 4 * g[i, n_occ + t, j, n_occ + s] ) * K[0, j*n_virt + t + n_ex] * K[1, j*n_virt + t] * K[2, j*n_virt + t + n_ex]

										elif ((t != s) and (u == t) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s + n_ex] += (-4 * g[i, n_occ + s, j, n_occ + v] + 2 * g[i, n_occ + v, j, n_occ + s] ) * K[0, j*n_virt + t + n_ex] * K[1, j*n_virt + t] * K[2, j*n_virt + v + n_ex]

										elif ((t != s) and (u != s) and (u != t) and (v == u)):

											L4[i*n_virt + s + n_ex] += (-4 * g[i, n_occ + s, j, n_occ + t] + 2 * g[i, n_occ + t, j, n_occ + s] ) * K[0, j*n_virt + t + n_ex] * K[1, j*n_virt + u] * K[2, j*n_virt + u + n_ex]

									elif ((j != i) and (k == j) and (m != i) and (m != j) and (m != k)):

										if ((t == s) and (u == s) and (v == s)):

											L4[i*n_virt + s + n_ex] += (-4 * g[i, n_occ + s, m, n_occ + s] ) * K[0, j*n_virt + s + n_ex] * K[1, j*n_virt + s] * K[2, m*n_virt + s + n_ex]

										elif ((t == s) and (u == s) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s + n_ex] += (-4 * g[i, n_occ + s, m, n_occ + v] + 2 * g[i, n_occ + v, m, n_occ + s] ) * K[0, j*n_virt + s + n_ex] * K[1, j*n_virt + s] * K[2, m*n_virt + v + n_ex]

										elif ((t == s) and (u != s) and (u != t) and (v == u)):

											L4[i*n_virt + s + n_ex] += (-2 * g[i, n_occ + s, m, n_occ + s] ) * K[0, j*n_virt + s + n_ex] * K[1, j*n_virt + u] * K[2, m*n_virt + u + n_ex]

										elif ((t != s) and (u == s) and (v == s)):

											L4[i*n_virt + s + n_ex] += (-2 * g[i, n_occ + t, m, n_occ + s] + -2 * g[i, n_occ + s, m, n_occ + t] ) * K[0, j*n_virt + t + n_ex] * K[1, j*n_virt + s] * K[2, m*n_virt + s + n_ex]

										elif ((t != s) and (u == s) and (v == t)):

											L4[i*n_virt + s + n_ex] += (-2 * g[i, n_occ + t, m, n_occ + t] ) * K[0, j*n_virt + t + n_ex] * K[1, j*n_virt + s] * K[2, m*n_virt + t + n_ex]

										elif ((t != s) and (u == s) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s + n_ex] += (-4 * g[i, n_occ + t, m, n_occ + v] + 2 * g[i, n_occ + v, m, n_occ + t] ) * K[0, j*n_virt + t + n_ex] * K[1, j*n_virt + s] * K[2, m*n_virt + v + n_ex]

										elif ((t != s) and (u == t) and (v == t)):

											L4[i*n_virt + s + n_ex] += (-4 * g[i, n_occ + s, m, n_occ + t] + 2 * g[i, n_occ + t, m, n_occ + s] ) * K[0, j*n_virt + t + n_ex] * K[1, j*n_virt + t] * K[2, m*n_virt + t + n_ex]

										elif ((t != s) and (u != s) and (u != t) and (v == u)):

											L4[i*n_virt + s + n_ex] += (-4 * g[i, n_occ + s, m, n_occ + t] + 2 * g[i, n_occ + t, m, n_occ + s] ) * K[0, j*n_virt + t + n_ex] * K[1, j*n_virt + u] * K[2, m*n_virt + u + n_ex]

									elif ((j != i) and (k != i) and (k != j) and (m == k)):

										if ((t == s) and (u == s) and (v == s)):

											L4[i*n_virt + s + n_ex] += (-2 * g[i, n_occ + s, j, n_occ + s] ) * K[0, j*n_virt + s + n_ex] * K[1, k*n_virt + s] * K[2, k*n_virt + s + n_ex]

										elif ((t == s) and (u == s) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s + n_ex] += (-4 * g[i, n_occ + s, j, n_occ + v] + 2 * g[i, n_occ + v, j, n_occ + s] ) * K[0, j*n_virt + s + n_ex] * K[1, k*n_virt + s] * K[2, k*n_virt + v + n_ex]

										elif ((t != s) and (u == t) and (v == s)):

											L4[i*n_virt + s + n_ex] += (-2 * g[i, n_occ + s, j, n_occ + s] ) * K[0, j*n_virt + t + n_ex] * K[1, k*n_virt + t] * K[2, k*n_virt + s + n_ex]

										elif ((t != s) and (u == t) and (v == t)):

											L4[i*n_virt + s + n_ex] += (-4 * g[i, n_occ + s, j, n_occ + t] + 2 * g[i, n_occ + t, j, n_occ + s] ) * K[0, j*n_virt + t + n_ex] * K[1, k*n_virt + t] * K[2, k*n_virt + t + n_ex]

										elif ((t != s) and (u == t) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s + n_ex] += (-4 * g[i, n_occ + s, j, n_occ + v] + 2 * g[i, n_occ + v, j, n_occ + s] ) * K[0, j*n_virt + t + n_ex] * K[1, k*n_virt + t] * K[2, k*n_virt + v + n_ex]

	# Current operator combination: {'a': 2, 'b': 1, 'c': 2, 'd': 3}
	# All terms vanished for this combination

	# Current operator combination: {'a': 2, 'b': 1, 'c': 3, 'd': 1}
	# This combination was excluded by the contr_type_only argument {'a': 2, 'b': 1, 'c': 3, 'd': 1}

	# Current operator combination: {'a': 2, 'b': 1, 'c': 3, 'd': 2}
	# This combination was excluded by the contr_type_only argument {'a': 2, 'b': 1, 'c': 3, 'd': 2}

	# Current operator combination: {'a': 2, 'b': 1, 'c': 3, 'd': 3}
	# This combination was excluded by the contr_type_only argument {'a': 2, 'b': 1, 'c': 3, 'd': 3}

	# Current operator combination: {'a': 2, 'b': 2, 'c': 1, 'd': 1}
	for i in range(n_occ):
		for j in range(n_occ):
			for k in range(n_occ):
				for m in range(n_occ):
					for s in range(n_virt):
						for t in range(n_virt):
							for u in range(n_virt):
								for v in range(n_virt):

									if ((j == i) and (k == i) and (m == i)):

										if ((t == s) and (u == s) and (v == s)):

											L4[i*n_virt + s] += (4 * F[n_occ + s, n_occ + s] + -4 * F[i, i] + 4 * g[i, i, n_occ + s, n_occ + s] + 16 * g[i, n_occ + s, i, n_occ + s] + -4 * g[n_occ + s, n_occ + s, n_occ + s, n_occ + s] + -4 * g[i, i, i, i] ) * K[0, i*n_virt + s] * K[1, i*n_virt + s + n_ex] * K[2, i*n_virt + s + n_ex]

										elif ((t == s) and (u == s) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s] += (2 * F[n_occ + s, n_occ + v] + -4 * g[n_occ + s, n_occ + s, n_occ + s, n_occ + v] + 2 * g[i, i, n_occ + s, n_occ + v] + 8 * g[i, n_occ + s, i, n_occ + v] ) * K[0, i*n_virt + s] * K[1, i*n_virt + s + n_ex] * K[2, i*n_virt + v + n_ex]

										elif ((t == s) and (u != s) and (u != t) and (v == s)):

											L4[i*n_virt + s] += (2 * F[n_occ + s, n_occ + u] + 2 * g[i, i, n_occ + s, n_occ + u] + 8 * g[i, n_occ + s, i, n_occ + u] + -4 * g[n_occ + s, n_occ + s, n_occ + s, n_occ + u] ) * K[0, i*n_virt + s] * K[1, i*n_virt + u + n_ex] * K[2, i*n_virt + s + n_ex]

										elif ((t == s) and (u != s) and (u != t) and (v == u)):

											L4[i*n_virt + s] += (-4 * g[n_occ + s, n_occ + u, n_occ + s, n_occ + u] ) * K[0, i*n_virt + s] * K[1, i*n_virt + u + n_ex] * K[2, i*n_virt + u + n_ex]

										elif ((t == s) and (u != s) and (u != t) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s] += (-4 * g[n_occ + s, n_occ + u, n_occ + s, n_occ + v] ) * K[0, i*n_virt + s] * K[1, i*n_virt + u + n_ex] * K[2, i*n_virt + v + n_ex]

										elif ((t != s) and (u == s) and (v == s)):

											L4[i*n_virt + s] += (4 * F[n_occ + s, n_occ + t] + -4 * g[n_occ + s, n_occ + s, n_occ + s, n_occ + t] + 12 * g[i, n_occ + s, i, n_occ + t] ) * K[0, i*n_virt + t] * K[1, i*n_virt + s + n_ex] * K[2, i*n_virt + s + n_ex]

										elif ((t != s) and (u == s) and (v == t)):

											L4[i*n_virt + s] += (-2 * F[i, i] + 2 * F[n_occ + t, n_occ + t] + -2 * g[n_occ + s, n_occ + s, n_occ + t, n_occ + t] + -2 * g[n_occ + s, n_occ + t, n_occ + s, n_occ + t] + 6 * g[i, n_occ + t, i, n_occ + t] + 2 * g[i, i, n_occ + s, n_occ + s] + 2 * g[i, n_occ + s, i, n_occ + s] + -2 * g[i, i, i, i] ) * K[0, i*n_virt + t] * K[1, i*n_virt + s + n_ex] * K[2, i*n_virt + t + n_ex]

										elif ((t != s) and (u == s) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s] += (2 * F[n_occ + t, n_occ + v] + -2 * g[n_occ + s, n_occ + t, n_occ + s, n_occ + v] + -2 * g[n_occ + s, n_occ + s, n_occ + t, n_occ + v] + 6 * g[i, n_occ + t, i, n_occ + v] ) * K[0, i*n_virt + t] * K[1, i*n_virt + s + n_ex] * K[2, i*n_virt + v + n_ex]

										elif ((t != s) and (u == t) and (v == s)):

											L4[i*n_virt + s] += (-2 * F[i, i] + 2 * F[n_occ + t, n_occ + t] + -2 * g[n_occ + s, n_occ + s, n_occ + t, n_occ + t] + -2 * g[n_occ + s, n_occ + t, n_occ + s, n_occ + t] + 6 * g[i, n_occ + t, i, n_occ + t] + 2 * g[i, i, n_occ + s, n_occ + s] + 2 * g[i, n_occ + s, i, n_occ + s] + -2 * g[i, i, i, i] ) * K[0, i*n_virt + t] * K[1, i*n_virt + t + n_ex] * K[2, i*n_virt + s + n_ex]

										elif ((t != s) and (u == t) and (v == t)):

											L4[i*n_virt + s] += (-4 * g[n_occ + s, n_occ + t, n_occ + t, n_occ + t] + 4 * g[i, n_occ + s, i, n_occ + t] + 4 * g[i, i, n_occ + s, n_occ + t] ) * K[0, i*n_virt + t] * K[1, i*n_virt + t + n_ex] * K[2, i*n_virt + t + n_ex]

										elif ((t != s) and (u == t) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s] += (-2 * g[n_occ + s, n_occ + v, n_occ + t, n_occ + t] + -2 * g[n_occ + s, n_occ + t, n_occ + t, n_occ + v] + 2 * g[i, i, n_occ + s, n_occ + v] + 2 * g[i, n_occ + s, i, n_occ + v] ) * K[0, i*n_virt + t] * K[1, i*n_virt + t + n_ex] * K[2, i*n_virt + v + n_ex]

										elif ((t != s) and (u != s) and (u != t) and (v == s)):

											L4[i*n_virt + s] += (2 * F[n_occ + t, n_occ + u] + -2 * g[n_occ + s, n_occ + s, n_occ + t, n_occ + u] + -2 * g[n_occ + s, n_occ + t, n_occ + s, n_occ + u] + 6 * g[i, n_occ + t, i, n_occ + u] ) * K[0, i*n_virt + t] * K[1, i*n_virt + u + n_ex] * K[2, i*n_virt + s + n_ex]

										elif ((t != s) and (u != s) and (u != t) and (v == t)):

											L4[i*n_virt + s] += (-2 * g[n_occ + s, n_occ + t, n_occ + t, n_occ + u] + -2 * g[n_occ + s, n_occ + u, n_occ + t, n_occ + t] + 2 * g[i, n_occ + s, i, n_occ + u] + 2 * g[i, i, n_occ + s, n_occ + u] ) * K[0, i*n_virt + t] * K[1, i*n_virt + u + n_ex] * K[2, i*n_virt + t + n_ex]

										elif ((t != s) and (u != s) and (u != t) and (v == u)):

											L4[i*n_virt + s] += (-4 * g[n_occ + s, n_occ + u, n_occ + t, n_occ + u] ) * K[0, i*n_virt + t] * K[1, i*n_virt + u + n_ex] * K[2, i*n_virt + u + n_ex]

										elif ((t != s) and (u != s) and (u != t) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s] += (-2 * g[n_occ + s, n_occ + v, n_occ + t, n_occ + u] + -2 * g[n_occ + s, n_occ + u, n_occ + t, n_occ + v] ) * K[0, i*n_virt + t] * K[1, i*n_virt + u + n_ex] * K[2, i*n_virt + v + n_ex]

									elif ((j == i) and (k == i) and (m != i) and (m != j) and (m != k)):

										if ((t == s) and (u == s) and (v == s)):

											L4[i*n_virt + s] += (-2 * F[i, m] + 2 * g[i, m, n_occ + s, n_occ + s] + -4 * g[i, i, i, m] + 8 * g[i, n_occ + s, m, n_occ + s] ) * K[0, i*n_virt + s] * K[1, i*n_virt + s + n_ex] * K[2, m*n_virt + s + n_ex]

										elif ((t == s) and (u == s) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s] += (-4 * g[i, m, n_occ + s, n_occ + v] + 8 * g[i, n_occ + s, m, n_occ + v] ) * K[0, i*n_virt + s] * K[1, i*n_virt + s + n_ex] * K[2, m*n_virt + v + n_ex]

										elif ((t == s) and (u != s) and (u != t) and (v == s)):

											L4[i*n_virt + s] += (6 * g[i, m, n_occ + s, n_occ + u] ) * K[0, i*n_virt + s] * K[1, i*n_virt + u + n_ex] * K[2, m*n_virt + s + n_ex]

										elif ((t != s) and (u == s) and (v == s)):

											L4[i*n_virt + s] += (6 * g[i, n_occ + t, m, n_occ + s] ) * K[0, i*n_virt + t] * K[1, i*n_virt + s + n_ex] * K[2, m*n_virt + s + n_ex]

										elif ((t != s) and (u == s) and (v == t)):

											L4[i*n_virt + s] += (4 * g[i, m, n_occ + s, n_occ + s] + -2 * g[i, i, i, m] + 4 * g[i, n_occ + t, m, n_occ + t] + -2 * g[i, m, n_occ + t, n_occ + t] + -2 * g[i, n_occ + s, m, n_occ + s] ) * K[0, i*n_virt + t] * K[1, i*n_virt + s + n_ex] * K[2, m*n_virt + t + n_ex]

										elif ((t != s) and (u == s) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s] += (-2 * g[i, m, n_occ + t, n_occ + v] + 4 * g[i, n_occ + t, m, n_occ + v] ) * K[0, i*n_virt + t] * K[1, i*n_virt + s + n_ex] * K[2, m*n_virt + v + n_ex]

										elif ((t != s) and (u == t) and (v == s)):

											L4[i*n_virt + s] += (-2 * F[i, m] + 2 * g[i, n_occ + t, m, n_occ + t] + 2 * g[i, m, n_occ + t, n_occ + t] + 4 * g[i, n_occ + s, m, n_occ + s] + -2 * g[i, m, n_occ + s, n_occ + s] + -2 * g[i, i, i, m] ) * K[0, i*n_virt + t] * K[1, i*n_virt + t + n_ex] * K[2, m*n_virt + s + n_ex]

										elif ((t != s) and (u == t) and (v == t)):

											L4[i*n_virt + s] += (2 * g[i, m, n_occ + s, n_occ + t] + 2 * g[i, n_occ + s, m, n_occ + t] ) * K[0, i*n_virt + t] * K[1, i*n_virt + t + n_ex] * K[2, m*n_virt + t + n_ex]

										elif ((t != s) and (u == t) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s] += (4 * g[i, n_occ + s, m, n_occ + v] + -2 * g[i, m, n_occ + s, n_occ + v] ) * K[0, i*n_virt + t] * K[1, i*n_virt + t + n_ex] * K[2, m*n_virt + v + n_ex]

										elif ((t != s) and (u != s) and (u != t) and (v == s)):

											L4[i*n_virt + s] += (2 * g[i, n_occ + t, m, n_occ + u] + 2 * g[i, m, n_occ + t, n_occ + u] ) * K[0, i*n_virt + t] * K[1, i*n_virt + u + n_ex] * K[2, m*n_virt + s + n_ex]

										elif ((t != s) and (u != s) and (u != t) and (v == t)):

											L4[i*n_virt + s] += (4 * g[i, m, n_occ + s, n_occ + u] + -2 * g[i, n_occ + s, m, n_occ + u] ) * K[0, i*n_virt + t] * K[1, i*n_virt + u + n_ex] * K[2, m*n_virt + t + n_ex]

									elif ((j == i) and (k != i) and (k != j) and (m == i)):

										if ((t == s) and (u == s) and (v == s)):

											L4[i*n_virt + s] += (-2 * F[i, k] + 8 * g[i, n_occ + s, k, n_occ + s] + -4 * g[i, i, i, k] + 2 * g[i, k, n_occ + s, n_occ + s] ) * K[0, i*n_virt + s] * K[1, k*n_virt + s + n_ex] * K[2, i*n_virt + s + n_ex]

										elif ((t == s) and (u == s) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s] += (6 * g[i, k, n_occ + s, n_occ + v] ) * K[0, i*n_virt + s] * K[1, k*n_virt + s + n_ex] * K[2, i*n_virt + v + n_ex]

										elif ((t == s) and (u != s) and (u != t) and (v == s)):

											L4[i*n_virt + s] += (-4 * g[i, k, n_occ + s, n_occ + u] + 8 * g[i, n_occ + s, k, n_occ + u] ) * K[0, i*n_virt + s] * K[1, k*n_virt + u + n_ex] * K[2, i*n_virt + s + n_ex]

										elif ((t != s) and (u == s) and (v == s)):

											L4[i*n_virt + s] += (6 * g[i, n_occ + t, k, n_occ + s] ) * K[0, i*n_virt + t] * K[1, k*n_virt + s + n_ex] * K[2, i*n_virt + s + n_ex]

										elif ((t != s) and (u == s) and (v == t)):

											L4[i*n_virt + s] += (-2 * F[i, k] + 2 * g[i, n_occ + t, k, n_occ + t] + 2 * g[i, k, n_occ + t, n_occ + t] + 4 * g[i, n_occ + s, k, n_occ + s] + -2 * g[i, k, n_occ + s, n_occ + s] + -2 * g[i, i, i, k] ) * K[0, i*n_virt + t] * K[1, k*n_virt + s + n_ex] * K[2, i*n_virt + t + n_ex]

										elif ((t != s) and (u == s) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s] += (2 * g[i, n_occ + t, k, n_occ + v] + 2 * g[i, k, n_occ + t, n_occ + v] ) * K[0, i*n_virt + t] * K[1, k*n_virt + s + n_ex] * K[2, i*n_virt + v + n_ex]

										elif ((t != s) and (u == t) and (v == s)):

											L4[i*n_virt + s] += (4 * g[i, k, n_occ + s, n_occ + s] + -2 * g[i, i, i, k] + 4 * g[i, n_occ + t, k, n_occ + t] + -2 * g[i, k, n_occ + t, n_occ + t] + -2 * g[i, n_occ + s, k, n_occ + s] ) * K[0, i*n_virt + t] * K[1, k*n_virt + t + n_ex] * K[2, i*n_virt + s + n_ex]

										elif ((t != s) and (u == t) and (v == t)):

											L4[i*n_virt + s] += (2 * g[i, k, n_occ + s, n_occ + t] + 2 * g[i, n_occ + s, k, n_occ + t] ) * K[0, i*n_virt + t] * K[1, k*n_virt + t + n_ex] * K[2, i*n_virt + t + n_ex]

										elif ((t != s) and (u == t) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s] += (4 * g[i, k, n_occ + s, n_occ + v] + -2 * g[i, n_occ + s, k, n_occ + v] ) * K[0, i*n_virt + t] * K[1, k*n_virt + t + n_ex] * K[2, i*n_virt + v + n_ex]

										elif ((t != s) and (u != s) and (u != t) and (v == s)):

											L4[i*n_virt + s] += (-2 * g[i, k, n_occ + t, n_occ + u] + 4 * g[i, n_occ + t, k, n_occ + u] ) * K[0, i*n_virt + t] * K[1, k*n_virt + u + n_ex] * K[2, i*n_virt + s + n_ex]

										elif ((t != s) and (u != s) and (u != t) and (v == t)):

											L4[i*n_virt + s] += (4 * g[i, n_occ + s, k, n_occ + u] + -2 * g[i, k, n_occ + s, n_occ + u] ) * K[0, i*n_virt + t] * K[1, k*n_virt + u + n_ex] * K[2, i*n_virt + t + n_ex]

									elif ((j == i) and (k != i) and (k != j) and (m == k)):

										if ((t == s) and (u == s) and (v == s)):

											L4[i*n_virt + s] += (-4 * g[i, k, i, k] ) * K[0, i*n_virt + s] * K[1, k*n_virt + s + n_ex] * K[2, k*n_virt + s + n_ex]

										elif ((t != s) and (u == s) and (v == t)):

											L4[i*n_virt + s] += (-2 * g[i, k, i, k] ) * K[0, i*n_virt + t] * K[1, k*n_virt + s + n_ex] * K[2, k*n_virt + t + n_ex]

										elif ((t != s) and (u == t) and (v == s)):

											L4[i*n_virt + s] += (-2 * g[i, k, i, k] ) * K[0, i*n_virt + t] * K[1, k*n_virt + t + n_ex] * K[2, k*n_virt + s + n_ex]

									elif ((j == i) and (k != i) and (k != j) and (m != i) and (m != j) and (m != k)):

										if ((t == s) and (u == s) and (v == s)):

											L4[i*n_virt + s] += (-4 * g[i, k, i, m] ) * K[0, i*n_virt + s] * K[1, k*n_virt + s + n_ex] * K[2, m*n_virt + s + n_ex]

										elif ((t != s) and (u == s) and (v == t)):

											L4[i*n_virt + s] += (-2 * g[i, k, i, m] ) * K[0, i*n_virt + t] * K[1, k*n_virt + s + n_ex] * K[2, m*n_virt + t + n_ex]

										elif ((t != s) and (u == t) and (v == s)):

											L4[i*n_virt + s] += (-2 * g[i, k, i, m] ) * K[0, i*n_virt + t] * K[1, k*n_virt + t + n_ex] * K[2, m*n_virt + s + n_ex]

									elif ((j != i) and (k == i) and (m == i)):

										if ((t == s) and (u == s) and (v == s)):

											L4[i*n_virt + s] += (-4 * F[i, j] + 12 * g[i, n_occ + s, j, n_occ + s] + -4 * g[i, i, i, j] ) * K[0, j*n_virt + s] * K[1, i*n_virt + s + n_ex] * K[2, i*n_virt + s + n_ex]

										elif ((t == s) and (u == s) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s] += (6 * g[i, n_occ + v, j, n_occ + s] ) * K[0, j*n_virt + s] * K[1, i*n_virt + s + n_ex] * K[2, i*n_virt + v + n_ex]

										elif ((t == s) and (u != s) and (u != t) and (v == s)):

											L4[i*n_virt + s] += (6 * g[i, n_occ + u, j, n_occ + s] ) * K[0, j*n_virt + s] * K[1, i*n_virt + u + n_ex] * K[2, i*n_virt + s + n_ex]

										elif ((t != s) and (u == s) and (v == s)):

											L4[i*n_virt + s] += (-4 * g[i, j, n_occ + s, n_occ + t] + 8 * g[i, n_occ + s, j, n_occ + t] ) * K[0, j*n_virt + t] * K[1, i*n_virt + s + n_ex] * K[2, i*n_virt + s + n_ex]

										elif ((t != s) and (u == s) and (v == t)):

											L4[i*n_virt + s] += (-2 * F[i, j] + 2 * g[i, n_occ + s, j, n_occ + s] + 2 * g[i, j, n_occ + s, n_occ + s] + 4 * g[i, n_occ + t, j, n_occ + t] + -2 * g[i, j, n_occ + t, n_occ + t] + -2 * g[i, i, i, j] ) * K[0, j*n_virt + t] * K[1, i*n_virt + s + n_ex] * K[2, i*n_virt + t + n_ex]

										elif ((t != s) and (u == s) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s] += (-2 * g[i, j, n_occ + t, n_occ + v] + 4 * g[i, n_occ + v, j, n_occ + t] ) * K[0, j*n_virt + t] * K[1, i*n_virt + s + n_ex] * K[2, i*n_virt + v + n_ex]

										elif ((t != s) and (u == t) and (v == s)):

											L4[i*n_virt + s] += (-2 * F[i, j] + 2 * g[i, n_occ + s, j, n_occ + s] + 2 * g[i, j, n_occ + s, n_occ + s] + 4 * g[i, n_occ + t, j, n_occ + t] + -2 * g[i, j, n_occ + t, n_occ + t] + -2 * g[i, i, i, j] ) * K[0, j*n_virt + t] * K[1, i*n_virt + t + n_ex] * K[2, i*n_virt + s + n_ex]

										elif ((t != s) and (u == t) and (v == t)):

											L4[i*n_virt + s] += (4 * g[i, n_occ + t, j, n_occ + s] + 4 * g[i, j, n_occ + s, n_occ + t] ) * K[0, j*n_virt + t] * K[1, i*n_virt + t + n_ex] * K[2, i*n_virt + t + n_ex]

										elif ((t != s) and (u == t) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s] += (2 * g[i, n_occ + v, j, n_occ + s] + 2 * g[i, j, n_occ + s, n_occ + v] ) * K[0, j*n_virt + t] * K[1, i*n_virt + t + n_ex] * K[2, i*n_virt + v + n_ex]

										elif ((t != s) and (u != s) and (u != t) and (v == s)):

											L4[i*n_virt + s] += (-2 * g[i, j, n_occ + t, n_occ + u] + 4 * g[i, n_occ + u, j, n_occ + t] ) * K[0, j*n_virt + t] * K[1, i*n_virt + u + n_ex] * K[2, i*n_virt + s + n_ex]

										elif ((t != s) and (u != s) and (u != t) and (v == t)):

											L4[i*n_virt + s] += (2 * g[i, n_occ + u, j, n_occ + s] + 2 * g[i, j, n_occ + s, n_occ + u] ) * K[0, j*n_virt + t] * K[1, i*n_virt + u + n_ex] * K[2, i*n_virt + t + n_ex]

									elif ((j != i) and (k == i) and (m == j)):

										if ((t == s) and (u == s) and (v == s)):

											L4[i*n_virt + s] += (2 * F[n_occ + s, n_occ + s] + -2 * F[j, j] + -2 * g[n_occ + s, n_occ + s, n_occ + s, n_occ + s] + 2 * g[i, i, n_occ + s, n_occ + s] + 6 * g[j, n_occ + s, j, n_occ + s] + -2 * g[i, i, j, j] + 2 * g[i, n_occ + s, i, n_occ + s] + -2 * g[i, j, i, j] ) * K[0, j*n_virt + s] * K[1, i*n_virt + s + n_ex] * K[2, j*n_virt + s + n_ex]

										elif ((t == s) and (u == s) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s] += (-2 * g[n_occ + s, n_occ + s, n_occ + s, n_occ + v] + 4 * g[i, i, n_occ + s, n_occ + v] + 4 * g[j, n_occ + s, j, n_occ + v] + -2 * g[i, n_occ + s, i, n_occ + v] + -2 * g[j, j, n_occ + s, n_occ + v] ) * K[0, j*n_virt + s] * K[1, i*n_virt + s + n_ex] * K[2, j*n_virt + v + n_ex]

										elif ((t == s) and (u != s) and (u != t) and (v == s)):

											L4[i*n_virt + s] += (2 * F[n_occ + s, n_occ + u] + -2 * g[n_occ + s, n_occ + s, n_occ + s, n_occ + u] + 2 * g[j, j, n_occ + s, n_occ + u] + 4 * g[i, n_occ + s, i, n_occ + u] + -2 * g[i, i, n_occ + s, n_occ + u] + 2 * g[j, n_occ + s, j, n_occ + u] ) * K[0, j*n_virt + s] * K[1, i*n_virt + u + n_ex] * K[2, j*n_virt + s + n_ex]

										elif ((t == s) and (u != s) and (u != t) and (v == u)):

											L4[i*n_virt + s] += (-2 * g[n_occ + s, n_occ + u, n_occ + s, n_occ + u] ) * K[0, j*n_virt + s] * K[1, i*n_virt + u + n_ex] * K[2, j*n_virt + u + n_ex]

										elif ((t == s) and (u != s) and (u != t) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s] += (-2 * g[n_occ + s, n_occ + u, n_occ + s, n_occ + v] ) * K[0, j*n_virt + s] * K[1, i*n_virt + u + n_ex] * K[2, j*n_virt + v + n_ex]

										elif ((t != s) and (u == s) and (v == s)):

											L4[i*n_virt + s] += (2 * F[n_occ + s, n_occ + t] + -2 * g[n_occ + s, n_occ + s, n_occ + s, n_occ + t] + 2 * g[i, i, n_occ + s, n_occ + t] + -2 * g[j, j, n_occ + s, n_occ + t] + 4 * g[j, n_occ + s, j, n_occ + t] + 2 * g[i, n_occ + s, i, n_occ + t] ) * K[0, j*n_virt + t] * K[1, i*n_virt + s + n_ex] * K[2, j*n_virt + s + n_ex]

										elif ((t != s) and (u == s) and (v == t)):

											L4[i*n_virt + s] += (2 * g[n_occ + s, n_occ + t, n_occ + s, n_occ + t] + -4 * g[n_occ + s, n_occ + s, n_occ + t, n_occ + t] + -2 * g[i, n_occ + t, i, n_occ + t] + 4 * g[i, i, n_occ + t, n_occ + t] + 2 * g[i, j, i, j] + -4 * g[i, i, j, j] + 4 * g[j, j, n_occ + s, n_occ + s] + -2 * g[j, n_occ + s, j, n_occ + s] ) * K[0, j*n_virt + t] * K[1, i*n_virt + s + n_ex] * K[2, j*n_virt + t + n_ex]

										elif ((t != s) and (u == s) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s] += (2 * g[n_occ + s, n_occ + t, n_occ + s, n_occ + v] + -4 * g[n_occ + s, n_occ + s, n_occ + t, n_occ + v] + -2 * g[i, n_occ + t, i, n_occ + v] + 4 * g[i, i, n_occ + t, n_occ + v] ) * K[0, j*n_virt + t] * K[1, i*n_virt + s + n_ex] * K[2, j*n_virt + v + n_ex]

										elif ((t != s) and (u == t) and (v == s)):

											L4[i*n_virt + s] += (-2 * F[j, j] + 2 * F[n_occ + t, n_occ + t] + -4 * g[n_occ + s, n_occ + t, n_occ + s, n_occ + t] + 2 * g[n_occ + s, n_occ + s, n_occ + t, n_occ + t] + -2 * g[i, i, n_occ + t, n_occ + t] + -2 * g[j, j, n_occ + t, n_occ + t] + 4 * g[i, n_occ + t, i, n_occ + t] + 4 * g[j, n_occ + s, j, n_occ + s] + 4 * g[j, n_occ + t, j, n_occ + t] + -4 * g[i, j, i, j] + 2 * g[i, i, j, j] + -2 * g[j, j, n_occ + s, n_occ + s] ) * K[0, j*n_virt + t] * K[1, i*n_virt + t + n_ex] * K[2, j*n_virt + s + n_ex]

										elif ((t != s) and (u == t) and (v == t)):

											L4[i*n_virt + s] += (-2 * g[n_occ + s, n_occ + t, n_occ + t, n_occ + t] + 2 * g[j, n_occ + s, j, n_occ + t] + 2 * g[j, j, n_occ + s, n_occ + t] ) * K[0, j*n_virt + t] * K[1, i*n_virt + t + n_ex] * K[2, j*n_virt + t + n_ex]

										elif ((t != s) and (u == t) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s] += (-4 * g[n_occ + s, n_occ + t, n_occ + t, n_occ + v] + 2 * g[n_occ + s, n_occ + v, n_occ + t, n_occ + t] + 4 * g[j, n_occ + s, j, n_occ + v] + -2 * g[j, j, n_occ + s, n_occ + v] ) * K[0, j*n_virt + t] * K[1, i*n_virt + t + n_ex] * K[2, j*n_virt + v + n_ex]

										elif ((t != s) and (u != s) and (u != t) and (v == s)):

											L4[i*n_virt + s] += (2 * F[n_occ + t, n_occ + u] + -4 * g[n_occ + s, n_occ + t, n_occ + s, n_occ + u] + 2 * g[n_occ + s, n_occ + s, n_occ + t, n_occ + u] + -2 * g[i, i, n_occ + t, n_occ + u] + -2 * g[j, j, n_occ + t, n_occ + u] + 4 * g[i, n_occ + t, i, n_occ + u] + 4 * g[j, n_occ + t, j, n_occ + u] ) * K[0, j*n_virt + t] * K[1, i*n_virt + u + n_ex] * K[2, j*n_virt + s + n_ex]

										elif ((t != s) and (u != s) and (u != t) and (v == t)):

											L4[i*n_virt + s] += (2 * g[n_occ + s, n_occ + t, n_occ + t, n_occ + u] + -4 * g[n_occ + s, n_occ + u, n_occ + t, n_occ + t] + -2 * g[j, n_occ + s, j, n_occ + u] + 4 * g[j, j, n_occ + s, n_occ + u] ) * K[0, j*n_virt + t] * K[1, i*n_virt + u + n_ex] * K[2, j*n_virt + t + n_ex]

										elif ((t != s) and (u != s) and (u != t) and (v == u)):

											L4[i*n_virt + s] += (-2 * g[n_occ + s, n_occ + u, n_occ + t, n_occ + u] ) * K[0, j*n_virt + t] * K[1, i*n_virt + u + n_ex] * K[2, j*n_virt + u + n_ex]

										elif ((t != s) and (u != s) and (u != t) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s] += (-4 * g[n_occ + s, n_occ + u, n_occ + t, n_occ + v] + 2 * g[n_occ + s, n_occ + v, n_occ + t, n_occ + u] ) * K[0, j*n_virt + t] * K[1, i*n_virt + u + n_ex] * K[2, j*n_virt + v + n_ex]

									elif ((j != i) and (k == i) and (m != i) and (m != j) and (m != k)):

										if ((t == s) and (u == s) and (v == s)):

											L4[i*n_virt + s] += (-2 * F[j, m] + 6 * g[j, n_occ + s, m, n_occ + s] + -2 * g[i, i, j, m] + -2 * g[i, j, i, m] ) * K[0, j*n_virt + s] * K[1, i*n_virt + s + n_ex] * K[2, m*n_virt + s + n_ex]

										elif ((t == s) and (u == s) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s] += (-2 * g[j, m, n_occ + s, n_occ + v] + 4 * g[j, n_occ + s, m, n_occ + v] ) * K[0, j*n_virt + s] * K[1, i*n_virt + s + n_ex] * K[2, m*n_virt + v + n_ex]

										elif ((t == s) and (u != s) and (u != t) and (v == s)):

											L4[i*n_virt + s] += (2 * g[j, n_occ + s, m, n_occ + u] + 2 * g[j, m, n_occ + s, n_occ + u] ) * K[0, j*n_virt + s] * K[1, i*n_virt + u + n_ex] * K[2, m*n_virt + s + n_ex]

										elif ((t != s) and (u == s) and (v == s)):

											L4[i*n_virt + s] += (-2 * g[j, m, n_occ + s, n_occ + t] + 4 * g[j, n_occ + t, m, n_occ + s] ) * K[0, j*n_virt + t] * K[1, i*n_virt + s + n_ex] * K[2, m*n_virt + s + n_ex]

										elif ((t != s) and (u == s) and (v == t)):

											L4[i*n_virt + s] += (-2 * g[j, n_occ + s, m, n_occ + s] + 4 * g[j, m, n_occ + s, n_occ + s] + 2 * g[i, j, i, m] + -4 * g[i, i, j, m] ) * K[0, j*n_virt + t] * K[1, i*n_virt + s + n_ex] * K[2, m*n_virt + t + n_ex]

										elif ((t != s) and (u == t) and (v == s)):

											L4[i*n_virt + s] += (-2 * F[j, m] + 4 * g[j, n_occ + s, m, n_occ + s] + 4 * g[j, n_occ + t, m, n_occ + t] + -2 * g[j, m, n_occ + s, n_occ + s] + -2 * g[j, m, n_occ + t, n_occ + t] + 2 * g[i, i, j, m] + -4 * g[i, j, i, m] ) * K[0, j*n_virt + t] * K[1, i*n_virt + t + n_ex] * K[2, m*n_virt + s + n_ex]

										elif ((t != s) and (u == t) and (v == t)):

											L4[i*n_virt + s] += (2 * g[j, n_occ + s, m, n_occ + t] + 2 * g[j, m, n_occ + s, n_occ + t] ) * K[0, j*n_virt + t] * K[1, i*n_virt + t + n_ex] * K[2, m*n_virt + t + n_ex]

										elif ((t != s) and (u == t) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s] += (-2 * g[j, m, n_occ + s, n_occ + v] + 4 * g[j, n_occ + s, m, n_occ + v] ) * K[0, j*n_virt + t] * K[1, i*n_virt + t + n_ex] * K[2, m*n_virt + v + n_ex]

										elif ((t != s) and (u != s) and (u != t) and (v == s)):

											L4[i*n_virt + s] += (-2 * g[j, m, n_occ + t, n_occ + u] + 4 * g[j, n_occ + t, m, n_occ + u] ) * K[0, j*n_virt + t] * K[1, i*n_virt + u + n_ex] * K[2, m*n_virt + s + n_ex]

										elif ((t != s) and (u != s) and (u != t) and (v == t)):

											L4[i*n_virt + s] += (4 * g[j, m, n_occ + s, n_occ + u] + -2 * g[j, n_occ + s, m, n_occ + u] ) * K[0, j*n_virt + t] * K[1, i*n_virt + u + n_ex] * K[2, m*n_virt + t + n_ex]

									elif ((j != i) and (k == j) and (m == i)):

										if ((t == s) and (u == s) and (v == s)):

											L4[i*n_virt + s] += (2 * F[n_occ + s, n_occ + s] + -2 * F[j, j] + -2 * g[n_occ + s, n_occ + s, n_occ + s, n_occ + s] + 2 * g[i, i, n_occ + s, n_occ + s] + 6 * g[j, n_occ + s, j, n_occ + s] + -2 * g[i, i, j, j] + 2 * g[i, n_occ + s, i, n_occ + s] + -2 * g[i, j, i, j] ) * K[0, j*n_virt + s] * K[1, j*n_virt + s + n_ex] * K[2, i*n_virt + s + n_ex]

										elif ((t == s) and (u == s) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s] += (2 * F[n_occ + s, n_occ + v] + -2 * g[n_occ + s, n_occ + s, n_occ + s, n_occ + v] + 2 * g[j, j, n_occ + s, n_occ + v] + 4 * g[i, n_occ + s, i, n_occ + v] + -2 * g[i, i, n_occ + s, n_occ + v] + 2 * g[j, n_occ + s, j, n_occ + v] ) * K[0, j*n_virt + s] * K[1, j*n_virt + s + n_ex] * K[2, i*n_virt + v + n_ex]

										elif ((t == s) and (u != s) and (u != t) and (v == s)):

											L4[i*n_virt + s] += (-2 * g[n_occ + s, n_occ + s, n_occ + s, n_occ + u] + 4 * g[i, i, n_occ + s, n_occ + u] + 4 * g[j, n_occ + s, j, n_occ + u] + -2 * g[i, n_occ + s, i, n_occ + u] + -2 * g[j, j, n_occ + s, n_occ + u] ) * K[0, j*n_virt + s] * K[1, j*n_virt + u + n_ex] * K[2, i*n_virt + s + n_ex]

										elif ((t == s) and (u != s) and (u != t) and (v == u)):

											L4[i*n_virt + s] += (-2 * g[n_occ + s, n_occ + u, n_occ + s, n_occ + u] ) * K[0, j*n_virt + s] * K[1, j*n_virt + u + n_ex] * K[2, i*n_virt + u + n_ex]

										elif ((t == s) and (u != s) and (u != t) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s] += (-2 * g[n_occ + s, n_occ + u, n_occ + s, n_occ + v] ) * K[0, j*n_virt + s] * K[1, j*n_virt + u + n_ex] * K[2, i*n_virt + v + n_ex]

										elif ((t != s) and (u == s) and (v == s)):

											L4[i*n_virt + s] += (2 * F[n_occ + s, n_occ + t] + -2 * g[n_occ + s, n_occ + s, n_occ + s, n_occ + t] + 2 * g[i, i, n_occ + s, n_occ + t] + -2 * g[j, j, n_occ + s, n_occ + t] + 4 * g[j, n_occ + s, j, n_occ + t] + 2 * g[i, n_occ + s, i, n_occ + t] ) * K[0, j*n_virt + t] * K[1, j*n_virt + s + n_ex] * K[2, i*n_virt + s + n_ex]

										elif ((t != s) and (u == s) and (v == t)):

											L4[i*n_virt + s] += (-2 * F[j, j] + 2 * F[n_occ + t, n_occ + t] + -4 * g[n_occ + s, n_occ + t, n_occ + s, n_occ + t] + 2 * g[n_occ + s, n_occ + s, n_occ + t, n_occ + t] + -2 * g[i, i, n_occ + t, n_occ + t] + -2 * g[j, j, n_occ + t, n_occ + t] + 4 * g[j, n_occ + s, j, n_occ + s] + 4 * g[i, n_occ + t, i, n_occ + t] + 4 * g[j, n_occ + t, j, n_occ + t] + -4 * g[i, j, i, j] + 2 * g[i, i, j, j] + -2 * g[j, j, n_occ + s, n_occ + s] ) * K[0, j*n_virt + t] * K[1, j*n_virt + s + n_ex] * K[2, i*n_virt + t + n_ex]

										elif ((t != s) and (u == s) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s] += (2 * F[n_occ + t, n_occ + v] + -4 * g[n_occ + s, n_occ + t, n_occ + s, n_occ + v] + 2 * g[n_occ + s, n_occ + s, n_occ + t, n_occ + v] + -2 * g[i, i, n_occ + t, n_occ + v] + -2 * g[j, j, n_occ + t, n_occ + v] + 4 * g[i, n_occ + t, i, n_occ + v] + 4 * g[j, n_occ + t, j, n_occ + v] ) * K[0, j*n_virt + t] * K[1, j*n_virt + s + n_ex] * K[2, i*n_virt + v + n_ex]

										elif ((t != s) and (u == t) and (v == s)):

											L4[i*n_virt + s] += (2 * g[n_occ + s, n_occ + t, n_occ + s, n_occ + t] + -4 * g[n_occ + s, n_occ + s, n_occ + t, n_occ + t] + -2 * g[i, n_occ + t, i, n_occ + t] + 4 * g[i, i, n_occ + t, n_occ + t] + 2 * g[i, j, i, j] + -4 * g[i, i, j, j] + 4 * g[j, j, n_occ + s, n_occ + s] + -2 * g[j, n_occ + s, j, n_occ + s] ) * K[0, j*n_virt + t] * K[1, j*n_virt + t + n_ex] * K[2, i*n_virt + s + n_ex]

										elif ((t != s) and (u == t) and (v == t)):

											L4[i*n_virt + s] += (-2 * g[n_occ + s, n_occ + t, n_occ + t, n_occ + t] + 2 * g[j, n_occ + s, j, n_occ + t] + 2 * g[j, j, n_occ + s, n_occ + t] ) * K[0, j*n_virt + t] * K[1, j*n_virt + t + n_ex] * K[2, i*n_virt + t + n_ex]

										elif ((t != s) and (u == t) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s] += (2 * g[n_occ + s, n_occ + t, n_occ + t, n_occ + v] + -4 * g[n_occ + s, n_occ + v, n_occ + t, n_occ + t] + -2 * g[j, n_occ + s, j, n_occ + v] + 4 * g[j, j, n_occ + s, n_occ + v] ) * K[0, j*n_virt + t] * K[1, j*n_virt + t + n_ex] * K[2, i*n_virt + v + n_ex]

										elif ((t != s) and (u != s) and (u != t) and (v == s)):

											L4[i*n_virt + s] += (2 * g[n_occ + s, n_occ + t, n_occ + s, n_occ + u] + -4 * g[n_occ + s, n_occ + s, n_occ + t, n_occ + u] + -2 * g[i, n_occ + t, i, n_occ + u] + 4 * g[i, i, n_occ + t, n_occ + u] ) * K[0, j*n_virt + t] * K[1, j*n_virt + u + n_ex] * K[2, i*n_virt + s + n_ex]

										elif ((t != s) and (u != s) and (u != t) and (v == t)):

											L4[i*n_virt + s] += (-4 * g[n_occ + s, n_occ + t, n_occ + t, n_occ + u] + 2 * g[n_occ + s, n_occ + u, n_occ + t, n_occ + t] + 4 * g[j, n_occ + s, j, n_occ + u] + -2 * g[j, j, n_occ + s, n_occ + u] ) * K[0, j*n_virt + t] * K[1, j*n_virt + u + n_ex] * K[2, i*n_virt + t + n_ex]

										elif ((t != s) and (u != s) and (u != t) and (v == u)):

											L4[i*n_virt + s] += (-2 * g[n_occ + s, n_occ + u, n_occ + t, n_occ + u] ) * K[0, j*n_virt + t] * K[1, j*n_virt + u + n_ex] * K[2, i*n_virt + u + n_ex]

										elif ((t != s) and (u != s) and (u != t) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s] += (2 * g[n_occ + s, n_occ + u, n_occ + t, n_occ + v] + -4 * g[n_occ + s, n_occ + v, n_occ + t, n_occ + u] ) * K[0, j*n_virt + t] * K[1, j*n_virt + u + n_ex] * K[2, i*n_virt + v + n_ex]

									elif ((j != i) and (k == j) and (m == j)):

										if ((t == s) and (u == s) and (v == s)):

											L4[i*n_virt + s] += (4 * g[i, j, n_occ + s, n_occ + s] + -4 * g[i, j, j, j] + 4 * g[i, n_occ + s, j, n_occ + s] ) * K[0, j*n_virt + s] * K[1, j*n_virt + s + n_ex] * K[2, j*n_virt + s + n_ex]

										elif ((t == s) and (u == s) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s] += (2 * g[i, j, n_occ + s, n_occ + v] + 2 * g[i, n_occ + s, j, n_occ + v] ) * K[0, j*n_virt + s] * K[1, j*n_virt + s + n_ex] * K[2, j*n_virt + v + n_ex]

										elif ((t == s) and (u != s) and (u != t) and (v == s)):

											L4[i*n_virt + s] += (2 * g[i, j, n_occ + s, n_occ + u] + 2 * g[i, n_occ + s, j, n_occ + u] ) * K[0, j*n_virt + s] * K[1, j*n_virt + u + n_ex] * K[2, j*n_virt + s + n_ex]

										elif ((t != s) and (u == s) and (v == s)):

											L4[i*n_virt + s] += (4 * g[i, n_occ + t, j, n_occ + s] + 4 * g[i, j, n_occ + s, n_occ + t] ) * K[0, j*n_virt + t] * K[1, j*n_virt + s + n_ex] * K[2, j*n_virt + s + n_ex]

										elif ((t != s) and (u == s) and (v == t)):

											L4[i*n_virt + s] += (2 * g[i, n_occ + t, j, n_occ + t] + 2 * g[i, j, n_occ + t, n_occ + t] + -2 * g[i, j, j, j] ) * K[0, j*n_virt + t] * K[1, j*n_virt + s + n_ex] * K[2, j*n_virt + t + n_ex]

										elif ((t != s) and (u == s) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s] += (2 * g[i, n_occ + t, j, n_occ + v] + 2 * g[i, j, n_occ + t, n_occ + v] ) * K[0, j*n_virt + t] * K[1, j*n_virt + s + n_ex] * K[2, j*n_virt + v + n_ex]

										elif ((t != s) and (u == t) and (v == s)):

											L4[i*n_virt + s] += (2 * g[i, n_occ + t, j, n_occ + t] + 2 * g[i, j, n_occ + t, n_occ + t] + -2 * g[i, j, j, j] ) * K[0, j*n_virt + t] * K[1, j*n_virt + t + n_ex] * K[2, j*n_virt + s + n_ex]

										elif ((t != s) and (u != s) and (u != t) and (v == s)):

											L4[i*n_virt + s] += (2 * g[i, n_occ + t, j, n_occ + u] + 2 * g[i, j, n_occ + t, n_occ + u] ) * K[0, j*n_virt + t] * K[1, j*n_virt + u + n_ex] * K[2, j*n_virt + s + n_ex]

									elif ((j != i) and (k == j) and (m != i) and (m != j) and (m != k)):

										if ((t == s) and (u == s) and (v == s)):

											L4[i*n_virt + s] += (-2 * g[i, j, j, m] + 2 * g[i, m, n_occ + s, n_occ + s] + 2 * g[i, n_occ + s, m, n_occ + s] + -2 * g[i, m, j, j] ) * K[0, j*n_virt + s] * K[1, j*n_virt + s + n_ex] * K[2, m*n_virt + s + n_ex]

										elif ((t == s) and (u == s) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s] += (4 * g[i, n_occ + s, m, n_occ + v] + -2 * g[i, m, n_occ + s, n_occ + v] ) * K[0, j*n_virt + s] * K[1, j*n_virt + s + n_ex] * K[2, m*n_virt + v + n_ex]

										elif ((t == s) and (u != s) and (u != t) and (v == s)):

											L4[i*n_virt + s] += (4 * g[i, m, n_occ + s, n_occ + u] + -2 * g[i, n_occ + s, m, n_occ + u] ) * K[0, j*n_virt + s] * K[1, j*n_virt + u + n_ex] * K[2, m*n_virt + s + n_ex]

										elif ((t != s) and (u == s) and (v == s)):

											L4[i*n_virt + s] += (2 * g[i, n_occ + t, m, n_occ + s] + 2 * g[i, m, n_occ + s, n_occ + t] ) * K[0, j*n_virt + t] * K[1, j*n_virt + s + n_ex] * K[2, m*n_virt + s + n_ex]

										elif ((t != s) and (u == s) and (v == t)):

											L4[i*n_virt + s] += (4 * g[i, n_occ + t, m, n_occ + t] + -2 * g[i, m, n_occ + t, n_occ + t] + -4 * g[i, j, j, m] + 2 * g[i, m, j, j] ) * K[0, j*n_virt + t] * K[1, j*n_virt + s + n_ex] * K[2, m*n_virt + t + n_ex]

										elif ((t != s) and (u == s) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s] += (-2 * g[i, m, n_occ + t, n_occ + v] + 4 * g[i, n_occ + t, m, n_occ + v] ) * K[0, j*n_virt + t] * K[1, j*n_virt + s + n_ex] * K[2, m*n_virt + v + n_ex]

										elif ((t != s) and (u == t) and (v == s)):

											L4[i*n_virt + s] += (-2 * g[i, n_occ + t, m, n_occ + t] + 4 * g[i, m, n_occ + t, n_occ + t] + 2 * g[i, j, j, m] + -4 * g[i, m, j, j] ) * K[0, j*n_virt + t] * K[1, j*n_virt + t + n_ex] * K[2, m*n_virt + s + n_ex]

										elif ((t != s) and (u != s) and (u != t) and (v == s)):

											L4[i*n_virt + s] += (4 * g[i, m, n_occ + t, n_occ + u] + -2 * g[i, n_occ + t, m, n_occ + u] ) * K[0, j*n_virt + t] * K[1, j*n_virt + u + n_ex] * K[2, m*n_virt + s + n_ex]

									elif ((j != i) and (k != i) and (k != j) and (m == i)):

										if ((t == s) and (u == s) and (v == s)):

											L4[i*n_virt + s] += (-2 * F[j, k] + 6 * g[j, n_occ + s, k, n_occ + s] + -2 * g[i, i, j, k] + -2 * g[i, j, i, k] ) * K[0, j*n_virt + s] * K[1, k*n_virt + s + n_ex] * K[2, i*n_virt + s + n_ex]

										elif ((t == s) and (u == s) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s] += (2 * g[j, n_occ + s, k, n_occ + v] + 2 * g[j, k, n_occ + s, n_occ + v] ) * K[0, j*n_virt + s] * K[1, k*n_virt + s + n_ex] * K[2, i*n_virt + v + n_ex]

										elif ((t == s) and (u != s) and (u != t) and (v == s)):

											L4[i*n_virt + s] += (-2 * g[j, k, n_occ + s, n_occ + u] + 4 * g[j, n_occ + s, k, n_occ + u] ) * K[0, j*n_virt + s] * K[1, k*n_virt + u + n_ex] * K[2, i*n_virt + s + n_ex]

										elif ((t != s) and (u == s) and (v == s)):

											L4[i*n_virt + s] += (-2 * g[j, k, n_occ + s, n_occ + t] + 4 * g[j, n_occ + t, k, n_occ + s] ) * K[0, j*n_virt + t] * K[1, k*n_virt + s + n_ex] * K[2, i*n_virt + s + n_ex]

										elif ((t != s) and (u == s) and (v == t)):

											L4[i*n_virt + s] += (-2 * F[j, k] + 4 * g[j, n_occ + s, k, n_occ + s] + 4 * g[j, n_occ + t, k, n_occ + t] + -2 * g[j, k, n_occ + s, n_occ + s] + -2 * g[j, k, n_occ + t, n_occ + t] + 2 * g[i, i, j, k] + -4 * g[i, j, i, k] ) * K[0, j*n_virt + t] * K[1, k*n_virt + s + n_ex] * K[2, i*n_virt + t + n_ex]

										elif ((t != s) and (u == s) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s] += (-2 * g[j, k, n_occ + t, n_occ + v] + 4 * g[j, n_occ + t, k, n_occ + v] ) * K[0, j*n_virt + t] * K[1, k*n_virt + s + n_ex] * K[2, i*n_virt + v + n_ex]

										elif ((t != s) and (u == t) and (v == s)):

											L4[i*n_virt + s] += (-2 * g[j, n_occ + s, k, n_occ + s] + 4 * g[j, k, n_occ + s, n_occ + s] + 2 * g[i, j, i, k] + -4 * g[i, i, j, k] ) * K[0, j*n_virt + t] * K[1, k*n_virt + t + n_ex] * K[2, i*n_virt + s + n_ex]

										elif ((t != s) and (u == t) and (v == t)):

											L4[i*n_virt + s] += (2 * g[j, n_occ + s, k, n_occ + t] + 2 * g[j, k, n_occ + s, n_occ + t] ) * K[0, j*n_virt + t] * K[1, k*n_virt + t + n_ex] * K[2, i*n_virt + t + n_ex]

										elif ((t != s) and (u == t) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s] += (4 * g[j, k, n_occ + s, n_occ + v] + -2 * g[j, n_occ + s, k, n_occ + v] ) * K[0, j*n_virt + t] * K[1, k*n_virt + t + n_ex] * K[2, i*n_virt + v + n_ex]

										elif ((t != s) and (u != s) and (u != t) and (v == t)):

											L4[i*n_virt + s] += (-2 * g[j, k, n_occ + s, n_occ + u] + 4 * g[j, n_occ + s, k, n_occ + u] ) * K[0, j*n_virt + t] * K[1, k*n_virt + u + n_ex] * K[2, i*n_virt + t + n_ex]

									elif ((j != i) and (k != i) and (k != j) and (m == j)):

										if ((t == s) and (u == s) and (v == s)):

											L4[i*n_virt + s] += (-2 * g[i, j, j, k] + 2 * g[i, k, n_occ + s, n_occ + s] + 2 * g[i, n_occ + s, k, n_occ + s] + -2 * g[i, k, j, j] ) * K[0, j*n_virt + s] * K[1, k*n_virt + s + n_ex] * K[2, j*n_virt + s + n_ex]

										elif ((t == s) and (u == s) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s] += (4 * g[i, k, n_occ + s, n_occ + v] + -2 * g[i, n_occ + s, k, n_occ + v] ) * K[0, j*n_virt + s] * K[1, k*n_virt + s + n_ex] * K[2, j*n_virt + v + n_ex]

										elif ((t == s) and (u != s) and (u != t) and (v == s)):

											L4[i*n_virt + s] += (4 * g[i, n_occ + s, k, n_occ + u] + -2 * g[i, k, n_occ + s, n_occ + u] ) * K[0, j*n_virt + s] * K[1, k*n_virt + u + n_ex] * K[2, j*n_virt + s + n_ex]

										elif ((t != s) and (u == s) and (v == s)):

											L4[i*n_virt + s] += (2 * g[i, n_occ + t, k, n_occ + s] + 2 * g[i, k, n_occ + s, n_occ + t] ) * K[0, j*n_virt + t] * K[1, k*n_virt + s + n_ex] * K[2, j*n_virt + s + n_ex]

										elif ((t != s) and (u == s) and (v == t)):

											L4[i*n_virt + s] += (-2 * g[i, n_occ + t, k, n_occ + t] + 4 * g[i, k, n_occ + t, n_occ + t] + 2 * g[i, j, j, k] + -4 * g[i, k, j, j] ) * K[0, j*n_virt + t] * K[1, k*n_virt + s + n_ex] * K[2, j*n_virt + t + n_ex]

										elif ((t != s) and (u == s) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s] += (4 * g[i, k, n_occ + t, n_occ + v] + -2 * g[i, n_occ + t, k, n_occ + v] ) * K[0, j*n_virt + t] * K[1, k*n_virt + s + n_ex] * K[2, j*n_virt + v + n_ex]

										elif ((t != s) and (u == t) and (v == s)):

											L4[i*n_virt + s] += (4 * g[i, n_occ + t, k, n_occ + t] + -2 * g[i, k, n_occ + t, n_occ + t] + -4 * g[i, j, j, k] + 2 * g[i, k, j, j] ) * K[0, j*n_virt + t] * K[1, k*n_virt + t + n_ex] * K[2, j*n_virt + s + n_ex]

										elif ((t != s) and (u != s) and (u != t) and (v == s)):

											L4[i*n_virt + s] += (-2 * g[i, k, n_occ + t, n_occ + u] + 4 * g[i, n_occ + t, k, n_occ + u] ) * K[0, j*n_virt + t] * K[1, k*n_virt + u + n_ex] * K[2, j*n_virt + s + n_ex]

									elif ((j != i) and (k != i) and (k != j) and (m == k)):

										if ((t == s) and (u == s) and (v == s)):

											L4[i*n_virt + s] += (-4 * g[i, k, j, k] ) * K[0, j*n_virt + s] * K[1, k*n_virt + s + n_ex] * K[2, k*n_virt + s + n_ex]

										elif ((t != s) and (u == s) and (v == t)):

											L4[i*n_virt + s] += (-2 * g[i, k, j, k] ) * K[0, j*n_virt + t] * K[1, k*n_virt + s + n_ex] * K[2, k*n_virt + t + n_ex]

										elif ((t != s) and (u == t) and (v == s)):

											L4[i*n_virt + s] += (-2 * g[i, k, j, k] ) * K[0, j*n_virt + t] * K[1, k*n_virt + t + n_ex] * K[2, k*n_virt + s + n_ex]

									elif ((j != i) and (k != i) and (k != j) and (m != i) and (m != j) and (m != k)):

										if ((t == s) and (u == s) and (v == s)):

											L4[i*n_virt + s] += (-2 * g[i, m, j, k] + -2 * g[i, k, j, m] ) * K[0, j*n_virt + s] * K[1, k*n_virt + s + n_ex] * K[2, m*n_virt + s + n_ex]

										elif ((t != s) and (u == s) and (v == t)):

											L4[i*n_virt + s] += (-4 * g[i, k, j, m] + 2 * g[i, m, j, k] ) * K[0, j*n_virt + t] * K[1, k*n_virt + s + n_ex] * K[2, m*n_virt + t + n_ex]

										elif ((t != s) and (u == t) and (v == s)):

											L4[i*n_virt + s] += (2 * g[i, k, j, m] + -4 * g[i, m, j, k] ) * K[0, j*n_virt + t] * K[1, k*n_virt + t + n_ex] * K[2, m*n_virt + s + n_ex]

	# Current operator combination: {'a': 2, 'b': 2, 'c': 1, 'd': 2}
	# All terms vanished for this combination

	# Current operator combination: {'a': 2, 'b': 2, 'c': 1, 'd': 3}
	# All terms vanished for this combination

	# Current operator combination: {'a': 2, 'b': 2, 'c': 2, 'd': 1}
	for i in range(n_occ):
		for j in range(n_occ):
			for k in range(n_occ):
				for m in range(n_occ):
					for s in range(n_virt):
						for t in range(n_virt):
							for u in range(n_virt):
								for v in range(n_virt):

									if ((j == i) and (k == i) and (m == i)):

										if ((t == s) and (u == s) and (v == s)):

											L4[i*n_virt + s] += (12 * g[i, n_occ + s, i, n_occ + s] ) * K[0, i*n_virt + s + n_ex] * K[1, i*n_virt + s + n_ex] * K[2, i*n_virt + s + n_ex]

										elif ((t == s) and (u == s) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s] += (8 * g[i, n_occ + s, i, n_occ + v] ) * K[0, i*n_virt + s + n_ex] * K[1, i*n_virt + s + n_ex] * K[2, i*n_virt + v + n_ex]

										elif ((t == s) and (u != s) and (u != t) and (v == s)):

											L4[i*n_virt + s] += (8 * g[i, n_occ + s, i, n_occ + u] ) * K[0, i*n_virt + s + n_ex] * K[1, i*n_virt + u + n_ex] * K[2, i*n_virt + s + n_ex]

										elif ((t == s) and (u != s) and (u != t) and (v == u)):

											L4[i*n_virt + s] += (4 * g[i, n_occ + u, i, n_occ + u] ) * K[0, i*n_virt + s + n_ex] * K[1, i*n_virt + u + n_ex] * K[2, i*n_virt + u + n_ex]

										elif ((t == s) and (u != s) and (u != t) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s] += (4 * g[i, n_occ + u, i, n_occ + v] ) * K[0, i*n_virt + s + n_ex] * K[1, i*n_virt + u + n_ex] * K[2, i*n_virt + v + n_ex]

										elif ((t != s) and (u == s) and (v == s)):

											L4[i*n_virt + s] += (8 * g[i, n_occ + s, i, n_occ + t] ) * K[0, i*n_virt + t + n_ex] * K[1, i*n_virt + s + n_ex] * K[2, i*n_virt + s + n_ex]

										elif ((t != s) and (u == s) and (v == t)):

											L4[i*n_virt + s] += (4 * g[i, n_occ + t, i, n_occ + t] ) * K[0, i*n_virt + t + n_ex] * K[1, i*n_virt + s + n_ex] * K[2, i*n_virt + t + n_ex]

										elif ((t != s) and (u == s) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s] += (4 * g[i, n_occ + t, i, n_occ + v] ) * K[0, i*n_virt + t + n_ex] * K[1, i*n_virt + s + n_ex] * K[2, i*n_virt + v + n_ex]

										elif ((t != s) and (u == t) and (v == s)):

											L4[i*n_virt + s] += (4 * g[i, n_occ + t, i, n_occ + t] ) * K[0, i*n_virt + t + n_ex] * K[1, i*n_virt + t + n_ex] * K[2, i*n_virt + s + n_ex]

										elif ((t != s) and (u != s) and (u != t) and (v == s)):

											L4[i*n_virt + s] += (4 * g[i, n_occ + t, i, n_occ + u] ) * K[0, i*n_virt + t + n_ex] * K[1, i*n_virt + u + n_ex] * K[2, i*n_virt + s + n_ex]

									elif ((j == i) and (k == i) and (m != i) and (m != j) and (m != k)):

										if ((t == s) and (u == s) and (v == s)):

											L4[i*n_virt + s] += (8 * g[i, n_occ + s, m, n_occ + s] ) * K[0, i*n_virt + s + n_ex] * K[1, i*n_virt + s + n_ex] * K[2, m*n_virt + s + n_ex]

										elif ((t == s) and (u == s) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s] += (8 * g[i, n_occ + s, m, n_occ + v] + -4 * g[i, n_occ + v, m, n_occ + s] ) * K[0, i*n_virt + s + n_ex] * K[1, i*n_virt + s + n_ex] * K[2, m*n_virt + v + n_ex]

										elif ((t == s) and (u != s) and (u != t) and (v == s)):

											L4[i*n_virt + s] += (6 * g[i, n_occ + u, m, n_occ + s] ) * K[0, i*n_virt + s + n_ex] * K[1, i*n_virt + u + n_ex] * K[2, m*n_virt + s + n_ex]

										elif ((t == s) and (u != s) and (u != t) and (v == u)):

											L4[i*n_virt + s] += (2 * g[i, n_occ + u, m, n_occ + u] ) * K[0, i*n_virt + s + n_ex] * K[1, i*n_virt + u + n_ex] * K[2, m*n_virt + u + n_ex]

										elif ((t == s) and (u != s) and (u != t) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s] += (4 * g[i, n_occ + u, m, n_occ + v] + -2 * g[i, n_occ + v, m, n_occ + u] ) * K[0, i*n_virt + s + n_ex] * K[1, i*n_virt + u + n_ex] * K[2, m*n_virt + v + n_ex]

										elif ((t != s) and (u == s) and (v == s)):

											L4[i*n_virt + s] += (6 * g[i, n_occ + t, m, n_occ + s] ) * K[0, i*n_virt + t + n_ex] * K[1, i*n_virt + s + n_ex] * K[2, m*n_virt + s + n_ex]

										elif ((t != s) and (u == s) and (v == t)):

											L4[i*n_virt + s] += (2 * g[i, n_occ + t, m, n_occ + t] ) * K[0, i*n_virt + t + n_ex] * K[1, i*n_virt + s + n_ex] * K[2, m*n_virt + t + n_ex]

										elif ((t != s) and (u == s) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s] += (4 * g[i, n_occ + t, m, n_occ + v] + -2 * g[i, n_occ + v, m, n_occ + t] ) * K[0, i*n_virt + t + n_ex] * K[1, i*n_virt + s + n_ex] * K[2, m*n_virt + v + n_ex]

										elif ((t != s) and (u == t) and (v == s)):

											L4[i*n_virt + s] += (4 * g[i, n_occ + t, m, n_occ + t] ) * K[0, i*n_virt + t + n_ex] * K[1, i*n_virt + t + n_ex] * K[2, m*n_virt + s + n_ex]

										elif ((t != s) and (u != s) and (u != t) and (v == s)):

											L4[i*n_virt + s] += (2 * g[i, n_occ + t, m, n_occ + u] + 2 * g[i, n_occ + u, m, n_occ + t] ) * K[0, i*n_virt + t + n_ex] * K[1, i*n_virt + u + n_ex] * K[2, m*n_virt + s + n_ex]

									elif ((j == i) and (k != i) and (k != j) and (m == i)):

										if ((t == s) and (u == s) and (v == s)):

											L4[i*n_virt + s] += (8 * g[i, n_occ + s, k, n_occ + s] ) * K[0, i*n_virt + s + n_ex] * K[1, k*n_virt + s + n_ex] * K[2, i*n_virt + s + n_ex]

										elif ((t == s) and (u == s) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s] += (6 * g[i, n_occ + v, k, n_occ + s] ) * K[0, i*n_virt + s + n_ex] * K[1, k*n_virt + s + n_ex] * K[2, i*n_virt + v + n_ex]

										elif ((t == s) and (u != s) and (u != t) and (v == s)):

											L4[i*n_virt + s] += (8 * g[i, n_occ + s, k, n_occ + u] + -4 * g[i, n_occ + u, k, n_occ + s] ) * K[0, i*n_virt + s + n_ex] * K[1, k*n_virt + u + n_ex] * K[2, i*n_virt + s + n_ex]

										elif ((t == s) and (u != s) and (u != t) and (v == u)):

											L4[i*n_virt + s] += (2 * g[i, n_occ + u, k, n_occ + u] ) * K[0, i*n_virt + s + n_ex] * K[1, k*n_virt + u + n_ex] * K[2, i*n_virt + u + n_ex]

										elif ((t == s) and (u != s) and (u != t) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s] += (-2 * g[i, n_occ + u, k, n_occ + v] + 4 * g[i, n_occ + v, k, n_occ + u] ) * K[0, i*n_virt + s + n_ex] * K[1, k*n_virt + u + n_ex] * K[2, i*n_virt + v + n_ex]

										elif ((t != s) and (u == s) and (v == s)):

											L4[i*n_virt + s] += (6 * g[i, n_occ + t, k, n_occ + s] ) * K[0, i*n_virt + t + n_ex] * K[1, k*n_virt + s + n_ex] * K[2, i*n_virt + s + n_ex]

										elif ((t != s) and (u == s) and (v == t)):

											L4[i*n_virt + s] += (4 * g[i, n_occ + t, k, n_occ + t] ) * K[0, i*n_virt + t + n_ex] * K[1, k*n_virt + s + n_ex] * K[2, i*n_virt + t + n_ex]

										elif ((t != s) and (u == s) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s] += (2 * g[i, n_occ + t, k, n_occ + v] + 2 * g[i, n_occ + v, k, n_occ + t] ) * K[0, i*n_virt + t + n_ex] * K[1, k*n_virt + s + n_ex] * K[2, i*n_virt + v + n_ex]

										elif ((t != s) and (u == t) and (v == s)):

											L4[i*n_virt + s] += (2 * g[i, n_occ + t, k, n_occ + t] ) * K[0, i*n_virt + t + n_ex] * K[1, k*n_virt + t + n_ex] * K[2, i*n_virt + s + n_ex]

										elif ((t != s) and (u != s) and (u != t) and (v == s)):

											L4[i*n_virt + s] += (4 * g[i, n_occ + t, k, n_occ + u] + -2 * g[i, n_occ + u, k, n_occ + t] ) * K[0, i*n_virt + t + n_ex] * K[1, k*n_virt + u + n_ex] * K[2, i*n_virt + s + n_ex]

									elif ((j == i) and (k != i) and (k != j) and (m == k)):

										if ((t == s) and (u == s) and (v == s)):

											L4[i*n_virt + s] += (4 * g[k, n_occ + s, k, n_occ + s] ) * K[0, i*n_virt + s + n_ex] * K[1, k*n_virt + s + n_ex] * K[2, k*n_virt + s + n_ex]

										elif ((t == s) and (u == s) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s] += (2 * g[k, n_occ + s, k, n_occ + v] ) * K[0, i*n_virt + s + n_ex] * K[1, k*n_virt + s + n_ex] * K[2, k*n_virt + v + n_ex]

										elif ((t == s) and (u != s) and (u != t) and (v == s)):

											L4[i*n_virt + s] += (2 * g[k, n_occ + s, k, n_occ + u] ) * K[0, i*n_virt + s + n_ex] * K[1, k*n_virt + u + n_ex] * K[2, k*n_virt + s + n_ex]

										elif ((t != s) and (u == s) and (v == s)):

											L4[i*n_virt + s] += (4 * g[k, n_occ + s, k, n_occ + t] ) * K[0, i*n_virt + t + n_ex] * K[1, k*n_virt + s + n_ex] * K[2, k*n_virt + s + n_ex]

										elif ((t != s) and (u == s) and (v == t)):

											L4[i*n_virt + s] += (2 * g[k, n_occ + t, k, n_occ + t] ) * K[0, i*n_virt + t + n_ex] * K[1, k*n_virt + s + n_ex] * K[2, k*n_virt + t + n_ex]

										elif ((t != s) and (u == s) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s] += (2 * g[k, n_occ + t, k, n_occ + v] ) * K[0, i*n_virt + t + n_ex] * K[1, k*n_virt + s + n_ex] * K[2, k*n_virt + v + n_ex]

										elif ((t != s) and (u == t) and (v == s)):

											L4[i*n_virt + s] += (2 * g[k, n_occ + t, k, n_occ + t] ) * K[0, i*n_virt + t + n_ex] * K[1, k*n_virt + t + n_ex] * K[2, k*n_virt + s + n_ex]

										elif ((t != s) and (u != s) and (u != t) and (v == s)):

											L4[i*n_virt + s] += (2 * g[k, n_occ + t, k, n_occ + u] ) * K[0, i*n_virt + t + n_ex] * K[1, k*n_virt + u + n_ex] * K[2, k*n_virt + s + n_ex]

									elif ((j == i) and (k != i) and (k != j) and (m != i) and (m != j) and (m != k)):

										if ((t == s) and (u == s) and (v == s)):

											L4[i*n_virt + s] += (4 * g[k, n_occ + s, m, n_occ + s] ) * K[0, i*n_virt + s + n_ex] * K[1, k*n_virt + s + n_ex] * K[2, m*n_virt + s + n_ex]

										elif ((t == s) and (u == s) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s] += (4 * g[k, n_occ + s, m, n_occ + v] + -2 * g[k, n_occ + v, m, n_occ + s] ) * K[0, i*n_virt + s + n_ex] * K[1, k*n_virt + s + n_ex] * K[2, m*n_virt + v + n_ex]

										elif ((t == s) and (u != s) and (u != t) and (v == s)):

											L4[i*n_virt + s] += (-2 * g[k, n_occ + s, m, n_occ + u] + 4 * g[k, n_occ + u, m, n_occ + s] ) * K[0, i*n_virt + s + n_ex] * K[1, k*n_virt + u + n_ex] * K[2, m*n_virt + s + n_ex]

										elif ((t != s) and (u == s) and (v == s)):

											L4[i*n_virt + s] += (2 * g[k, n_occ + s, m, n_occ + t] + 2 * g[k, n_occ + t, m, n_occ + s] ) * K[0, i*n_virt + t + n_ex] * K[1, k*n_virt + s + n_ex] * K[2, m*n_virt + s + n_ex]

										elif ((t != s) and (u == s) and (v == t)):

											L4[i*n_virt + s] += (2 * g[k, n_occ + t, m, n_occ + t] ) * K[0, i*n_virt + t + n_ex] * K[1, k*n_virt + s + n_ex] * K[2, m*n_virt + t + n_ex]

										elif ((t != s) and (u == s) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s] += (4 * g[k, n_occ + t, m, n_occ + v] + -2 * g[k, n_occ + v, m, n_occ + t] ) * K[0, i*n_virt + t + n_ex] * K[1, k*n_virt + s + n_ex] * K[2, m*n_virt + v + n_ex]

										elif ((t != s) and (u == t) and (v == s)):

											L4[i*n_virt + s] += (2 * g[k, n_occ + t, m, n_occ + t] ) * K[0, i*n_virt + t + n_ex] * K[1, k*n_virt + t + n_ex] * K[2, m*n_virt + s + n_ex]

										elif ((t != s) and (u != s) and (u != t) and (v == s)):

											L4[i*n_virt + s] += (-2 * g[k, n_occ + t, m, n_occ + u] + 4 * g[k, n_occ + u, m, n_occ + t] ) * K[0, i*n_virt + t + n_ex] * K[1, k*n_virt + u + n_ex] * K[2, m*n_virt + s + n_ex]

									elif ((j != i) and (k == i) and (m == i)):

										if ((t == s) and (u == s) and (v == s)):

											L4[i*n_virt + s] += (8 * g[i, n_occ + s, j, n_occ + s] ) * K[0, j*n_virt + s + n_ex] * K[1, i*n_virt + s + n_ex] * K[2, i*n_virt + s + n_ex]

										elif ((t == s) and (u == s) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s] += (6 * g[i, n_occ + v, j, n_occ + s] ) * K[0, j*n_virt + s + n_ex] * K[1, i*n_virt + s + n_ex] * K[2, i*n_virt + v + n_ex]

										elif ((t == s) and (u != s) and (u != t) and (v == s)):

											L4[i*n_virt + s] += (6 * g[i, n_occ + u, j, n_occ + s] ) * K[0, j*n_virt + s + n_ex] * K[1, i*n_virt + u + n_ex] * K[2, i*n_virt + s + n_ex]

										elif ((t == s) and (u != s) and (u != t) and (v == u)):

											L4[i*n_virt + s] += (4 * g[i, n_occ + u, j, n_occ + u] ) * K[0, j*n_virt + s + n_ex] * K[1, i*n_virt + u + n_ex] * K[2, i*n_virt + u + n_ex]

										elif ((t == s) and (u != s) and (u != t) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s] += (2 * g[i, n_occ + u, j, n_occ + v] + 2 * g[i, n_occ + v, j, n_occ + u] ) * K[0, j*n_virt + s + n_ex] * K[1, i*n_virt + u + n_ex] * K[2, i*n_virt + v + n_ex]

										elif ((t != s) and (u == s) and (v == s)):

											L4[i*n_virt + s] += (8 * g[i, n_occ + s, j, n_occ + t] + -4 * g[i, n_occ + t, j, n_occ + s] ) * K[0, j*n_virt + t + n_ex] * K[1, i*n_virt + s + n_ex] * K[2, i*n_virt + s + n_ex]

										elif ((t != s) and (u == s) and (v == t)):

											L4[i*n_virt + s] += (2 * g[i, n_occ + t, j, n_occ + t] ) * K[0, j*n_virt + t + n_ex] * K[1, i*n_virt + s + n_ex] * K[2, i*n_virt + t + n_ex]

										elif ((t != s) and (u == s) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s] += (-2 * g[i, n_occ + t, j, n_occ + v] + 4 * g[i, n_occ + v, j, n_occ + t] ) * K[0, j*n_virt + t + n_ex] * K[1, i*n_virt + s + n_ex] * K[2, i*n_virt + v + n_ex]

										elif ((t != s) and (u == t) and (v == s)):

											L4[i*n_virt + s] += (2 * g[i, n_occ + t, j, n_occ + t] ) * K[0, j*n_virt + t + n_ex] * K[1, i*n_virt + t + n_ex] * K[2, i*n_virt + s + n_ex]

										elif ((t != s) and (u != s) and (u != t) and (v == s)):

											L4[i*n_virt + s] += (-2 * g[i, n_occ + t, j, n_occ + u] + 4 * g[i, n_occ + u, j, n_occ + t] ) * K[0, j*n_virt + t + n_ex] * K[1, i*n_virt + u + n_ex] * K[2, i*n_virt + s + n_ex]

									elif ((j != i) and (k == i) and (m == j)):

										if ((t == s) and (u == s) and (v == s)):

											L4[i*n_virt + s] += (4 * g[j, n_occ + s, j, n_occ + s] ) * K[0, j*n_virt + s + n_ex] * K[1, i*n_virt + s + n_ex] * K[2, j*n_virt + s + n_ex]

										elif ((t == s) and (u == s) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s] += (2 * g[j, n_occ + s, j, n_occ + v] ) * K[0, j*n_virt + s + n_ex] * K[1, i*n_virt + s + n_ex] * K[2, j*n_virt + v + n_ex]

										elif ((t == s) and (u != s) and (u != t) and (v == s)):

											L4[i*n_virt + s] += (4 * g[j, n_occ + s, j, n_occ + u] ) * K[0, j*n_virt + s + n_ex] * K[1, i*n_virt + u + n_ex] * K[2, j*n_virt + s + n_ex]

										elif ((t == s) and (u != s) and (u != t) and (v == u)):

											L4[i*n_virt + s] += (2 * g[j, n_occ + u, j, n_occ + u] ) * K[0, j*n_virt + s + n_ex] * K[1, i*n_virt + u + n_ex] * K[2, j*n_virt + u + n_ex]

										elif ((t == s) and (u != s) and (u != t) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s] += (2 * g[j, n_occ + u, j, n_occ + v] ) * K[0, j*n_virt + s + n_ex] * K[1, i*n_virt + u + n_ex] * K[2, j*n_virt + v + n_ex]

										elif ((t != s) and (u == s) and (v == s)):

											L4[i*n_virt + s] += (2 * g[j, n_occ + s, j, n_occ + t] ) * K[0, j*n_virt + t + n_ex] * K[1, i*n_virt + s + n_ex] * K[2, j*n_virt + s + n_ex]

										elif ((t != s) and (u == t) and (v == s)):

											L4[i*n_virt + s] += (2 * g[j, n_occ + t, j, n_occ + t] ) * K[0, j*n_virt + t + n_ex] * K[1, i*n_virt + t + n_ex] * K[2, j*n_virt + s + n_ex]

										elif ((t != s) and (u != s) and (u != t) and (v == s)):

											L4[i*n_virt + s] += (2 * g[j, n_occ + t, j, n_occ + u] ) * K[0, j*n_virt + t + n_ex] * K[1, i*n_virt + u + n_ex] * K[2, j*n_virt + s + n_ex]

									elif ((j != i) and (k == i) and (m != i) and (m != j) and (m != k)):

										if ((t == s) and (u == s) and (v == s)):

											L4[i*n_virt + s] += (4 * g[j, n_occ + s, m, n_occ + s] ) * K[0, j*n_virt + s + n_ex] * K[1, i*n_virt + s + n_ex] * K[2, m*n_virt + s + n_ex]

										elif ((t == s) and (u == s) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s] += (4 * g[j, n_occ + s, m, n_occ + v] + -2 * g[j, n_occ + v, m, n_occ + s] ) * K[0, j*n_virt + s + n_ex] * K[1, i*n_virt + s + n_ex] * K[2, m*n_virt + v + n_ex]

										elif ((t == s) and (u != s) and (u != t) and (v == s)):

											L4[i*n_virt + s] += (2 * g[j, n_occ + s, m, n_occ + u] + 2 * g[j, n_occ + u, m, n_occ + s] ) * K[0, j*n_virt + s + n_ex] * K[1, i*n_virt + u + n_ex] * K[2, m*n_virt + s + n_ex]

										elif ((t == s) and (u != s) and (u != t) and (v == u)):

											L4[i*n_virt + s] += (2 * g[j, n_occ + u, m, n_occ + u] ) * K[0, j*n_virt + s + n_ex] * K[1, i*n_virt + u + n_ex] * K[2, m*n_virt + u + n_ex]

										elif ((t == s) and (u != s) and (u != t) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s] += (4 * g[j, n_occ + u, m, n_occ + v] + -2 * g[j, n_occ + v, m, n_occ + u] ) * K[0, j*n_virt + s + n_ex] * K[1, i*n_virt + u + n_ex] * K[2, m*n_virt + v + n_ex]

										elif ((t != s) and (u == s) and (v == s)):

											L4[i*n_virt + s] += (-2 * g[j, n_occ + s, m, n_occ + t] + 4 * g[j, n_occ + t, m, n_occ + s] ) * K[0, j*n_virt + t + n_ex] * K[1, i*n_virt + s + n_ex] * K[2, m*n_virt + s + n_ex]

										elif ((t != s) and (u == t) and (v == s)):

											L4[i*n_virt + s] += (2 * g[j, n_occ + t, m, n_occ + t] ) * K[0, j*n_virt + t + n_ex] * K[1, i*n_virt + t + n_ex] * K[2, m*n_virt + s + n_ex]

										elif ((t != s) and (u != s) and (u != t) and (v == s)):

											L4[i*n_virt + s] += (4 * g[j, n_occ + t, m, n_occ + u] + -2 * g[j, n_occ + u, m, n_occ + t] ) * K[0, j*n_virt + t + n_ex] * K[1, i*n_virt + u + n_ex] * K[2, m*n_virt + s + n_ex]

									elif ((j != i) and (k == j) and (m == i)):

										if ((t == s) and (u == s) and (v == s)):

											L4[i*n_virt + s] += (4 * g[j, n_occ + s, j, n_occ + s] ) * K[0, j*n_virt + s + n_ex] * K[1, j*n_virt + s + n_ex] * K[2, i*n_virt + s + n_ex]

										elif ((t == s) and (u == s) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s] += (4 * g[j, n_occ + s, j, n_occ + v] ) * K[0, j*n_virt + s + n_ex] * K[1, j*n_virt + s + n_ex] * K[2, i*n_virt + v + n_ex]

										elif ((t == s) and (u != s) and (u != t) and (v == s)):

											L4[i*n_virt + s] += (2 * g[j, n_occ + s, j, n_occ + u] ) * K[0, j*n_virt + s + n_ex] * K[1, j*n_virt + u + n_ex] * K[2, i*n_virt + s + n_ex]

										elif ((t == s) and (u != s) and (u != t) and (v == u)):

											L4[i*n_virt + s] += (2 * g[j, n_occ + u, j, n_occ + u] ) * K[0, j*n_virt + s + n_ex] * K[1, j*n_virt + u + n_ex] * K[2, i*n_virt + u + n_ex]

										elif ((t == s) and (u != s) and (u != t) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s] += (2 * g[j, n_occ + u, j, n_occ + v] ) * K[0, j*n_virt + s + n_ex] * K[1, j*n_virt + u + n_ex] * K[2, i*n_virt + v + n_ex]

										elif ((t != s) and (u == s) and (v == s)):

											L4[i*n_virt + s] += (2 * g[j, n_occ + s, j, n_occ + t] ) * K[0, j*n_virt + t + n_ex] * K[1, j*n_virt + s + n_ex] * K[2, i*n_virt + s + n_ex]

										elif ((t != s) and (u == s) and (v == t)):

											L4[i*n_virt + s] += (2 * g[j, n_occ + t, j, n_occ + t] ) * K[0, j*n_virt + t + n_ex] * K[1, j*n_virt + s + n_ex] * K[2, i*n_virt + t + n_ex]

										elif ((t != s) and (u == s) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s] += (2 * g[j, n_occ + t, j, n_occ + v] ) * K[0, j*n_virt + t + n_ex] * K[1, j*n_virt + s + n_ex] * K[2, i*n_virt + v + n_ex]

									elif ((j != i) and (k != i) and (k != j) and (m == i)):

										if ((t == s) and (u == s) and (v == s)):

											L4[i*n_virt + s] += (4 * g[j, n_occ + s, k, n_occ + s] ) * K[0, j*n_virt + s + n_ex] * K[1, k*n_virt + s + n_ex] * K[2, i*n_virt + s + n_ex]

										elif ((t == s) and (u == s) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s] += (2 * g[j, n_occ + s, k, n_occ + v] + 2 * g[j, n_occ + v, k, n_occ + s] ) * K[0, j*n_virt + s + n_ex] * K[1, k*n_virt + s + n_ex] * K[2, i*n_virt + v + n_ex]

										elif ((t == s) and (u != s) and (u != t) and (v == s)):

											L4[i*n_virt + s] += (4 * g[j, n_occ + s, k, n_occ + u] + -2 * g[j, n_occ + u, k, n_occ + s] ) * K[0, j*n_virt + s + n_ex] * K[1, k*n_virt + u + n_ex] * K[2, i*n_virt + s + n_ex]

										elif ((t == s) and (u != s) and (u != t) and (v == u)):

											L4[i*n_virt + s] += (2 * g[j, n_occ + u, k, n_occ + u] ) * K[0, j*n_virt + s + n_ex] * K[1, k*n_virt + u + n_ex] * K[2, i*n_virt + u + n_ex]

										elif ((t == s) and (u != s) and (u != t) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s] += (-2 * g[j, n_occ + u, k, n_occ + v] + 4 * g[j, n_occ + v, k, n_occ + u] ) * K[0, j*n_virt + s + n_ex] * K[1, k*n_virt + u + n_ex] * K[2, i*n_virt + v + n_ex]

										elif ((t != s) and (u == s) and (v == s)):

											L4[i*n_virt + s] += (-2 * g[j, n_occ + s, k, n_occ + t] + 4 * g[j, n_occ + t, k, n_occ + s] ) * K[0, j*n_virt + t + n_ex] * K[1, k*n_virt + s + n_ex] * K[2, i*n_virt + s + n_ex]

										elif ((t != s) and (u == s) and (v == t)):

											L4[i*n_virt + s] += (2 * g[j, n_occ + t, k, n_occ + t] ) * K[0, j*n_virt + t + n_ex] * K[1, k*n_virt + s + n_ex] * K[2, i*n_virt + t + n_ex]

										elif ((t != s) and (u == s) and (v != s) and (v != t) and (v != u)):

											L4[i*n_virt + s] += (4 * g[j, n_occ + t, k, n_occ + v] + -2 * g[j, n_occ + v, k, n_occ + t] ) * K[0, j*n_virt + t + n_ex] * K[1, k*n_virt + s + n_ex] * K[2, i*n_virt + v + n_ex]

	# Current operator combination: {'a': 2, 'b': 2, 'c': 2, 'd': 2}
	# All terms vanished for this combination

	# Current operator combination: {'a': 2, 'b': 2, 'c': 2, 'd': 3}
	# All terms vanished for this combination

	# Current operator combination: {'a': 2, 'b': 2, 'c': 3, 'd': 1}
	# This combination was excluded by the contr_type_only argument {'a': 2, 'b': 2, 'c': 3, 'd': 1}

	# Current operator combination: {'a': 2, 'b': 2, 'c': 3, 'd': 2}
	# This combination was excluded by the contr_type_only argument {'a': 2, 'b': 2, 'c': 3, 'd': 2}

	# Current operator combination: {'a': 2, 'b': 2, 'c': 3, 'd': 3}
	# This combination was excluded by the contr_type_only argument {'a': 2, 'b': 2, 'c': 3, 'd': 3}

	# Current operator combination: {'a': 2, 'b': 3, 'c': 1, 'd': 1}
	# This combination was excluded by the contr_type_only argument {'a': 2, 'b': 3, 'c': 1, 'd': 1}

	# Current operator combination: {'a': 2, 'b': 3, 'c': 1, 'd': 2}
	# This combination was excluded by the contr_type_only argument {'a': 2, 'b': 3, 'c': 1, 'd': 2}

	# Current operator combination: {'a': 2, 'b': 3, 'c': 1, 'd': 3}
	# This combination was excluded by the contr_type_only argument {'a': 2, 'b': 3, 'c': 1, 'd': 3}

	# Current operator combination: {'a': 2, 'b': 3, 'c': 2, 'd': 1}
	# This combination was excluded by the contr_type_only argument {'a': 2, 'b': 3, 'c': 2, 'd': 1}

	# Current operator combination: {'a': 2, 'b': 3, 'c': 2, 'd': 2}
	# This combination was excluded by the contr_type_only argument {'a': 2, 'b': 3, 'c': 2, 'd': 2}

	# Current operator combination: {'a': 2, 'b': 3, 'c': 2, 'd': 3}
	# This combination was excluded by the contr_type_only argument {'a': 2, 'b': 3, 'c': 2, 'd': 3}

	# Current operator combination: {'a': 2, 'b': 3, 'c': 3, 'd': 1}
	# This combination was excluded by the contr_type_only argument {'a': 2, 'b': 3, 'c': 3, 'd': 1}

	# Current operator combination: {'a': 2, 'b': 3, 'c': 3, 'd': 2}
	# This combination was excluded by the contr_type_only argument {'a': 2, 'b': 3, 'c': 3, 'd': 2}

	# Current operator combination: {'a': 2, 'b': 3, 'c': 3, 'd': 3}
	# This combination was excluded by the contr_type_only argument {'a': 2, 'b': 3, 'c': 3, 'd': 3}

	# Current operator combination: {'a': 3, 'b': 1, 'c': 1, 'd': 1}
	# This combination was excluded by the contr_type_only argument {'a': 3, 'b': 1, 'c': 1, 'd': 1}

	# Current operator combination: {'a': 3, 'b': 1, 'c': 1, 'd': 2}
	# This combination was excluded by the contr_type_only argument {'a': 3, 'b': 1, 'c': 1, 'd': 2}

	# Current operator combination: {'a': 3, 'b': 1, 'c': 1, 'd': 3}
	# This combination was excluded by the contr_type_only argument {'a': 3, 'b': 1, 'c': 1, 'd': 3}

	# Current operator combination: {'a': 3, 'b': 1, 'c': 2, 'd': 1}
	# This combination was excluded by the contr_type_only argument {'a': 3, 'b': 1, 'c': 2, 'd': 1}

	# Current operator combination: {'a': 3, 'b': 1, 'c': 2, 'd': 2}
	# This combination was excluded by the contr_type_only argument {'a': 3, 'b': 1, 'c': 2, 'd': 2}

	# Current operator combination: {'a': 3, 'b': 1, 'c': 2, 'd': 3}
	# This combination was excluded by the contr_type_only argument {'a': 3, 'b': 1, 'c': 2, 'd': 3}

	# Current operator combination: {'a': 3, 'b': 1, 'c': 3, 'd': 1}
	# This combination was excluded by the contr_type_only argument {'a': 3, 'b': 1, 'c': 3, 'd': 1}

	# Current operator combination: {'a': 3, 'b': 1, 'c': 3, 'd': 2}
	# This combination was excluded by the contr_type_only argument {'a': 3, 'b': 1, 'c': 3, 'd': 2}

	# Current operator combination: {'a': 3, 'b': 1, 'c': 3, 'd': 3}
	# This combination was excluded by the contr_type_only argument {'a': 3, 'b': 1, 'c': 3, 'd': 3}

	# Current operator combination: {'a': 3, 'b': 2, 'c': 1, 'd': 1}
	# This combination was excluded by the contr_type_only argument {'a': 3, 'b': 2, 'c': 1, 'd': 1}

	# Current operator combination: {'a': 3, 'b': 2, 'c': 1, 'd': 2}
	# This combination was excluded by the contr_type_only argument {'a': 3, 'b': 2, 'c': 1, 'd': 2}

	# Current operator combination: {'a': 3, 'b': 2, 'c': 1, 'd': 3}
	# This combination was excluded by the contr_type_only argument {'a': 3, 'b': 2, 'c': 1, 'd': 3}

	# Current operator combination: {'a': 3, 'b': 2, 'c': 2, 'd': 1}
	# This combination was excluded by the contr_type_only argument {'a': 3, 'b': 2, 'c': 2, 'd': 1}

	# Current operator combination: {'a': 3, 'b': 2, 'c': 2, 'd': 2}
	# This combination was excluded by the contr_type_only argument {'a': 3, 'b': 2, 'c': 2, 'd': 2}

	# Current operator combination: {'a': 3, 'b': 2, 'c': 2, 'd': 3}
	# This combination was excluded by the contr_type_only argument {'a': 3, 'b': 2, 'c': 2, 'd': 3}

	# Current operator combination: {'a': 3, 'b': 2, 'c': 3, 'd': 1}
	# This combination was excluded by the contr_type_only argument {'a': 3, 'b': 2, 'c': 3, 'd': 1}

	# Current operator combination: {'a': 3, 'b': 2, 'c': 3, 'd': 2}
	# This combination was excluded by the contr_type_only argument {'a': 3, 'b': 2, 'c': 3, 'd': 2}

	# Current operator combination: {'a': 3, 'b': 2, 'c': 3, 'd': 3}
	# This combination was excluded by the contr_type_only argument {'a': 3, 'b': 2, 'c': 3, 'd': 3}

	# Current operator combination: {'a': 3, 'b': 3, 'c': 1, 'd': 1}
	# This combination was excluded by the contr_type_only argument {'a': 3, 'b': 3, 'c': 1, 'd': 1}

	# Current operator combination: {'a': 3, 'b': 3, 'c': 1, 'd': 2}
	# This combination was excluded by the contr_type_only argument {'a': 3, 'b': 3, 'c': 1, 'd': 2}

	# Current operator combination: {'a': 3, 'b': 3, 'c': 1, 'd': 3}
	# This combination was excluded by the contr_type_only argument {'a': 3, 'b': 3, 'c': 1, 'd': 3}

	# Current operator combination: {'a': 3, 'b': 3, 'c': 2, 'd': 1}
	# This combination was excluded by the contr_type_only argument {'a': 3, 'b': 3, 'c': 2, 'd': 1}

	# Current operator combination: {'a': 3, 'b': 3, 'c': 2, 'd': 2}
	# This combination was excluded by the contr_type_only argument {'a': 3, 'b': 3, 'c': 2, 'd': 2}

	# Current operator combination: {'a': 3, 'b': 3, 'c': 2, 'd': 3}
	# This combination was excluded by the contr_type_only argument {'a': 3, 'b': 3, 'c': 2, 'd': 3}

	# Current operator combination: {'a': 3, 'b': 3, 'c': 3, 'd': 1}
	# This combination was excluded by the contr_type_only argument {'a': 3, 'b': 3, 'c': 3, 'd': 1}

	# Current operator combination: {'a': 3, 'b': 3, 'c': 3, 'd': 2}
	# This combination was excluded by the contr_type_only argument {'a': 3, 'b': 3, 'c': 3, 'd': 2}

	# Current operator combination: {'a': 3, 'b': 3, 'c': 3, 'd': 3}
	# This combination was excluded by the contr_type_only argument {'a': 3, 'b': 3, 'c': 3, 'd': 3}

