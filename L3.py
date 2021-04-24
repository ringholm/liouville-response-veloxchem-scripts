import numpy as np


def L3_f(n_occ, n_virt, H00, F, g, K): 

	n_ex = n_occ * n_virt

	L3_ans = np.zeros(2*n_ex + n_ex**2, dtype=complex)
 


	# Current operator combination: {'a': 1, 'b': 1, 'c': 1}
	# All terms vanished for this combination

	# Current operator combination: {'a': 1, 'b': 1, 'c': 2}
	for i in range(n_occ):
		for j in range(n_occ):
			for k in range(n_occ):
				for s in range(n_virt):
					for t in range(n_virt):
						for u in range(n_virt):

							if ((j == i) and (k == i)):

								if ((t == s) and (u == s)):

									L3_ans[i*n_virt + s + n_ex] += (4 * F[i, n_occ + s] + -4 * g[i, n_occ + s, n_occ + s, n_occ + s] + 4 * g[i, i, i, n_occ + s] ) * K[0, i*n_virt + s] * K[1, i*n_virt + s]

								elif ((t == s) and (u != s) and (u != t)):

									L3_ans[i*n_virt + s + n_ex] += (2 * F[i, n_occ + u] + -2 * g[i, n_occ + s, n_occ + s, n_occ + u] + -2 * g[i, n_occ + u, n_occ + s, n_occ + s] + 2 * g[i, i, i, n_occ + u] ) * K[0, i*n_virt + s] * K[1, i*n_virt + u]

								elif ((t != s) and (u == s)):

									L3_ans[i*n_virt + s + n_ex] += (2 * F[i, n_occ + t] + -2 * g[i, n_occ + t, n_occ + s, n_occ + s] + -2 * g[i, n_occ + s, n_occ + s, n_occ + t] + 2 * g[i, i, i, n_occ + t] ) * K[0, i*n_virt + t] * K[1, i*n_virt + s]

								elif ((t != s) and (u == t)):

									L3_ans[i*n_virt + s + n_ex] += (-4 * g[i, n_occ + t, n_occ + s, n_occ + t] ) * K[0, i*n_virt + t] * K[1, i*n_virt + t]

								elif ((t != s) and (u != s) and (u != t)):

									L3_ans[i*n_virt + s + n_ex] += (-2 * g[i, n_occ + t, n_occ + s, n_occ + u] + -2 * g[i, n_occ + u, n_occ + s, n_occ + t] ) * K[0, i*n_virt + t] * K[1, i*n_virt + u]

							elif ((j == i) and (k != i) and (k != j)):

								if ((t == s) and (u == s)):

									L3_ans[i*n_virt + s + n_ex] += (2 * F[k, n_occ + s] + 2 * g[i, i, k, n_occ + s] + -2 * g[k, n_occ + s, n_occ + s, n_occ + s] + 2 * g[i, k, i, n_occ + s] ) * K[0, i*n_virt + s] * K[1, k*n_virt + s]

								elif ((t == s) and (u != s) and (u != t)):

									L3_ans[i*n_virt + s + n_ex] += (-2 * g[i, k, i, n_occ + u] + 4 * g[i, i, k, n_occ + u] + 2 * g[k, n_occ + s, n_occ + s, n_occ + u] + -4 * g[k, n_occ + u, n_occ + s, n_occ + s] ) * K[0, i*n_virt + s] * K[1, k*n_virt + u]

								elif ((t != s) and (u == s)):

									L3_ans[i*n_virt + s + n_ex] += (2 * F[k, n_occ + t] + -4 * g[k, n_occ + s, n_occ + s, n_occ + t] + 2 * g[k, n_occ + t, n_occ + s, n_occ + s] + -2 * g[i, i, k, n_occ + t] + 4 * g[i, k, i, n_occ + t] ) * K[0, i*n_virt + t] * K[1, k*n_virt + s]

								elif ((t != s) and (u == t)):

									L3_ans[i*n_virt + s + n_ex] += (-2 * g[k, n_occ + t, n_occ + s, n_occ + t] ) * K[0, i*n_virt + t] * K[1, k*n_virt + t]

								elif ((t != s) and (u != s) and (u != t)):

									L3_ans[i*n_virt + s + n_ex] += (2 * g[k, n_occ + t, n_occ + s, n_occ + u] + -4 * g[k, n_occ + u, n_occ + s, n_occ + t] ) * K[0, i*n_virt + t] * K[1, k*n_virt + u]

							elif ((j != i) and (k == i)):

								if ((t == s) and (u == s)):

									L3_ans[i*n_virt + s + n_ex] += (2 * F[j, n_occ + s] + 2 * g[i, i, j, n_occ + s] + -2 * g[j, n_occ + s, n_occ + s, n_occ + s] + 2 * g[i, j, i, n_occ + s] ) * K[0, j*n_virt + s] * K[1, i*n_virt + s]

								elif ((t == s) and (u != s) and (u != t)):

									L3_ans[i*n_virt + s + n_ex] += (2 * F[j, n_occ + u] + -4 * g[j, n_occ + s, n_occ + s, n_occ + u] + 2 * g[j, n_occ + u, n_occ + s, n_occ + s] + -2 * g[i, i, j, n_occ + u] + 4 * g[i, j, i, n_occ + u] ) * K[0, j*n_virt + s] * K[1, i*n_virt + u]

								elif ((t != s) and (u == s)):

									L3_ans[i*n_virt + s + n_ex] += (-2 * g[i, j, i, n_occ + t] + 4 * g[i, i, j, n_occ + t] + 2 * g[j, n_occ + s, n_occ + s, n_occ + t] + -4 * g[j, n_occ + t, n_occ + s, n_occ + s] ) * K[0, j*n_virt + t] * K[1, i*n_virt + s]

								elif ((t != s) and (u == t)):

									L3_ans[i*n_virt + s + n_ex] += (-2 * g[j, n_occ + t, n_occ + s, n_occ + t] ) * K[0, j*n_virt + t] * K[1, i*n_virt + t]

								elif ((t != s) and (u != s) and (u != t)):

									L3_ans[i*n_virt + s + n_ex] += (-4 * g[j, n_occ + t, n_occ + s, n_occ + u] + 2 * g[j, n_occ + u, n_occ + s, n_occ + t] ) * K[0, j*n_virt + t] * K[1, i*n_virt + u]

							elif ((j != i) and (k == j)):

								if ((t == s) and (u == s)):

									L3_ans[i*n_virt + s + n_ex] += (4 * g[i, j, j, n_occ + s] ) * K[0, j*n_virt + s] * K[1, j*n_virt + s]

								elif ((t == s) and (u != s) and (u != t)):

									L3_ans[i*n_virt + s + n_ex] += (2 * g[i, j, j, n_occ + u] ) * K[0, j*n_virt + s] * K[1, j*n_virt + u]

								elif ((t != s) and (u == s)):

									L3_ans[i*n_virt + s + n_ex] += (2 * g[i, j, j, n_occ + t] ) * K[0, j*n_virt + t] * K[1, j*n_virt + s]

							elif ((j != i) and (k != i) and (k != j)):

								if ((t == s) and (u == s)):

									L3_ans[i*n_virt + s + n_ex] += (2 * g[i, k, j, n_occ + s] + 2 * g[i, j, k, n_occ + s] ) * K[0, j*n_virt + s] * K[1, k*n_virt + s]

								elif ((t == s) and (u != s) and (u != t)):

									L3_ans[i*n_virt + s + n_ex] += (4 * g[i, j, k, n_occ + u] + -2 * g[i, k, j, n_occ + u] ) * K[0, j*n_virt + s] * K[1, k*n_virt + u]

								elif ((t != s) and (u == s)):

									L3_ans[i*n_virt + s + n_ex] += (-2 * g[i, j, k, n_occ + t] + 4 * g[i, k, j, n_occ + t] ) * K[0, j*n_virt + t] * K[1, k*n_virt + s]

	# Current operator combination: {'a': 1, 'b': 1, 'c': 3}
	# All terms vanished for this combination

	# Current operator combination: {'a': 1, 'b': 2, 'c': 1}
	for i in range(n_occ):
		for j in range(n_occ):
			for k in range(n_occ):
				for s in range(n_virt):
					for t in range(n_virt):
						for u in range(n_virt):

							if ((j == i) and (k == i)):

								if ((t == s) and (u == s)):

									L3_ans[i*n_virt + s] += (4 * g[i, n_occ + s, n_occ + s, n_occ + s] + -4 * g[i, i, i, n_occ + s] ) * K[0, i*n_virt + s + n_ex] * K[1, i*n_virt + s]

								elif ((t == s) and (u != s) and (u != t)):

									L3_ans[i*n_virt + s] += (2 * g[i, n_occ + u, n_occ + s, n_occ + s] + 2 * g[i, n_occ + s, n_occ + s, n_occ + u] + -2 * g[i, i, i, n_occ + u] ) * K[0, i*n_virt + s + n_ex] * K[1, i*n_virt + u]

								elif ((t != s) and (u == s)):

									L3_ans[i*n_virt + s] += (4 * g[i, n_occ + s, n_occ + s, n_occ + t] ) * K[0, i*n_virt + t + n_ex] * K[1, i*n_virt + s]

								elif ((t != s) and (u == t)):

									L3_ans[i*n_virt + s] += (2 * g[i, n_occ + t, n_occ + s, n_occ + t] + 2 * g[i, n_occ + s, n_occ + t, n_occ + t] + -2 * g[i, i, i, n_occ + s] ) * K[0, i*n_virt + t + n_ex] * K[1, i*n_virt + t]

								elif ((t != s) and (u != s) and (u != t)):

									L3_ans[i*n_virt + s] += (2 * g[i, n_occ + u, n_occ + s, n_occ + t] + 2 * g[i, n_occ + s, n_occ + t, n_occ + u] ) * K[0, i*n_virt + t + n_ex] * K[1, i*n_virt + u]

							elif ((j == i) and (k != i) and (k != j)):

								if ((t == s) and (u == s)):

									L3_ans[i*n_virt + s] += (-2 * g[i, k, i, n_occ + s] + 2 * g[k, n_occ + s, n_occ + s, n_occ + s] + -2 * g[i, i, k, n_occ + s] ) * K[0, i*n_virt + s + n_ex] * K[1, k*n_virt + s]

								elif ((t == s) and (u != s) and (u != t)):

									L3_ans[i*n_virt + s] += (-2 * g[k, n_occ + s, n_occ + s, n_occ + u] + 4 * g[k, n_occ + u, n_occ + s, n_occ + s] + 2 * g[i, k, i, n_occ + u] + -4 * g[i, i, k, n_occ + u] ) * K[0, i*n_virt + s + n_ex] * K[1, k*n_virt + u]

								elif ((t != s) and (u == s)):

									L3_ans[i*n_virt + s] += (2 * g[k, n_occ + s, n_occ + s, n_occ + t] ) * K[0, i*n_virt + t + n_ex] * K[1, k*n_virt + s]

								elif ((t != s) and (u == t)):

									L3_ans[i*n_virt + s] += (-4 * g[i, k, i, n_occ + s] + 2 * g[i, i, k, n_occ + s] + 4 * g[k, n_occ + t, n_occ + s, n_occ + t] + -2 * g[k, n_occ + s, n_occ + t, n_occ + t] ) * K[0, i*n_virt + t + n_ex] * K[1, k*n_virt + t]

								elif ((t != s) and (u != s) and (u != t)):

									L3_ans[i*n_virt + s] += (-2 * g[k, n_occ + s, n_occ + t, n_occ + u] + 4 * g[k, n_occ + u, n_occ + s, n_occ + t] ) * K[0, i*n_virt + t + n_ex] * K[1, k*n_virt + u]

							elif ((j != i) and (k == i)):

								if ((t == s) and (u == s)):

									L3_ans[i*n_virt + s] += (-4 * g[i, j, i, n_occ + s] ) * K[0, j*n_virt + s + n_ex] * K[1, i*n_virt + s]

								elif ((t == s) and (u != s) and (u != t)):

									L3_ans[i*n_virt + s] += (-2 * g[i, j, i, n_occ + u] ) * K[0, j*n_virt + s + n_ex] * K[1, i*n_virt + u]

								elif ((t != s) and (u == t)):

									L3_ans[i*n_virt + s] += (-2 * g[i, j, i, n_occ + s] ) * K[0, j*n_virt + t + n_ex] * K[1, i*n_virt + t]

							elif ((j != i) and (k == j)):

								if ((t == s) and (u == s)):

									L3_ans[i*n_virt + s] += (-2 * g[i, j, j, n_occ + s] + 2 * g[i, n_occ + s, n_occ + s, n_occ + s] + -2 * g[i, n_occ + s, j, j] ) * K[0, j*n_virt + s + n_ex] * K[1, j*n_virt + s]

								elif ((t == s) and (u != s) and (u != t)):

									L3_ans[i*n_virt + s] += (-4 * g[i, j, j, n_occ + u] + 2 * g[i, n_occ + u, j, j] + 4 * g[i, n_occ + s, n_occ + s, n_occ + u] + -2 * g[i, n_occ + u, n_occ + s, n_occ + s] ) * K[0, j*n_virt + s + n_ex] * K[1, j*n_virt + u]

								elif ((t != s) and (u == s)):

									L3_ans[i*n_virt + s] += (2 * g[i, n_occ + s, n_occ + s, n_occ + t] ) * K[0, j*n_virt + t + n_ex] * K[1, j*n_virt + s]

								elif ((t != s) and (u == t)):

									L3_ans[i*n_virt + s] += (-2 * g[i, n_occ + t, n_occ + s, n_occ + t] + 4 * g[i, n_occ + s, n_occ + t, n_occ + t] + 2 * g[i, j, j, n_occ + s] + -4 * g[i, n_occ + s, j, j] ) * K[0, j*n_virt + t + n_ex] * K[1, j*n_virt + t]

								elif ((t != s) and (u != s) and (u != t)):

									L3_ans[i*n_virt + s] += (4 * g[i, n_occ + s, n_occ + t, n_occ + u] + -2 * g[i, n_occ + u, n_occ + s, n_occ + t] ) * K[0, j*n_virt + t + n_ex] * K[1, j*n_virt + u]

							elif ((j != i) and (k != i) and (k != j)):

								if ((t == s) and (u == s)):

									L3_ans[i*n_virt + s] += (-2 * g[i, j, k, n_occ + s] + -2 * g[i, n_occ + s, j, k] ) * K[0, j*n_virt + s + n_ex] * K[1, k*n_virt + s]

								elif ((t == s) and (u != s) and (u != t)):

									L3_ans[i*n_virt + s] += (-4 * g[i, j, k, n_occ + u] + 2 * g[i, n_occ + u, j, k] ) * K[0, j*n_virt + s + n_ex] * K[1, k*n_virt + u]

								elif ((t != s) and (u == t)):

									L3_ans[i*n_virt + s] += (2 * g[i, j, k, n_occ + s] + -4 * g[i, n_occ + s, j, k] ) * K[0, j*n_virt + t + n_ex] * K[1, k*n_virt + t]

	# Current operator combination: {'a': 1, 'b': 2, 'c': 2}
	for i in range(n_occ):
		for j in range(n_occ):
			for k in range(n_occ):
				for s in range(n_virt):
					for t in range(n_virt):
						for u in range(n_virt):

							if ((j == i) and (k == i)):

								if ((t == s) and (u == s)):

									L3_ans[i*n_virt + s + n_ex] += (4 * F[i, n_occ + s] + -4 * g[i, n_occ + s, n_occ + s, n_occ + s] + 4 * g[i, i, i, n_occ + s] ) * K[0, i*n_virt + s + n_ex] * K[1, i*n_virt + s]

								elif ((t == s) and (u != s) and (u != t)):

									L3_ans[i*n_virt + s + n_ex] += (-4 * g[i, n_occ + s, n_occ + s, n_occ + u] ) * K[0, i*n_virt + s + n_ex] * K[1, i*n_virt + u]

								elif ((t != s) and (u == s)):

									L3_ans[i*n_virt + s + n_ex] += (2 * F[i, n_occ + t] + -2 * g[i, n_occ + t, n_occ + s, n_occ + s] + -2 * g[i, n_occ + s, n_occ + s, n_occ + t] + 2 * g[i, i, i, n_occ + t] ) * K[0, i*n_virt + t + n_ex] * K[1, i*n_virt + s]

								elif ((t != s) and (u == t)):

									L3_ans[i*n_virt + s + n_ex] += (2 * F[i, n_occ + s] + -2 * g[i, n_occ + t, n_occ + s, n_occ + t] + -2 * g[i, n_occ + s, n_occ + t, n_occ + t] + 2 * g[i, i, i, n_occ + s] ) * K[0, i*n_virt + t + n_ex] * K[1, i*n_virt + t]

								elif ((t != s) and (u != s) and (u != t)):

									L3_ans[i*n_virt + s + n_ex] += (-2 * g[i, n_occ + t, n_occ + s, n_occ + u] + -2 * g[i, n_occ + s, n_occ + t, n_occ + u] ) * K[0, i*n_virt + t + n_ex] * K[1, i*n_virt + u]

							elif ((j == i) and (k != i) and (k != j)):

								if ((t == s) and (u == s)):

									L3_ans[i*n_virt + s + n_ex] += (4 * g[i, k, i, n_occ + s] ) * K[0, i*n_virt + s + n_ex] * K[1, k*n_virt + s]

								elif ((t != s) and (u == s)):

									L3_ans[i*n_virt + s + n_ex] += (2 * g[i, k, i, n_occ + t] ) * K[0, i*n_virt + t + n_ex] * K[1, k*n_virt + s]

								elif ((t != s) and (u == t)):

									L3_ans[i*n_virt + s + n_ex] += (2 * g[i, k, i, n_occ + s] ) * K[0, i*n_virt + t + n_ex] * K[1, k*n_virt + t]

							elif ((j != i) and (k == i)):

								if ((t == s) and (u == s)):

									L3_ans[i*n_virt + s + n_ex] += (2 * F[j, n_occ + s] + -2 * g[j, n_occ + s, n_occ + s, n_occ + s] + 2 * g[i, i, j, n_occ + s] + 2 * g[i, j, i, n_occ + s] ) * K[0, j*n_virt + s + n_ex] * K[1, i*n_virt + s]

								elif ((t == s) and (u != s) and (u != t)):

									L3_ans[i*n_virt + s + n_ex] += (-2 * g[j, n_occ + s, n_occ + s, n_occ + u] ) * K[0, j*n_virt + s + n_ex] * K[1, i*n_virt + u]

								elif ((t != s) and (u == s)):

									L3_ans[i*n_virt + s + n_ex] += (2 * g[j, n_occ + s, n_occ + s, n_occ + t] + -4 * g[j, n_occ + t, n_occ + s, n_occ + s] + -2 * g[i, j, i, n_occ + t] + 4 * g[i, i, j, n_occ + t] ) * K[0, j*n_virt + t + n_ex] * K[1, i*n_virt + s]

								elif ((t != s) and (u == t)):

									L3_ans[i*n_virt + s + n_ex] += (2 * F[j, n_occ + s] + -4 * g[j, n_occ + t, n_occ + s, n_occ + t] + 2 * g[j, n_occ + s, n_occ + t, n_occ + t] + -2 * g[i, i, j, n_occ + s] + 4 * g[i, j, i, n_occ + s] ) * K[0, j*n_virt + t + n_ex] * K[1, i*n_virt + t]

								elif ((t != s) and (u != s) and (u != t)):

									L3_ans[i*n_virt + s + n_ex] += (2 * g[j, n_occ + s, n_occ + t, n_occ + u] + -4 * g[j, n_occ + t, n_occ + s, n_occ + u] ) * K[0, j*n_virt + t + n_ex] * K[1, i*n_virt + u]

							elif ((j != i) and (k == j)):

								if ((t == s) and (u == s)):

									L3_ans[i*n_virt + s + n_ex] += (2 * F[i, n_occ + s] + -2 * g[i, n_occ + s, n_occ + s, n_occ + s] + 2 * g[i, n_occ + s, j, j] + 2 * g[i, j, j, n_occ + s] ) * K[0, j*n_virt + s + n_ex] * K[1, j*n_virt + s]

								elif ((t == s) and (u != s) and (u != t)):

									L3_ans[i*n_virt + s + n_ex] += (-2 * g[i, n_occ + s, n_occ + s, n_occ + u] ) * K[0, j*n_virt + s + n_ex] * K[1, j*n_virt + u]

								elif ((t != s) and (u == s)):

									L3_ans[i*n_virt + s + n_ex] += (2 * F[i, n_occ + t] + -4 * g[i, n_occ + s, n_occ + s, n_occ + t] + 2 * g[i, n_occ + t, n_occ + s, n_occ + s] + -2 * g[i, n_occ + t, j, j] + 4 * g[i, j, j, n_occ + t] ) * K[0, j*n_virt + t + n_ex] * K[1, j*n_virt + s]

								elif ((t != s) and (u == t)):

									L3_ans[i*n_virt + s + n_ex] += (2 * g[i, n_occ + t, n_occ + s, n_occ + t] + -4 * g[i, n_occ + s, n_occ + t, n_occ + t] + -2 * g[i, j, j, n_occ + s] + 4 * g[i, n_occ + s, j, j] ) * K[0, j*n_virt + t + n_ex] * K[1, j*n_virt + t]

								elif ((t != s) and (u != s) and (u != t)):

									L3_ans[i*n_virt + s + n_ex] += (-4 * g[i, n_occ + s, n_occ + t, n_occ + u] + 2 * g[i, n_occ + t, n_occ + s, n_occ + u] ) * K[0, j*n_virt + t + n_ex] * K[1, j*n_virt + u]

							elif ((j != i) and (k != i) and (k != j)):

								if ((t == s) and (u == s)):

									L3_ans[i*n_virt + s + n_ex] += (2 * g[i, k, j, n_occ + s] + 2 * g[i, n_occ + s, j, k] ) * K[0, j*n_virt + s + n_ex] * K[1, k*n_virt + s]

								elif ((t != s) and (u == s)):

									L3_ans[i*n_virt + s + n_ex] += (4 * g[i, k, j, n_occ + t] + -2 * g[i, n_occ + t, j, k] ) * K[0, j*n_virt + t + n_ex] * K[1, k*n_virt + s]

								elif ((t != s) and (u == t)):

									L3_ans[i*n_virt + s + n_ex] += (-2 * g[i, k, j, n_occ + s] + 4 * g[i, n_occ + s, j, k] ) * K[0, j*n_virt + t + n_ex] * K[1, k*n_virt + t]

	# Current operator combination: {'a': 1, 'b': 2, 'c': 3}
	# All terms vanished for this combination

	# Current operator combination: {'a': 1, 'b': 3, 'c': 1}
	# This combination was excluded by the contr_type_only argument {'a': 1, 'b': 3, 'c': 1}
	# Current operator combination: {'a': 1, 'b': 3, 'c': 2}
	# This combination was excluded by the contr_type_only argument {'a': 1, 'b': 3, 'c': 2}
	# Current operator combination: {'a': 1, 'b': 3, 'c': 3}
	# This combination was excluded by the contr_type_only argument {'a': 1, 'b': 3, 'c': 3}
	# Current operator combination: {'a': 2, 'b': 1, 'c': 1}
	for i in range(n_occ):
		for j in range(n_occ):
			for k in range(n_occ):
				for s in range(n_virt):
					for t in range(n_virt):
						for u in range(n_virt):

							if ((j == i) and (k == i)):

								if ((t == s) and (u == s)):

									L3_ans[i*n_virt + s] += (-4 * F[i, n_occ + s] + 4 * g[i, n_occ + s, n_occ + s, n_occ + s] + -4 * g[i, i, i, n_occ + s] ) * K[0, i*n_virt + s] * K[1, i*n_virt + s + n_ex]

								elif ((t == s) and (u != s) and (u != t)):

									L3_ans[i*n_virt + s] += (4 * g[i, n_occ + s, n_occ + s, n_occ + u] ) * K[0, i*n_virt + s] * K[1, i*n_virt + u + n_ex]

								elif ((t != s) and (u == s)):

									L3_ans[i*n_virt + s] += (-2 * F[i, n_occ + t] + 2 * g[i, n_occ + t, n_occ + s, n_occ + s] + 2 * g[i, n_occ + s, n_occ + s, n_occ + t] + -2 * g[i, i, i, n_occ + t] ) * K[0, i*n_virt + t] * K[1, i*n_virt + s + n_ex]

								elif ((t != s) and (u == t)):

									L3_ans[i*n_virt + s] += (-2 * F[i, n_occ + s] + 2 * g[i, n_occ + t, n_occ + s, n_occ + t] + 2 * g[i, n_occ + s, n_occ + t, n_occ + t] + -2 * g[i, i, i, n_occ + s] ) * K[0, i*n_virt + t] * K[1, i*n_virt + t + n_ex]

								elif ((t != s) and (u != s) and (u != t)):

									L3_ans[i*n_virt + s] += (2 * g[i, n_occ + t, n_occ + s, n_occ + u] + 2 * g[i, n_occ + s, n_occ + t, n_occ + u] ) * K[0, i*n_virt + t] * K[1, i*n_virt + u + n_ex]

							elif ((j == i) and (k != i) and (k != j)):

								if ((t == s) and (u == s)):

									L3_ans[i*n_virt + s] += (-4 * g[i, k, i, n_occ + s] ) * K[0, i*n_virt + s] * K[1, k*n_virt + s + n_ex]

								elif ((t != s) and (u == s)):

									L3_ans[i*n_virt + s] += (-2 * g[i, k, i, n_occ + t] ) * K[0, i*n_virt + t] * K[1, k*n_virt + s + n_ex]

								elif ((t != s) and (u == t)):

									L3_ans[i*n_virt + s] += (-2 * g[i, k, i, n_occ + s] ) * K[0, i*n_virt + t] * K[1, k*n_virt + t + n_ex]

							elif ((j != i) and (k == i)):

								if ((t == s) and (u == s)):

									L3_ans[i*n_virt + s] += (-2 * F[j, n_occ + s] + 2 * g[j, n_occ + s, n_occ + s, n_occ + s] + -2 * g[i, i, j, n_occ + s] + -2 * g[i, j, i, n_occ + s] ) * K[0, j*n_virt + s] * K[1, i*n_virt + s + n_ex]

								elif ((t == s) and (u != s) and (u != t)):

									L3_ans[i*n_virt + s] += (2 * g[j, n_occ + s, n_occ + s, n_occ + u] ) * K[0, j*n_virt + s] * K[1, i*n_virt + u + n_ex]

								elif ((t != s) and (u == s)):

									L3_ans[i*n_virt + s] += (-2 * g[j, n_occ + s, n_occ + s, n_occ + t] + 4 * g[j, n_occ + t, n_occ + s, n_occ + s] + 2 * g[i, j, i, n_occ + t] + -4 * g[i, i, j, n_occ + t] ) * K[0, j*n_virt + t] * K[1, i*n_virt + s + n_ex]

								elif ((t != s) and (u == t)):

									L3_ans[i*n_virt + s] += (-2 * F[j, n_occ + s] + 4 * g[j, n_occ + t, n_occ + s, n_occ + t] + -2 * g[j, n_occ + s, n_occ + t, n_occ + t] + 2 * g[i, i, j, n_occ + s] + -4 * g[i, j, i, n_occ + s] ) * K[0, j*n_virt + t] * K[1, i*n_virt + t + n_ex]

								elif ((t != s) and (u != s) and (u != t)):

									L3_ans[i*n_virt + s] += (-2 * g[j, n_occ + s, n_occ + t, n_occ + u] + 4 * g[j, n_occ + t, n_occ + s, n_occ + u] ) * K[0, j*n_virt + t] * K[1, i*n_virt + u + n_ex]

							elif ((j != i) and (k == j)):

								if ((t == s) and (u == s)):

									L3_ans[i*n_virt + s] += (-2 * F[i, n_occ + s] + 2 * g[i, n_occ + s, n_occ + s, n_occ + s] + -2 * g[i, n_occ + s, j, j] + -2 * g[i, j, j, n_occ + s] ) * K[0, j*n_virt + s] * K[1, j*n_virt + s + n_ex]

								elif ((t == s) and (u != s) and (u != t)):

									L3_ans[i*n_virt + s] += (2 * g[i, n_occ + s, n_occ + s, n_occ + u] ) * K[0, j*n_virt + s] * K[1, j*n_virt + u + n_ex]

								elif ((t != s) and (u == s)):

									L3_ans[i*n_virt + s] += (-2 * F[i, n_occ + t] + 4 * g[i, n_occ + s, n_occ + s, n_occ + t] + -2 * g[i, n_occ + t, n_occ + s, n_occ + s] + 2 * g[i, n_occ + t, j, j] + -4 * g[i, j, j, n_occ + t] ) * K[0, j*n_virt + t] * K[1, j*n_virt + s + n_ex]

								elif ((t != s) and (u == t)):

									L3_ans[i*n_virt + s] += (-2 * g[i, n_occ + t, n_occ + s, n_occ + t] + 4 * g[i, n_occ + s, n_occ + t, n_occ + t] + 2 * g[i, j, j, n_occ + s] + -4 * g[i, n_occ + s, j, j] ) * K[0, j*n_virt + t] * K[1, j*n_virt + t + n_ex]

								elif ((t != s) and (u != s) and (u != t)):

									L3_ans[i*n_virt + s] += (4 * g[i, n_occ + s, n_occ + t, n_occ + u] + -2 * g[i, n_occ + t, n_occ + s, n_occ + u] ) * K[0, j*n_virt + t] * K[1, j*n_virt + u + n_ex]

							elif ((j != i) and (k != i) and (k != j)):

								if ((t == s) and (u == s)):

									L3_ans[i*n_virt + s] += (-2 * g[i, k, j, n_occ + s] + -2 * g[i, n_occ + s, j, k] ) * K[0, j*n_virt + s] * K[1, k*n_virt + s + n_ex]

								elif ((t != s) and (u == s)):

									L3_ans[i*n_virt + s] += (-4 * g[i, k, j, n_occ + t] + 2 * g[i, n_occ + t, j, k] ) * K[0, j*n_virt + t] * K[1, k*n_virt + s + n_ex]

								elif ((t != s) and (u == t)):

									L3_ans[i*n_virt + s] += (2 * g[i, k, j, n_occ + s] + -4 * g[i, n_occ + s, j, k] ) * K[0, j*n_virt + t] * K[1, k*n_virt + t + n_ex]

	# Current operator combination: {'a': 2, 'b': 1, 'c': 2}
	for i in range(n_occ):
		for j in range(n_occ):
			for k in range(n_occ):
				for s in range(n_virt):
					for t in range(n_virt):
						for u in range(n_virt):

							if ((j == i) and (k == i)):

								if ((t == s) and (u == s)):

									L3_ans[i*n_virt + s + n_ex] += (-4 * g[i, n_occ + s, n_occ + s, n_occ + s] + 4 * g[i, i, i, n_occ + s] ) * K[0, i*n_virt + s] * K[1, i*n_virt + s + n_ex]

								elif ((t == s) and (u != s) and (u != t)):

									L3_ans[i*n_virt + s + n_ex] += (-2 * g[i, n_occ + u, n_occ + s, n_occ + s] + -2 * g[i, n_occ + s, n_occ + s, n_occ + u] + 2 * g[i, i, i, n_occ + u] ) * K[0, i*n_virt + s] * K[1, i*n_virt + u + n_ex]

								elif ((t != s) and (u == s)):

									L3_ans[i*n_virt + s + n_ex] += (-4 * g[i, n_occ + s, n_occ + s, n_occ + t] ) * K[0, i*n_virt + t] * K[1, i*n_virt + s + n_ex]

								elif ((t != s) and (u == t)):

									L3_ans[i*n_virt + s + n_ex] += (-2 * g[i, n_occ + t, n_occ + s, n_occ + t] + -2 * g[i, n_occ + s, n_occ + t, n_occ + t] + 2 * g[i, i, i, n_occ + s] ) * K[0, i*n_virt + t] * K[1, i*n_virt + t + n_ex]

								elif ((t != s) and (u != s) and (u != t)):

									L3_ans[i*n_virt + s + n_ex] += (-2 * g[i, n_occ + u, n_occ + s, n_occ + t] + -2 * g[i, n_occ + s, n_occ + t, n_occ + u] ) * K[0, i*n_virt + t] * K[1, i*n_virt + u + n_ex]

							elif ((j == i) and (k != i) and (k != j)):

								if ((t == s) and (u == s)):

									L3_ans[i*n_virt + s + n_ex] += (2 * g[i, k, i, n_occ + s] + -2 * g[k, n_occ + s, n_occ + s, n_occ + s] + 2 * g[i, i, k, n_occ + s] ) * K[0, i*n_virt + s] * K[1, k*n_virt + s + n_ex]

								elif ((t == s) and (u != s) and (u != t)):

									L3_ans[i*n_virt + s + n_ex] += (2 * g[k, n_occ + s, n_occ + s, n_occ + u] + -4 * g[k, n_occ + u, n_occ + s, n_occ + s] + -2 * g[i, k, i, n_occ + u] + 4 * g[i, i, k, n_occ + u] ) * K[0, i*n_virt + s] * K[1, k*n_virt + u + n_ex]

								elif ((t != s) and (u == s)):

									L3_ans[i*n_virt + s + n_ex] += (-2 * g[k, n_occ + s, n_occ + s, n_occ + t] ) * K[0, i*n_virt + t] * K[1, k*n_virt + s + n_ex]

								elif ((t != s) and (u == t)):

									L3_ans[i*n_virt + s + n_ex] += (4 * g[i, k, i, n_occ + s] + -2 * g[i, i, k, n_occ + s] + -4 * g[k, n_occ + t, n_occ + s, n_occ + t] + 2 * g[k, n_occ + s, n_occ + t, n_occ + t] ) * K[0, i*n_virt + t] * K[1, k*n_virt + t + n_ex]

								elif ((t != s) and (u != s) and (u != t)):

									L3_ans[i*n_virt + s + n_ex] += (2 * g[k, n_occ + s, n_occ + t, n_occ + u] + -4 * g[k, n_occ + u, n_occ + s, n_occ + t] ) * K[0, i*n_virt + t] * K[1, k*n_virt + u + n_ex]

							elif ((j != i) and (k == i)):

								if ((t == s) and (u == s)):

									L3_ans[i*n_virt + s + n_ex] += (4 * g[i, j, i, n_occ + s] ) * K[0, j*n_virt + s] * K[1, i*n_virt + s + n_ex]

								elif ((t == s) and (u != s) and (u != t)):

									L3_ans[i*n_virt + s + n_ex] += (2 * g[i, j, i, n_occ + u] ) * K[0, j*n_virt + s] * K[1, i*n_virt + u + n_ex]

								elif ((t != s) and (u == t)):

									L3_ans[i*n_virt + s + n_ex] += (2 * g[i, j, i, n_occ + s] ) * K[0, j*n_virt + t] * K[1, i*n_virt + t + n_ex]

							elif ((j != i) and (k == j)):

								if ((t == s) and (u == s)):

									L3_ans[i*n_virt + s + n_ex] += (2 * g[i, j, j, n_occ + s] + -2 * g[i, n_occ + s, n_occ + s, n_occ + s] + 2 * g[i, n_occ + s, j, j] ) * K[0, j*n_virt + s] * K[1, j*n_virt + s + n_ex]

								elif ((t == s) and (u != s) and (u != t)):

									L3_ans[i*n_virt + s + n_ex] += (4 * g[i, j, j, n_occ + u] + -2 * g[i, n_occ + u, j, j] + -4 * g[i, n_occ + s, n_occ + s, n_occ + u] + 2 * g[i, n_occ + u, n_occ + s, n_occ + s] ) * K[0, j*n_virt + s] * K[1, j*n_virt + u + n_ex]

								elif ((t != s) and (u == s)):

									L3_ans[i*n_virt + s + n_ex] += (-2 * g[i, n_occ + s, n_occ + s, n_occ + t] ) * K[0, j*n_virt + t] * K[1, j*n_virt + s + n_ex]

								elif ((t != s) and (u == t)):

									L3_ans[i*n_virt + s + n_ex] += (2 * g[i, n_occ + t, n_occ + s, n_occ + t] + -4 * g[i, n_occ + s, n_occ + t, n_occ + t] + -2 * g[i, j, j, n_occ + s] + 4 * g[i, n_occ + s, j, j] ) * K[0, j*n_virt + t] * K[1, j*n_virt + t + n_ex]

								elif ((t != s) and (u != s) and (u != t)):

									L3_ans[i*n_virt + s + n_ex] += (-4 * g[i, n_occ + s, n_occ + t, n_occ + u] + 2 * g[i, n_occ + u, n_occ + s, n_occ + t] ) * K[0, j*n_virt + t] * K[1, j*n_virt + u + n_ex]

							elif ((j != i) and (k != i) and (k != j)):

								if ((t == s) and (u == s)):

									L3_ans[i*n_virt + s + n_ex] += (2 * g[i, j, k, n_occ + s] + 2 * g[i, n_occ + s, j, k] ) * K[0, j*n_virt + s] * K[1, k*n_virt + s + n_ex]

								elif ((t == s) and (u != s) and (u != t)):

									L3_ans[i*n_virt + s + n_ex] += (4 * g[i, j, k, n_occ + u] + -2 * g[i, n_occ + u, j, k] ) * K[0, j*n_virt + s] * K[1, k*n_virt + u + n_ex]

								elif ((t != s) and (u == t)):

									L3_ans[i*n_virt + s + n_ex] += (-2 * g[i, j, k, n_occ + s] + 4 * g[i, n_occ + s, j, k] ) * K[0, j*n_virt + t] * K[1, k*n_virt + t + n_ex]

	# Current operator combination: {'a': 2, 'b': 1, 'c': 3}
	# All terms vanished for this combination

	# Current operator combination: {'a': 2, 'b': 2, 'c': 1}
	for i in range(n_occ):
		for j in range(n_occ):
			for k in range(n_occ):
				for s in range(n_virt):
					for t in range(n_virt):
						for u in range(n_virt):

							if ((j == i) and (k == i)):

								if ((t == s) and (u == s)):

									L3_ans[i*n_virt + s] += (-4 * F[i, n_occ + s] + 4 * g[i, n_occ + s, n_occ + s, n_occ + s] + -4 * g[i, i, i, n_occ + s] ) * K[0, i*n_virt + s + n_ex] * K[1, i*n_virt + s + n_ex]

								elif ((t == s) and (u != s) and (u != t)):

									L3_ans[i*n_virt + s] += (-2 * F[i, n_occ + u] + 2 * g[i, n_occ + s, n_occ + s, n_occ + u] + 2 * g[i, n_occ + u, n_occ + s, n_occ + s] + -2 * g[i, i, i, n_occ + u] ) * K[0, i*n_virt + s + n_ex] * K[1, i*n_virt + u + n_ex]

								elif ((t != s) and (u == s)):

									L3_ans[i*n_virt + s] += (-2 * F[i, n_occ + t] + 2 * g[i, n_occ + t, n_occ + s, n_occ + s] + 2 * g[i, n_occ + s, n_occ + s, n_occ + t] + -2 * g[i, i, i, n_occ + t] ) * K[0, i*n_virt + t + n_ex] * K[1, i*n_virt + s + n_ex]

								elif ((t != s) and (u == t)):

									L3_ans[i*n_virt + s] += (4 * g[i, n_occ + t, n_occ + s, n_occ + t] ) * K[0, i*n_virt + t + n_ex] * K[1, i*n_virt + t + n_ex]

								elif ((t != s) and (u != s) and (u != t)):

									L3_ans[i*n_virt + s] += (2 * g[i, n_occ + t, n_occ + s, n_occ + u] + 2 * g[i, n_occ + u, n_occ + s, n_occ + t] ) * K[0, i*n_virt + t + n_ex] * K[1, i*n_virt + u + n_ex]

							elif ((j == i) and (k != i) and (k != j)):

								if ((t == s) and (u == s)):

									L3_ans[i*n_virt + s] += (-2 * F[k, n_occ + s] + -2 * g[i, i, k, n_occ + s] + 2 * g[k, n_occ + s, n_occ + s, n_occ + s] + -2 * g[i, k, i, n_occ + s] ) * K[0, i*n_virt + s + n_ex] * K[1, k*n_virt + s + n_ex]

								elif ((t == s) and (u != s) and (u != t)):

									L3_ans[i*n_virt + s] += (2 * g[i, k, i, n_occ + u] + -4 * g[i, i, k, n_occ + u] + -2 * g[k, n_occ + s, n_occ + s, n_occ + u] + 4 * g[k, n_occ + u, n_occ + s, n_occ + s] ) * K[0, i*n_virt + s + n_ex] * K[1, k*n_virt + u + n_ex]

								elif ((t != s) and (u == s)):

									L3_ans[i*n_virt + s] += (-2 * F[k, n_occ + t] + 4 * g[k, n_occ + s, n_occ + s, n_occ + t] + -2 * g[k, n_occ + t, n_occ + s, n_occ + s] + 2 * g[i, i, k, n_occ + t] + -4 * g[i, k, i, n_occ + t] ) * K[0, i*n_virt + t + n_ex] * K[1, k*n_virt + s + n_ex]

								elif ((t != s) and (u == t)):

									L3_ans[i*n_virt + s] += (2 * g[k, n_occ + t, n_occ + s, n_occ + t] ) * K[0, i*n_virt + t + n_ex] * K[1, k*n_virt + t + n_ex]

								elif ((t != s) and (u != s) and (u != t)):

									L3_ans[i*n_virt + s] += (-2 * g[k, n_occ + t, n_occ + s, n_occ + u] + 4 * g[k, n_occ + u, n_occ + s, n_occ + t] ) * K[0, i*n_virt + t + n_ex] * K[1, k*n_virt + u + n_ex]

							elif ((j != i) and (k == i)):

								if ((t == s) and (u == s)):

									L3_ans[i*n_virt + s] += (-2 * F[j, n_occ + s] + -2 * g[i, i, j, n_occ + s] + 2 * g[j, n_occ + s, n_occ + s, n_occ + s] + -2 * g[i, j, i, n_occ + s] ) * K[0, j*n_virt + s + n_ex] * K[1, i*n_virt + s + n_ex]

								elif ((t == s) and (u != s) and (u != t)):

									L3_ans[i*n_virt + s] += (-2 * F[j, n_occ + u] + 4 * g[j, n_occ + s, n_occ + s, n_occ + u] + -2 * g[j, n_occ + u, n_occ + s, n_occ + s] + 2 * g[i, i, j, n_occ + u] + -4 * g[i, j, i, n_occ + u] ) * K[0, j*n_virt + s + n_ex] * K[1, i*n_virt + u + n_ex]

								elif ((t != s) and (u == s)):

									L3_ans[i*n_virt + s] += (2 * g[i, j, i, n_occ + t] + -4 * g[i, i, j, n_occ + t] + -2 * g[j, n_occ + s, n_occ + s, n_occ + t] + 4 * g[j, n_occ + t, n_occ + s, n_occ + s] ) * K[0, j*n_virt + t + n_ex] * K[1, i*n_virt + s + n_ex]

								elif ((t != s) and (u == t)):

									L3_ans[i*n_virt + s] += (2 * g[j, n_occ + t, n_occ + s, n_occ + t] ) * K[0, j*n_virt + t + n_ex] * K[1, i*n_virt + t + n_ex]

								elif ((t != s) and (u != s) and (u != t)):

									L3_ans[i*n_virt + s] += (4 * g[j, n_occ + t, n_occ + s, n_occ + u] + -2 * g[j, n_occ + u, n_occ + s, n_occ + t] ) * K[0, j*n_virt + t + n_ex] * K[1, i*n_virt + u + n_ex]

							elif ((j != i) and (k == j)):

								if ((t == s) and (u == s)):

									L3_ans[i*n_virt + s] += (-4 * g[i, j, j, n_occ + s] ) * K[0, j*n_virt + s + n_ex] * K[1, j*n_virt + s + n_ex]

								elif ((t == s) and (u != s) and (u != t)):

									L3_ans[i*n_virt + s] += (-2 * g[i, j, j, n_occ + u] ) * K[0, j*n_virt + s + n_ex] * K[1, j*n_virt + u + n_ex]

								elif ((t != s) and (u == s)):

									L3_ans[i*n_virt + s] += (-2 * g[i, j, j, n_occ + t] ) * K[0, j*n_virt + t + n_ex] * K[1, j*n_virt + s + n_ex]

							elif ((j != i) and (k != i) and (k != j)):

								if ((t == s) and (u == s)):

									L3_ans[i*n_virt + s] += (-2 * g[i, k, j, n_occ + s] + -2 * g[i, j, k, n_occ + s] ) * K[0, j*n_virt + s + n_ex] * K[1, k*n_virt + s + n_ex]

								elif ((t == s) and (u != s) and (u != t)):

									L3_ans[i*n_virt + s] += (-4 * g[i, j, k, n_occ + u] + 2 * g[i, k, j, n_occ + u] ) * K[0, j*n_virt + s + n_ex] * K[1, k*n_virt + u + n_ex]

								elif ((t != s) and (u == s)):

									L3_ans[i*n_virt + s] += (2 * g[i, j, k, n_occ + t] + -4 * g[i, k, j, n_occ + t] ) * K[0, j*n_virt + t + n_ex] * K[1, k*n_virt + s + n_ex]

	# Current operator combination: {'a': 2, 'b': 2, 'c': 2}
	# All terms vanished for this combination

	# Current operator combination: {'a': 2, 'b': 2, 'c': 3}
	# All terms vanished for this combination

	# Current operator combination: {'a': 2, 'b': 3, 'c': 1}
	# This combination was excluded by the contr_type_only argument {'a': 2, 'b': 3, 'c': 1}
	# Current operator combination: {'a': 2, 'b': 3, 'c': 2}
	# This combination was excluded by the contr_type_only argument {'a': 2, 'b': 3, 'c': 2}
	# Current operator combination: {'a': 2, 'b': 3, 'c': 3}
	# This combination was excluded by the contr_type_only argument {'a': 2, 'b': 3, 'c': 3}
	# Current operator combination: {'a': 3, 'b': 1, 'c': 1}
	# This combination was excluded by the contr_type_only argument {'a': 3, 'b': 1, 'c': 1}
	# Current operator combination: {'a': 3, 'b': 1, 'c': 2}
	# This combination was excluded by the contr_type_only argument {'a': 3, 'b': 1, 'c': 2}
	# Current operator combination: {'a': 3, 'b': 1, 'c': 3}
	# This combination was excluded by the contr_type_only argument {'a': 3, 'b': 1, 'c': 3}
	# Current operator combination: {'a': 3, 'b': 2, 'c': 1}
	# This combination was excluded by the contr_type_only argument {'a': 3, 'b': 2, 'c': 1}
	# Current operator combination: {'a': 3, 'b': 2, 'c': 2}
	# This combination was excluded by the contr_type_only argument {'a': 3, 'b': 2, 'c': 2}
	# Current operator combination: {'a': 3, 'b': 2, 'c': 3}
	# This combination was excluded by the contr_type_only argument {'a': 3, 'b': 2, 'c': 3}
	# Current operator combination: {'a': 3, 'b': 3, 'c': 1}
	# This combination was excluded by the contr_type_only argument {'a': 3, 'b': 3, 'c': 1}
	# Current operator combination: {'a': 3, 'b': 3, 'c': 2}
	# This combination was excluded by the contr_type_only argument {'a': 3, 'b': 3, 'c': 2}
	# Current operator combination: {'a': 3, 'b': 3, 'c': 3}
	# This combination was excluded by the contr_type_only argument {'a': 3, 'b': 3, 'c': 3}
	
	return 0.5* L3_ans
