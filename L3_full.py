import numpy as np


def L3(n_occ, n_virt, H00, F, g, K): 
 
	n_ex = n_occ * n_virt

	# This operator combination: {'a': 1, 'b': 1, 'c': 1}
	# All terms vanished for this combination

	# This operator combination: {'a': 1, 'b': 1, 'c': 2}
	for i in range(n_occ):
		for j in range(n_occ):
			for k in range(n_occ):
				for s in range(n_virt):
					for t in range(n_virt):
						for u in range(n_virt):

							if ((j == i) and (k == i)):

								if ((t == s) and (u == s)):

									L3[i*n_virt + s + n_ex] += (4 * F[i, n_occ + s] + -4 * g[i, n_occ + s, n_occ + s, n_occ + s] + 4 * g[i, i, i, n_occ + s] ) * K[0, i*n_virt + s] * K[1, i*n_virt + s]

								elif ((t == s) and (u != s) and (u != t)):

									L3[i*n_virt + s + n_ex] += (2 * F[i, n_occ + u] + -2 * g[i, n_occ + s, n_occ + s, n_occ + u] + -2 * g[i, n_occ + u, n_occ + s, n_occ + s] + 2 * g[i, i, i, n_occ + u] ) * K[0, i*n_virt + s] * K[1, i*n_virt + u]

								elif ((t != s) and (u == s)):

									L3[i*n_virt + s + n_ex] += (2 * F[i, n_occ + t] + -2 * g[i, n_occ + t, n_occ + s, n_occ + s] + -2 * g[i, n_occ + s, n_occ + s, n_occ + t] + 2 * g[i, i, i, n_occ + t] ) * K[0, i*n_virt + t] * K[1, i*n_virt + s]

								elif ((t != s) and (u == t)):

									L3[i*n_virt + s + n_ex] += (-4 * g[i, n_occ + t, n_occ + s, n_occ + t] ) * K[0, i*n_virt + t] * K[1, i*n_virt + t]

								elif ((t != s) and (u != s) and (u != t)):

									L3[i*n_virt + s + n_ex] += (-2 * g[i, n_occ + t, n_occ + s, n_occ + u] + -2 * g[i, n_occ + u, n_occ + s, n_occ + t] ) * K[0, i*n_virt + t] * K[1, i*n_virt + u]

							elif ((j == i) and (k != i) and (k != j)):

								if ((t == s) and (u == s)):

									L3[i*n_virt + s + n_ex] += (2 * F[k, n_occ + s] + 2 * g[i, i, k, n_occ + s] + -2 * g[k, n_occ + s, n_occ + s, n_occ + s] + 2 * g[i, k, i, n_occ + s] ) * K[0, i*n_virt + s] * K[1, k*n_virt + s]

								elif ((t == s) and (u != s) and (u != t)):

									L3[i*n_virt + s + n_ex] += (-2 * g[i, k, i, n_occ + u] + 4 * g[i, i, k, n_occ + u] + 2 * g[k, n_occ + s, n_occ + s, n_occ + u] + -4 * g[k, n_occ + u, n_occ + s, n_occ + s] ) * K[0, i*n_virt + s] * K[1, k*n_virt + u]

								elif ((t != s) and (u == s)):

									L3[i*n_virt + s + n_ex] += (2 * F[k, n_occ + t] + -4 * g[k, n_occ + s, n_occ + s, n_occ + t] + 2 * g[k, n_occ + t, n_occ + s, n_occ + s] + -2 * g[i, i, k, n_occ + t] + 4 * g[i, k, i, n_occ + t] ) * K[0, i*n_virt + t] * K[1, k*n_virt + s]

								elif ((t != s) and (u == t)):

									L3[i*n_virt + s + n_ex] += (-2 * g[k, n_occ + t, n_occ + s, n_occ + t] ) * K[0, i*n_virt + t] * K[1, k*n_virt + t]

								elif ((t != s) and (u != s) and (u != t)):

									L3[i*n_virt + s + n_ex] += (2 * g[k, n_occ + t, n_occ + s, n_occ + u] + -4 * g[k, n_occ + u, n_occ + s, n_occ + t] ) * K[0, i*n_virt + t] * K[1, k*n_virt + u]

							elif ((j != i) and (k == i)):

								if ((t == s) and (u == s)):

									L3[i*n_virt + s + n_ex] += (2 * F[j, n_occ + s] + 2 * g[i, i, j, n_occ + s] + -2 * g[j, n_occ + s, n_occ + s, n_occ + s] + 2 * g[i, j, i, n_occ + s] ) * K[0, j*n_virt + s] * K[1, i*n_virt + s]

								elif ((t == s) and (u != s) and (u != t)):

									L3[i*n_virt + s + n_ex] += (2 * F[j, n_occ + u] + -4 * g[j, n_occ + s, n_occ + s, n_occ + u] + 2 * g[j, n_occ + u, n_occ + s, n_occ + s] + -2 * g[i, i, j, n_occ + u] + 4 * g[i, j, i, n_occ + u] ) * K[0, j*n_virt + s] * K[1, i*n_virt + u]

								elif ((t != s) and (u == s)):

									L3[i*n_virt + s + n_ex] += (-2 * g[i, j, i, n_occ + t] + 4 * g[i, i, j, n_occ + t] + 2 * g[j, n_occ + s, n_occ + s, n_occ + t] + -4 * g[j, n_occ + t, n_occ + s, n_occ + s] ) * K[0, j*n_virt + t] * K[1, i*n_virt + s]

								elif ((t != s) and (u == t)):

									L3[i*n_virt + s + n_ex] += (-2 * g[j, n_occ + t, n_occ + s, n_occ + t] ) * K[0, j*n_virt + t] * K[1, i*n_virt + t]

								elif ((t != s) and (u != s) and (u != t)):

									L3[i*n_virt + s + n_ex] += (-4 * g[j, n_occ + t, n_occ + s, n_occ + u] + 2 * g[j, n_occ + u, n_occ + s, n_occ + t] ) * K[0, j*n_virt + t] * K[1, i*n_virt + u]

							elif ((j != i) and (k == j)):

								if ((t == s) and (u == s)):

									L3[i*n_virt + s + n_ex] += (4 * g[i, j, j, n_occ + s] ) * K[0, j*n_virt + s] * K[1, j*n_virt + s]

								elif ((t == s) and (u != s) and (u != t)):

									L3[i*n_virt + s + n_ex] += (2 * g[i, j, j, n_occ + u] ) * K[0, j*n_virt + s] * K[1, j*n_virt + u]

								elif ((t != s) and (u == s)):

									L3[i*n_virt + s + n_ex] += (2 * g[i, j, j, n_occ + t] ) * K[0, j*n_virt + t] * K[1, j*n_virt + s]

							elif ((j != i) and (k != i) and (k != j)):

								if ((t == s) and (u == s)):

									L3[i*n_virt + s + n_ex] += (2 * g[i, k, j, n_occ + s] + 2 * g[i, j, k, n_occ + s] ) * K[0, j*n_virt + s] * K[1, k*n_virt + s]

								elif ((t == s) and (u != s) and (u != t)):

									L3[i*n_virt + s + n_ex] += (4 * g[i, j, k, n_occ + u] + -2 * g[i, k, j, n_occ + u] ) * K[0, j*n_virt + s] * K[1, k*n_virt + u]

								elif ((t != s) and (u == s)):

									L3[i*n_virt + s + n_ex] += (-2 * g[i, j, k, n_occ + t] + 4 * g[i, k, j, n_occ + t] ) * K[0, j*n_virt + t] * K[1, k*n_virt + s]

	# This operator combination: {'a': 1, 'b': 1, 'c': 3}
	# All terms vanished for this combination

	# This operator combination: {'a': 1, 'b': 2, 'c': 1}
	for i in range(n_occ):
		for j in range(n_occ):
			for k in range(n_occ):
				for s in range(n_virt):
					for t in range(n_virt):
						for u in range(n_virt):

							if ((j == i) and (k == i)):

								if ((t == s) and (u == s)):

									L3[i*n_virt + s] += (4 * g[i, n_occ + s, n_occ + s, n_occ + s] + -4 * g[i, i, i, n_occ + s] ) * K[0, i*n_virt + s + n_ex] * K[1, i*n_virt + s]

								elif ((t == s) and (u != s) and (u != t)):

									L3[i*n_virt + s] += (2 * g[i, n_occ + u, n_occ + s, n_occ + s] + 2 * g[i, n_occ + s, n_occ + s, n_occ + u] + -2 * g[i, i, i, n_occ + u] ) * K[0, i*n_virt + s + n_ex] * K[1, i*n_virt + u]

								elif ((t != s) and (u == s)):

									L3[i*n_virt + s] += (4 * g[i, n_occ + s, n_occ + s, n_occ + t] ) * K[0, i*n_virt + t + n_ex] * K[1, i*n_virt + s]

								elif ((t != s) and (u == t)):

									L3[i*n_virt + s] += (2 * g[i, n_occ + t, n_occ + s, n_occ + t] + 2 * g[i, n_occ + s, n_occ + t, n_occ + t] + -2 * g[i, i, i, n_occ + s] ) * K[0, i*n_virt + t + n_ex] * K[1, i*n_virt + t]

								elif ((t != s) and (u != s) and (u != t)):

									L3[i*n_virt + s] += (2 * g[i, n_occ + u, n_occ + s, n_occ + t] + 2 * g[i, n_occ + s, n_occ + t, n_occ + u] ) * K[0, i*n_virt + t + n_ex] * K[1, i*n_virt + u]

							elif ((j == i) and (k != i) and (k != j)):

								if ((t == s) and (u == s)):

									L3[i*n_virt + s] += (-2 * g[i, k, i, n_occ + s] + 2 * g[k, n_occ + s, n_occ + s, n_occ + s] + -2 * g[i, i, k, n_occ + s] ) * K[0, i*n_virt + s + n_ex] * K[1, k*n_virt + s]

								elif ((t == s) and (u != s) and (u != t)):

									L3[i*n_virt + s] += (-2 * g[k, n_occ + s, n_occ + s, n_occ + u] + 4 * g[k, n_occ + u, n_occ + s, n_occ + s] + 2 * g[i, k, i, n_occ + u] + -4 * g[i, i, k, n_occ + u] ) * K[0, i*n_virt + s + n_ex] * K[1, k*n_virt + u]

								elif ((t != s) and (u == s)):

									L3[i*n_virt + s] += (2 * g[k, n_occ + s, n_occ + s, n_occ + t] ) * K[0, i*n_virt + t + n_ex] * K[1, k*n_virt + s]

								elif ((t != s) and (u == t)):

									L3[i*n_virt + s] += (-4 * g[i, k, i, n_occ + s] + 2 * g[i, i, k, n_occ + s] + 4 * g[k, n_occ + t, n_occ + s, n_occ + t] + -2 * g[k, n_occ + s, n_occ + t, n_occ + t] ) * K[0, i*n_virt + t + n_ex] * K[1, k*n_virt + t]

								elif ((t != s) and (u != s) and (u != t)):

									L3[i*n_virt + s] += (-2 * g[k, n_occ + s, n_occ + t, n_occ + u] + 4 * g[k, n_occ + u, n_occ + s, n_occ + t] ) * K[0, i*n_virt + t + n_ex] * K[1, k*n_virt + u]

							elif ((j != i) and (k == i)):

								if ((t == s) and (u == s)):

									L3[i*n_virt + s] += (-4 * g[i, j, i, n_occ + s] ) * K[0, j*n_virt + s + n_ex] * K[1, i*n_virt + s]

								elif ((t == s) and (u != s) and (u != t)):

									L3[i*n_virt + s] += (-2 * g[i, j, i, n_occ + u] ) * K[0, j*n_virt + s + n_ex] * K[1, i*n_virt + u]

								elif ((t != s) and (u == t)):

									L3[i*n_virt + s] += (-2 * g[i, j, i, n_occ + s] ) * K[0, j*n_virt + t + n_ex] * K[1, i*n_virt + t]

							elif ((j != i) and (k == j)):

								if ((t == s) and (u == s)):

									L3[i*n_virt + s] += (-2 * g[i, j, j, n_occ + s] + 2 * g[i, n_occ + s, n_occ + s, n_occ + s] + -2 * g[i, n_occ + s, j, j] ) * K[0, j*n_virt + s + n_ex] * K[1, j*n_virt + s]

								elif ((t == s) and (u != s) and (u != t)):

									L3[i*n_virt + s] += (-4 * g[i, j, j, n_occ + u] + 2 * g[i, n_occ + u, j, j] + 4 * g[i, n_occ + s, n_occ + s, n_occ + u] + -2 * g[i, n_occ + u, n_occ + s, n_occ + s] ) * K[0, j*n_virt + s + n_ex] * K[1, j*n_virt + u]

								elif ((t != s) and (u == s)):

									L3[i*n_virt + s] += (2 * g[i, n_occ + s, n_occ + s, n_occ + t] ) * K[0, j*n_virt + t + n_ex] * K[1, j*n_virt + s]

								elif ((t != s) and (u == t)):

									L3[i*n_virt + s] += (-2 * g[i, n_occ + t, n_occ + s, n_occ + t] + 4 * g[i, n_occ + s, n_occ + t, n_occ + t] + 2 * g[i, j, j, n_occ + s] + -4 * g[i, n_occ + s, j, j] ) * K[0, j*n_virt + t + n_ex] * K[1, j*n_virt + t]

								elif ((t != s) and (u != s) and (u != t)):

									L3[i*n_virt + s] += (4 * g[i, n_occ + s, n_occ + t, n_occ + u] + -2 * g[i, n_occ + u, n_occ + s, n_occ + t] ) * K[0, j*n_virt + t + n_ex] * K[1, j*n_virt + u]

							elif ((j != i) and (k != i) and (k != j)):

								if ((t == s) and (u == s)):

									L3[i*n_virt + s] += (-2 * g[i, j, k, n_occ + s] + -2 * g[i, n_occ + s, j, k] ) * K[0, j*n_virt + s + n_ex] * K[1, k*n_virt + s]

								elif ((t == s) and (u != s) and (u != t)):

									L3[i*n_virt + s] += (-4 * g[i, j, k, n_occ + u] + 2 * g[i, n_occ + u, j, k] ) * K[0, j*n_virt + s + n_ex] * K[1, k*n_virt + u]

								elif ((t != s) and (u == t)):

									L3[i*n_virt + s] += (2 * g[i, j, k, n_occ + s] + -4 * g[i, n_occ + s, j, k] ) * K[0, j*n_virt + t + n_ex] * K[1, k*n_virt + t]

	# This operator combination: {'a': 1, 'b': 2, 'c': 2}
	for i in range(n_occ):
		for j in range(n_occ):
			for k in range(n_occ):
				for s in range(n_virt):
					for t in range(n_virt):
						for u in range(n_virt):

							if ((j == i) and (k == i)):

								if ((t == s) and (u == s)):

									L3[i*n_virt + s + n_ex] += (4 * F[i, n_occ + s] + -4 * g[i, n_occ + s, n_occ + s, n_occ + s] + 4 * g[i, i, i, n_occ + s] ) * K[0, i*n_virt + s + n_ex] * K[1, i*n_virt + s]

								elif ((t == s) and (u != s) and (u != t)):

									L3[i*n_virt + s + n_ex] += (-4 * g[i, n_occ + s, n_occ + s, n_occ + u] ) * K[0, i*n_virt + s + n_ex] * K[1, i*n_virt + u]

								elif ((t != s) and (u == s)):

									L3[i*n_virt + s + n_ex] += (2 * F[i, n_occ + t] + -2 * g[i, n_occ + t, n_occ + s, n_occ + s] + -2 * g[i, n_occ + s, n_occ + s, n_occ + t] + 2 * g[i, i, i, n_occ + t] ) * K[0, i*n_virt + t + n_ex] * K[1, i*n_virt + s]

								elif ((t != s) and (u == t)):

									L3[i*n_virt + s + n_ex] += (2 * F[i, n_occ + s] + -2 * g[i, n_occ + t, n_occ + s, n_occ + t] + -2 * g[i, n_occ + s, n_occ + t, n_occ + t] + 2 * g[i, i, i, n_occ + s] ) * K[0, i*n_virt + t + n_ex] * K[1, i*n_virt + t]

								elif ((t != s) and (u != s) and (u != t)):

									L3[i*n_virt + s + n_ex] += (-2 * g[i, n_occ + t, n_occ + s, n_occ + u] + -2 * g[i, n_occ + s, n_occ + t, n_occ + u] ) * K[0, i*n_virt + t + n_ex] * K[1, i*n_virt + u]

							elif ((j == i) and (k != i) and (k != j)):

								if ((t == s) and (u == s)):

									L3[i*n_virt + s + n_ex] += (4 * g[i, k, i, n_occ + s] ) * K[0, i*n_virt + s + n_ex] * K[1, k*n_virt + s]

								elif ((t != s) and (u == s)):

									L3[i*n_virt + s + n_ex] += (2 * g[i, k, i, n_occ + t] ) * K[0, i*n_virt + t + n_ex] * K[1, k*n_virt + s]

								elif ((t != s) and (u == t)):

									L3[i*n_virt + s + n_ex] += (2 * g[i, k, i, n_occ + s] ) * K[0, i*n_virt + t + n_ex] * K[1, k*n_virt + t]

							elif ((j != i) and (k == i)):

								if ((t == s) and (u == s)):

									L3[i*n_virt + s + n_ex] += (2 * F[j, n_occ + s] + -2 * g[j, n_occ + s, n_occ + s, n_occ + s] + 2 * g[i, i, j, n_occ + s] + 2 * g[i, j, i, n_occ + s] ) * K[0, j*n_virt + s + n_ex] * K[1, i*n_virt + s]

								elif ((t == s) and (u != s) and (u != t)):

									L3[i*n_virt + s + n_ex] += (-2 * g[j, n_occ + s, n_occ + s, n_occ + u] ) * K[0, j*n_virt + s + n_ex] * K[1, i*n_virt + u]

								elif ((t != s) and (u == s)):

									L3[i*n_virt + s + n_ex] += (2 * g[j, n_occ + s, n_occ + s, n_occ + t] + -4 * g[j, n_occ + t, n_occ + s, n_occ + s] + -2 * g[i, j, i, n_occ + t] + 4 * g[i, i, j, n_occ + t] ) * K[0, j*n_virt + t + n_ex] * K[1, i*n_virt + s]

								elif ((t != s) and (u == t)):

									L3[i*n_virt + s + n_ex] += (2 * F[j, n_occ + s] + -4 * g[j, n_occ + t, n_occ + s, n_occ + t] + 2 * g[j, n_occ + s, n_occ + t, n_occ + t] + -2 * g[i, i, j, n_occ + s] + 4 * g[i, j, i, n_occ + s] ) * K[0, j*n_virt + t + n_ex] * K[1, i*n_virt + t]

								elif ((t != s) and (u != s) and (u != t)):

									L3[i*n_virt + s + n_ex] += (2 * g[j, n_occ + s, n_occ + t, n_occ + u] + -4 * g[j, n_occ + t, n_occ + s, n_occ + u] ) * K[0, j*n_virt + t + n_ex] * K[1, i*n_virt + u]

							elif ((j != i) and (k == j)):

								if ((t == s) and (u == s)):

									L3[i*n_virt + s + n_ex] += (2 * F[i, n_occ + s] + -2 * g[i, n_occ + s, n_occ + s, n_occ + s] + 2 * g[i, n_occ + s, j, j] + 2 * g[i, j, j, n_occ + s] ) * K[0, j*n_virt + s + n_ex] * K[1, j*n_virt + s]

								elif ((t == s) and (u != s) and (u != t)):

									L3[i*n_virt + s + n_ex] += (-2 * g[i, n_occ + s, n_occ + s, n_occ + u] ) * K[0, j*n_virt + s + n_ex] * K[1, j*n_virt + u]

								elif ((t != s) and (u == s)):

									L3[i*n_virt + s + n_ex] += (2 * F[i, n_occ + t] + -4 * g[i, n_occ + s, n_occ + s, n_occ + t] + 2 * g[i, n_occ + t, n_occ + s, n_occ + s] + -2 * g[i, n_occ + t, j, j] + 4 * g[i, j, j, n_occ + t] ) * K[0, j*n_virt + t + n_ex] * K[1, j*n_virt + s]

								elif ((t != s) and (u == t)):

									L3[i*n_virt + s + n_ex] += (2 * g[i, n_occ + t, n_occ + s, n_occ + t] + -4 * g[i, n_occ + s, n_occ + t, n_occ + t] + -2 * g[i, j, j, n_occ + s] + 4 * g[i, n_occ + s, j, j] ) * K[0, j*n_virt + t + n_ex] * K[1, j*n_virt + t]

								elif ((t != s) and (u != s) and (u != t)):

									L3[i*n_virt + s + n_ex] += (-4 * g[i, n_occ + s, n_occ + t, n_occ + u] + 2 * g[i, n_occ + t, n_occ + s, n_occ + u] ) * K[0, j*n_virt + t + n_ex] * K[1, j*n_virt + u]

							elif ((j != i) and (k != i) and (k != j)):

								if ((t == s) and (u == s)):

									L3[i*n_virt + s + n_ex] += (2 * g[i, k, j, n_occ + s] + 2 * g[i, n_occ + s, j, k] ) * K[0, j*n_virt + s + n_ex] * K[1, k*n_virt + s]

								elif ((t != s) and (u == s)):

									L3[i*n_virt + s + n_ex] += (4 * g[i, k, j, n_occ + t] + -2 * g[i, n_occ + t, j, k] ) * K[0, j*n_virt + t + n_ex] * K[1, k*n_virt + s]

								elif ((t != s) and (u == t)):

									L3[i*n_virt + s + n_ex] += (-2 * g[i, k, j, n_occ + s] + 4 * g[i, n_occ + s, j, k] ) * K[0, j*n_virt + t + n_ex] * K[1, k*n_virt + t]

	# This operator combination: {'a': 1, 'b': 2, 'c': 3}
	# All terms vanished for this combination

	# This operator combination: {'a': 1, 'b': 3, 'c': 1}
	for i in range(n_occ):
		for k in range(n_occ):
			for j in range(n_occ):
				for m in range(n_occ):
					for s in range(n_virt):
						for u in range(n_virt):
							for t in range(n_virt):
								for v in range(n_virt):

									if ((k == i) and (j == i) and (m == i)):

										if ((u == s) and (t == s) and (v != s) and (v != t) and (v != u)):

											L3[i*n_virt + s] += (-4 * g[i, n_occ + s, i, n_occ + v] ) * K[0, (i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] * K[1, i*n_virt + v]

										elif ((u != s) and (u != t) and (t == s) and (v == u)):

											L3[i*n_virt + s] += (-4 * g[i, n_occ + u, i, n_occ + u] ) * K[0, (i*n_virt + u) * n_ex + i*n_virt + s+ 2*n_ex] * K[1, i*n_virt + u]

										elif ((u != s) and (u != t) and (t == s) and (v != s) and (v != t) and (v != u)):

											L3[i*n_virt + s] += (-4 * g[i, n_occ + u, i, n_occ + v] ) * K[0, (i*n_virt + u) * n_ex + i*n_virt + s+ 2*n_ex] * K[1, i*n_virt + v]

										elif ((u == s) and (t != s) and (v == t)):

											L3[i*n_virt + s] += (4 * g[i, n_occ + s, i, n_occ + s] ) * K[0, (i*n_virt + s) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, i*n_virt + t]

										elif ((u == t) and (t != s) and (v == t)):

											L3[i*n_virt + s] += (4 * g[i, n_occ + s, i, n_occ + t] ) * K[0, (i*n_virt + t) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, i*n_virt + t]

										elif ((u != s) and (u != t) and (t != s) and (v == t)):

											L3[i*n_virt + s] += (4 * g[i, n_occ + s, i, n_occ + u] ) * K[0, (i*n_virt + u) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, i*n_virt + t]

									elif ((k == i) and (j == i) and (m != i) and (m != j) and (m != k)):

										if ((u == s) and (t == s) and (v == s)):

											L3[i*n_virt + s] += (-4 * g[i, n_occ + s, m, n_occ + s] ) * K[0, (i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] * K[1, m*n_virt + s]

										elif ((u == s) and (t == s) and (v != s) and (v != t) and (v != u)):

											L3[i*n_virt + s] += (-8 * g[i, n_occ + s, m, n_occ + v] + 4 * g[i, n_occ + v, m, n_occ + s] ) * K[0, (i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] * K[1, m*n_virt + v]

										elif ((u != s) and (u != t) and (t == s) and (v == s)):

											L3[i*n_virt + s] += (4 * g[i, n_occ + s, m, n_occ + u] + -8 * g[i, n_occ + u, m, n_occ + s] ) * K[0, (i*n_virt + u) * n_ex + i*n_virt + s+ 2*n_ex] * K[1, m*n_virt + s]

										elif ((u != s) and (u != t) and (t == s) and (v == u)):

											L3[i*n_virt + s] += (-4 * g[i, n_occ + u, m, n_occ + u] ) * K[0, (i*n_virt + u) * n_ex + i*n_virt + s+ 2*n_ex] * K[1, m*n_virt + u]

										elif ((u != s) and (u != t) and (t == s) and (v != s) and (v != t) and (v != u)):

											L3[i*n_virt + s] += (-8 * g[i, n_occ + u, m, n_occ + v] + 4 * g[i, n_occ + v, m, n_occ + u] ) * K[0, (i*n_virt + u) * n_ex + i*n_virt + s+ 2*n_ex] * K[1, m*n_virt + v]

									elif ((k != i) and (k != j) and (j == i) and (m == i)):

										if ((u == s) and (t == s) and (v != s) and (v != t) and (v != u)):

											L3[i*n_virt + s] += (4 * g[i, n_occ + s, k, n_occ + v] + -8 * g[i, n_occ + v, k, n_occ + s] ) * K[0, (k*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] * K[1, i*n_virt + v]

										elif ((u != s) and (u != t) and (t == s) and (v == u)):

											L3[i*n_virt + s] += (-4 * g[i, n_occ + u, k, n_occ + u] ) * K[0, (k*n_virt + u) * n_ex + i*n_virt + s+ 2*n_ex] * K[1, i*n_virt + u]

										elif ((u != s) and (u != t) and (t == s) and (v != s) and (v != t) and (v != u)):

											L3[i*n_virt + s] += (4 * g[i, n_occ + u, k, n_occ + v] + -8 * g[i, n_occ + v, k, n_occ + u] ) * K[0, (k*n_virt + u) * n_ex + i*n_virt + s+ 2*n_ex] * K[1, i*n_virt + v]

										elif ((u == s) and (t != s) and (v == t)):

											L3[i*n_virt + s] += (4 * g[i, n_occ + s, k, n_occ + s] ) * K[0, (k*n_virt + s) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, i*n_virt + t]

										elif ((u == t) and (t != s) and (v == t)):

											L3[i*n_virt + s] += (8 * g[i, n_occ + s, k, n_occ + t] + -4 * g[i, n_occ + t, k, n_occ + s] ) * K[0, (k*n_virt + t) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, i*n_virt + t]

										elif ((u != s) and (u != t) and (t != s) and (v == t)):

											L3[i*n_virt + s] += (8 * g[i, n_occ + s, k, n_occ + u] + -4 * g[i, n_occ + u, k, n_occ + s] ) * K[0, (k*n_virt + u) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, i*n_virt + t]

									elif ((k != i) and (k != j) and (j == i) and (m == k)):

										if ((u == s) and (t == s) and (v == s)):

											L3[i*n_virt + s] += (-4 * g[k, n_occ + s, k, n_occ + s] ) * K[0, (k*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] * K[1, k*n_virt + s]

										elif ((u == s) and (t == s) and (v != s) and (v != t) and (v != u)):

											L3[i*n_virt + s] += (-4 * g[k, n_occ + s, k, n_occ + v] ) * K[0, (k*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] * K[1, k*n_virt + v]

										elif ((u != s) and (u != t) and (t == s) and (v == s)):

											L3[i*n_virt + s] += (-4 * g[k, n_occ + s, k, n_occ + u] ) * K[0, (k*n_virt + u) * n_ex + i*n_virt + s+ 2*n_ex] * K[1, k*n_virt + s]

										elif ((u != s) and (u != t) and (t == s) and (v == u)):

											L3[i*n_virt + s] += (-4 * g[k, n_occ + u, k, n_occ + u] ) * K[0, (k*n_virt + u) * n_ex + i*n_virt + s+ 2*n_ex] * K[1, k*n_virt + u]

										elif ((u != s) and (u != t) and (t == s) and (v != s) and (v != t) and (v != u)):

											L3[i*n_virt + s] += (-4 * g[k, n_occ + u, k, n_occ + v] ) * K[0, (k*n_virt + u) * n_ex + i*n_virt + s+ 2*n_ex] * K[1, k*n_virt + v]

									elif ((k != i) and (k != j) and (j == i) and (m != i) and (m != j) and (m != k)):

										if ((u == s) and (t == s) and (v == s)):

											L3[i*n_virt + s] += (-4 * g[k, n_occ + s, m, n_occ + s] ) * K[0, (k*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] * K[1, m*n_virt + s]

										elif ((u == s) and (t == s) and (v != s) and (v != t) and (v != u)):

											L3[i*n_virt + s] += (-8 * g[k, n_occ + s, m, n_occ + v] + 4 * g[k, n_occ + v, m, n_occ + s] ) * K[0, (k*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] * K[1, m*n_virt + v]

										elif ((u != s) and (u != t) and (t == s) and (v == s)):

											L3[i*n_virt + s] += (4 * g[k, n_occ + s, m, n_occ + u] + -8 * g[k, n_occ + u, m, n_occ + s] ) * K[0, (k*n_virt + u) * n_ex + i*n_virt + s+ 2*n_ex] * K[1, m*n_virt + s]

										elif ((u != s) and (u != t) and (t == s) and (v == u)):

											L3[i*n_virt + s] += (-4 * g[k, n_occ + u, m, n_occ + u] ) * K[0, (k*n_virt + u) * n_ex + i*n_virt + s+ 2*n_ex] * K[1, m*n_virt + u]

										elif ((u != s) and (u != t) and (t == s) and (v != s) and (v != t) and (v != u)):

											L3[i*n_virt + s] += (-8 * g[k, n_occ + u, m, n_occ + v] + 4 * g[k, n_occ + v, m, n_occ + u] ) * K[0, (k*n_virt + u) * n_ex + i*n_virt + s+ 2*n_ex] * K[1, m*n_virt + v]

									elif ((k == i) and (j != i) and (m == j)):

										if ((u == s) and (t == s) and (v == s)):

											L3[i*n_virt + s] += (4 * g[i, n_occ + s, i, n_occ + s] ) * K[0, (i*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, j*n_virt + s]

										elif ((u != s) and (u != t) and (t == s) and (v == s)):

											L3[i*n_virt + s] += (4 * g[i, n_occ + s, i, n_occ + u] ) * K[0, (i*n_virt + u) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, j*n_virt + s]

										elif ((u == s) and (t != s) and (v == t)):

											L3[i*n_virt + s] += (4 * g[i, n_occ + s, i, n_occ + s] ) * K[0, (i*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, j*n_virt + t]

										elif ((u == t) and (t != s) and (v == t)):

											L3[i*n_virt + s] += (4 * g[i, n_occ + s, i, n_occ + t] ) * K[0, (i*n_virt + t) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, j*n_virt + t]

										elif ((u != s) and (u != t) and (t != s) and (v == t)):

											L3[i*n_virt + s] += (4 * g[i, n_occ + s, i, n_occ + u] ) * K[0, (i*n_virt + u) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, j*n_virt + t]

									elif ((k == j) and (j != i) and (m == j)):

										if ((u == s) and (t == s) and (v == s)):

											L3[i*n_virt + s] += (4 * g[i, n_occ + s, j, n_occ + s] ) * K[0, (j*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, j*n_virt + s]

										elif ((u != s) and (u != t) and (t == s) and (v == s)):

											L3[i*n_virt + s] += (8 * g[i, n_occ + s, j, n_occ + u] + -4 * g[i, n_occ + u, j, n_occ + s] ) * K[0, (j*n_virt + u) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, j*n_virt + s]

										elif ((u == s) and (t != s) and (v == t)):

											L3[i*n_virt + s] += (4 * g[i, n_occ + s, j, n_occ + s] ) * K[0, (j*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, j*n_virt + t]

										elif ((u == t) and (t != s) and (v == t)):

											L3[i*n_virt + s] += (8 * g[i, n_occ + s, j, n_occ + t] + -4 * g[i, n_occ + t, j, n_occ + s] ) * K[0, (j*n_virt + t) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, j*n_virt + t]

										elif ((u != s) and (u != t) and (t != s) and (v == t)):

											L3[i*n_virt + s] += (8 * g[i, n_occ + s, j, n_occ + u] + -4 * g[i, n_occ + u, j, n_occ + s] ) * K[0, (j*n_virt + u) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, j*n_virt + t]

									elif ((k != i) and (k != j) and (j != i) and (m == j)):

										if ((u == s) and (t == s) and (v == s)):

											L3[i*n_virt + s] += (4 * g[i, n_occ + s, k, n_occ + s] ) * K[0, (k*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, j*n_virt + s]

										elif ((u != s) and (u != t) and (t == s) and (v == s)):

											L3[i*n_virt + s] += (8 * g[i, n_occ + s, k, n_occ + u] + -4 * g[i, n_occ + u, k, n_occ + s] ) * K[0, (k*n_virt + u) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, j*n_virt + s]

										elif ((u == s) and (t != s) and (v == t)):

											L3[i*n_virt + s] += (4 * g[i, n_occ + s, k, n_occ + s] ) * K[0, (k*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, j*n_virt + t]

										elif ((u == t) and (t != s) and (v == t)):

											L3[i*n_virt + s] += (8 * g[i, n_occ + s, k, n_occ + t] + -4 * g[i, n_occ + t, k, n_occ + s] ) * K[0, (k*n_virt + t) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, j*n_virt + t]

										elif ((u != s) and (u != t) and (t != s) and (v == t)):

											L3[i*n_virt + s] += (8 * g[i, n_occ + s, k, n_occ + u] + -4 * g[i, n_occ + u, k, n_occ + s] ) * K[0, (k*n_virt + u) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, j*n_virt + t]

	# This operator combination: {'a': 1, 'b': 3, 'c': 2}
	for i in range(n_occ):
		for k in range(n_occ):
			for j in range(n_occ):
				for m in range(n_occ):
					for s in range(n_virt):
						for u in range(n_virt):
							for t in range(n_virt):
								for v in range(n_virt):

									if ((k == i) and (j == i) and (m == i)):

										if ((u == s) and (t == s) and (v != s) and (v != t) and (v != u)):

											L3[i*n_virt + s + n_ex] += (4 * F[n_occ + s, n_occ + v] + -4 * g[i, i, n_occ + s, n_occ + v] + 8 * g[i, n_occ + s, i, n_occ + v] ) * K[0, (i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] * K[1, i*n_virt + v]

										elif ((u != s) and (u != t) and (t == s) and (v == s)):

											L3[i*n_virt + s + n_ex] += (-4 * F[n_occ + s, n_occ + u] + 4 * g[i, i, n_occ + s, n_occ + u] + -8 * g[i, n_occ + s, i, n_occ + u] ) * K[0, (i*n_virt + u) * n_ex + i*n_virt + s+ 2*n_ex] * K[1, i*n_virt + s]

										elif ((u == s) and (t != s) and (v == s)):

											L3[i*n_virt + s + n_ex] += (4 * F[n_occ + s, n_occ + t] + -4 * g[i, i, n_occ + s, n_occ + t] + 8 * g[i, n_occ + s, i, n_occ + t] ) * K[0, (i*n_virt + s) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, i*n_virt + s]

										elif ((u == s) and (t != s) and (v == t)):

											L3[i*n_virt + s + n_ex] += (4 * F[n_occ + t, n_occ + t] + -4 * F[n_occ + s, n_occ + s] + 4 * g[i, i, n_occ + s, n_occ + s] + -4 * g[i, i, n_occ + t, n_occ + t] + 8 * g[i, n_occ + t, i, n_occ + t] + -8 * g[i, n_occ + s, i, n_occ + s] ) * K[0, (i*n_virt + s) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, i*n_virt + t]

										elif ((u == s) and (t != s) and (v != s) and (v != t) and (v != u)):

											L3[i*n_virt + s + n_ex] += (4 * F[n_occ + t, n_occ + v] + -4 * g[i, i, n_occ + t, n_occ + v] + 8 * g[i, n_occ + t, i, n_occ + v] ) * K[0, (i*n_virt + s) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, i*n_virt + v]

										elif ((u == t) and (t != s) and (v == t)):

											L3[i*n_virt + s + n_ex] += (-4 * F[n_occ + s, n_occ + t] + 4 * g[i, i, n_occ + s, n_occ + t] + -8 * g[i, n_occ + s, i, n_occ + t] ) * K[0, (i*n_virt + t) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, i*n_virt + t]

										elif ((u != s) and (u != t) and (t != s) and (v == t)):

											L3[i*n_virt + s + n_ex] += (-4 * F[n_occ + s, n_occ + u] + 4 * g[i, i, n_occ + s, n_occ + u] + -8 * g[i, n_occ + s, i, n_occ + u] ) * K[0, (i*n_virt + u) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, i*n_virt + t]

									elif ((k == i) and (j == i) and (m != i) and (m != j) and (m != k)):

										if ((u == s) and (t == s) and (v == s)):

											L3[i*n_virt + s + n_ex] += (-4 * F[i, m] + 8 * g[i, n_occ + s, m, n_occ + s] + -4 * g[i, m, n_occ + s, n_occ + s] ) * K[0, (i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] * K[1, m*n_virt + s]

										elif ((u == s) and (t == s) and (v != s) and (v != t) and (v != u)):

											L3[i*n_virt + s + n_ex] += (-4 * g[i, m, n_occ + s, n_occ + v] + 8 * g[i, n_occ + s, m, n_occ + v] ) * K[0, (i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] * K[1, m*n_virt + v]

										elif ((u == s) and (t != s) and (v == s)):

											L3[i*n_virt + s + n_ex] += (-4 * g[i, m, n_occ + s, n_occ + t] + 8 * g[i, n_occ + t, m, n_occ + s] ) * K[0, (i*n_virt + s) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, m*n_virt + s]

										elif ((u == s) and (t != s) and (v == t)):

											L3[i*n_virt + s + n_ex] += (-4 * F[i, m] + 8 * g[i, n_occ + t, m, n_occ + t] + -4 * g[i, m, n_occ + t, n_occ + t] ) * K[0, (i*n_virt + s) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, m*n_virt + t]

										elif ((u == s) and (t != s) and (v != s) and (v != t) and (v != u)):

											L3[i*n_virt + s + n_ex] += (-4 * g[i, m, n_occ + t, n_occ + v] + 8 * g[i, n_occ + t, m, n_occ + v] ) * K[0, (i*n_virt + s) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, m*n_virt + v]

									elif ((k != i) and (k != j) and (j == i) and (m == i)):

										if ((u == s) and (t == s) and (v == s)):

											L3[i*n_virt + s + n_ex] += (4 * F[i, k] + -8 * g[i, n_occ + s, k, n_occ + s] + 4 * g[i, k, n_occ + s, n_occ + s] ) * K[0, (k*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] * K[1, i*n_virt + s]

										elif ((u != s) and (u != t) and (t == s) and (v == s)):

											L3[i*n_virt + s + n_ex] += (4 * g[i, k, n_occ + s, n_occ + u] + -8 * g[i, n_occ + s, k, n_occ + u] ) * K[0, (k*n_virt + u) * n_ex + i*n_virt + s+ 2*n_ex] * K[1, i*n_virt + s]

										elif ((u == s) and (t != s) and (v == t)):

											L3[i*n_virt + s + n_ex] += (4 * F[i, k] + -8 * g[i, n_occ + s, k, n_occ + s] + 4 * g[i, k, n_occ + s, n_occ + s] ) * K[0, (k*n_virt + s) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, i*n_virt + t]

										elif ((u == t) and (t != s) and (v == t)):

											L3[i*n_virt + s + n_ex] += (4 * g[i, k, n_occ + s, n_occ + t] + -8 * g[i, n_occ + s, k, n_occ + t] ) * K[0, (k*n_virt + t) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, i*n_virt + t]

										elif ((u != s) and (u != t) and (t != s) and (v == t)):

											L3[i*n_virt + s + n_ex] += (4 * g[i, k, n_occ + s, n_occ + u] + -8 * g[i, n_occ + s, k, n_occ + u] ) * K[0, (k*n_virt + u) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, i*n_virt + t]

									elif ((k == i) and (j != i) and (m == i)):

										if ((u == s) and (t == s) and (v == s)):

											L3[i*n_virt + s + n_ex] += (-4 * F[i, j] + 8 * g[i, n_occ + s, j, n_occ + s] + -4 * g[i, j, n_occ + s, n_occ + s] ) * K[0, (i*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, i*n_virt + s]

										elif ((u == s) and (t == s) and (v != s) and (v != t) and (v != u)):

											L3[i*n_virt + s + n_ex] += (-4 * g[i, j, n_occ + s, n_occ + v] + 8 * g[i, n_occ + v, j, n_occ + s] ) * K[0, (i*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, i*n_virt + v]

										elif ((u == s) and (t != s) and (v == s)):

											L3[i*n_virt + s + n_ex] += (-4 * g[i, j, n_occ + s, n_occ + t] + 8 * g[i, n_occ + s, j, n_occ + t] ) * K[0, (i*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, i*n_virt + s]

										elif ((u == s) and (t != s) and (v == t)):

											L3[i*n_virt + s + n_ex] += (-4 * F[i, j] + 8 * g[i, n_occ + t, j, n_occ + t] + -4 * g[i, j, n_occ + t, n_occ + t] ) * K[0, (i*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, i*n_virt + t]

										elif ((u == s) and (t != s) and (v != s) and (v != t) and (v != u)):

											L3[i*n_virt + s + n_ex] += (-4 * g[i, j, n_occ + t, n_occ + v] + 8 * g[i, n_occ + v, j, n_occ + t] ) * K[0, (i*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, i*n_virt + v]

									elif ((k == i) and (j != i) and (m == j)):

										if ((u == s) and (t == s) and (v == s)):

											L3[i*n_virt + s + n_ex] += (4 * F[i, i] + -4 * F[j, j] + -4 * g[j, j, n_occ + s, n_occ + s] + -8 * g[i, n_occ + s, i, n_occ + s] + 8 * g[j, n_occ + s, j, n_occ + s] + 4 * g[i, i, n_occ + s, n_occ + s] ) * K[0, (i*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, j*n_virt + s]

										elif ((u == s) and (t == s) and (v != s) and (v != t) and (v != u)):

											L3[i*n_virt + s + n_ex] += (4 * F[n_occ + s, n_occ + v] + -4 * g[j, j, n_occ + s, n_occ + v] + 8 * g[j, n_occ + s, j, n_occ + v] ) * K[0, (i*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, j*n_virt + v]

										elif ((u != s) and (u != t) and (t == s) and (v == s)):

											L3[i*n_virt + s + n_ex] += (-4 * F[n_occ + s, n_occ + u] + 4 * g[i, i, n_occ + s, n_occ + u] + -8 * g[i, n_occ + s, i, n_occ + u] ) * K[0, (i*n_virt + u) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, j*n_virt + s]

										elif ((u == s) and (t != s) and (v == s)):

											L3[i*n_virt + s + n_ex] += (4 * F[n_occ + s, n_occ + t] + -4 * g[j, j, n_occ + s, n_occ + t] + 8 * g[j, n_occ + s, j, n_occ + t] ) * K[0, (i*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, j*n_virt + s]

										elif ((u == s) and (t != s) and (v == t)):

											L3[i*n_virt + s + n_ex] += (4 * F[i, i] + 4 * F[n_occ + t, n_occ + t] + -4 * F[n_occ + s, n_occ + s] + -4 * F[j, j] + 4 * g[i, i, n_occ + s, n_occ + s] + -4 * g[j, j, n_occ + t, n_occ + t] + 8 * g[j, n_occ + t, j, n_occ + t] + -8 * g[i, n_occ + s, i, n_occ + s] ) * K[0, (i*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, j*n_virt + t]

										elif ((u == s) and (t != s) and (v != s) and (v != t) and (v != u)):

											L3[i*n_virt + s + n_ex] += (4 * F[n_occ + t, n_occ + v] + -4 * g[j, j, n_occ + t, n_occ + v] + 8 * g[j, n_occ + t, j, n_occ + v] ) * K[0, (i*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, j*n_virt + v]

										elif ((u == t) and (t != s) and (v == t)):

											L3[i*n_virt + s + n_ex] += (-4 * F[n_occ + s, n_occ + t] + 4 * g[i, i, n_occ + s, n_occ + t] + -8 * g[i, n_occ + s, i, n_occ + t] ) * K[0, (i*n_virt + t) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, j*n_virt + t]

										elif ((u != s) and (u != t) and (t != s) and (v == t)):

											L3[i*n_virt + s + n_ex] += (-4 * F[n_occ + s, n_occ + u] + 4 * g[i, i, n_occ + s, n_occ + u] + -8 * g[i, n_occ + s, i, n_occ + u] ) * K[0, (i*n_virt + u) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, j*n_virt + t]

									elif ((k == i) and (j != i) and (m != i) and (m != j) and (m != k)):

										if ((u == s) and (t == s) and (v == s)):

											L3[i*n_virt + s + n_ex] += (-4 * F[j, m] + 8 * g[j, n_occ + s, m, n_occ + s] + -4 * g[j, m, n_occ + s, n_occ + s] ) * K[0, (i*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, m*n_virt + s]

										elif ((u == s) and (t == s) and (v != s) and (v != t) and (v != u)):

											L3[i*n_virt + s + n_ex] += (-4 * g[j, m, n_occ + s, n_occ + v] + 8 * g[j, n_occ + s, m, n_occ + v] ) * K[0, (i*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, m*n_virt + v]

										elif ((u == s) and (t != s) and (v == s)):

											L3[i*n_virt + s + n_ex] += (-4 * g[j, m, n_occ + s, n_occ + t] + 8 * g[j, n_occ + t, m, n_occ + s] ) * K[0, (i*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, m*n_virt + s]

										elif ((u == s) and (t != s) and (v == t)):

											L3[i*n_virt + s + n_ex] += (-4 * F[j, m] + 8 * g[j, n_occ + t, m, n_occ + t] + -4 * g[j, m, n_occ + t, n_occ + t] ) * K[0, (i*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, m*n_virt + t]

										elif ((u == s) and (t != s) and (v != s) and (v != t) and (v != u)):

											L3[i*n_virt + s + n_ex] += (-4 * g[j, m, n_occ + t, n_occ + v] + 8 * g[j, n_occ + t, m, n_occ + v] ) * K[0, (i*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, m*n_virt + v]

									elif ((k == j) and (j != i) and (m == j)):

										if ((u == s) and (t == s) and (v == s)):

											L3[i*n_virt + s + n_ex] += (4 * F[i, j] + -8 * g[i, n_occ + s, j, n_occ + s] + 4 * g[i, j, n_occ + s, n_occ + s] ) * K[0, (j*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, j*n_virt + s]

										elif ((u != s) and (u != t) and (t == s) and (v == s)):

											L3[i*n_virt + s + n_ex] += (4 * g[i, j, n_occ + s, n_occ + u] + -8 * g[i, n_occ + s, j, n_occ + u] ) * K[0, (j*n_virt + u) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, j*n_virt + s]

										elif ((u == s) and (t != s) and (v == t)):

											L3[i*n_virt + s + n_ex] += (4 * F[i, j] + -8 * g[i, n_occ + s, j, n_occ + s] + 4 * g[i, j, n_occ + s, n_occ + s] ) * K[0, (j*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, j*n_virt + t]

										elif ((u == t) and (t != s) and (v == t)):

											L3[i*n_virt + s + n_ex] += (4 * g[i, j, n_occ + s, n_occ + t] + -8 * g[i, n_occ + s, j, n_occ + t] ) * K[0, (j*n_virt + t) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, j*n_virt + t]

										elif ((u != s) and (u != t) and (t != s) and (v == t)):

											L3[i*n_virt + s + n_ex] += (4 * g[i, j, n_occ + s, n_occ + u] + -8 * g[i, n_occ + s, j, n_occ + u] ) * K[0, (j*n_virt + u) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, j*n_virt + t]

									elif ((k != i) and (k != j) and (j != i) and (m == j)):

										if ((u == s) and (t == s) and (v == s)):

											L3[i*n_virt + s + n_ex] += (4 * F[i, k] + -8 * g[i, n_occ + s, k, n_occ + s] + 4 * g[i, k, n_occ + s, n_occ + s] ) * K[0, (k*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, j*n_virt + s]

										elif ((u != s) and (u != t) and (t == s) and (v == s)):

											L3[i*n_virt + s + n_ex] += (4 * g[i, k, n_occ + s, n_occ + u] + -8 * g[i, n_occ + s, k, n_occ + u] ) * K[0, (k*n_virt + u) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, j*n_virt + s]

										elif ((u == s) and (t != s) and (v == t)):

											L3[i*n_virt + s + n_ex] += (4 * F[i, k] + -8 * g[i, n_occ + s, k, n_occ + s] + 4 * g[i, k, n_occ + s, n_occ + s] ) * K[0, (k*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, j*n_virt + t]

										elif ((u == t) and (t != s) and (v == t)):

											L3[i*n_virt + s + n_ex] += (4 * g[i, k, n_occ + s, n_occ + t] + -8 * g[i, n_occ + s, k, n_occ + t] ) * K[0, (k*n_virt + t) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, j*n_virt + t]

										elif ((u != s) and (u != t) and (t != s) and (v == t)):

											L3[i*n_virt + s + n_ex] += (4 * g[i, k, n_occ + s, n_occ + u] + -8 * g[i, n_occ + s, k, n_occ + u] ) * K[0, (k*n_virt + u) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, j*n_virt + t]

	# This operator combination: {'a': 1, 'b': 3, 'c': 3}
	for j in range(n_occ):
		for i in range(n_occ):
			for m in range(n_occ):
				for k in range(n_occ):
					for n in range(n_occ):
						for t in range(n_virt):
							for s in range(n_virt):
								for v in range(n_virt):
									for u in range(n_virt):
										for w in range(n_virt):

											if ((j == i) and (m == i) and (k == i) and (n == i)):

												if ((t == s) and (v == s) and (u == s) and (w == s)):

													L3[(i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (8 * F[i, n_occ + s] ) * K[0, (i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] * K[1, i*n_virt + s]

												elif ((t == s) and (v == s) and (u == s) and (w != s) and (w != t) and (w != u) and (w != v)):

													L3[(i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * F[i, n_occ + w] ) * K[0, (i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] * K[1, i*n_virt + w]

												elif ((t == s) and (v != s) and (v != t) and (v != u) and (u == s) and (w == s)):

													L3[(i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * F[i, n_occ + v] + -4 * g[i, n_occ + v, n_occ + s, n_occ + s] + -4 * g[i, n_occ + s, n_occ + s, n_occ + v] + 4 * g[i, i, i, n_occ + v] ) * K[0, (i*n_virt + v) * n_ex + i*n_virt + s+ 2*n_ex] * K[1, i*n_virt + s]

												elif ((t == s) and (v != s) and (v != t) and (v != u) and (u == s) and (w == v)):

													L3[(i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-8 * g[i, n_occ + v, n_occ + s, n_occ + v] ) * K[0, (i*n_virt + v) * n_ex + i*n_virt + s+ 2*n_ex] * K[1, i*n_virt + v]

												elif ((t == s) and (v != s) and (v != t) and (v != u) and (u == s) and (w != s) and (w != t) and (w != u) and (w != v)):

													L3[(i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, n_occ + v, n_occ + s, n_occ + w] + -4 * g[i, n_occ + w, n_occ + s, n_occ + v] ) * K[0, (i*n_virt + v) * n_ex + i*n_virt + s+ 2*n_ex] * K[1, i*n_virt + w]

												elif ((t == s) and (v == s) and (u != s) and (u != t) and (w == s)):

													L3[(i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (8 * g[i, n_occ + s, n_occ + s, n_occ + u] ) * K[0, (i*n_virt + s) * n_ex + i*n_virt + u+ 2*n_ex] * K[1, i*n_virt + s]

												elif ((t == s) and (v == s) and (u != s) and (u != t) and (w == u)):

													L3[(i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, i, i, n_occ + s] + 4 * g[i, n_occ + u, n_occ + s, n_occ + u] + 4 * g[i, n_occ + s, n_occ + u, n_occ + u] ) * K[0, (i*n_virt + s) * n_ex + i*n_virt + u+ 2*n_ex] * K[1, i*n_virt + u]

												elif ((t == s) and (v == s) and (u != s) and (u != t) and (w != s) and (w != t) and (w != u) and (w != v)):

													L3[(i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, n_occ + w, n_occ + s, n_occ + u] + 4 * g[i, n_occ + s, n_occ + u, n_occ + w] ) * K[0, (i*n_virt + s) * n_ex + i*n_virt + u+ 2*n_ex] * K[1, i*n_virt + w]

												elif ((t != s) and (v == s) and (u == s) and (w == s)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, i, i, n_occ + t] + 4 * g[i, n_occ + s, n_occ + s, n_occ + t] + 4 * g[i, n_occ + t, n_occ + s, n_occ + s] ) * K[0, (i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] * K[1, i*n_virt + s]

												elif ((t != s) and (v == s) and (u == s) and (w == t)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (8 * g[i, n_occ + t, n_occ + s, n_occ + t] ) * K[0, (i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] * K[1, i*n_virt + t]

												elif ((t != s) and (v == s) and (u == s) and (w != s) and (w != t) and (w != u) and (w != v)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, n_occ + w, n_occ + s, n_occ + t] + 4 * g[i, n_occ + t, n_occ + s, n_occ + w] ) * K[0, (i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] * K[1, i*n_virt + w]

												elif ((t != s) and (v == s) and (u == t) and (w == s)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (8 * F[i, n_occ + s] + 4 * g[i, i, i, n_occ + s] + 4 * g[i, n_occ + s, n_occ + t, n_occ + t] + 4 * g[i, n_occ + t, n_occ + s, n_occ + t] + -8 * g[i, n_occ + s, n_occ + s, n_occ + s] ) * K[0, (i*n_virt + s) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, i*n_virt + s]

												elif ((t != s) and (v == s) and (u == t) and (w == t)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * F[i, n_occ + t] + 8 * g[i, n_occ + t, n_occ + t, n_occ + t] + -4 * g[i, n_occ + s, n_occ + s, n_occ + t] + -4 * g[i, n_occ + t, n_occ + s, n_occ + s] + -4 * g[i, i, i, n_occ + t] ) * K[0, (i*n_virt + s) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, i*n_virt + t]

												elif ((t != s) and (v == s) and (u == t) and (w != s) and (w != t) and (w != u) and (w != v)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * F[i, n_occ + w] + 4 * g[i, n_occ + w, n_occ + t, n_occ + t] + 4 * g[i, n_occ + t, n_occ + t, n_occ + w] + -4 * g[i, n_occ + s, n_occ + s, n_occ + w] + -4 * g[i, n_occ + w, n_occ + s, n_occ + s] ) * K[0, (i*n_virt + s) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, i*n_virt + w]

												elif ((t != s) and (v == t) and (u == t) and (w == s)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * F[i, n_occ + t] + -4 * g[i, n_occ + t, n_occ + s, n_occ + s] + -4 * g[i, n_occ + s, n_occ + s, n_occ + t] + 4 * g[i, i, i, n_occ + t] ) * K[0, (i*n_virt + t) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, i*n_virt + s]

												elif ((t != s) and (v == t) and (u == t) and (w == t)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-8 * g[i, n_occ + t, n_occ + s, n_occ + t] ) * K[0, (i*n_virt + t) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, i*n_virt + t]

												elif ((t != s) and (v == t) and (u == t) and (w != s) and (w != t) and (w != u) and (w != v)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, n_occ + t, n_occ + s, n_occ + w] + -4 * g[i, n_occ + w, n_occ + s, n_occ + t] ) * K[0, (i*n_virt + t) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, i*n_virt + w]

												elif ((t != s) and (v != s) and (v != t) and (v != u) and (u == t) and (w == s)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * F[i, n_occ + v] + -4 * g[i, n_occ + v, n_occ + s, n_occ + s] + -4 * g[i, n_occ + s, n_occ + s, n_occ + v] + 4 * g[i, i, i, n_occ + v] ) * K[0, (i*n_virt + v) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, i*n_virt + s]

												elif ((t != s) and (v != s) and (v != t) and (v != u) and (u == t) and (w == t)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, n_occ + v, n_occ + s, n_occ + t] + -4 * g[i, n_occ + t, n_occ + s, n_occ + v] ) * K[0, (i*n_virt + v) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, i*n_virt + t]

												elif ((t != s) and (v != s) and (v != t) and (v != u) and (u == t) and (w == v)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-8 * g[i, n_occ + v, n_occ + s, n_occ + v] ) * K[0, (i*n_virt + v) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, i*n_virt + v]

												elif ((t != s) and (v != s) and (v != t) and (v != u) and (u == t) and (w != s) and (w != t) and (w != u) and (w != v)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, n_occ + v, n_occ + s, n_occ + w] + -4 * g[i, n_occ + w, n_occ + s, n_occ + v] ) * K[0, (i*n_virt + v) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, i*n_virt + w]

												elif ((t != s) and (v == s) and (u != s) and (u != t) and (w == s)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, n_occ + s, n_occ + t, n_occ + u] + 4 * g[i, n_occ + t, n_occ + s, n_occ + u] ) * K[0, (i*n_virt + s) * n_ex + i*n_virt + u+ 2*n_ex] * K[1, i*n_virt + s]

												elif ((t != s) and (v == s) and (u != s) and (u != t) and (w == t)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (8 * g[i, n_occ + t, n_occ + t, n_occ + u] ) * K[0, (i*n_virt + s) * n_ex + i*n_virt + u+ 2*n_ex] * K[1, i*n_virt + t]

												elif ((t != s) and (v == s) and (u != s) and (u != t) and (w == u)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, i, i, n_occ + t] + 4 * g[i, n_occ + u, n_occ + t, n_occ + u] + 4 * g[i, n_occ + t, n_occ + u, n_occ + u] ) * K[0, (i*n_virt + s) * n_ex + i*n_virt + u+ 2*n_ex] * K[1, i*n_virt + u]

												elif ((t != s) and (v == s) and (u != s) and (u != t) and (w != s) and (w != t) and (w != u) and (w != v)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, n_occ + w, n_occ + t, n_occ + u] + 4 * g[i, n_occ + t, n_occ + u, n_occ + w] ) * K[0, (i*n_virt + s) * n_ex + i*n_virt + u+ 2*n_ex] * K[1, i*n_virt + w]

											elif ((j == i) and (m == i) and (k == i) and (n != i) and (n != j) and (n != k) and (n != m)):

												if ((t == s) and (v == s) and (u == s) and (w == s)):

													L3[(i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * F[n, n_occ + s] ) * K[0, (i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] * K[1, n*n_virt + s]

												elif ((t == s) and (v != s) and (v != t) and (v != u) and (u == s) and (w == s)):

													L3[(i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * F[n, n_occ + v] + -8 * g[n, n_occ + s, n_occ + s, n_occ + v] + 4 * g[n, n_occ + v, n_occ + s, n_occ + s] + -4 * g[i, i, n, n_occ + v] + 8 * g[i, n, i, n_occ + v] ) * K[0, (i*n_virt + v) * n_ex + i*n_virt + s+ 2*n_ex] * K[1, n*n_virt + s]

												elif ((t == s) and (v != s) and (v != t) and (v != u) and (u == s) and (w == v)):

													L3[(i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[n, n_occ + v, n_occ + s, n_occ + v] ) * K[0, (i*n_virt + v) * n_ex + i*n_virt + s+ 2*n_ex] * K[1, n*n_virt + v]

												elif ((t == s) and (v != s) and (v != t) and (v != u) and (u == s) and (w != s) and (w != t) and (w != u) and (w != v)):

													L3[(i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[n, n_occ + v, n_occ + s, n_occ + w] + -8 * g[n, n_occ + w, n_occ + s, n_occ + v] ) * K[0, (i*n_virt + v) * n_ex + i*n_virt + s+ 2*n_ex] * K[1, n*n_virt + w]

												elif ((t == s) and (v == s) and (u != s) and (u != t) and (w == s)):

													L3[(i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[n, n_occ + s, n_occ + s, n_occ + u] ) * K[0, (i*n_virt + s) * n_ex + i*n_virt + u+ 2*n_ex] * K[1, n*n_virt + s]

												elif ((t == s) and (v == s) and (u != s) and (u != t) and (w == u)):

													L3[(i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-8 * g[i, n, i, n_occ + s] + 4 * g[i, i, n, n_occ + s] + 8 * g[n, n_occ + u, n_occ + s, n_occ + u] + -4 * g[n, n_occ + s, n_occ + u, n_occ + u] ) * K[0, (i*n_virt + s) * n_ex + i*n_virt + u+ 2*n_ex] * K[1, n*n_virt + u]

												elif ((t == s) and (v == s) and (u != s) and (u != t) and (w != s) and (w != t) and (w != u) and (w != v)):

													L3[(i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[n, n_occ + s, n_occ + u, n_occ + w] + 8 * g[n, n_occ + w, n_occ + s, n_occ + u] ) * K[0, (i*n_virt + s) * n_ex + i*n_virt + u+ 2*n_ex] * K[1, n*n_virt + w]

												elif ((t != s) and (v == s) and (u == s) and (w == s)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-8 * g[i, n, i, n_occ + t] + 4 * g[i, i, n, n_occ + t] + 8 * g[n, n_occ + s, n_occ + s, n_occ + t] + -4 * g[n, n_occ + t, n_occ + s, n_occ + s] ) * K[0, (i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] * K[1, n*n_virt + s]

												elif ((t != s) and (v == s) and (u == s) and (w == t)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[n, n_occ + t, n_occ + s, n_occ + t] ) * K[0, (i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] * K[1, n*n_virt + t]

												elif ((t != s) and (v == s) and (u == s) and (w != s) and (w != t) and (w != u) and (w != v)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[n, n_occ + t, n_occ + s, n_occ + w] + 8 * g[n, n_occ + w, n_occ + s, n_occ + t] ) * K[0, (i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] * K[1, n*n_virt + w]

												elif ((t != s) and (v == s) and (u == t) and (w == s)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * F[n, n_occ + s] + -4 * g[n, n_occ + t, n_occ + s, n_occ + t] + 8 * g[n, n_occ + s, n_occ + t, n_occ + t] + -4 * g[i, i, n, n_occ + s] + -4 * g[n, n_occ + s, n_occ + s, n_occ + s] + 8 * g[i, n, i, n_occ + s] ) * K[0, (i*n_virt + s) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, n*n_virt + s]

												elif ((t != s) and (v == s) and (u == t) and (w == t)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-8 * g[i, n, i, n_occ + t] + 4 * g[i, i, n, n_occ + t] + 4 * g[n, n_occ + t, n_occ + t, n_occ + t] + 4 * g[n, n_occ + s, n_occ + s, n_occ + t] + -8 * g[n, n_occ + t, n_occ + s, n_occ + s] ) * K[0, (i*n_virt + s) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, n*n_virt + t]

												elif ((t != s) and (v == s) and (u == t) and (w != s) and (w != t) and (w != u) and (w != v)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[n, n_occ + t, n_occ + t, n_occ + w] + 8 * g[n, n_occ + w, n_occ + t, n_occ + t] + 4 * g[n, n_occ + s, n_occ + s, n_occ + w] + -8 * g[n, n_occ + w, n_occ + s, n_occ + s] ) * K[0, (i*n_virt + s) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, n*n_virt + w]

												elif ((t != s) and (v == t) and (u == t) and (w == s)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * F[n, n_occ + t] + -8 * g[n, n_occ + s, n_occ + s, n_occ + t] + 4 * g[n, n_occ + t, n_occ + s, n_occ + s] + -4 * g[i, i, n, n_occ + t] + 8 * g[i, n, i, n_occ + t] ) * K[0, (i*n_virt + t) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, n*n_virt + s]

												elif ((t != s) and (v == t) and (u == t) and (w == t)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[n, n_occ + t, n_occ + s, n_occ + t] ) * K[0, (i*n_virt + t) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, n*n_virt + t]

												elif ((t != s) and (v == t) and (u == t) and (w != s) and (w != t) and (w != u) and (w != v)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[n, n_occ + t, n_occ + s, n_occ + w] + -8 * g[n, n_occ + w, n_occ + s, n_occ + t] ) * K[0, (i*n_virt + t) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, n*n_virt + w]

												elif ((t != s) and (v != s) and (v != t) and (v != u) and (u == t) and (w == s)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * F[n, n_occ + v] + -8 * g[n, n_occ + s, n_occ + s, n_occ + v] + 4 * g[n, n_occ + v, n_occ + s, n_occ + s] + -4 * g[i, i, n, n_occ + v] + 8 * g[i, n, i, n_occ + v] ) * K[0, (i*n_virt + v) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, n*n_virt + s]

												elif ((t != s) and (v != s) and (v != t) and (v != u) and (u == t) and (w == t)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-8 * g[n, n_occ + t, n_occ + s, n_occ + v] + 4 * g[n, n_occ + v, n_occ + s, n_occ + t] ) * K[0, (i*n_virt + v) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, n*n_virt + t]

												elif ((t != s) and (v != s) and (v != t) and (v != u) and (u == t) and (w == v)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[n, n_occ + v, n_occ + s, n_occ + v] ) * K[0, (i*n_virt + v) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, n*n_virt + v]

												elif ((t != s) and (v != s) and (v != t) and (v != u) and (u == t) and (w != s) and (w != t) and (w != u) and (w != v)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[n, n_occ + v, n_occ + s, n_occ + w] + -8 * g[n, n_occ + w, n_occ + s, n_occ + v] ) * K[0, (i*n_virt + v) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, n*n_virt + w]

												elif ((t != s) and (v == s) and (u != s) and (u != t) and (w == s)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (8 * g[n, n_occ + s, n_occ + t, n_occ + u] + -4 * g[n, n_occ + t, n_occ + s, n_occ + u] ) * K[0, (i*n_virt + s) * n_ex + i*n_virt + u+ 2*n_ex] * K[1, n*n_virt + s]

												elif ((t != s) and (v == s) and (u != s) and (u != t) and (w == t)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[n, n_occ + t, n_occ + t, n_occ + u] ) * K[0, (i*n_virt + s) * n_ex + i*n_virt + u+ 2*n_ex] * K[1, n*n_virt + t]

												elif ((t != s) and (v == s) and (u != s) and (u != t) and (w == u)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-8 * g[i, n, i, n_occ + t] + 4 * g[i, i, n, n_occ + t] + 8 * g[n, n_occ + u, n_occ + t, n_occ + u] + -4 * g[n, n_occ + t, n_occ + u, n_occ + u] ) * K[0, (i*n_virt + s) * n_ex + i*n_virt + u+ 2*n_ex] * K[1, n*n_virt + u]

												elif ((t != s) and (v == s) and (u != s) and (u != t) and (w != s) and (w != t) and (w != u) and (w != v)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[n, n_occ + t, n_occ + u, n_occ + w] + 8 * g[n, n_occ + w, n_occ + t, n_occ + u] ) * K[0, (i*n_virt + s) * n_ex + i*n_virt + u+ 2*n_ex] * K[1, n*n_virt + w]

											elif ((j == i) and (m != i) and (m != j) and (m != k) and (k == i) and (n == i)):

												if ((t == s) and (v == s) and (u == s) and (w == s)):

													L3[(i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * F[m, n_occ + s] + 4 * g[i, i, m, n_occ + s] + -4 * g[m, n_occ + s, n_occ + s, n_occ + s] + 4 * g[i, m, i, n_occ + s] ) * K[0, (m*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] * K[1, i*n_virt + s]

												elif ((t == s) and (v == s) and (u == s) and (w != s) and (w != t) and (w != u) and (w != v)):

													L3[(i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * F[m, n_occ + w] + -8 * g[m, n_occ + s, n_occ + s, n_occ + w] + 4 * g[m, n_occ + w, n_occ + s, n_occ + s] + -4 * g[i, i, m, n_occ + w] + 8 * g[i, m, i, n_occ + w] ) * K[0, (m*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] * K[1, i*n_virt + w]

												elif ((t == s) and (v != s) and (v != t) and (v != u) and (u == s) and (w == s)):

													L3[(i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, m, i, n_occ + v] + 8 * g[i, i, m, n_occ + v] + 4 * g[m, n_occ + s, n_occ + s, n_occ + v] + -8 * g[m, n_occ + v, n_occ + s, n_occ + s] ) * K[0, (m*n_virt + v) * n_ex + i*n_virt + s+ 2*n_ex] * K[1, i*n_virt + s]

												elif ((t == s) and (v != s) and (v != t) and (v != u) and (u == s) and (w == v)):

													L3[(i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[m, n_occ + v, n_occ + s, n_occ + v] ) * K[0, (m*n_virt + v) * n_ex + i*n_virt + s+ 2*n_ex] * K[1, i*n_virt + v]

												elif ((t == s) and (v != s) and (v != t) and (v != u) and (u == s) and (w != s) and (w != t) and (w != u) and (w != v)):

													L3[(i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-8 * g[m, n_occ + v, n_occ + s, n_occ + w] + 4 * g[m, n_occ + w, n_occ + s, n_occ + v] ) * K[0, (m*n_virt + v) * n_ex + i*n_virt + s+ 2*n_ex] * K[1, i*n_virt + w]

												elif ((t != s) and (v == s) and (u == t) and (w == s)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * F[m, n_occ + s] + 4 * g[i, i, m, n_occ + s] + -4 * g[m, n_occ + s, n_occ + s, n_occ + s] + 4 * g[i, m, i, n_occ + s] ) * K[0, (m*n_virt + s) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, i*n_virt + s]

												elif ((t != s) and (v == s) and (u == t) and (w == t)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * F[m, n_occ + t] + -8 * g[m, n_occ + s, n_occ + s, n_occ + t] + 4 * g[m, n_occ + t, n_occ + s, n_occ + s] + -4 * g[i, i, m, n_occ + t] + 8 * g[i, m, i, n_occ + t] ) * K[0, (m*n_virt + s) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, i*n_virt + t]

												elif ((t != s) and (v == s) and (u == t) and (w != s) and (w != t) and (w != u) and (w != v)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * F[m, n_occ + w] + -8 * g[m, n_occ + s, n_occ + s, n_occ + w] + 4 * g[m, n_occ + w, n_occ + s, n_occ + s] + -4 * g[i, i, m, n_occ + w] + 8 * g[i, m, i, n_occ + w] ) * K[0, (m*n_virt + s) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, i*n_virt + w]

												elif ((t != s) and (v == t) and (u == t) and (w == s)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, m, i, n_occ + t] + 8 * g[i, i, m, n_occ + t] + 4 * g[m, n_occ + s, n_occ + s, n_occ + t] + -8 * g[m, n_occ + t, n_occ + s, n_occ + s] ) * K[0, (m*n_virt + t) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, i*n_virt + s]

												elif ((t != s) and (v == t) and (u == t) and (w == t)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[m, n_occ + t, n_occ + s, n_occ + t] ) * K[0, (m*n_virt + t) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, i*n_virt + t]

												elif ((t != s) and (v == t) and (u == t) and (w != s) and (w != t) and (w != u) and (w != v)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-8 * g[m, n_occ + t, n_occ + s, n_occ + w] + 4 * g[m, n_occ + w, n_occ + s, n_occ + t] ) * K[0, (m*n_virt + t) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, i*n_virt + w]

												elif ((t != s) and (v != s) and (v != t) and (v != u) and (u == t) and (w == s)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, m, i, n_occ + v] + 8 * g[i, i, m, n_occ + v] + 4 * g[m, n_occ + s, n_occ + s, n_occ + v] + -8 * g[m, n_occ + v, n_occ + s, n_occ + s] ) * K[0, (m*n_virt + v) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, i*n_virt + s]

												elif ((t != s) and (v != s) and (v != t) and (v != u) and (u == t) and (w == t)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[m, n_occ + t, n_occ + s, n_occ + v] + -8 * g[m, n_occ + v, n_occ + s, n_occ + t] ) * K[0, (m*n_virt + v) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, i*n_virt + t]

												elif ((t != s) and (v != s) and (v != t) and (v != u) and (u == t) and (w == v)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[m, n_occ + v, n_occ + s, n_occ + v] ) * K[0, (m*n_virt + v) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, i*n_virt + v]

												elif ((t != s) and (v != s) and (v != t) and (v != u) and (u == t) and (w != s) and (w != t) and (w != u) and (w != v)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-8 * g[m, n_occ + v, n_occ + s, n_occ + w] + 4 * g[m, n_occ + w, n_occ + s, n_occ + v] ) * K[0, (m*n_virt + v) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, i*n_virt + w]

											elif ((j == i) and (m != i) and (m != j) and (m != k) and (k == i) and (n == m)):

												if ((t == s) and (v == s) and (u == s) and (w == s)):

													L3[(i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (8 * g[i, m, m, n_occ + s] ) * K[0, (m*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] * K[1, m*n_virt + s]

												elif ((t == s) and (v == s) and (u == s) and (w != s) and (w != t) and (w != u) and (w != v)):

													L3[(i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, m, m, n_occ + w] ) * K[0, (m*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] * K[1, m*n_virt + w]

												elif ((t == s) and (v != s) and (v != t) and (v != u) and (u == s) and (w == s)):

													L3[(i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, m, m, n_occ + v] ) * K[0, (m*n_virt + v) * n_ex + i*n_virt + s+ 2*n_ex] * K[1, m*n_virt + s]

												elif ((t != s) and (v == s) and (u == t) and (w == s)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (8 * g[i, m, m, n_occ + s] ) * K[0, (m*n_virt + s) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, m*n_virt + s]

												elif ((t != s) and (v == s) and (u == t) and (w == t)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, m, m, n_occ + t] ) * K[0, (m*n_virt + s) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, m*n_virt + t]

												elif ((t != s) and (v == s) and (u == t) and (w != s) and (w != t) and (w != u) and (w != v)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, m, m, n_occ + w] ) * K[0, (m*n_virt + s) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, m*n_virt + w]

												elif ((t != s) and (v == t) and (u == t) and (w == s)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, m, m, n_occ + t] ) * K[0, (m*n_virt + t) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, m*n_virt + s]

												elif ((t != s) and (v != s) and (v != t) and (v != u) and (u == t) and (w == s)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, m, m, n_occ + v] ) * K[0, (m*n_virt + v) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, m*n_virt + s]

											elif ((j == i) and (m != i) and (m != j) and (m != k) and (k == i) and (n != i) and (n != j) and (n != k) and (n != m)):

												if ((t == s) and (v == s) and (u == s) and (w == s)):

													L3[(i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, n, m, n_occ + s] + 4 * g[i, m, n, n_occ + s] ) * K[0, (m*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] * K[1, n*n_virt + s]

												elif ((t == s) and (v == s) and (u == s) and (w != s) and (w != t) and (w != u) and (w != v)):

													L3[(i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (8 * g[i, m, n, n_occ + w] + -4 * g[i, n, m, n_occ + w] ) * K[0, (m*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] * K[1, n*n_virt + w]

												elif ((t == s) and (v != s) and (v != t) and (v != u) and (u == s) and (w == s)):

													L3[(i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, m, n, n_occ + v] + 8 * g[i, n, m, n_occ + v] ) * K[0, (m*n_virt + v) * n_ex + i*n_virt + s+ 2*n_ex] * K[1, n*n_virt + s]

												elif ((t != s) and (v == s) and (u == t) and (w == s)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, n, m, n_occ + s] + 4 * g[i, m, n, n_occ + s] ) * K[0, (m*n_virt + s) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, n*n_virt + s]

												elif ((t != s) and (v == s) and (u == t) and (w == t)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (8 * g[i, m, n, n_occ + t] + -4 * g[i, n, m, n_occ + t] ) * K[0, (m*n_virt + s) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, n*n_virt + t]

												elif ((t != s) and (v == s) and (u == t) and (w != s) and (w != t) and (w != u) and (w != v)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (8 * g[i, m, n, n_occ + w] + -4 * g[i, n, m, n_occ + w] ) * K[0, (m*n_virt + s) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, n*n_virt + w]

												elif ((t != s) and (v == t) and (u == t) and (w == s)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, m, n, n_occ + t] + 8 * g[i, n, m, n_occ + t] ) * K[0, (m*n_virt + t) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, n*n_virt + s]

												elif ((t != s) and (v != s) and (v != t) and (v != u) and (u == t) and (w == s)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, m, n, n_occ + v] + 8 * g[i, n, m, n_occ + v] ) * K[0, (m*n_virt + v) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, n*n_virt + s]

											elif ((j == i) and (m == i) and (k != i) and (k != j) and (n == i)):

												if ((t == s) and (v == s) and (u == s) and (w == s)):

													L3[(i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-8 * g[i, k, i, n_occ + s] ) * K[0, (i*n_virt + s) * n_ex + k*n_virt + s+ 2*n_ex] * K[1, i*n_virt + s]

												elif ((t == s) and (v == s) and (u == s) and (w != s) and (w != t) and (w != u) and (w != v)):

													L3[(i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, k, i, n_occ + w] ) * K[0, (i*n_virt + s) * n_ex + k*n_virt + s+ 2*n_ex] * K[1, i*n_virt + w]

												elif ((t == s) and (v == s) and (u != s) and (u != t) and (w == u)):

													L3[(i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, k, i, n_occ + s] ) * K[0, (i*n_virt + s) * n_ex + k*n_virt + u+ 2*n_ex] * K[1, i*n_virt + u]

												elif ((t != s) and (v == s) and (u == s) and (w == s)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, k, i, n_occ + t] ) * K[0, (i*n_virt + s) * n_ex + k*n_virt + s+ 2*n_ex] * K[1, i*n_virt + s]

												elif ((t != s) and (v == s) and (u == t) and (w == s)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, k, i, n_occ + s] ) * K[0, (i*n_virt + s) * n_ex + k*n_virt + t+ 2*n_ex] * K[1, i*n_virt + s]

												elif ((t != s) and (v == s) and (u == t) and (w == t)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-8 * g[i, k, i, n_occ + t] ) * K[0, (i*n_virt + s) * n_ex + k*n_virt + t+ 2*n_ex] * K[1, i*n_virt + t]

												elif ((t != s) and (v == s) and (u == t) and (w != s) and (w != t) and (w != u) and (w != v)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, k, i, n_occ + w] ) * K[0, (i*n_virt + s) * n_ex + k*n_virt + t+ 2*n_ex] * K[1, i*n_virt + w]

												elif ((t != s) and (v == s) and (u != s) and (u != t) and (w == u)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, k, i, n_occ + t] ) * K[0, (i*n_virt + s) * n_ex + k*n_virt + u+ 2*n_ex] * K[1, i*n_virt + u]

											elif ((j == i) and (m == i) and (k != i) and (k != j) and (n == k)):

												if ((t == s) and (v == s) and (u == s) and (w == s)):

													L3[(i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, n_occ + s, k, k] + 4 * g[i, n_occ + s, n_occ + s, n_occ + s] + -4 * g[i, k, k, n_occ + s] ) * K[0, (i*n_virt + s) * n_ex + k*n_virt + s+ 2*n_ex] * K[1, k*n_virt + s]

												elif ((t == s) and (v == s) and (u == s) and (w != s) and (w != t) and (w != u) and (w != v)):

													L3[(i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-8 * g[i, k, k, n_occ + w] + 4 * g[i, n_occ + w, k, k] + 8 * g[i, n_occ + s, n_occ + s, n_occ + w] + -4 * g[i, n_occ + w, n_occ + s, n_occ + s] ) * K[0, (i*n_virt + s) * n_ex + k*n_virt + s+ 2*n_ex] * K[1, k*n_virt + w]

												elif ((t == s) and (v == s) and (u != s) and (u != t) and (w == s)):

													L3[(i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, n_occ + s, n_occ + s, n_occ + u] ) * K[0, (i*n_virt + s) * n_ex + k*n_virt + u+ 2*n_ex] * K[1, k*n_virt + s]

												elif ((t == s) and (v == s) and (u != s) and (u != t) and (w == u)):

													L3[(i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, k, k, n_occ + s] + -8 * g[i, n_occ + s, k, k] + -4 * g[i, n_occ + u, n_occ + s, n_occ + u] + 8 * g[i, n_occ + s, n_occ + u, n_occ + u] ) * K[0, (i*n_virt + s) * n_ex + k*n_virt + u+ 2*n_ex] * K[1, k*n_virt + u]

												elif ((t == s) and (v == s) and (u != s) and (u != t) and (w != s) and (w != t) and (w != u) and (w != v)):

													L3[(i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (8 * g[i, n_occ + s, n_occ + u, n_occ + w] + -4 * g[i, n_occ + w, n_occ + s, n_occ + u] ) * K[0, (i*n_virt + s) * n_ex + k*n_virt + u+ 2*n_ex] * K[1, k*n_virt + w]

												elif ((t != s) and (v == s) and (u == s) and (w == s)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, k, k, n_occ + t] + -8 * g[i, n_occ + t, k, k] + -4 * g[i, n_occ + s, n_occ + s, n_occ + t] + 8 * g[i, n_occ + t, n_occ + s, n_occ + s] ) * K[0, (i*n_virt + s) * n_ex + k*n_virt + s+ 2*n_ex] * K[1, k*n_virt + s]

												elif ((t != s) and (v == s) and (u == s) and (w == t)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, n_occ + t, n_occ + s, n_occ + t] ) * K[0, (i*n_virt + s) * n_ex + k*n_virt + s+ 2*n_ex] * K[1, k*n_virt + t]

												elif ((t != s) and (v == s) and (u == s) and (w != s) and (w != t) and (w != u) and (w != v)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (8 * g[i, n_occ + t, n_occ + s, n_occ + w] + -4 * g[i, n_occ + w, n_occ + s, n_occ + t] ) * K[0, (i*n_virt + s) * n_ex + k*n_virt + s+ 2*n_ex] * K[1, k*n_virt + w]

												elif ((t != s) and (v == s) and (u == t) and (w == s)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-8 * g[i, k, k, n_occ + s] + 4 * g[i, n_occ + s, k, k] + 8 * g[i, n_occ + t, n_occ + s, n_occ + t] + -4 * g[i, n_occ + s, n_occ + t, n_occ + t] ) * K[0, (i*n_virt + s) * n_ex + k*n_virt + t+ 2*n_ex] * K[1, k*n_virt + s]

												elif ((t != s) and (v == s) and (u == t) and (w == t)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, n_occ + t, k, k] + 4 * g[i, n_occ + t, n_occ + t, n_occ + t] + -4 * g[i, k, k, n_occ + t] ) * K[0, (i*n_virt + s) * n_ex + k*n_virt + t+ 2*n_ex] * K[1, k*n_virt + t]

												elif ((t != s) and (v == s) and (u == t) and (w != s) and (w != t) and (w != u) and (w != v)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-8 * g[i, k, k, n_occ + w] + 4 * g[i, n_occ + w, k, k] + 8 * g[i, n_occ + t, n_occ + t, n_occ + w] + -4 * g[i, n_occ + w, n_occ + t, n_occ + t] ) * K[0, (i*n_virt + s) * n_ex + k*n_virt + t+ 2*n_ex] * K[1, k*n_virt + w]

												elif ((t != s) and (v == s) and (u != s) and (u != t) and (w == s)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, n_occ + s, n_occ + t, n_occ + u] + 8 * g[i, n_occ + t, n_occ + s, n_occ + u] ) * K[0, (i*n_virt + s) * n_ex + k*n_virt + u+ 2*n_ex] * K[1, k*n_virt + s]

												elif ((t != s) and (v == s) and (u != s) and (u != t) and (w == t)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, n_occ + t, n_occ + t, n_occ + u] ) * K[0, (i*n_virt + s) * n_ex + k*n_virt + u+ 2*n_ex] * K[1, k*n_virt + t]

												elif ((t != s) and (v == s) and (u != s) and (u != t) and (w == u)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, k, k, n_occ + t] + -8 * g[i, n_occ + t, k, k] + -4 * g[i, n_occ + u, n_occ + t, n_occ + u] + 8 * g[i, n_occ + t, n_occ + u, n_occ + u] ) * K[0, (i*n_virt + s) * n_ex + k*n_virt + u+ 2*n_ex] * K[1, k*n_virt + u]

												elif ((t != s) and (v == s) and (u != s) and (u != t) and (w != s) and (w != t) and (w != u) and (w != v)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (8 * g[i, n_occ + t, n_occ + u, n_occ + w] + -4 * g[i, n_occ + w, n_occ + t, n_occ + u] ) * K[0, (i*n_virt + s) * n_ex + k*n_virt + u+ 2*n_ex] * K[1, k*n_virt + w]

											elif ((j == i) and (m == i) and (k != i) and (k != j) and (n != i) and (n != j) and (n != k) and (n != m)):

												if ((t == s) and (v == s) and (u == s) and (w == s)):

													L3[(i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, k, n, n_occ + s] + -4 * g[i, n_occ + s, k, n] ) * K[0, (i*n_virt + s) * n_ex + k*n_virt + s+ 2*n_ex] * K[1, n*n_virt + s]

												elif ((t == s) and (v == s) and (u == s) and (w != s) and (w != t) and (w != u) and (w != v)):

													L3[(i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-8 * g[i, k, n, n_occ + w] + 4 * g[i, n_occ + w, k, n] ) * K[0, (i*n_virt + s) * n_ex + k*n_virt + s+ 2*n_ex] * K[1, n*n_virt + w]

												elif ((t == s) and (v == s) and (u != s) and (u != t) and (w == u)):

													L3[(i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, k, n, n_occ + s] + -8 * g[i, n_occ + s, k, n] ) * K[0, (i*n_virt + s) * n_ex + k*n_virt + u+ 2*n_ex] * K[1, n*n_virt + u]

												elif ((t != s) and (v == s) and (u == s) and (w == s)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, k, n, n_occ + t] + -8 * g[i, n_occ + t, k, n] ) * K[0, (i*n_virt + s) * n_ex + k*n_virt + s+ 2*n_ex] * K[1, n*n_virt + s]

												elif ((t != s) and (v == s) and (u == t) and (w == s)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-8 * g[i, k, n, n_occ + s] + 4 * g[i, n_occ + s, k, n] ) * K[0, (i*n_virt + s) * n_ex + k*n_virt + t+ 2*n_ex] * K[1, n*n_virt + s]

												elif ((t != s) and (v == s) and (u == t) and (w == t)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, k, n, n_occ + t] + -4 * g[i, n_occ + t, k, n] ) * K[0, (i*n_virt + s) * n_ex + k*n_virt + t+ 2*n_ex] * K[1, n*n_virt + t]

												elif ((t != s) and (v == s) and (u == t) and (w != s) and (w != t) and (w != u) and (w != v)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-8 * g[i, k, n, n_occ + w] + 4 * g[i, n_occ + w, k, n] ) * K[0, (i*n_virt + s) * n_ex + k*n_virt + t+ 2*n_ex] * K[1, n*n_virt + w]

												elif ((t != s) and (v == s) and (u != s) and (u != t) and (w == u)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, k, n, n_occ + t] + -8 * g[i, n_occ + t, k, n] ) * K[0, (i*n_virt + s) * n_ex + k*n_virt + u+ 2*n_ex] * K[1, n*n_virt + u]

											elif ((j != i) and (m == i) and (k == i) and (n == i)):

												if ((t == s) and (v == s) and (u == s) and (w == s)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, i, j, n_occ + s] + 4 * g[j, n_occ + s, n_occ + s, n_occ + s] + -4 * g[i, j, i, n_occ + s] ) * K[0, (i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] * K[1, i*n_virt + s]

												elif ((t == s) and (v == s) and (u == s) and (w != s) and (w != t) and (w != u) and (w != v)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-8 * g[i, j, i, n_occ + w] + 4 * g[i, i, j, n_occ + w] + 8 * g[j, n_occ + s, n_occ + s, n_occ + w] + -4 * g[j, n_occ + w, n_occ + s, n_occ + s] ) * K[0, (i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] * K[1, i*n_virt + w]

												elif ((t == s) and (v == s) and (u != s) and (u != t) and (w == s)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[j, n_occ + s, n_occ + s, n_occ + u] ) * K[0, (i*n_virt + s) * n_ex + i*n_virt + u+ 2*n_ex] * K[1, i*n_virt + s]

												elif ((t == s) and (v == s) and (u != s) and (u != t) and (w == u)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, j, i, n_occ + s] + -8 * g[i, i, j, n_occ + s] + -4 * g[j, n_occ + u, n_occ + s, n_occ + u] + 8 * g[j, n_occ + s, n_occ + u, n_occ + u] ) * K[0, (i*n_virt + s) * n_ex + i*n_virt + u+ 2*n_ex] * K[1, i*n_virt + u]

												elif ((t == s) and (v == s) and (u != s) and (u != t) and (w != s) and (w != t) and (w != u) and (w != v)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (8 * g[j, n_occ + s, n_occ + u, n_occ + w] + -4 * g[j, n_occ + w, n_occ + s, n_occ + u] ) * K[0, (i*n_virt + s) * n_ex + i*n_virt + u+ 2*n_ex] * K[1, i*n_virt + w]

												elif ((t != s) and (v == s) and (u == s) and (w == s)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, j, i, n_occ + t] + -8 * g[i, i, j, n_occ + t] + -4 * g[j, n_occ + s, n_occ + s, n_occ + t] + 8 * g[j, n_occ + t, n_occ + s, n_occ + s] ) * K[0, (i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] * K[1, i*n_virt + s]

												elif ((t != s) and (v == s) and (u == s) and (w == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[j, n_occ + t, n_occ + s, n_occ + t] ) * K[0, (i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] * K[1, i*n_virt + t]

												elif ((t != s) and (v == s) and (u == s) and (w != s) and (w != t) and (w != u) and (w != v)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (8 * g[j, n_occ + t, n_occ + s, n_occ + w] + -4 * g[j, n_occ + w, n_occ + s, n_occ + t] ) * K[0, (i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] * K[1, i*n_virt + w]

												elif ((t != s) and (v == s) and (u == t) and (w == s)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-8 * g[i, j, i, n_occ + s] + 4 * g[i, i, j, n_occ + s] + 8 * g[j, n_occ + t, n_occ + s, n_occ + t] + -4 * g[j, n_occ + s, n_occ + t, n_occ + t] ) * K[0, (i*n_virt + s) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, i*n_virt + s]

												elif ((t != s) and (v == s) and (u == t) and (w == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, i, j, n_occ + t] + 4 * g[j, n_occ + t, n_occ + t, n_occ + t] + -4 * g[i, j, i, n_occ + t] ) * K[0, (i*n_virt + s) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, i*n_virt + t]

												elif ((t != s) and (v == s) and (u == t) and (w != s) and (w != t) and (w != u) and (w != v)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-8 * g[i, j, i, n_occ + w] + 4 * g[i, i, j, n_occ + w] + 8 * g[j, n_occ + t, n_occ + t, n_occ + w] + -4 * g[j, n_occ + w, n_occ + t, n_occ + t] ) * K[0, (i*n_virt + s) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, i*n_virt + w]

												elif ((t != s) and (v == s) and (u != s) and (u != t) and (w == s)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[j, n_occ + s, n_occ + t, n_occ + u] + 8 * g[j, n_occ + t, n_occ + s, n_occ + u] ) * K[0, (i*n_virt + s) * n_ex + i*n_virt + u+ 2*n_ex] * K[1, i*n_virt + s]

												elif ((t != s) and (v == s) and (u != s) and (u != t) and (w == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[j, n_occ + t, n_occ + t, n_occ + u] ) * K[0, (i*n_virt + s) * n_ex + i*n_virt + u+ 2*n_ex] * K[1, i*n_virt + t]

												elif ((t != s) and (v == s) and (u != s) and (u != t) and (w == u)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, j, i, n_occ + t] + -8 * g[i, i, j, n_occ + t] + -4 * g[j, n_occ + u, n_occ + t, n_occ + u] + 8 * g[j, n_occ + t, n_occ + u, n_occ + u] ) * K[0, (i*n_virt + s) * n_ex + i*n_virt + u+ 2*n_ex] * K[1, i*n_virt + u]

												elif ((t != s) and (v == s) and (u != s) and (u != t) and (w != s) and (w != t) and (w != u) and (w != v)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (8 * g[j, n_occ + t, n_occ + u, n_occ + w] + -4 * g[j, n_occ + w, n_occ + t, n_occ + u] ) * K[0, (i*n_virt + s) * n_ex + i*n_virt + u+ 2*n_ex] * K[1, i*n_virt + w]

											elif ((j != i) and (m == i) and (k == i) and (n == j)):

												if ((t == s) and (v == s) and (u == s) and (w == s)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-8 * g[i, j, j, n_occ + s] ) * K[0, (i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] * K[1, j*n_virt + s]

												elif ((t == s) and (v == s) and (u == s) and (w != s) and (w != t) and (w != u) and (w != v)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, j, j, n_occ + w] ) * K[0, (i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] * K[1, j*n_virt + w]

												elif ((t == s) and (v == s) and (u != s) and (u != t) and (w == u)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, j, j, n_occ + s] ) * K[0, (i*n_virt + s) * n_ex + i*n_virt + u+ 2*n_ex] * K[1, j*n_virt + u]

												elif ((t != s) and (v == s) and (u == s) and (w == s)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, j, j, n_occ + t] ) * K[0, (i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] * K[1, j*n_virt + s]

												elif ((t != s) and (v == s) and (u == t) and (w == s)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, j, j, n_occ + s] ) * K[0, (i*n_virt + s) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, j*n_virt + s]

												elif ((t != s) and (v == s) and (u == t) and (w == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-8 * g[i, j, j, n_occ + t] ) * K[0, (i*n_virt + s) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, j*n_virt + t]

												elif ((t != s) and (v == s) and (u == t) and (w != s) and (w != t) and (w != u) and (w != v)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, j, j, n_occ + w] ) * K[0, (i*n_virt + s) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, j*n_virt + w]

												elif ((t != s) and (v == s) and (u != s) and (u != t) and (w == u)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, j, j, n_occ + t] ) * K[0, (i*n_virt + s) * n_ex + i*n_virt + u+ 2*n_ex] * K[1, j*n_virt + u]

											elif ((j != i) and (m == i) and (k == i) and (n != i) and (n != j) and (n != k) and (n != m)):

												if ((t == s) and (v == s) and (u == s) and (w == s)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, j, n, n_occ + s] + -4 * g[i, n, j, n_occ + s] ) * K[0, (i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] * K[1, n*n_virt + s]

												elif ((t == s) and (v == s) and (u == s) and (w != s) and (w != t) and (w != u) and (w != v)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-8 * g[i, j, n, n_occ + w] + 4 * g[i, n, j, n_occ + w] ) * K[0, (i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] * K[1, n*n_virt + w]

												elif ((t == s) and (v == s) and (u != s) and (u != t) and (w == u)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, j, n, n_occ + s] + -8 * g[i, n, j, n_occ + s] ) * K[0, (i*n_virt + s) * n_ex + i*n_virt + u+ 2*n_ex] * K[1, n*n_virt + u]

												elif ((t != s) and (v == s) and (u == s) and (w == s)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, j, n, n_occ + t] + -8 * g[i, n, j, n_occ + t] ) * K[0, (i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] * K[1, n*n_virt + s]

												elif ((t != s) and (v == s) and (u == t) and (w == s)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-8 * g[i, j, n, n_occ + s] + 4 * g[i, n, j, n_occ + s] ) * K[0, (i*n_virt + s) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, n*n_virt + s]

												elif ((t != s) and (v == s) and (u == t) and (w == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, j, n, n_occ + t] + -4 * g[i, n, j, n_occ + t] ) * K[0, (i*n_virt + s) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, n*n_virt + t]

												elif ((t != s) and (v == s) and (u == t) and (w != s) and (w != t) and (w != u) and (w != v)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-8 * g[i, j, n, n_occ + w] + 4 * g[i, n, j, n_occ + w] ) * K[0, (i*n_virt + s) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, n*n_virt + w]

												elif ((t != s) and (v == s) and (u != s) and (u != t) and (w == u)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, j, n, n_occ + t] + -8 * g[i, n, j, n_occ + t] ) * K[0, (i*n_virt + s) * n_ex + i*n_virt + u+ 2*n_ex] * K[1, n*n_virt + u]

											elif ((j != i) and (m == i) and (k == j) and (n == i)):

												if ((t == s) and (v == s) and (u == s) and (w == s)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (8 * F[i, n_occ + s] + -4 * g[i, j, j, n_occ + s] + -4 * g[i, n_occ + s, j, j] + -4 * g[i, n_occ + s, n_occ + s, n_occ + s] + 8 * g[i, i, i, n_occ + s] ) * K[0, (i*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, i*n_virt + s]

												elif ((t == s) and (v == s) and (u == s) and (w != s) and (w != t) and (w != u) and (w != v)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * F[i, n_occ + w] + -8 * g[i, n_occ + s, n_occ + s, n_occ + w] + 4 * g[i, n_occ + w, n_occ + s, n_occ + s] + 4 * g[i, i, i, n_occ + w] + -8 * g[i, n_occ + w, j, j] + 4 * g[i, j, j, n_occ + w] ) * K[0, (i*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, i*n_virt + w]

												elif ((t == s) and (v != s) and (v != t) and (v != u) and (u == s) and (w == s)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * F[i, n_occ + v] + -4 * g[i, n_occ + v, n_occ + s, n_occ + s] + -4 * g[i, n_occ + s, n_occ + s, n_occ + v] + 4 * g[i, i, i, n_occ + v] ) * K[0, (i*n_virt + v) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, i*n_virt + s]

												elif ((t == s) and (v != s) and (v != t) and (v != u) and (u == s) and (w == v)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-8 * g[i, n_occ + v, n_occ + s, n_occ + v] ) * K[0, (i*n_virt + v) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, i*n_virt + v]

												elif ((t == s) and (v != s) and (v != t) and (v != u) and (u == s) and (w != s) and (w != t) and (w != u) and (w != v)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, n_occ + v, n_occ + s, n_occ + w] + -4 * g[i, n_occ + w, n_occ + s, n_occ + v] ) * K[0, (i*n_virt + v) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, i*n_virt + w]

												elif ((t == s) and (v == s) and (u != s) and (u != t) and (w == s)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, n_occ + s, n_occ + s, n_occ + u] ) * K[0, (i*n_virt + s) * n_ex + j*n_virt + u+ 2*n_ex] * K[1, i*n_virt + s]

												elif ((t == s) and (v == s) and (u != s) and (u != t) and (w == u)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-8 * g[i, j, j, n_occ + s] + 4 * g[i, n_occ + s, j, j] + 8 * g[i, n_occ + u, n_occ + s, n_occ + u] + -4 * g[i, n_occ + s, n_occ + u, n_occ + u] ) * K[0, (i*n_virt + s) * n_ex + j*n_virt + u+ 2*n_ex] * K[1, i*n_virt + u]

												elif ((t == s) and (v == s) and (u != s) and (u != t) and (w != s) and (w != t) and (w != u) and (w != v)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, n_occ + s, n_occ + u, n_occ + w] + 8 * g[i, n_occ + w, n_occ + s, n_occ + u] ) * K[0, (i*n_virt + s) * n_ex + j*n_virt + u+ 2*n_ex] * K[1, i*n_virt + w]

												elif ((t != s) and (v == s) and (u == s) and (w == s)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-8 * g[i, j, j, n_occ + t] + 4 * g[i, n_occ + t, j, j] + 8 * g[i, n_occ + s, n_occ + s, n_occ + t] + -4 * g[i, n_occ + t, n_occ + s, n_occ + s] ) * K[0, (i*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, i*n_virt + s]

												elif ((t != s) and (v == s) and (u == s) and (w == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, n_occ + t, n_occ + s, n_occ + t] ) * K[0, (i*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, i*n_virt + t]

												elif ((t != s) and (v == s) and (u == s) and (w != s) and (w != t) and (w != u) and (w != v)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, n_occ + t, n_occ + s, n_occ + w] + 8 * g[i, n_occ + w, n_occ + s, n_occ + t] ) * K[0, (i*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, i*n_virt + w]

												elif ((t != s) and (v == s) and (u == t) and (w == s)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (8 * F[i, n_occ + s] + 4 * g[i, j, j, n_occ + s] + -8 * g[i, n_occ + s, j, j] + -4 * g[i, n_occ + t, n_occ + s, n_occ + t] + 8 * g[i, n_occ + s, n_occ + t, n_occ + t] + -8 * g[i, n_occ + s, n_occ + s, n_occ + s] + 8 * g[i, i, i, n_occ + s] ) * K[0, (i*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, i*n_virt + s]

												elif ((t != s) and (v == s) and (u == t) and (w == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * F[i, n_occ + t] + -4 * g[i, j, j, n_occ + t] + -4 * g[i, n_occ + t, j, j] + 4 * g[i, n_occ + t, n_occ + t, n_occ + t] + -4 * g[i, n_occ + s, n_occ + s, n_occ + t] + -4 * g[i, n_occ + t, n_occ + s, n_occ + s] + 4 * g[i, i, i, n_occ + t] ) * K[0, (i*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, i*n_virt + t]

												elif ((t != s) and (v == s) and (u == t) and (w != s) and (w != t) and (w != u) and (w != v)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * F[i, n_occ + w] + -4 * g[i, n_occ + t, n_occ + t, n_occ + w] + 8 * g[i, n_occ + w, n_occ + t, n_occ + t] + -4 * g[i, n_occ + s, n_occ + s, n_occ + w] + -4 * g[i, n_occ + w, n_occ + s, n_occ + s] + 4 * g[i, i, i, n_occ + w] + -8 * g[i, n_occ + w, j, j] + 4 * g[i, j, j, n_occ + w] ) * K[0, (i*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, i*n_virt + w]

												elif ((t != s) and (v == t) and (u == t) and (w == s)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * F[i, n_occ + t] + -4 * g[i, n_occ + t, n_occ + s, n_occ + s] + -4 * g[i, n_occ + s, n_occ + s, n_occ + t] + 4 * g[i, i, i, n_occ + t] ) * K[0, (i*n_virt + t) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, i*n_virt + s]

												elif ((t != s) and (v == t) and (u == t) and (w == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-8 * g[i, n_occ + t, n_occ + s, n_occ + t] ) * K[0, (i*n_virt + t) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, i*n_virt + t]

												elif ((t != s) and (v == t) and (u == t) and (w != s) and (w != t) and (w != u) and (w != v)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, n_occ + t, n_occ + s, n_occ + w] + -4 * g[i, n_occ + w, n_occ + s, n_occ + t] ) * K[0, (i*n_virt + t) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, i*n_virt + w]

												elif ((t != s) and (v != s) and (v != t) and (v != u) and (u == t) and (w == s)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * F[i, n_occ + v] + -4 * g[i, n_occ + v, n_occ + s, n_occ + s] + -4 * g[i, n_occ + s, n_occ + s, n_occ + v] + 4 * g[i, i, i, n_occ + v] ) * K[0, (i*n_virt + v) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, i*n_virt + s]

												elif ((t != s) and (v != s) and (v != t) and (v != u) and (u == t) and (w == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, n_occ + v, n_occ + s, n_occ + t] + -4 * g[i, n_occ + t, n_occ + s, n_occ + v] ) * K[0, (i*n_virt + v) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, i*n_virt + t]

												elif ((t != s) and (v != s) and (v != t) and (v != u) and (u == t) and (w == v)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-8 * g[i, n_occ + v, n_occ + s, n_occ + v] ) * K[0, (i*n_virt + v) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, i*n_virt + v]

												elif ((t != s) and (v != s) and (v != t) and (v != u) and (u == t) and (w != s) and (w != t) and (w != u) and (w != v)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, n_occ + v, n_occ + s, n_occ + w] + -4 * g[i, n_occ + w, n_occ + s, n_occ + v] ) * K[0, (i*n_virt + v) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, i*n_virt + w]

												elif ((t != s) and (v == s) and (u != s) and (u != t) and (w == s)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (8 * g[i, n_occ + s, n_occ + t, n_occ + u] + -4 * g[i, n_occ + t, n_occ + s, n_occ + u] ) * K[0, (i*n_virt + s) * n_ex + j*n_virt + u+ 2*n_ex] * K[1, i*n_virt + s]

												elif ((t != s) and (v == s) and (u != s) and (u != t) and (w == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, n_occ + t, n_occ + t, n_occ + u] ) * K[0, (i*n_virt + s) * n_ex + j*n_virt + u+ 2*n_ex] * K[1, i*n_virt + t]

												elif ((t != s) and (v == s) and (u != s) and (u != t) and (w == u)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-8 * g[i, j, j, n_occ + t] + 4 * g[i, n_occ + t, j, j] + 8 * g[i, n_occ + u, n_occ + t, n_occ + u] + -4 * g[i, n_occ + t, n_occ + u, n_occ + u] ) * K[0, (i*n_virt + s) * n_ex + j*n_virt + u+ 2*n_ex] * K[1, i*n_virt + u]

												elif ((t != s) and (v == s) and (u != s) and (u != t) and (w != s) and (w != t) and (w != u) and (w != v)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, n_occ + t, n_occ + u, n_occ + w] + 8 * g[i, n_occ + w, n_occ + t, n_occ + u] ) * K[0, (i*n_virt + s) * n_ex + j*n_virt + u+ 2*n_ex] * K[1, i*n_virt + w]

											elif ((j != i) and (m == i) and (k == j) and (n == j)):

												if ((t == s) and (v == s) and (u == s) and (w == s)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * F[j, n_occ + s] + 4 * g[i, i, j, n_occ + s] + 4 * g[j, n_occ + s, n_occ + s, n_occ + s] + -8 * g[j, j, j, n_occ + s] + 4 * g[i, j, i, n_occ + s] ) * K[0, (i*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, j*n_virt + s]

												elif ((t == s) and (v == s) and (u == s) and (w != s) and (w != t) and (w != u) and (w != v)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, j, i, n_occ + w] + 8 * g[i, i, j, n_occ + w] + 8 * g[j, n_occ + s, n_occ + s, n_occ + w] + -4 * g[j, n_occ + w, n_occ + s, n_occ + s] + -4 * g[j, j, j, n_occ + w] ) * K[0, (i*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, j*n_virt + w]

												elif ((t == s) and (v != s) and (v != t) and (v != u) and (u == s) and (w == s)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * F[j, n_occ + v] + -8 * g[j, n_occ + s, n_occ + s, n_occ + v] + 4 * g[j, n_occ + v, n_occ + s, n_occ + s] + -4 * g[i, i, j, n_occ + v] + 8 * g[i, j, i, n_occ + v] ) * K[0, (i*n_virt + v) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, j*n_virt + s]

												elif ((t == s) and (v != s) and (v != t) and (v != u) and (u == s) and (w == v)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[j, n_occ + v, n_occ + s, n_occ + v] ) * K[0, (i*n_virt + v) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, j*n_virt + v]

												elif ((t == s) and (v != s) and (v != t) and (v != u) and (u == s) and (w != s) and (w != t) and (w != u) and (w != v)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[j, n_occ + v, n_occ + s, n_occ + w] + -8 * g[j, n_occ + w, n_occ + s, n_occ + v] ) * K[0, (i*n_virt + v) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, j*n_virt + w]

												elif ((t == s) and (v == s) and (u != s) and (u != t) and (w == s)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (8 * g[j, n_occ + s, n_occ + s, n_occ + u] ) * K[0, (i*n_virt + s) * n_ex + j*n_virt + u+ 2*n_ex] * K[1, j*n_virt + s]

												elif ((t == s) and (v == s) and (u != s) and (u != t) and (w == u)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[j, j, j, n_occ + s] + 4 * g[j, n_occ + u, n_occ + s, n_occ + u] + 4 * g[j, n_occ + s, n_occ + u, n_occ + u] ) * K[0, (i*n_virt + s) * n_ex + j*n_virt + u+ 2*n_ex] * K[1, j*n_virt + u]

												elif ((t == s) and (v == s) and (u != s) and (u != t) and (w != s) and (w != t) and (w != u) and (w != v)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[j, n_occ + w, n_occ + s, n_occ + u] + 4 * g[j, n_occ + s, n_occ + u, n_occ + w] ) * K[0, (i*n_virt + s) * n_ex + j*n_virt + u+ 2*n_ex] * K[1, j*n_virt + w]

												elif ((t != s) and (v == s) and (u == s) and (w == s)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[j, j, j, n_occ + t] + 4 * g[j, n_occ + s, n_occ + s, n_occ + t] + 4 * g[j, n_occ + t, n_occ + s, n_occ + s] ) * K[0, (i*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, j*n_virt + s]

												elif ((t != s) and (v == s) and (u == s) and (w == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (8 * g[j, n_occ + t, n_occ + s, n_occ + t] ) * K[0, (i*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, j*n_virt + t]

												elif ((t != s) and (v == s) and (u == s) and (w != s) and (w != t) and (w != u) and (w != v)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[j, n_occ + w, n_occ + s, n_occ + t] + 4 * g[j, n_occ + t, n_occ + s, n_occ + w] ) * K[0, (i*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, j*n_virt + w]

												elif ((t != s) and (v == s) and (u == t) and (w == s)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * F[j, n_occ + s] + 4 * g[i, i, j, n_occ + s] + 4 * g[j, n_occ + s, n_occ + t, n_occ + t] + 4 * g[j, n_occ + t, n_occ + s, n_occ + t] + -4 * g[j, n_occ + s, n_occ + s, n_occ + s] + 4 * g[i, j, i, n_occ + s] + -4 * g[j, j, j, n_occ + s] ) * K[0, (i*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, j*n_virt + s]

												elif ((t != s) and (v == s) and (u == t) and (w == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, j, i, n_occ + t] + 8 * g[i, i, j, n_occ + t] + 8 * g[j, n_occ + t, n_occ + t, n_occ + t] + 4 * g[j, n_occ + s, n_occ + s, n_occ + t] + -8 * g[j, n_occ + t, n_occ + s, n_occ + s] + -8 * g[j, j, j, n_occ + t] ) * K[0, (i*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, j*n_virt + t]

												elif ((t != s) and (v == s) and (u == t) and (w != s) and (w != t) and (w != u) and (w != v)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, j, i, n_occ + w] + 8 * g[i, i, j, n_occ + w] + 4 * g[j, n_occ + w, n_occ + t, n_occ + t] + 4 * g[j, n_occ + t, n_occ + t, n_occ + w] + 4 * g[j, n_occ + s, n_occ + s, n_occ + w] + -8 * g[j, n_occ + w, n_occ + s, n_occ + s] + -4 * g[j, j, j, n_occ + w] ) * K[0, (i*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, j*n_virt + w]

												elif ((t != s) and (v == t) and (u == t) and (w == s)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * F[j, n_occ + t] + -8 * g[j, n_occ + s, n_occ + s, n_occ + t] + 4 * g[j, n_occ + t, n_occ + s, n_occ + s] + -4 * g[i, i, j, n_occ + t] + 8 * g[i, j, i, n_occ + t] ) * K[0, (i*n_virt + t) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, j*n_virt + s]

												elif ((t != s) and (v == t) and (u == t) and (w == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[j, n_occ + t, n_occ + s, n_occ + t] ) * K[0, (i*n_virt + t) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, j*n_virt + t]

												elif ((t != s) and (v == t) and (u == t) and (w != s) and (w != t) and (w != u) and (w != v)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[j, n_occ + t, n_occ + s, n_occ + w] + -8 * g[j, n_occ + w, n_occ + s, n_occ + t] ) * K[0, (i*n_virt + t) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, j*n_virt + w]

												elif ((t != s) and (v != s) and (v != t) and (v != u) and (u == t) and (w == s)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * F[j, n_occ + v] + -8 * g[j, n_occ + s, n_occ + s, n_occ + v] + 4 * g[j, n_occ + v, n_occ + s, n_occ + s] + -4 * g[i, i, j, n_occ + v] + 8 * g[i, j, i, n_occ + v] ) * K[0, (i*n_virt + v) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, j*n_virt + s]

												elif ((t != s) and (v != s) and (v != t) and (v != u) and (u == t) and (w == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-8 * g[j, n_occ + t, n_occ + s, n_occ + v] + 4 * g[j, n_occ + v, n_occ + s, n_occ + t] ) * K[0, (i*n_virt + v) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, j*n_virt + t]

												elif ((t != s) and (v != s) and (v != t) and (v != u) and (u == t) and (w == v)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[j, n_occ + v, n_occ + s, n_occ + v] ) * K[0, (i*n_virt + v) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, j*n_virt + v]

												elif ((t != s) and (v != s) and (v != t) and (v != u) and (u == t) and (w != s) and (w != t) and (w != u) and (w != v)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[j, n_occ + v, n_occ + s, n_occ + w] + -8 * g[j, n_occ + w, n_occ + s, n_occ + v] ) * K[0, (i*n_virt + v) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, j*n_virt + w]

												elif ((t != s) and (v == s) and (u != s) and (u != t) and (w == s)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[j, n_occ + s, n_occ + t, n_occ + u] + 4 * g[j, n_occ + t, n_occ + s, n_occ + u] ) * K[0, (i*n_virt + s) * n_ex + j*n_virt + u+ 2*n_ex] * K[1, j*n_virt + s]

												elif ((t != s) and (v == s) and (u != s) and (u != t) and (w == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (8 * g[j, n_occ + t, n_occ + t, n_occ + u] ) * K[0, (i*n_virt + s) * n_ex + j*n_virt + u+ 2*n_ex] * K[1, j*n_virt + t]

												elif ((t != s) and (v == s) and (u != s) and (u != t) and (w == u)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[j, j, j, n_occ + t] + 4 * g[j, n_occ + u, n_occ + t, n_occ + u] + 4 * g[j, n_occ + t, n_occ + u, n_occ + u] ) * K[0, (i*n_virt + s) * n_ex + j*n_virt + u+ 2*n_ex] * K[1, j*n_virt + u]

												elif ((t != s) and (v == s) and (u != s) and (u != t) and (w != s) and (w != t) and (w != u) and (w != v)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[j, n_occ + w, n_occ + t, n_occ + u] + 4 * g[j, n_occ + t, n_occ + u, n_occ + w] ) * K[0, (i*n_virt + s) * n_ex + j*n_virt + u+ 2*n_ex] * K[1, j*n_virt + w]

											elif ((j != i) and (m == i) and (k == j) and (n != i) and (n != j) and (n != k) and (n != m)):

												if ((t == s) and (v == s) and (u == s) and (w == s)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * F[n, n_occ + s] + -4 * g[j, n, j, n_occ + s] + 4 * g[i, i, n, n_occ + s] + -4 * g[j, j, n, n_occ + s] + 4 * g[i, n, i, n_occ + s] ) * K[0, (i*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, n*n_virt + s]

												elif ((t == s) and (v == s) and (u == s) and (w != s) and (w != t) and (w != u) and (w != v)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, n, i, n_occ + w] + 8 * g[i, i, n, n_occ + w] + 4 * g[j, n, j, n_occ + w] + -8 * g[j, j, n, n_occ + w] ) * K[0, (i*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, n*n_virt + w]

												elif ((t == s) and (v != s) and (v != t) and (v != u) and (u == s) and (w == s)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * F[n, n_occ + v] + -8 * g[n, n_occ + s, n_occ + s, n_occ + v] + 4 * g[n, n_occ + v, n_occ + s, n_occ + s] + -4 * g[i, i, n, n_occ + v] + 8 * g[i, n, i, n_occ + v] ) * K[0, (i*n_virt + v) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, n*n_virt + s]

												elif ((t == s) and (v != s) and (v != t) and (v != u) and (u == s) and (w == v)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[n, n_occ + v, n_occ + s, n_occ + v] ) * K[0, (i*n_virt + v) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, n*n_virt + v]

												elif ((t == s) and (v != s) and (v != t) and (v != u) and (u == s) and (w != s) and (w != t) and (w != u) and (w != v)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[n, n_occ + v, n_occ + s, n_occ + w] + -8 * g[n, n_occ + w, n_occ + s, n_occ + v] ) * K[0, (i*n_virt + v) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, n*n_virt + w]

												elif ((t == s) and (v == s) and (u != s) and (u != t) and (w == s)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[n, n_occ + s, n_occ + s, n_occ + u] ) * K[0, (i*n_virt + s) * n_ex + j*n_virt + u+ 2*n_ex] * K[1, n*n_virt + s]

												elif ((t == s) and (v == s) and (u != s) and (u != t) and (w == u)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-8 * g[j, n, j, n_occ + s] + 4 * g[j, j, n, n_occ + s] + 8 * g[n, n_occ + u, n_occ + s, n_occ + u] + -4 * g[n, n_occ + s, n_occ + u, n_occ + u] ) * K[0, (i*n_virt + s) * n_ex + j*n_virt + u+ 2*n_ex] * K[1, n*n_virt + u]

												elif ((t == s) and (v == s) and (u != s) and (u != t) and (w != s) and (w != t) and (w != u) and (w != v)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[n, n_occ + s, n_occ + u, n_occ + w] + 8 * g[n, n_occ + w, n_occ + s, n_occ + u] ) * K[0, (i*n_virt + s) * n_ex + j*n_virt + u+ 2*n_ex] * K[1, n*n_virt + w]

												elif ((t != s) and (v == s) and (u == s) and (w == s)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-8 * g[j, n, j, n_occ + t] + 4 * g[j, j, n, n_occ + t] + 8 * g[n, n_occ + s, n_occ + s, n_occ + t] + -4 * g[n, n_occ + t, n_occ + s, n_occ + s] ) * K[0, (i*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, n*n_virt + s]

												elif ((t != s) and (v == s) and (u == s) and (w == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[n, n_occ + t, n_occ + s, n_occ + t] ) * K[0, (i*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, n*n_virt + t]

												elif ((t != s) and (v == s) and (u == s) and (w != s) and (w != t) and (w != u) and (w != v)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[n, n_occ + t, n_occ + s, n_occ + w] + 8 * g[n, n_occ + w, n_occ + s, n_occ + t] ) * K[0, (i*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, n*n_virt + w]

												elif ((t != s) and (v == s) and (u == t) and (w == s)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * F[n, n_occ + s] + -4 * g[n, n_occ + t, n_occ + s, n_occ + t] + 4 * g[i, i, n, n_occ + s] + 8 * g[n, n_occ + s, n_occ + t, n_occ + t] + -4 * g[n, n_occ + s, n_occ + s, n_occ + s] + 4 * g[i, n, i, n_occ + s] + -8 * g[j, j, n, n_occ + s] + 4 * g[j, n, j, n_occ + s] ) * K[0, (i*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, n*n_virt + s]

												elif ((t != s) and (v == s) and (u == t) and (w == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, n, i, n_occ + t] + -4 * g[j, n, j, n_occ + t] + 8 * g[i, i, n, n_occ + t] + 4 * g[n, n_occ + t, n_occ + t, n_occ + t] + 4 * g[n, n_occ + s, n_occ + s, n_occ + t] + -8 * g[n, n_occ + t, n_occ + s, n_occ + s] + -4 * g[j, j, n, n_occ + t] ) * K[0, (i*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, n*n_virt + t]

												elif ((t != s) and (v == s) and (u == t) and (w != s) and (w != t) and (w != u) and (w != v)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, n, i, n_occ + w] + -4 * g[n, n_occ + t, n_occ + t, n_occ + w] + 8 * g[i, i, n, n_occ + w] + 8 * g[n, n_occ + w, n_occ + t, n_occ + t] + 4 * g[n, n_occ + s, n_occ + s, n_occ + w] + -8 * g[n, n_occ + w, n_occ + s, n_occ + s] + 4 * g[j, n, j, n_occ + w] + -8 * g[j, j, n, n_occ + w] ) * K[0, (i*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, n*n_virt + w]

												elif ((t != s) and (v == t) and (u == t) and (w == s)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * F[n, n_occ + t] + -8 * g[n, n_occ + s, n_occ + s, n_occ + t] + 4 * g[n, n_occ + t, n_occ + s, n_occ + s] + -4 * g[i, i, n, n_occ + t] + 8 * g[i, n, i, n_occ + t] ) * K[0, (i*n_virt + t) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, n*n_virt + s]

												elif ((t != s) and (v == t) and (u == t) and (w == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[n, n_occ + t, n_occ + s, n_occ + t] ) * K[0, (i*n_virt + t) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, n*n_virt + t]

												elif ((t != s) and (v == t) and (u == t) and (w != s) and (w != t) and (w != u) and (w != v)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[n, n_occ + t, n_occ + s, n_occ + w] + -8 * g[n, n_occ + w, n_occ + s, n_occ + t] ) * K[0, (i*n_virt + t) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, n*n_virt + w]

												elif ((t != s) and (v != s) and (v != t) and (v != u) and (u == t) and (w == s)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * F[n, n_occ + v] + -8 * g[n, n_occ + s, n_occ + s, n_occ + v] + 4 * g[n, n_occ + v, n_occ + s, n_occ + s] + -4 * g[i, i, n, n_occ + v] + 8 * g[i, n, i, n_occ + v] ) * K[0, (i*n_virt + v) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, n*n_virt + s]

												elif ((t != s) and (v != s) and (v != t) and (v != u) and (u == t) and (w == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-8 * g[n, n_occ + t, n_occ + s, n_occ + v] + 4 * g[n, n_occ + v, n_occ + s, n_occ + t] ) * K[0, (i*n_virt + v) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, n*n_virt + t]

												elif ((t != s) and (v != s) and (v != t) and (v != u) and (u == t) and (w == v)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[n, n_occ + v, n_occ + s, n_occ + v] ) * K[0, (i*n_virt + v) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, n*n_virt + v]

												elif ((t != s) and (v != s) and (v != t) and (v != u) and (u == t) and (w != s) and (w != t) and (w != u) and (w != v)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[n, n_occ + v, n_occ + s, n_occ + w] + -8 * g[n, n_occ + w, n_occ + s, n_occ + v] ) * K[0, (i*n_virt + v) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, n*n_virt + w]

												elif ((t != s) and (v == s) and (u != s) and (u != t) and (w == s)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (8 * g[n, n_occ + s, n_occ + t, n_occ + u] + -4 * g[n, n_occ + t, n_occ + s, n_occ + u] ) * K[0, (i*n_virt + s) * n_ex + j*n_virt + u+ 2*n_ex] * K[1, n*n_virt + s]

												elif ((t != s) and (v == s) and (u != s) and (u != t) and (w == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[n, n_occ + t, n_occ + t, n_occ + u] ) * K[0, (i*n_virt + s) * n_ex + j*n_virt + u+ 2*n_ex] * K[1, n*n_virt + t]

												elif ((t != s) and (v == s) and (u != s) and (u != t) and (w == u)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-8 * g[j, n, j, n_occ + t] + 4 * g[j, j, n, n_occ + t] + 8 * g[n, n_occ + u, n_occ + t, n_occ + u] + -4 * g[n, n_occ + t, n_occ + u, n_occ + u] ) * K[0, (i*n_virt + s) * n_ex + j*n_virt + u+ 2*n_ex] * K[1, n*n_virt + u]

												elif ((t != s) and (v == s) and (u != s) and (u != t) and (w != s) and (w != t) and (w != u) and (w != v)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[n, n_occ + t, n_occ + u, n_occ + w] + 8 * g[n, n_occ + w, n_occ + t, n_occ + u] ) * K[0, (i*n_virt + s) * n_ex + j*n_virt + u+ 2*n_ex] * K[1, n*n_virt + w]

											elif ((j != i) and (m == j) and (k == j) and (n == i)):

												if ((t == s) and (v == s) and (u == s) and (w == s)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * F[j, n_occ + s] + 4 * g[i, i, j, n_occ + s] + -4 * g[j, n_occ + s, n_occ + s, n_occ + s] + 4 * g[i, j, i, n_occ + s] ) * K[0, (j*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, i*n_virt + s]

												elif ((t == s) and (v == s) and (u == s) and (w != s) and (w != t) and (w != u) and (w != v)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * F[j, n_occ + w] + -8 * g[j, n_occ + s, n_occ + s, n_occ + w] + 4 * g[j, n_occ + w, n_occ + s, n_occ + s] + -4 * g[i, i, j, n_occ + w] + 8 * g[i, j, i, n_occ + w] ) * K[0, (j*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, i*n_virt + w]

												elif ((t == s) and (v != s) and (v != t) and (v != u) and (u == s) and (w == s)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, j, i, n_occ + v] + 8 * g[i, i, j, n_occ + v] + 4 * g[j, n_occ + s, n_occ + s, n_occ + v] + -8 * g[j, n_occ + v, n_occ + s, n_occ + s] ) * K[0, (j*n_virt + v) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, i*n_virt + s]

												elif ((t == s) and (v != s) and (v != t) and (v != u) and (u == s) and (w == v)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[j, n_occ + v, n_occ + s, n_occ + v] ) * K[0, (j*n_virt + v) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, i*n_virt + v]

												elif ((t == s) and (v != s) and (v != t) and (v != u) and (u == s) and (w != s) and (w != t) and (w != u) and (w != v)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-8 * g[j, n_occ + v, n_occ + s, n_occ + w] + 4 * g[j, n_occ + w, n_occ + s, n_occ + v] ) * K[0, (j*n_virt + v) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, i*n_virt + w]

												elif ((t != s) and (v == s) and (u == t) and (w == s)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * F[j, n_occ + s] + 4 * g[i, i, j, n_occ + s] + -4 * g[j, n_occ + s, n_occ + s, n_occ + s] + 4 * g[i, j, i, n_occ + s] ) * K[0, (j*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, i*n_virt + s]

												elif ((t != s) and (v == s) and (u == t) and (w == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * F[j, n_occ + t] + -8 * g[j, n_occ + s, n_occ + s, n_occ + t] + 4 * g[j, n_occ + t, n_occ + s, n_occ + s] + -4 * g[i, i, j, n_occ + t] + 8 * g[i, j, i, n_occ + t] ) * K[0, (j*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, i*n_virt + t]

												elif ((t != s) and (v == s) and (u == t) and (w != s) and (w != t) and (w != u) and (w != v)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * F[j, n_occ + w] + -8 * g[j, n_occ + s, n_occ + s, n_occ + w] + 4 * g[j, n_occ + w, n_occ + s, n_occ + s] + -4 * g[i, i, j, n_occ + w] + 8 * g[i, j, i, n_occ + w] ) * K[0, (j*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, i*n_virt + w]

												elif ((t != s) and (v == t) and (u == t) and (w == s)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, j, i, n_occ + t] + 8 * g[i, i, j, n_occ + t] + 4 * g[j, n_occ + s, n_occ + s, n_occ + t] + -8 * g[j, n_occ + t, n_occ + s, n_occ + s] ) * K[0, (j*n_virt + t) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, i*n_virt + s]

												elif ((t != s) and (v == t) and (u == t) and (w == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[j, n_occ + t, n_occ + s, n_occ + t] ) * K[0, (j*n_virt + t) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, i*n_virt + t]

												elif ((t != s) and (v == t) and (u == t) and (w != s) and (w != t) and (w != u) and (w != v)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-8 * g[j, n_occ + t, n_occ + s, n_occ + w] + 4 * g[j, n_occ + w, n_occ + s, n_occ + t] ) * K[0, (j*n_virt + t) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, i*n_virt + w]

												elif ((t != s) and (v != s) and (v != t) and (v != u) and (u == t) and (w == s)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, j, i, n_occ + v] + 8 * g[i, i, j, n_occ + v] + 4 * g[j, n_occ + s, n_occ + s, n_occ + v] + -8 * g[j, n_occ + v, n_occ + s, n_occ + s] ) * K[0, (j*n_virt + v) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, i*n_virt + s]

												elif ((t != s) and (v != s) and (v != t) and (v != u) and (u == t) and (w == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[j, n_occ + t, n_occ + s, n_occ + v] + -8 * g[j, n_occ + v, n_occ + s, n_occ + t] ) * K[0, (j*n_virt + v) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, i*n_virt + t]

												elif ((t != s) and (v != s) and (v != t) and (v != u) and (u == t) and (w == v)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[j, n_occ + v, n_occ + s, n_occ + v] ) * K[0, (j*n_virt + v) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, i*n_virt + v]

												elif ((t != s) and (v != s) and (v != t) and (v != u) and (u == t) and (w != s) and (w != t) and (w != u) and (w != v)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-8 * g[j, n_occ + v, n_occ + s, n_occ + w] + 4 * g[j, n_occ + w, n_occ + s, n_occ + v] ) * K[0, (j*n_virt + v) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, i*n_virt + w]

											elif ((j != i) and (m == j) and (k == j) and (n == j)):

												if ((t == s) and (v == s) and (u == s) and (w == s)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (8 * g[i, j, j, n_occ + s] ) * K[0, (j*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, j*n_virt + s]

												elif ((t == s) and (v == s) and (u == s) and (w != s) and (w != t) and (w != u) and (w != v)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, j, j, n_occ + w] ) * K[0, (j*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, j*n_virt + w]

												elif ((t == s) and (v != s) and (v != t) and (v != u) and (u == s) and (w == s)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, j, j, n_occ + v] ) * K[0, (j*n_virt + v) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, j*n_virt + s]

												elif ((t != s) and (v == s) and (u == t) and (w == s)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (8 * g[i, j, j, n_occ + s] ) * K[0, (j*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, j*n_virt + s]

												elif ((t != s) and (v == s) and (u == t) and (w == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, j, j, n_occ + t] ) * K[0, (j*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, j*n_virt + t]

												elif ((t != s) and (v == s) and (u == t) and (w != s) and (w != t) and (w != u) and (w != v)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, j, j, n_occ + w] ) * K[0, (j*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, j*n_virt + w]

												elif ((t != s) and (v == t) and (u == t) and (w == s)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, j, j, n_occ + t] ) * K[0, (j*n_virt + t) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, j*n_virt + s]

												elif ((t != s) and (v != s) and (v != t) and (v != u) and (u == t) and (w == s)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, j, j, n_occ + v] ) * K[0, (j*n_virt + v) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, j*n_virt + s]

											elif ((j != i) and (m == j) and (k == j) and (n != i) and (n != j) and (n != k) and (n != m)):

												if ((t == s) and (v == s) and (u == s) and (w == s)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, n, j, n_occ + s] + 4 * g[i, j, n, n_occ + s] ) * K[0, (j*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, n*n_virt + s]

												elif ((t == s) and (v == s) and (u == s) and (w != s) and (w != t) and (w != u) and (w != v)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (8 * g[i, j, n, n_occ + w] + -4 * g[i, n, j, n_occ + w] ) * K[0, (j*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, n*n_virt + w]

												elif ((t == s) and (v != s) and (v != t) and (v != u) and (u == s) and (w == s)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, j, n, n_occ + v] + 8 * g[i, n, j, n_occ + v] ) * K[0, (j*n_virt + v) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, n*n_virt + s]

												elif ((t != s) and (v == s) and (u == t) and (w == s)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, n, j, n_occ + s] + 4 * g[i, j, n, n_occ + s] ) * K[0, (j*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, n*n_virt + s]

												elif ((t != s) and (v == s) and (u == t) and (w == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (8 * g[i, j, n, n_occ + t] + -4 * g[i, n, j, n_occ + t] ) * K[0, (j*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, n*n_virt + t]

												elif ((t != s) and (v == s) and (u == t) and (w != s) and (w != t) and (w != u) and (w != v)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (8 * g[i, j, n, n_occ + w] + -4 * g[i, n, j, n_occ + w] ) * K[0, (j*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, n*n_virt + w]

												elif ((t != s) and (v == t) and (u == t) and (w == s)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, j, n, n_occ + t] + 8 * g[i, n, j, n_occ + t] ) * K[0, (j*n_virt + t) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, n*n_virt + s]

												elif ((t != s) and (v != s) and (v != t) and (v != u) and (u == t) and (w == s)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, j, n, n_occ + v] + 8 * g[i, n, j, n_occ + v] ) * K[0, (j*n_virt + v) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, n*n_virt + s]

											elif ((j != i) and (m != i) and (m != j) and (m != k) and (k == j) and (n == i)):

												if ((t == s) and (v == s) and (u == s) and (w == s)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * F[m, n_occ + s] + 4 * g[i, i, m, n_occ + s] + -4 * g[m, n_occ + s, n_occ + s, n_occ + s] + 4 * g[i, m, i, n_occ + s] ) * K[0, (m*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, i*n_virt + s]

												elif ((t == s) and (v == s) and (u == s) and (w != s) and (w != t) and (w != u) and (w != v)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * F[m, n_occ + w] + -8 * g[m, n_occ + s, n_occ + s, n_occ + w] + 4 * g[m, n_occ + w, n_occ + s, n_occ + s] + -4 * g[i, i, m, n_occ + w] + 8 * g[i, m, i, n_occ + w] ) * K[0, (m*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, i*n_virt + w]

												elif ((t == s) and (v != s) and (v != t) and (v != u) and (u == s) and (w == s)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, m, i, n_occ + v] + 8 * g[i, i, m, n_occ + v] + 4 * g[m, n_occ + s, n_occ + s, n_occ + v] + -8 * g[m, n_occ + v, n_occ + s, n_occ + s] ) * K[0, (m*n_virt + v) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, i*n_virt + s]

												elif ((t == s) and (v != s) and (v != t) and (v != u) and (u == s) and (w == v)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[m, n_occ + v, n_occ + s, n_occ + v] ) * K[0, (m*n_virt + v) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, i*n_virt + v]

												elif ((t == s) and (v != s) and (v != t) and (v != u) and (u == s) and (w != s) and (w != t) and (w != u) and (w != v)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-8 * g[m, n_occ + v, n_occ + s, n_occ + w] + 4 * g[m, n_occ + w, n_occ + s, n_occ + v] ) * K[0, (m*n_virt + v) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, i*n_virt + w]

												elif ((t != s) and (v == s) and (u == t) and (w == s)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * F[m, n_occ + s] + 4 * g[i, i, m, n_occ + s] + -4 * g[m, n_occ + s, n_occ + s, n_occ + s] + 4 * g[i, m, i, n_occ + s] ) * K[0, (m*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, i*n_virt + s]

												elif ((t != s) and (v == s) and (u == t) and (w == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * F[m, n_occ + t] + -8 * g[m, n_occ + s, n_occ + s, n_occ + t] + 4 * g[m, n_occ + t, n_occ + s, n_occ + s] + -4 * g[i, i, m, n_occ + t] + 8 * g[i, m, i, n_occ + t] ) * K[0, (m*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, i*n_virt + t]

												elif ((t != s) and (v == s) and (u == t) and (w != s) and (w != t) and (w != u) and (w != v)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * F[m, n_occ + w] + -8 * g[m, n_occ + s, n_occ + s, n_occ + w] + 4 * g[m, n_occ + w, n_occ + s, n_occ + s] + -4 * g[i, i, m, n_occ + w] + 8 * g[i, m, i, n_occ + w] ) * K[0, (m*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, i*n_virt + w]

												elif ((t != s) and (v == t) and (u == t) and (w == s)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, m, i, n_occ + t] + 8 * g[i, i, m, n_occ + t] + 4 * g[m, n_occ + s, n_occ + s, n_occ + t] + -8 * g[m, n_occ + t, n_occ + s, n_occ + s] ) * K[0, (m*n_virt + t) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, i*n_virt + s]

												elif ((t != s) and (v == t) and (u == t) and (w == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[m, n_occ + t, n_occ + s, n_occ + t] ) * K[0, (m*n_virt + t) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, i*n_virt + t]

												elif ((t != s) and (v == t) and (u == t) and (w != s) and (w != t) and (w != u) and (w != v)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-8 * g[m, n_occ + t, n_occ + s, n_occ + w] + 4 * g[m, n_occ + w, n_occ + s, n_occ + t] ) * K[0, (m*n_virt + t) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, i*n_virt + w]

												elif ((t != s) and (v != s) and (v != t) and (v != u) and (u == t) and (w == s)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, m, i, n_occ + v] + 8 * g[i, i, m, n_occ + v] + 4 * g[m, n_occ + s, n_occ + s, n_occ + v] + -8 * g[m, n_occ + v, n_occ + s, n_occ + s] ) * K[0, (m*n_virt + v) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, i*n_virt + s]

												elif ((t != s) and (v != s) and (v != t) and (v != u) and (u == t) and (w == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[m, n_occ + t, n_occ + s, n_occ + v] + -8 * g[m, n_occ + v, n_occ + s, n_occ + t] ) * K[0, (m*n_virt + v) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, i*n_virt + t]

												elif ((t != s) and (v != s) and (v != t) and (v != u) and (u == t) and (w == v)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[m, n_occ + v, n_occ + s, n_occ + v] ) * K[0, (m*n_virt + v) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, i*n_virt + v]

												elif ((t != s) and (v != s) and (v != t) and (v != u) and (u == t) and (w != s) and (w != t) and (w != u) and (w != v)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-8 * g[m, n_occ + v, n_occ + s, n_occ + w] + 4 * g[m, n_occ + w, n_occ + s, n_occ + v] ) * K[0, (m*n_virt + v) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, i*n_virt + w]

											elif ((j != i) and (m != i) and (m != j) and (m != k) and (k == j) and (n == j)):

												if ((t == s) and (v == s) and (u == s) and (w == s)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, j, m, n_occ + s] + 4 * g[i, m, j, n_occ + s] ) * K[0, (m*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, j*n_virt + s]

												elif ((t == s) and (v == s) and (u == s) and (w != s) and (w != t) and (w != u) and (w != v)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, j, m, n_occ + w] + 8 * g[i, m, j, n_occ + w] ) * K[0, (m*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, j*n_virt + w]

												elif ((t == s) and (v != s) and (v != t) and (v != u) and (u == s) and (w == s)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (8 * g[i, j, m, n_occ + v] + -4 * g[i, m, j, n_occ + v] ) * K[0, (m*n_virt + v) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, j*n_virt + s]

												elif ((t != s) and (v == s) and (u == t) and (w == s)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, j, m, n_occ + s] + 4 * g[i, m, j, n_occ + s] ) * K[0, (m*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, j*n_virt + s]

												elif ((t != s) and (v == s) and (u == t) and (w == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, j, m, n_occ + t] + 8 * g[i, m, j, n_occ + t] ) * K[0, (m*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, j*n_virt + t]

												elif ((t != s) and (v == s) and (u == t) and (w != s) and (w != t) and (w != u) and (w != v)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, j, m, n_occ + w] + 8 * g[i, m, j, n_occ + w] ) * K[0, (m*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, j*n_virt + w]

												elif ((t != s) and (v == t) and (u == t) and (w == s)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (8 * g[i, j, m, n_occ + t] + -4 * g[i, m, j, n_occ + t] ) * K[0, (m*n_virt + t) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, j*n_virt + s]

												elif ((t != s) and (v != s) and (v != t) and (v != u) and (u == t) and (w == s)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (8 * g[i, j, m, n_occ + v] + -4 * g[i, m, j, n_occ + v] ) * K[0, (m*n_virt + v) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, j*n_virt + s]

											elif ((j != i) and (m != i) and (m != j) and (m != k) and (k == j) and (n == m)):

												if ((t == s) and (v == s) and (u == s) and (w == s)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (8 * g[i, m, m, n_occ + s] ) * K[0, (m*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, m*n_virt + s]

												elif ((t == s) and (v == s) and (u == s) and (w != s) and (w != t) and (w != u) and (w != v)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, m, m, n_occ + w] ) * K[0, (m*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, m*n_virt + w]

												elif ((t == s) and (v != s) and (v != t) and (v != u) and (u == s) and (w == s)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, m, m, n_occ + v] ) * K[0, (m*n_virt + v) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, m*n_virt + s]

												elif ((t != s) and (v == s) and (u == t) and (w == s)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (8 * g[i, m, m, n_occ + s] ) * K[0, (m*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, m*n_virt + s]

												elif ((t != s) and (v == s) and (u == t) and (w == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, m, m, n_occ + t] ) * K[0, (m*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, m*n_virt + t]

												elif ((t != s) and (v == s) and (u == t) and (w != s) and (w != t) and (w != u) and (w != v)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, m, m, n_occ + w] ) * K[0, (m*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, m*n_virt + w]

												elif ((t != s) and (v == t) and (u == t) and (w == s)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, m, m, n_occ + t] ) * K[0, (m*n_virt + t) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, m*n_virt + s]

												elif ((t != s) and (v != s) and (v != t) and (v != u) and (u == t) and (w == s)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, m, m, n_occ + v] ) * K[0, (m*n_virt + v) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, m*n_virt + s]

											elif ((j != i) and (m != i) and (m != j) and (m != k) and (k == j) and (n != i) and (n != j) and (n != k) and (n != m)):

												if ((t == s) and (v == s) and (u == s) and (w == s)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, n, m, n_occ + s] + 4 * g[i, m, n, n_occ + s] ) * K[0, (m*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, n*n_virt + s]

												elif ((t == s) and (v == s) and (u == s) and (w != s) and (w != t) and (w != u) and (w != v)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (8 * g[i, m, n, n_occ + w] + -4 * g[i, n, m, n_occ + w] ) * K[0, (m*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, n*n_virt + w]

												elif ((t == s) and (v != s) and (v != t) and (v != u) and (u == s) and (w == s)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, m, n, n_occ + v] + 8 * g[i, n, m, n_occ + v] ) * K[0, (m*n_virt + v) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, n*n_virt + s]

												elif ((t != s) and (v == s) and (u == t) and (w == s)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, n, m, n_occ + s] + 4 * g[i, m, n, n_occ + s] ) * K[0, (m*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, n*n_virt + s]

												elif ((t != s) and (v == s) and (u == t) and (w == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (8 * g[i, m, n, n_occ + t] + -4 * g[i, n, m, n_occ + t] ) * K[0, (m*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, n*n_virt + t]

												elif ((t != s) and (v == s) and (u == t) and (w != s) and (w != t) and (w != u) and (w != v)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (8 * g[i, m, n, n_occ + w] + -4 * g[i, n, m, n_occ + w] ) * K[0, (m*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, n*n_virt + w]

												elif ((t != s) and (v == t) and (u == t) and (w == s)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, m, n, n_occ + t] + 8 * g[i, n, m, n_occ + t] ) * K[0, (m*n_virt + t) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, n*n_virt + s]

												elif ((t != s) and (v != s) and (v != t) and (v != u) and (u == t) and (w == s)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, m, n, n_occ + v] + 8 * g[i, n, m, n_occ + v] ) * K[0, (m*n_virt + v) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, n*n_virt + s]

											elif ((j != i) and (m == i) and (k != i) and (k != j) and (n == i)):

												if ((t == s) and (v == s) and (u == s) and (w == s)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, n_occ + s, j, k] + -4 * g[i, k, j, n_occ + s] ) * K[0, (i*n_virt + s) * n_ex + k*n_virt + s+ 2*n_ex] * K[1, i*n_virt + s]

												elif ((t == s) and (v == s) and (u == s) and (w != s) and (w != t) and (w != u) and (w != v)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, k, j, n_occ + w] + -8 * g[i, n_occ + w, j, k] ) * K[0, (i*n_virt + s) * n_ex + k*n_virt + s+ 2*n_ex] * K[1, i*n_virt + w]

												elif ((t == s) and (v == s) and (u != s) and (u != t) and (w == u)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-8 * g[i, k, j, n_occ + s] + 4 * g[i, n_occ + s, j, k] ) * K[0, (i*n_virt + s) * n_ex + k*n_virt + u+ 2*n_ex] * K[1, i*n_virt + u]

												elif ((t != s) and (v == s) and (u == s) and (w == s)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-8 * g[i, k, j, n_occ + t] + 4 * g[i, n_occ + t, j, k] ) * K[0, (i*n_virt + s) * n_ex + k*n_virt + s+ 2*n_ex] * K[1, i*n_virt + s]

												elif ((t != s) and (v == s) and (u == t) and (w == s)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, k, j, n_occ + s] + -8 * g[i, n_occ + s, j, k] ) * K[0, (i*n_virt + s) * n_ex + k*n_virt + t+ 2*n_ex] * K[1, i*n_virt + s]

												elif ((t != s) and (v == s) and (u == t) and (w == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, n_occ + t, j, k] + -4 * g[i, k, j, n_occ + t] ) * K[0, (i*n_virt + s) * n_ex + k*n_virt + t+ 2*n_ex] * K[1, i*n_virt + t]

												elif ((t != s) and (v == s) and (u == t) and (w != s) and (w != t) and (w != u) and (w != v)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, k, j, n_occ + w] + -8 * g[i, n_occ + w, j, k] ) * K[0, (i*n_virt + s) * n_ex + k*n_virt + t+ 2*n_ex] * K[1, i*n_virt + w]

												elif ((t != s) and (v == s) and (u != s) and (u != t) and (w == u)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-8 * g[i, k, j, n_occ + t] + 4 * g[i, n_occ + t, j, k] ) * K[0, (i*n_virt + s) * n_ex + k*n_virt + u+ 2*n_ex] * K[1, i*n_virt + u]

											elif ((j != i) and (m == i) and (k != i) and (k != j) and (n == j)):

												if ((t == s) and (v == s) and (u == s) and (w == s)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-8 * g[j, k, j, n_occ + s] ) * K[0, (i*n_virt + s) * n_ex + k*n_virt + s+ 2*n_ex] * K[1, j*n_virt + s]

												elif ((t == s) and (v == s) and (u == s) and (w != s) and (w != t) and (w != u) and (w != v)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[j, k, j, n_occ + w] ) * K[0, (i*n_virt + s) * n_ex + k*n_virt + s+ 2*n_ex] * K[1, j*n_virt + w]

												elif ((t == s) and (v == s) and (u != s) and (u != t) and (w == u)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[j, k, j, n_occ + s] ) * K[0, (i*n_virt + s) * n_ex + k*n_virt + u+ 2*n_ex] * K[1, j*n_virt + u]

												elif ((t != s) and (v == s) and (u == s) and (w == s)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[j, k, j, n_occ + t] ) * K[0, (i*n_virt + s) * n_ex + k*n_virt + s+ 2*n_ex] * K[1, j*n_virt + s]

												elif ((t != s) and (v == s) and (u == t) and (w == s)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[j, k, j, n_occ + s] ) * K[0, (i*n_virt + s) * n_ex + k*n_virt + t+ 2*n_ex] * K[1, j*n_virt + s]

												elif ((t != s) and (v == s) and (u == t) and (w == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-8 * g[j, k, j, n_occ + t] ) * K[0, (i*n_virt + s) * n_ex + k*n_virt + t+ 2*n_ex] * K[1, j*n_virt + t]

												elif ((t != s) and (v == s) and (u == t) and (w != s) and (w != t) and (w != u) and (w != v)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[j, k, j, n_occ + w] ) * K[0, (i*n_virt + s) * n_ex + k*n_virt + t+ 2*n_ex] * K[1, j*n_virt + w]

												elif ((t != s) and (v == s) and (u != s) and (u != t) and (w == u)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[j, k, j, n_occ + t] ) * K[0, (i*n_virt + s) * n_ex + k*n_virt + u+ 2*n_ex] * K[1, j*n_virt + u]

											elif ((j != i) and (m == i) and (k != i) and (k != j) and (n == k)):

												if ((t == s) and (v == s) and (u == s) and (w == s)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[j, n_occ + s, k, k] + 4 * g[j, n_occ + s, n_occ + s, n_occ + s] + -4 * g[j, k, k, n_occ + s] ) * K[0, (i*n_virt + s) * n_ex + k*n_virt + s+ 2*n_ex] * K[1, k*n_virt + s]

												elif ((t == s) and (v == s) and (u == s) and (w != s) and (w != t) and (w != u) and (w != v)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-8 * g[j, k, k, n_occ + w] + 4 * g[j, n_occ + w, k, k] + 8 * g[j, n_occ + s, n_occ + s, n_occ + w] + -4 * g[j, n_occ + w, n_occ + s, n_occ + s] ) * K[0, (i*n_virt + s) * n_ex + k*n_virt + s+ 2*n_ex] * K[1, k*n_virt + w]

												elif ((t == s) and (v == s) and (u != s) and (u != t) and (w == s)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[j, n_occ + s, n_occ + s, n_occ + u] ) * K[0, (i*n_virt + s) * n_ex + k*n_virt + u+ 2*n_ex] * K[1, k*n_virt + s]

												elif ((t == s) and (v == s) and (u != s) and (u != t) and (w == u)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[j, k, k, n_occ + s] + -8 * g[j, n_occ + s, k, k] + -4 * g[j, n_occ + u, n_occ + s, n_occ + u] + 8 * g[j, n_occ + s, n_occ + u, n_occ + u] ) * K[0, (i*n_virt + s) * n_ex + k*n_virt + u+ 2*n_ex] * K[1, k*n_virt + u]

												elif ((t == s) and (v == s) and (u != s) and (u != t) and (w != s) and (w != t) and (w != u) and (w != v)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (8 * g[j, n_occ + s, n_occ + u, n_occ + w] + -4 * g[j, n_occ + w, n_occ + s, n_occ + u] ) * K[0, (i*n_virt + s) * n_ex + k*n_virt + u+ 2*n_ex] * K[1, k*n_virt + w]

												elif ((t != s) and (v == s) and (u == s) and (w == s)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[j, k, k, n_occ + t] + -8 * g[j, n_occ + t, k, k] + -4 * g[j, n_occ + s, n_occ + s, n_occ + t] + 8 * g[j, n_occ + t, n_occ + s, n_occ + s] ) * K[0, (i*n_virt + s) * n_ex + k*n_virt + s+ 2*n_ex] * K[1, k*n_virt + s]

												elif ((t != s) and (v == s) and (u == s) and (w == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[j, n_occ + t, n_occ + s, n_occ + t] ) * K[0, (i*n_virt + s) * n_ex + k*n_virt + s+ 2*n_ex] * K[1, k*n_virt + t]

												elif ((t != s) and (v == s) and (u == s) and (w != s) and (w != t) and (w != u) and (w != v)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (8 * g[j, n_occ + t, n_occ + s, n_occ + w] + -4 * g[j, n_occ + w, n_occ + s, n_occ + t] ) * K[0, (i*n_virt + s) * n_ex + k*n_virt + s+ 2*n_ex] * K[1, k*n_virt + w]

												elif ((t != s) and (v == s) and (u == t) and (w == s)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-8 * g[j, k, k, n_occ + s] + 4 * g[j, n_occ + s, k, k] + 8 * g[j, n_occ + t, n_occ + s, n_occ + t] + -4 * g[j, n_occ + s, n_occ + t, n_occ + t] ) * K[0, (i*n_virt + s) * n_ex + k*n_virt + t+ 2*n_ex] * K[1, k*n_virt + s]

												elif ((t != s) and (v == s) and (u == t) and (w == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[j, n_occ + t, k, k] + 4 * g[j, n_occ + t, n_occ + t, n_occ + t] + -4 * g[j, k, k, n_occ + t] ) * K[0, (i*n_virt + s) * n_ex + k*n_virt + t+ 2*n_ex] * K[1, k*n_virt + t]

												elif ((t != s) and (v == s) and (u == t) and (w != s) and (w != t) and (w != u) and (w != v)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-8 * g[j, k, k, n_occ + w] + 4 * g[j, n_occ + w, k, k] + 8 * g[j, n_occ + t, n_occ + t, n_occ + w] + -4 * g[j, n_occ + w, n_occ + t, n_occ + t] ) * K[0, (i*n_virt + s) * n_ex + k*n_virt + t+ 2*n_ex] * K[1, k*n_virt + w]

												elif ((t != s) and (v == s) and (u != s) and (u != t) and (w == s)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[j, n_occ + s, n_occ + t, n_occ + u] + 8 * g[j, n_occ + t, n_occ + s, n_occ + u] ) * K[0, (i*n_virt + s) * n_ex + k*n_virt + u+ 2*n_ex] * K[1, k*n_virt + s]

												elif ((t != s) and (v == s) and (u != s) and (u != t) and (w == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[j, n_occ + t, n_occ + t, n_occ + u] ) * K[0, (i*n_virt + s) * n_ex + k*n_virt + u+ 2*n_ex] * K[1, k*n_virt + t]

												elif ((t != s) and (v == s) and (u != s) and (u != t) and (w == u)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[j, k, k, n_occ + t] + -8 * g[j, n_occ + t, k, k] + -4 * g[j, n_occ + u, n_occ + t, n_occ + u] + 8 * g[j, n_occ + t, n_occ + u, n_occ + u] ) * K[0, (i*n_virt + s) * n_ex + k*n_virt + u+ 2*n_ex] * K[1, k*n_virt + u]

												elif ((t != s) and (v == s) and (u != s) and (u != t) and (w != s) and (w != t) and (w != u) and (w != v)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (8 * g[j, n_occ + t, n_occ + u, n_occ + w] + -4 * g[j, n_occ + w, n_occ + t, n_occ + u] ) * K[0, (i*n_virt + s) * n_ex + k*n_virt + u+ 2*n_ex] * K[1, k*n_virt + w]

											elif ((j != i) and (m == i) and (k != i) and (k != j) and (n != i) and (n != j) and (n != k) and (n != m)):

												if ((t == s) and (v == s) and (u == s) and (w == s)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[j, k, n, n_occ + s] + -4 * g[j, n_occ + s, k, n] ) * K[0, (i*n_virt + s) * n_ex + k*n_virt + s+ 2*n_ex] * K[1, n*n_virt + s]

												elif ((t == s) and (v == s) and (u == s) and (w != s) and (w != t) and (w != u) and (w != v)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-8 * g[j, k, n, n_occ + w] + 4 * g[j, n_occ + w, k, n] ) * K[0, (i*n_virt + s) * n_ex + k*n_virt + s+ 2*n_ex] * K[1, n*n_virt + w]

												elif ((t == s) and (v == s) and (u != s) and (u != t) and (w == u)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[j, k, n, n_occ + s] + -8 * g[j, n_occ + s, k, n] ) * K[0, (i*n_virt + s) * n_ex + k*n_virt + u+ 2*n_ex] * K[1, n*n_virt + u]

												elif ((t != s) and (v == s) and (u == s) and (w == s)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[j, k, n, n_occ + t] + -8 * g[j, n_occ + t, k, n] ) * K[0, (i*n_virt + s) * n_ex + k*n_virt + s+ 2*n_ex] * K[1, n*n_virt + s]

												elif ((t != s) and (v == s) and (u == t) and (w == s)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-8 * g[j, k, n, n_occ + s] + 4 * g[j, n_occ + s, k, n] ) * K[0, (i*n_virt + s) * n_ex + k*n_virt + t+ 2*n_ex] * K[1, n*n_virt + s]

												elif ((t != s) and (v == s) and (u == t) and (w == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[j, k, n, n_occ + t] + -4 * g[j, n_occ + t, k, n] ) * K[0, (i*n_virt + s) * n_ex + k*n_virt + t+ 2*n_ex] * K[1, n*n_virt + t]

												elif ((t != s) and (v == s) and (u == t) and (w != s) and (w != t) and (w != u) and (w != v)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-8 * g[j, k, n, n_occ + w] + 4 * g[j, n_occ + w, k, n] ) * K[0, (i*n_virt + s) * n_ex + k*n_virt + t+ 2*n_ex] * K[1, n*n_virt + w]

												elif ((t != s) and (v == s) and (u != s) and (u != t) and (w == u)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[j, k, n, n_occ + t] + -8 * g[j, n_occ + t, k, n] ) * K[0, (i*n_virt + s) * n_ex + k*n_virt + u+ 2*n_ex] * K[1, n*n_virt + u]

	# This operator combination: {'a': 2, 'b': 1, 'c': 1}
	for i in range(n_occ):
		for j in range(n_occ):
			for k in range(n_occ):
				for s in range(n_virt):
					for t in range(n_virt):
						for u in range(n_virt):

							if ((j == i) and (k == i)):

								if ((t == s) and (u == s)):

									L3[i*n_virt + s] += (-4 * F[i, n_occ + s] + 4 * g[i, n_occ + s, n_occ + s, n_occ + s] + -4 * g[i, i, i, n_occ + s] ) * K[0, i*n_virt + s] * K[1, i*n_virt + s + n_ex]

								elif ((t == s) and (u != s) and (u != t)):

									L3[i*n_virt + s] += (4 * g[i, n_occ + s, n_occ + s, n_occ + u] ) * K[0, i*n_virt + s] * K[1, i*n_virt + u + n_ex]

								elif ((t != s) and (u == s)):

									L3[i*n_virt + s] += (-2 * F[i, n_occ + t] + 2 * g[i, n_occ + t, n_occ + s, n_occ + s] + 2 * g[i, n_occ + s, n_occ + s, n_occ + t] + -2 * g[i, i, i, n_occ + t] ) * K[0, i*n_virt + t] * K[1, i*n_virt + s + n_ex]

								elif ((t != s) and (u == t)):

									L3[i*n_virt + s] += (-2 * F[i, n_occ + s] + 2 * g[i, n_occ + t, n_occ + s, n_occ + t] + 2 * g[i, n_occ + s, n_occ + t, n_occ + t] + -2 * g[i, i, i, n_occ + s] ) * K[0, i*n_virt + t] * K[1, i*n_virt + t + n_ex]

								elif ((t != s) and (u != s) and (u != t)):

									L3[i*n_virt + s] += (2 * g[i, n_occ + t, n_occ + s, n_occ + u] + 2 * g[i, n_occ + s, n_occ + t, n_occ + u] ) * K[0, i*n_virt + t] * K[1, i*n_virt + u + n_ex]

							elif ((j == i) and (k != i) and (k != j)):

								if ((t == s) and (u == s)):

									L3[i*n_virt + s] += (-4 * g[i, k, i, n_occ + s] ) * K[0, i*n_virt + s] * K[1, k*n_virt + s + n_ex]

								elif ((t != s) and (u == s)):

									L3[i*n_virt + s] += (-2 * g[i, k, i, n_occ + t] ) * K[0, i*n_virt + t] * K[1, k*n_virt + s + n_ex]

								elif ((t != s) and (u == t)):

									L3[i*n_virt + s] += (-2 * g[i, k, i, n_occ + s] ) * K[0, i*n_virt + t] * K[1, k*n_virt + t + n_ex]

							elif ((j != i) and (k == i)):

								if ((t == s) and (u == s)):

									L3[i*n_virt + s] += (-2 * F[j, n_occ + s] + 2 * g[j, n_occ + s, n_occ + s, n_occ + s] + -2 * g[i, i, j, n_occ + s] + -2 * g[i, j, i, n_occ + s] ) * K[0, j*n_virt + s] * K[1, i*n_virt + s + n_ex]

								elif ((t == s) and (u != s) and (u != t)):

									L3[i*n_virt + s] += (2 * g[j, n_occ + s, n_occ + s, n_occ + u] ) * K[0, j*n_virt + s] * K[1, i*n_virt + u + n_ex]

								elif ((t != s) and (u == s)):

									L3[i*n_virt + s] += (-2 * g[j, n_occ + s, n_occ + s, n_occ + t] + 4 * g[j, n_occ + t, n_occ + s, n_occ + s] + 2 * g[i, j, i, n_occ + t] + -4 * g[i, i, j, n_occ + t] ) * K[0, j*n_virt + t] * K[1, i*n_virt + s + n_ex]

								elif ((t != s) and (u == t)):

									L3[i*n_virt + s] += (-2 * F[j, n_occ + s] + 4 * g[j, n_occ + t, n_occ + s, n_occ + t] + -2 * g[j, n_occ + s, n_occ + t, n_occ + t] + 2 * g[i, i, j, n_occ + s] + -4 * g[i, j, i, n_occ + s] ) * K[0, j*n_virt + t] * K[1, i*n_virt + t + n_ex]

								elif ((t != s) and (u != s) and (u != t)):

									L3[i*n_virt + s] += (-2 * g[j, n_occ + s, n_occ + t, n_occ + u] + 4 * g[j, n_occ + t, n_occ + s, n_occ + u] ) * K[0, j*n_virt + t] * K[1, i*n_virt + u + n_ex]

							elif ((j != i) and (k == j)):

								if ((t == s) and (u == s)):

									L3[i*n_virt + s] += (-2 * F[i, n_occ + s] + 2 * g[i, n_occ + s, n_occ + s, n_occ + s] + -2 * g[i, n_occ + s, j, j] + -2 * g[i, j, j, n_occ + s] ) * K[0, j*n_virt + s] * K[1, j*n_virt + s + n_ex]

								elif ((t == s) and (u != s) and (u != t)):

									L3[i*n_virt + s] += (2 * g[i, n_occ + s, n_occ + s, n_occ + u] ) * K[0, j*n_virt + s] * K[1, j*n_virt + u + n_ex]

								elif ((t != s) and (u == s)):

									L3[i*n_virt + s] += (-2 * F[i, n_occ + t] + 4 * g[i, n_occ + s, n_occ + s, n_occ + t] + -2 * g[i, n_occ + t, n_occ + s, n_occ + s] + 2 * g[i, n_occ + t, j, j] + -4 * g[i, j, j, n_occ + t] ) * K[0, j*n_virt + t] * K[1, j*n_virt + s + n_ex]

								elif ((t != s) and (u == t)):

									L3[i*n_virt + s] += (-2 * g[i, n_occ + t, n_occ + s, n_occ + t] + 4 * g[i, n_occ + s, n_occ + t, n_occ + t] + 2 * g[i, j, j, n_occ + s] + -4 * g[i, n_occ + s, j, j] ) * K[0, j*n_virt + t] * K[1, j*n_virt + t + n_ex]

								elif ((t != s) and (u != s) and (u != t)):

									L3[i*n_virt + s] += (4 * g[i, n_occ + s, n_occ + t, n_occ + u] + -2 * g[i, n_occ + t, n_occ + s, n_occ + u] ) * K[0, j*n_virt + t] * K[1, j*n_virt + u + n_ex]

							elif ((j != i) and (k != i) and (k != j)):

								if ((t == s) and (u == s)):

									L3[i*n_virt + s] += (-2 * g[i, k, j, n_occ + s] + -2 * g[i, n_occ + s, j, k] ) * K[0, j*n_virt + s] * K[1, k*n_virt + s + n_ex]

								elif ((t != s) and (u == s)):

									L3[i*n_virt + s] += (-4 * g[i, k, j, n_occ + t] + 2 * g[i, n_occ + t, j, k] ) * K[0, j*n_virt + t] * K[1, k*n_virt + s + n_ex]

								elif ((t != s) and (u == t)):

									L3[i*n_virt + s] += (2 * g[i, k, j, n_occ + s] + -4 * g[i, n_occ + s, j, k] ) * K[0, j*n_virt + t] * K[1, k*n_virt + t + n_ex]

	# This operator combination: {'a': 2, 'b': 1, 'c': 2}
	for i in range(n_occ):
		for j in range(n_occ):
			for k in range(n_occ):
				for s in range(n_virt):
					for t in range(n_virt):
						for u in range(n_virt):

							if ((j == i) and (k == i)):

								if ((t == s) and (u == s)):

									L3[i*n_virt + s + n_ex] += (-4 * g[i, n_occ + s, n_occ + s, n_occ + s] + 4 * g[i, i, i, n_occ + s] ) * K[0, i*n_virt + s] * K[1, i*n_virt + s + n_ex]

								elif ((t == s) and (u != s) and (u != t)):

									L3[i*n_virt + s + n_ex] += (-2 * g[i, n_occ + u, n_occ + s, n_occ + s] + -2 * g[i, n_occ + s, n_occ + s, n_occ + u] + 2 * g[i, i, i, n_occ + u] ) * K[0, i*n_virt + s] * K[1, i*n_virt + u + n_ex]

								elif ((t != s) and (u == s)):

									L3[i*n_virt + s + n_ex] += (-4 * g[i, n_occ + s, n_occ + s, n_occ + t] ) * K[0, i*n_virt + t] * K[1, i*n_virt + s + n_ex]

								elif ((t != s) and (u == t)):

									L3[i*n_virt + s + n_ex] += (-2 * g[i, n_occ + t, n_occ + s, n_occ + t] + -2 * g[i, n_occ + s, n_occ + t, n_occ + t] + 2 * g[i, i, i, n_occ + s] ) * K[0, i*n_virt + t] * K[1, i*n_virt + t + n_ex]

								elif ((t != s) and (u != s) and (u != t)):

									L3[i*n_virt + s + n_ex] += (-2 * g[i, n_occ + u, n_occ + s, n_occ + t] + -2 * g[i, n_occ + s, n_occ + t, n_occ + u] ) * K[0, i*n_virt + t] * K[1, i*n_virt + u + n_ex]

							elif ((j == i) and (k != i) and (k != j)):

								if ((t == s) and (u == s)):

									L3[i*n_virt + s + n_ex] += (2 * g[i, k, i, n_occ + s] + -2 * g[k, n_occ + s, n_occ + s, n_occ + s] + 2 * g[i, i, k, n_occ + s] ) * K[0, i*n_virt + s] * K[1, k*n_virt + s + n_ex]

								elif ((t == s) and (u != s) and (u != t)):

									L3[i*n_virt + s + n_ex] += (2 * g[k, n_occ + s, n_occ + s, n_occ + u] + -4 * g[k, n_occ + u, n_occ + s, n_occ + s] + -2 * g[i, k, i, n_occ + u] + 4 * g[i, i, k, n_occ + u] ) * K[0, i*n_virt + s] * K[1, k*n_virt + u + n_ex]

								elif ((t != s) and (u == s)):

									L3[i*n_virt + s + n_ex] += (-2 * g[k, n_occ + s, n_occ + s, n_occ + t] ) * K[0, i*n_virt + t] * K[1, k*n_virt + s + n_ex]

								elif ((t != s) and (u == t)):

									L3[i*n_virt + s + n_ex] += (4 * g[i, k, i, n_occ + s] + -2 * g[i, i, k, n_occ + s] + -4 * g[k, n_occ + t, n_occ + s, n_occ + t] + 2 * g[k, n_occ + s, n_occ + t, n_occ + t] ) * K[0, i*n_virt + t] * K[1, k*n_virt + t + n_ex]

								elif ((t != s) and (u != s) and (u != t)):

									L3[i*n_virt + s + n_ex] += (2 * g[k, n_occ + s, n_occ + t, n_occ + u] + -4 * g[k, n_occ + u, n_occ + s, n_occ + t] ) * K[0, i*n_virt + t] * K[1, k*n_virt + u + n_ex]

							elif ((j != i) and (k == i)):

								if ((t == s) and (u == s)):

									L3[i*n_virt + s + n_ex] += (4 * g[i, j, i, n_occ + s] ) * K[0, j*n_virt + s] * K[1, i*n_virt + s + n_ex]

								elif ((t == s) and (u != s) and (u != t)):

									L3[i*n_virt + s + n_ex] += (2 * g[i, j, i, n_occ + u] ) * K[0, j*n_virt + s] * K[1, i*n_virt + u + n_ex]

								elif ((t != s) and (u == t)):

									L3[i*n_virt + s + n_ex] += (2 * g[i, j, i, n_occ + s] ) * K[0, j*n_virt + t] * K[1, i*n_virt + t + n_ex]

							elif ((j != i) and (k == j)):

								if ((t == s) and (u == s)):

									L3[i*n_virt + s + n_ex] += (2 * g[i, j, j, n_occ + s] + -2 * g[i, n_occ + s, n_occ + s, n_occ + s] + 2 * g[i, n_occ + s, j, j] ) * K[0, j*n_virt + s] * K[1, j*n_virt + s + n_ex]

								elif ((t == s) and (u != s) and (u != t)):

									L3[i*n_virt + s + n_ex] += (4 * g[i, j, j, n_occ + u] + -2 * g[i, n_occ + u, j, j] + -4 * g[i, n_occ + s, n_occ + s, n_occ + u] + 2 * g[i, n_occ + u, n_occ + s, n_occ + s] ) * K[0, j*n_virt + s] * K[1, j*n_virt + u + n_ex]

								elif ((t != s) and (u == s)):

									L3[i*n_virt + s + n_ex] += (-2 * g[i, n_occ + s, n_occ + s, n_occ + t] ) * K[0, j*n_virt + t] * K[1, j*n_virt + s + n_ex]

								elif ((t != s) and (u == t)):

									L3[i*n_virt + s + n_ex] += (2 * g[i, n_occ + t, n_occ + s, n_occ + t] + -4 * g[i, n_occ + s, n_occ + t, n_occ + t] + -2 * g[i, j, j, n_occ + s] + 4 * g[i, n_occ + s, j, j] ) * K[0, j*n_virt + t] * K[1, j*n_virt + t + n_ex]

								elif ((t != s) and (u != s) and (u != t)):

									L3[i*n_virt + s + n_ex] += (-4 * g[i, n_occ + s, n_occ + t, n_occ + u] + 2 * g[i, n_occ + u, n_occ + s, n_occ + t] ) * K[0, j*n_virt + t] * K[1, j*n_virt + u + n_ex]

							elif ((j != i) and (k != i) and (k != j)):

								if ((t == s) and (u == s)):

									L3[i*n_virt + s + n_ex] += (2 * g[i, j, k, n_occ + s] + 2 * g[i, n_occ + s, j, k] ) * K[0, j*n_virt + s] * K[1, k*n_virt + s + n_ex]

								elif ((t == s) and (u != s) and (u != t)):

									L3[i*n_virt + s + n_ex] += (4 * g[i, j, k, n_occ + u] + -2 * g[i, n_occ + u, j, k] ) * K[0, j*n_virt + s] * K[1, k*n_virt + u + n_ex]

								elif ((t != s) and (u == t)):

									L3[i*n_virt + s + n_ex] += (-2 * g[i, j, k, n_occ + s] + 4 * g[i, n_occ + s, j, k] ) * K[0, j*n_virt + t] * K[1, k*n_virt + t + n_ex]

	# This operator combination: {'a': 2, 'b': 1, 'c': 3}
	# All terms vanished for this combination

	# This operator combination: {'a': 2, 'b': 2, 'c': 1}
	for i in range(n_occ):
		for j in range(n_occ):
			for k in range(n_occ):
				for s in range(n_virt):
					for t in range(n_virt):
						for u in range(n_virt):

							if ((j == i) and (k == i)):

								if ((t == s) and (u == s)):

									L3[i*n_virt + s] += (-4 * F[i, n_occ + s] + 4 * g[i, n_occ + s, n_occ + s, n_occ + s] + -4 * g[i, i, i, n_occ + s] ) * K[0, i*n_virt + s + n_ex] * K[1, i*n_virt + s + n_ex]

								elif ((t == s) and (u != s) and (u != t)):

									L3[i*n_virt + s] += (-2 * F[i, n_occ + u] + 2 * g[i, n_occ + s, n_occ + s, n_occ + u] + 2 * g[i, n_occ + u, n_occ + s, n_occ + s] + -2 * g[i, i, i, n_occ + u] ) * K[0, i*n_virt + s + n_ex] * K[1, i*n_virt + u + n_ex]

								elif ((t != s) and (u == s)):

									L3[i*n_virt + s] += (-2 * F[i, n_occ + t] + 2 * g[i, n_occ + t, n_occ + s, n_occ + s] + 2 * g[i, n_occ + s, n_occ + s, n_occ + t] + -2 * g[i, i, i, n_occ + t] ) * K[0, i*n_virt + t + n_ex] * K[1, i*n_virt + s + n_ex]

								elif ((t != s) and (u == t)):

									L3[i*n_virt + s] += (4 * g[i, n_occ + t, n_occ + s, n_occ + t] ) * K[0, i*n_virt + t + n_ex] * K[1, i*n_virt + t + n_ex]

								elif ((t != s) and (u != s) and (u != t)):

									L3[i*n_virt + s] += (2 * g[i, n_occ + t, n_occ + s, n_occ + u] + 2 * g[i, n_occ + u, n_occ + s, n_occ + t] ) * K[0, i*n_virt + t + n_ex] * K[1, i*n_virt + u + n_ex]

							elif ((j == i) and (k != i) and (k != j)):

								if ((t == s) and (u == s)):

									L3[i*n_virt + s] += (-2 * F[k, n_occ + s] + -2 * g[i, i, k, n_occ + s] + 2 * g[k, n_occ + s, n_occ + s, n_occ + s] + -2 * g[i, k, i, n_occ + s] ) * K[0, i*n_virt + s + n_ex] * K[1, k*n_virt + s + n_ex]

								elif ((t == s) and (u != s) and (u != t)):

									L3[i*n_virt + s] += (2 * g[i, k, i, n_occ + u] + -4 * g[i, i, k, n_occ + u] + -2 * g[k, n_occ + s, n_occ + s, n_occ + u] + 4 * g[k, n_occ + u, n_occ + s, n_occ + s] ) * K[0, i*n_virt + s + n_ex] * K[1, k*n_virt + u + n_ex]

								elif ((t != s) and (u == s)):

									L3[i*n_virt + s] += (-2 * F[k, n_occ + t] + 4 * g[k, n_occ + s, n_occ + s, n_occ + t] + -2 * g[k, n_occ + t, n_occ + s, n_occ + s] + 2 * g[i, i, k, n_occ + t] + -4 * g[i, k, i, n_occ + t] ) * K[0, i*n_virt + t + n_ex] * K[1, k*n_virt + s + n_ex]

								elif ((t != s) and (u == t)):

									L3[i*n_virt + s] += (2 * g[k, n_occ + t, n_occ + s, n_occ + t] ) * K[0, i*n_virt + t + n_ex] * K[1, k*n_virt + t + n_ex]

								elif ((t != s) and (u != s) and (u != t)):

									L3[i*n_virt + s] += (-2 * g[k, n_occ + t, n_occ + s, n_occ + u] + 4 * g[k, n_occ + u, n_occ + s, n_occ + t] ) * K[0, i*n_virt + t + n_ex] * K[1, k*n_virt + u + n_ex]

							elif ((j != i) and (k == i)):

								if ((t == s) and (u == s)):

									L3[i*n_virt + s] += (-2 * F[j, n_occ + s] + -2 * g[i, i, j, n_occ + s] + 2 * g[j, n_occ + s, n_occ + s, n_occ + s] + -2 * g[i, j, i, n_occ + s] ) * K[0, j*n_virt + s + n_ex] * K[1, i*n_virt + s + n_ex]

								elif ((t == s) and (u != s) and (u != t)):

									L3[i*n_virt + s] += (-2 * F[j, n_occ + u] + 4 * g[j, n_occ + s, n_occ + s, n_occ + u] + -2 * g[j, n_occ + u, n_occ + s, n_occ + s] + 2 * g[i, i, j, n_occ + u] + -4 * g[i, j, i, n_occ + u] ) * K[0, j*n_virt + s + n_ex] * K[1, i*n_virt + u + n_ex]

								elif ((t != s) and (u == s)):

									L3[i*n_virt + s] += (2 * g[i, j, i, n_occ + t] + -4 * g[i, i, j, n_occ + t] + -2 * g[j, n_occ + s, n_occ + s, n_occ + t] + 4 * g[j, n_occ + t, n_occ + s, n_occ + s] ) * K[0, j*n_virt + t + n_ex] * K[1, i*n_virt + s + n_ex]

								elif ((t != s) and (u == t)):

									L3[i*n_virt + s] += (2 * g[j, n_occ + t, n_occ + s, n_occ + t] ) * K[0, j*n_virt + t + n_ex] * K[1, i*n_virt + t + n_ex]

								elif ((t != s) and (u != s) and (u != t)):

									L3[i*n_virt + s] += (4 * g[j, n_occ + t, n_occ + s, n_occ + u] + -2 * g[j, n_occ + u, n_occ + s, n_occ + t] ) * K[0, j*n_virt + t + n_ex] * K[1, i*n_virt + u + n_ex]

							elif ((j != i) and (k == j)):

								if ((t == s) and (u == s)):

									L3[i*n_virt + s] += (-4 * g[i, j, j, n_occ + s] ) * K[0, j*n_virt + s + n_ex] * K[1, j*n_virt + s + n_ex]

								elif ((t == s) and (u != s) and (u != t)):

									L3[i*n_virt + s] += (-2 * g[i, j, j, n_occ + u] ) * K[0, j*n_virt + s + n_ex] * K[1, j*n_virt + u + n_ex]

								elif ((t != s) and (u == s)):

									L3[i*n_virt + s] += (-2 * g[i, j, j, n_occ + t] ) * K[0, j*n_virt + t + n_ex] * K[1, j*n_virt + s + n_ex]

							elif ((j != i) and (k != i) and (k != j)):

								if ((t == s) and (u == s)):

									L3[i*n_virt + s] += (-2 * g[i, k, j, n_occ + s] + -2 * g[i, j, k, n_occ + s] ) * K[0, j*n_virt + s + n_ex] * K[1, k*n_virt + s + n_ex]

								elif ((t == s) and (u != s) and (u != t)):

									L3[i*n_virt + s] += (-4 * g[i, j, k, n_occ + u] + 2 * g[i, k, j, n_occ + u] ) * K[0, j*n_virt + s + n_ex] * K[1, k*n_virt + u + n_ex]

								elif ((t != s) and (u == s)):

									L3[i*n_virt + s] += (2 * g[i, j, k, n_occ + t] + -4 * g[i, k, j, n_occ + t] ) * K[0, j*n_virt + t + n_ex] * K[1, k*n_virt + s + n_ex]

	# This operator combination: {'a': 2, 'b': 2, 'c': 2}
	# All terms vanished for this combination

	# This operator combination: {'a': 2, 'b': 2, 'c': 3}
	# All terms vanished for this combination

	# This operator combination: {'a': 2, 'b': 3, 'c': 1}
	for i in range(n_occ):
		for k in range(n_occ):
			for j in range(n_occ):
				for m in range(n_occ):
					for s in range(n_virt):
						for u in range(n_virt):
							for t in range(n_virt):
								for v in range(n_virt):

									if ((k == i) and (j == i) and (m == i)):

										if ((u == s) and (t == s) and (v != s) and (v != t) and (v != u)):

											L3[i*n_virt + s] += (-4 * F[n_occ + s, n_occ + v] + 4 * g[i, i, n_occ + s, n_occ + v] + -8 * g[i, n_occ + s, i, n_occ + v] ) * K[0, (i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] * K[1, i*n_virt + v + n_ex]

										elif ((u != s) and (u != t) and (t == s) and (v == s)):

											L3[i*n_virt + s] += (-4 * F[n_occ + s, n_occ + u] + 4 * g[i, i, n_occ + s, n_occ + u] + -8 * g[i, n_occ + s, i, n_occ + u] ) * K[0, (i*n_virt + u) * n_ex + i*n_virt + s+ 2*n_ex] * K[1, i*n_virt + s + n_ex]

										elif ((u != s) and (u != t) and (t == s) and (v == u)):

											L3[i*n_virt + s] += (4 * F[n_occ + s, n_occ + s] + -4 * F[n_occ + u, n_occ + u] + 4 * g[i, i, n_occ + u, n_occ + u] + -4 * g[i, i, n_occ + s, n_occ + s] + -8 * g[i, n_occ + u, i, n_occ + u] + 8 * g[i, n_occ + s, i, n_occ + s] ) * K[0, (i*n_virt + u) * n_ex + i*n_virt + s+ 2*n_ex] * K[1, i*n_virt + u + n_ex]

										elif ((u != s) and (u != t) and (t == s) and (v != s) and (v != t) and (v != u)):

											L3[i*n_virt + s] += (-4 * F[n_occ + u, n_occ + v] + 4 * g[i, i, n_occ + u, n_occ + v] + -8 * g[i, n_occ + u, i, n_occ + v] ) * K[0, (i*n_virt + u) * n_ex + i*n_virt + s+ 2*n_ex] * K[1, i*n_virt + v + n_ex]

										elif ((u == s) and (t != s) and (v == s)):

											L3[i*n_virt + s] += (4 * F[n_occ + s, n_occ + t] + -4 * g[i, i, n_occ + s, n_occ + t] + 8 * g[i, n_occ + s, i, n_occ + t] ) * K[0, (i*n_virt + s) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, i*n_virt + s + n_ex]

										elif ((u == t) and (t != s) and (v == t)):

											L3[i*n_virt + s] += (4 * F[n_occ + s, n_occ + t] + -4 * g[i, i, n_occ + s, n_occ + t] + 8 * g[i, n_occ + s, i, n_occ + t] ) * K[0, (i*n_virt + t) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, i*n_virt + t + n_ex]

										elif ((u != s) and (u != t) and (t != s) and (v == u)):

											L3[i*n_virt + s] += (4 * F[n_occ + s, n_occ + t] + -4 * g[i, i, n_occ + s, n_occ + t] + 8 * g[i, n_occ + s, i, n_occ + t] ) * K[0, (i*n_virt + u) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, i*n_virt + u + n_ex]

									elif ((k == i) and (j == i) and (m != i) and (m != j) and (m != k)):

										if ((u == s) and (t == s) and (v == s)):

											L3[i*n_virt + s] += (4 * F[i, m] + -8 * g[i, n_occ + s, m, n_occ + s] + 4 * g[i, m, n_occ + s, n_occ + s] ) * K[0, (i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] * K[1, m*n_virt + s + n_ex]

										elif ((u == s) and (t == s) and (v != s) and (v != t) and (v != u)):

											L3[i*n_virt + s] += (4 * g[i, m, n_occ + s, n_occ + v] + -8 * g[i, n_occ + s, m, n_occ + v] ) * K[0, (i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] * K[1, m*n_virt + v + n_ex]

										elif ((u != s) and (u != t) and (t == s) and (v == s)):

											L3[i*n_virt + s] += (4 * g[i, m, n_occ + s, n_occ + u] + -8 * g[i, n_occ + u, m, n_occ + s] ) * K[0, (i*n_virt + u) * n_ex + i*n_virt + s+ 2*n_ex] * K[1, m*n_virt + s + n_ex]

										elif ((u != s) and (u != t) and (t == s) and (v == u)):

											L3[i*n_virt + s] += (4 * F[i, m] + -8 * g[i, n_occ + u, m, n_occ + u] + 4 * g[i, m, n_occ + u, n_occ + u] ) * K[0, (i*n_virt + u) * n_ex + i*n_virt + s+ 2*n_ex] * K[1, m*n_virt + u + n_ex]

										elif ((u != s) and (u != t) and (t == s) and (v != s) and (v != t) and (v != u)):

											L3[i*n_virt + s] += (4 * g[i, m, n_occ + u, n_occ + v] + -8 * g[i, n_occ + u, m, n_occ + v] ) * K[0, (i*n_virt + u) * n_ex + i*n_virt + s+ 2*n_ex] * K[1, m*n_virt + v + n_ex]

									elif ((k != i) and (k != j) and (j == i) and (m == i)):

										if ((u == s) and (t == s) and (v == s)):

											L3[i*n_virt + s] += (4 * F[i, k] + -8 * g[i, n_occ + s, k, n_occ + s] + 4 * g[i, k, n_occ + s, n_occ + s] ) * K[0, (k*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] * K[1, i*n_virt + s + n_ex]

										elif ((u == s) and (t == s) and (v != s) and (v != t) and (v != u)):

											L3[i*n_virt + s] += (4 * g[i, k, n_occ + s, n_occ + v] + -8 * g[i, n_occ + v, k, n_occ + s] ) * K[0, (k*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] * K[1, i*n_virt + v + n_ex]

										elif ((u != s) and (u != t) and (t == s) and (v == s)):

											L3[i*n_virt + s] += (4 * g[i, k, n_occ + s, n_occ + u] + -8 * g[i, n_occ + s, k, n_occ + u] ) * K[0, (k*n_virt + u) * n_ex + i*n_virt + s+ 2*n_ex] * K[1, i*n_virt + s + n_ex]

										elif ((u != s) and (u != t) and (t == s) and (v == u)):

											L3[i*n_virt + s] += (4 * F[i, k] + -8 * g[i, n_occ + u, k, n_occ + u] + 4 * g[i, k, n_occ + u, n_occ + u] ) * K[0, (k*n_virt + u) * n_ex + i*n_virt + s+ 2*n_ex] * K[1, i*n_virt + u + n_ex]

										elif ((u != s) and (u != t) and (t == s) and (v != s) and (v != t) and (v != u)):

											L3[i*n_virt + s] += (4 * g[i, k, n_occ + u, n_occ + v] + -8 * g[i, n_occ + v, k, n_occ + u] ) * K[0, (k*n_virt + u) * n_ex + i*n_virt + s+ 2*n_ex] * K[1, i*n_virt + v + n_ex]

									elif ((k != i) and (k != j) and (j == i) and (m == k)):

										if ((u == s) and (t == s) and (v == s)):

											L3[i*n_virt + s] += (4 * F[k, k] + -4 * F[i, i] + -4 * g[i, i, n_occ + s, n_occ + s] + -8 * g[k, n_occ + s, k, n_occ + s] + 8 * g[i, n_occ + s, i, n_occ + s] + 4 * g[k, k, n_occ + s, n_occ + s] ) * K[0, (k*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] * K[1, k*n_virt + s + n_ex]

										elif ((u == s) and (t == s) and (v != s) and (v != t) and (v != u)):

											L3[i*n_virt + s] += (-4 * F[n_occ + s, n_occ + v] + 4 * g[k, k, n_occ + s, n_occ + v] + -8 * g[k, n_occ + s, k, n_occ + v] ) * K[0, (k*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] * K[1, k*n_virt + v + n_ex]

										elif ((u != s) and (u != t) and (t == s) and (v == s)):

											L3[i*n_virt + s] += (-4 * F[n_occ + s, n_occ + u] + 4 * g[k, k, n_occ + s, n_occ + u] + -8 * g[k, n_occ + s, k, n_occ + u] ) * K[0, (k*n_virt + u) * n_ex + i*n_virt + s+ 2*n_ex] * K[1, k*n_virt + s + n_ex]

										elif ((u != s) and (u != t) and (t == s) and (v == u)):

											L3[i*n_virt + s] += (4 * F[k, k] + 4 * F[n_occ + s, n_occ + s] + -4 * F[n_occ + u, n_occ + u] + -4 * F[i, i] + 4 * g[k, k, n_occ + u, n_occ + u] + -4 * g[i, i, n_occ + s, n_occ + s] + -8 * g[k, n_occ + u, k, n_occ + u] + 8 * g[i, n_occ + s, i, n_occ + s] ) * K[0, (k*n_virt + u) * n_ex + i*n_virt + s+ 2*n_ex] * K[1, k*n_virt + u + n_ex]

										elif ((u != s) and (u != t) and (t == s) and (v != s) and (v != t) and (v != u)):

											L3[i*n_virt + s] += (-4 * F[n_occ + u, n_occ + v] + 4 * g[k, k, n_occ + u, n_occ + v] + -8 * g[k, n_occ + u, k, n_occ + v] ) * K[0, (k*n_virt + u) * n_ex + i*n_virt + s+ 2*n_ex] * K[1, k*n_virt + v + n_ex]

										elif ((u == s) and (t != s) and (v == s)):

											L3[i*n_virt + s] += (4 * F[n_occ + s, n_occ + t] + -4 * g[i, i, n_occ + s, n_occ + t] + 8 * g[i, n_occ + s, i, n_occ + t] ) * K[0, (k*n_virt + s) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, k*n_virt + s + n_ex]

										elif ((u == t) and (t != s) and (v == t)):

											L3[i*n_virt + s] += (4 * F[n_occ + s, n_occ + t] + -4 * g[i, i, n_occ + s, n_occ + t] + 8 * g[i, n_occ + s, i, n_occ + t] ) * K[0, (k*n_virt + t) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, k*n_virt + t + n_ex]

										elif ((u != s) and (u != t) and (t != s) and (v == u)):

											L3[i*n_virt + s] += (4 * F[n_occ + s, n_occ + t] + -4 * g[i, i, n_occ + s, n_occ + t] + 8 * g[i, n_occ + s, i, n_occ + t] ) * K[0, (k*n_virt + u) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, k*n_virt + u + n_ex]

									elif ((k != i) and (k != j) and (j == i) and (m != i) and (m != j) and (m != k)):

										if ((u == s) and (t == s) and (v == s)):

											L3[i*n_virt + s] += (4 * F[k, m] + -8 * g[k, n_occ + s, m, n_occ + s] + 4 * g[k, m, n_occ + s, n_occ + s] ) * K[0, (k*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] * K[1, m*n_virt + s + n_ex]

										elif ((u == s) and (t == s) and (v != s) and (v != t) and (v != u)):

											L3[i*n_virt + s] += (4 * g[k, m, n_occ + s, n_occ + v] + -8 * g[k, n_occ + s, m, n_occ + v] ) * K[0, (k*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] * K[1, m*n_virt + v + n_ex]

										elif ((u != s) and (u != t) and (t == s) and (v == s)):

											L3[i*n_virt + s] += (4 * g[k, m, n_occ + s, n_occ + u] + -8 * g[k, n_occ + u, m, n_occ + s] ) * K[0, (k*n_virt + u) * n_ex + i*n_virt + s+ 2*n_ex] * K[1, m*n_virt + s + n_ex]

										elif ((u != s) and (u != t) and (t == s) and (v == u)):

											L3[i*n_virt + s] += (4 * F[k, m] + -8 * g[k, n_occ + u, m, n_occ + u] + 4 * g[k, m, n_occ + u, n_occ + u] ) * K[0, (k*n_virt + u) * n_ex + i*n_virt + s+ 2*n_ex] * K[1, m*n_virt + u + n_ex]

										elif ((u != s) and (u != t) and (t == s) and (v != s) and (v != t) and (v != u)):

											L3[i*n_virt + s] += (4 * g[k, m, n_occ + u, n_occ + v] + -8 * g[k, n_occ + u, m, n_occ + v] ) * K[0, (k*n_virt + u) * n_ex + i*n_virt + s+ 2*n_ex] * K[1, m*n_virt + v + n_ex]

									elif ((k == i) and (j != i) and (m == i)):

										if ((u == s) and (t == s) and (v == s)):

											L3[i*n_virt + s] += (-4 * F[i, j] + 8 * g[i, n_occ + s, j, n_occ + s] + -4 * g[i, j, n_occ + s, n_occ + s] ) * K[0, (i*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, i*n_virt + s + n_ex]

										elif ((u != s) and (u != t) and (t == s) and (v == u)):

											L3[i*n_virt + s] += (-4 * F[i, j] + 8 * g[i, n_occ + s, j, n_occ + s] + -4 * g[i, j, n_occ + s, n_occ + s] ) * K[0, (i*n_virt + u) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, i*n_virt + u + n_ex]

										elif ((u == s) and (t != s) and (v == s)):

											L3[i*n_virt + s] += (-4 * g[i, j, n_occ + s, n_occ + t] + 8 * g[i, n_occ + s, j, n_occ + t] ) * K[0, (i*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, i*n_virt + s + n_ex]

										elif ((u == t) and (t != s) and (v == t)):

											L3[i*n_virt + s] += (-4 * g[i, j, n_occ + s, n_occ + t] + 8 * g[i, n_occ + s, j, n_occ + t] ) * K[0, (i*n_virt + t) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, i*n_virt + t + n_ex]

										elif ((u != s) and (u != t) and (t != s) and (v == u)):

											L3[i*n_virt + s] += (-4 * g[i, j, n_occ + s, n_occ + t] + 8 * g[i, n_occ + s, j, n_occ + t] ) * K[0, (i*n_virt + u) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, i*n_virt + u + n_ex]

									elif ((k == j) and (j != i) and (m == j)):

										if ((u == s) and (t == s) and (v == s)):

											L3[i*n_virt + s] += (-4 * F[i, j] + 8 * g[i, n_occ + s, j, n_occ + s] + -4 * g[i, j, n_occ + s, n_occ + s] ) * K[0, (j*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, j*n_virt + s + n_ex]

										elif ((u != s) and (u != t) and (t == s) and (v == u)):

											L3[i*n_virt + s] += (-4 * F[i, j] + 8 * g[i, n_occ + s, j, n_occ + s] + -4 * g[i, j, n_occ + s, n_occ + s] ) * K[0, (j*n_virt + u) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, j*n_virt + u + n_ex]

										elif ((u == s) and (t != s) and (v == s)):

											L3[i*n_virt + s] += (-4 * g[i, j, n_occ + s, n_occ + t] + 8 * g[i, n_occ + s, j, n_occ + t] ) * K[0, (j*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, j*n_virt + s + n_ex]

										elif ((u == t) and (t != s) and (v == t)):

											L3[i*n_virt + s] += (-4 * g[i, j, n_occ + s, n_occ + t] + 8 * g[i, n_occ + s, j, n_occ + t] ) * K[0, (j*n_virt + t) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, j*n_virt + t + n_ex]

										elif ((u != s) and (u != t) and (t != s) and (v == u)):

											L3[i*n_virt + s] += (-4 * g[i, j, n_occ + s, n_occ + t] + 8 * g[i, n_occ + s, j, n_occ + t] ) * K[0, (j*n_virt + u) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, j*n_virt + u + n_ex]

									elif ((k != i) and (k != j) and (j != i) and (m == k)):

										if ((u == s) and (t == s) and (v == s)):

											L3[i*n_virt + s] += (-4 * F[i, j] + 8 * g[i, n_occ + s, j, n_occ + s] + -4 * g[i, j, n_occ + s, n_occ + s] ) * K[0, (k*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, k*n_virt + s + n_ex]

										elif ((u != s) and (u != t) and (t == s) and (v == u)):

											L3[i*n_virt + s] += (-4 * F[i, j] + 8 * g[i, n_occ + s, j, n_occ + s] + -4 * g[i, j, n_occ + s, n_occ + s] ) * K[0, (k*n_virt + u) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, k*n_virt + u + n_ex]

										elif ((u == s) and (t != s) and (v == s)):

											L3[i*n_virt + s] += (-4 * g[i, j, n_occ + s, n_occ + t] + 8 * g[i, n_occ + s, j, n_occ + t] ) * K[0, (k*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, k*n_virt + s + n_ex]

										elif ((u == t) and (t != s) and (v == t)):

											L3[i*n_virt + s] += (-4 * g[i, j, n_occ + s, n_occ + t] + 8 * g[i, n_occ + s, j, n_occ + t] ) * K[0, (k*n_virt + t) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, k*n_virt + t + n_ex]

										elif ((u != s) and (u != t) and (t != s) and (v == u)):

											L3[i*n_virt + s] += (-4 * g[i, j, n_occ + s, n_occ + t] + 8 * g[i, n_occ + s, j, n_occ + t] ) * K[0, (k*n_virt + u) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, k*n_virt + u + n_ex]

	# This operator combination: {'a': 2, 'b': 3, 'c': 2}
	for i in range(n_occ):
		for k in range(n_occ):
			for j in range(n_occ):
				for m in range(n_occ):
					for s in range(n_virt):
						for u in range(n_virt):
							for t in range(n_virt):
								for v in range(n_virt):

									if ((k == i) and (j == i) and (m == i)):

										if ((u == s) and (t == s) and (v != s) and (v != t) and (v != u)):

											L3[i*n_virt + s + n_ex] += (4 * g[i, n_occ + s, i, n_occ + v] ) * K[0, (i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] * K[1, i*n_virt + v + n_ex]

										elif ((u != s) and (u != t) and (t == s) and (v == u)):

											L3[i*n_virt + s + n_ex] += (-4 * g[i, n_occ + s, i, n_occ + s] ) * K[0, (i*n_virt + u) * n_ex + i*n_virt + s+ 2*n_ex] * K[1, i*n_virt + u + n_ex]

										elif ((u == s) and (t != s) and (v == t)):

											L3[i*n_virt + s + n_ex] += (4 * g[i, n_occ + t, i, n_occ + t] ) * K[0, (i*n_virt + s) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, i*n_virt + t + n_ex]

										elif ((u == s) and (t != s) and (v != s) and (v != t) and (v != u)):

											L3[i*n_virt + s + n_ex] += (4 * g[i, n_occ + t, i, n_occ + v] ) * K[0, (i*n_virt + s) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, i*n_virt + v + n_ex]

										elif ((u == t) and (t != s) and (v == t)):

											L3[i*n_virt + s + n_ex] += (-4 * g[i, n_occ + s, i, n_occ + t] ) * K[0, (i*n_virt + t) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, i*n_virt + t + n_ex]

										elif ((u != s) and (u != t) and (t != s) and (v == u)):

											L3[i*n_virt + s + n_ex] += (-4 * g[i, n_occ + s, i, n_occ + t] ) * K[0, (i*n_virt + u) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, i*n_virt + u + n_ex]

									elif ((k == i) and (j == i) and (m != i) and (m != j) and (m != k)):

										if ((u == s) and (t == s) and (v == s)):

											L3[i*n_virt + s + n_ex] += (4 * g[i, n_occ + s, m, n_occ + s] ) * K[0, (i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] * K[1, m*n_virt + s + n_ex]

										elif ((u == s) and (t == s) and (v != s) and (v != t) and (v != u)):

											L3[i*n_virt + s + n_ex] += (8 * g[i, n_occ + s, m, n_occ + v] + -4 * g[i, n_occ + v, m, n_occ + s] ) * K[0, (i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] * K[1, m*n_virt + v + n_ex]

										elif ((u == s) and (t != s) and (v == s)):

											L3[i*n_virt + s + n_ex] += (-4 * g[i, n_occ + s, m, n_occ + t] + 8 * g[i, n_occ + t, m, n_occ + s] ) * K[0, (i*n_virt + s) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, m*n_virt + s + n_ex]

										elif ((u == s) and (t != s) and (v == t)):

											L3[i*n_virt + s + n_ex] += (4 * g[i, n_occ + t, m, n_occ + t] ) * K[0, (i*n_virt + s) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, m*n_virt + t + n_ex]

										elif ((u == s) and (t != s) and (v != s) and (v != t) and (v != u)):

											L3[i*n_virt + s + n_ex] += (8 * g[i, n_occ + t, m, n_occ + v] + -4 * g[i, n_occ + v, m, n_occ + t] ) * K[0, (i*n_virt + s) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, m*n_virt + v + n_ex]

									elif ((k != i) and (k != j) and (j == i) and (m == k)):

										if ((u == s) and (t == s) and (v == s)):

											L3[i*n_virt + s + n_ex] += (-4 * g[i, n_occ + s, i, n_occ + s] ) * K[0, (k*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] * K[1, k*n_virt + s + n_ex]

										elif ((u != s) and (u != t) and (t == s) and (v == u)):

											L3[i*n_virt + s + n_ex] += (-4 * g[i, n_occ + s, i, n_occ + s] ) * K[0, (k*n_virt + u) * n_ex + i*n_virt + s+ 2*n_ex] * K[1, k*n_virt + u + n_ex]

										elif ((u == s) and (t != s) and (v == s)):

											L3[i*n_virt + s + n_ex] += (-4 * g[i, n_occ + s, i, n_occ + t] ) * K[0, (k*n_virt + s) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, k*n_virt + s + n_ex]

										elif ((u == t) and (t != s) and (v == t)):

											L3[i*n_virt + s + n_ex] += (-4 * g[i, n_occ + s, i, n_occ + t] ) * K[0, (k*n_virt + t) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, k*n_virt + t + n_ex]

										elif ((u != s) and (u != t) and (t != s) and (v == u)):

											L3[i*n_virt + s + n_ex] += (-4 * g[i, n_occ + s, i, n_occ + t] ) * K[0, (k*n_virt + u) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, k*n_virt + u + n_ex]

									elif ((k == i) and (j != i) and (m == i)):

										if ((u == s) and (t == s) and (v != s) and (v != t) and (v != u)):

											L3[i*n_virt + s + n_ex] += (-4 * g[i, n_occ + s, j, n_occ + v] + 8 * g[i, n_occ + v, j, n_occ + s] ) * K[0, (i*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, i*n_virt + v + n_ex]

										elif ((u != s) and (u != t) and (t == s) and (v == u)):

											L3[i*n_virt + s + n_ex] += (-4 * g[i, n_occ + s, j, n_occ + s] ) * K[0, (i*n_virt + u) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, i*n_virt + u + n_ex]

										elif ((u == s) and (t != s) and (v == t)):

											L3[i*n_virt + s + n_ex] += (4 * g[i, n_occ + t, j, n_occ + t] ) * K[0, (i*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, i*n_virt + t + n_ex]

										elif ((u == s) and (t != s) and (v != s) and (v != t) and (v != u)):

											L3[i*n_virt + s + n_ex] += (-4 * g[i, n_occ + t, j, n_occ + v] + 8 * g[i, n_occ + v, j, n_occ + t] ) * K[0, (i*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, i*n_virt + v + n_ex]

										elif ((u == t) and (t != s) and (v == t)):

											L3[i*n_virt + s + n_ex] += (-8 * g[i, n_occ + s, j, n_occ + t] + 4 * g[i, n_occ + t, j, n_occ + s] ) * K[0, (i*n_virt + t) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, i*n_virt + t + n_ex]

										elif ((u != s) and (u != t) and (t != s) and (v == u)):

											L3[i*n_virt + s + n_ex] += (-8 * g[i, n_occ + s, j, n_occ + t] + 4 * g[i, n_occ + t, j, n_occ + s] ) * K[0, (i*n_virt + u) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, i*n_virt + u + n_ex]

									elif ((k == i) and (j != i) and (m == j)):

										if ((u == s) and (t == s) and (v == s)):

											L3[i*n_virt + s + n_ex] += (4 * g[j, n_occ + s, j, n_occ + s] ) * K[0, (i*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, j*n_virt + s + n_ex]

										elif ((u == s) and (t == s) and (v != s) and (v != t) and (v != u)):

											L3[i*n_virt + s + n_ex] += (4 * g[j, n_occ + s, j, n_occ + v] ) * K[0, (i*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, j*n_virt + v + n_ex]

										elif ((u == s) and (t != s) and (v == s)):

											L3[i*n_virt + s + n_ex] += (4 * g[j, n_occ + s, j, n_occ + t] ) * K[0, (i*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, j*n_virt + s + n_ex]

										elif ((u == s) and (t != s) and (v == t)):

											L3[i*n_virt + s + n_ex] += (4 * g[j, n_occ + t, j, n_occ + t] ) * K[0, (i*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, j*n_virt + t + n_ex]

										elif ((u == s) and (t != s) and (v != s) and (v != t) and (v != u)):

											L3[i*n_virt + s + n_ex] += (4 * g[j, n_occ + t, j, n_occ + v] ) * K[0, (i*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, j*n_virt + v + n_ex]

									elif ((k == i) and (j != i) and (m != i) and (m != j) and (m != k)):

										if ((u == s) and (t == s) and (v == s)):

											L3[i*n_virt + s + n_ex] += (4 * g[j, n_occ + s, m, n_occ + s] ) * K[0, (i*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, m*n_virt + s + n_ex]

										elif ((u == s) and (t == s) and (v != s) and (v != t) and (v != u)):

											L3[i*n_virt + s + n_ex] += (8 * g[j, n_occ + s, m, n_occ + v] + -4 * g[j, n_occ + v, m, n_occ + s] ) * K[0, (i*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, m*n_virt + v + n_ex]

										elif ((u == s) and (t != s) and (v == s)):

											L3[i*n_virt + s + n_ex] += (-4 * g[j, n_occ + s, m, n_occ + t] + 8 * g[j, n_occ + t, m, n_occ + s] ) * K[0, (i*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, m*n_virt + s + n_ex]

										elif ((u == s) and (t != s) and (v == t)):

											L3[i*n_virt + s + n_ex] += (4 * g[j, n_occ + t, m, n_occ + t] ) * K[0, (i*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, m*n_virt + t + n_ex]

										elif ((u == s) and (t != s) and (v != s) and (v != t) and (v != u)):

											L3[i*n_virt + s + n_ex] += (8 * g[j, n_occ + t, m, n_occ + v] + -4 * g[j, n_occ + v, m, n_occ + t] ) * K[0, (i*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, m*n_virt + v + n_ex]

									elif ((k == j) and (j != i) and (m == j)):

										if ((u == s) and (t == s) and (v == s)):

											L3[i*n_virt + s + n_ex] += (-4 * g[i, n_occ + s, j, n_occ + s] ) * K[0, (j*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, j*n_virt + s + n_ex]

										elif ((u != s) and (u != t) and (t == s) and (v == u)):

											L3[i*n_virt + s + n_ex] += (-4 * g[i, n_occ + s, j, n_occ + s] ) * K[0, (j*n_virt + u) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, j*n_virt + u + n_ex]

										elif ((u == s) and (t != s) and (v == s)):

											L3[i*n_virt + s + n_ex] += (-8 * g[i, n_occ + s, j, n_occ + t] + 4 * g[i, n_occ + t, j, n_occ + s] ) * K[0, (j*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, j*n_virt + s + n_ex]

										elif ((u == t) and (t != s) and (v == t)):

											L3[i*n_virt + s + n_ex] += (-8 * g[i, n_occ + s, j, n_occ + t] + 4 * g[i, n_occ + t, j, n_occ + s] ) * K[0, (j*n_virt + t) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, j*n_virt + t + n_ex]

										elif ((u != s) and (u != t) and (t != s) and (v == u)):

											L3[i*n_virt + s + n_ex] += (-8 * g[i, n_occ + s, j, n_occ + t] + 4 * g[i, n_occ + t, j, n_occ + s] ) * K[0, (j*n_virt + u) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, j*n_virt + u + n_ex]

									elif ((k != i) and (k != j) and (j != i) and (m == k)):

										if ((u == s) and (t == s) and (v == s)):

											L3[i*n_virt + s + n_ex] += (-4 * g[i, n_occ + s, j, n_occ + s] ) * K[0, (k*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, k*n_virt + s + n_ex]

										elif ((u != s) and (u != t) and (t == s) and (v == u)):

											L3[i*n_virt + s + n_ex] += (-4 * g[i, n_occ + s, j, n_occ + s] ) * K[0, (k*n_virt + u) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, k*n_virt + u + n_ex]

										elif ((u == s) and (t != s) and (v == s)):

											L3[i*n_virt + s + n_ex] += (-8 * g[i, n_occ + s, j, n_occ + t] + 4 * g[i, n_occ + t, j, n_occ + s] ) * K[0, (k*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, k*n_virt + s + n_ex]

										elif ((u == t) and (t != s) and (v == t)):

											L3[i*n_virt + s + n_ex] += (-8 * g[i, n_occ + s, j, n_occ + t] + 4 * g[i, n_occ + t, j, n_occ + s] ) * K[0, (k*n_virt + t) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, k*n_virt + t + n_ex]

										elif ((u != s) and (u != t) and (t != s) and (v == u)):

											L3[i*n_virt + s + n_ex] += (-8 * g[i, n_occ + s, j, n_occ + t] + 4 * g[i, n_occ + t, j, n_occ + s] ) * K[0, (k*n_virt + u) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, k*n_virt + u + n_ex]

	# This operator combination: {'a': 2, 'b': 3, 'c': 3}
	for j in range(n_occ):
		for i in range(n_occ):
			for m in range(n_occ):
				for k in range(n_occ):
					for n in range(n_occ):
						for t in range(n_virt):
							for s in range(n_virt):
								for v in range(n_virt):
									for u in range(n_virt):
										for w in range(n_virt):

											if ((j == i) and (m == i) and (k == i) and (n == i)):

												if ((t == s) and (v == s) and (u == s) and (w == s)):

													L3[(i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-8 * F[i, n_occ + s] ) * K[0, (i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] * K[1, i*n_virt + s + n_ex]

												elif ((t == s) and (v == s) and (u == s) and (w != s) and (w != t) and (w != u) and (w != v)):

													L3[(i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * F[i, n_occ + w] ) * K[0, (i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] * K[1, i*n_virt + w + n_ex]

												elif ((t == s) and (v != s) and (v != t) and (v != u) and (u == s) and (w == s)):

													L3[(i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-8 * g[i, n_occ + s, n_occ + s, n_occ + v] ) * K[0, (i*n_virt + v) * n_ex + i*n_virt + s+ 2*n_ex] * K[1, i*n_virt + s + n_ex]

												elif ((t == s) and (v != s) and (v != t) and (v != u) and (u == s) and (w == v)):

													L3[(i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, i, i, n_occ + s] + -4 * g[i, n_occ + v, n_occ + s, n_occ + v] + -4 * g[i, n_occ + s, n_occ + v, n_occ + v] ) * K[0, (i*n_virt + v) * n_ex + i*n_virt + s+ 2*n_ex] * K[1, i*n_virt + v + n_ex]

												elif ((t == s) and (v != s) and (v != t) and (v != u) and (u == s) and (w != s) and (w != t) and (w != u) and (w != v)):

													L3[(i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, n_occ + w, n_occ + s, n_occ + v] + -4 * g[i, n_occ + s, n_occ + v, n_occ + w] ) * K[0, (i*n_virt + v) * n_ex + i*n_virt + s+ 2*n_ex] * K[1, i*n_virt + w + n_ex]

												elif ((t == s) and (v == s) and (u != s) and (u != t) and (w == s)):

													L3[(i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * F[i, n_occ + u] + 4 * g[i, n_occ + u, n_occ + s, n_occ + s] + 4 * g[i, n_occ + s, n_occ + s, n_occ + u] + -4 * g[i, i, i, n_occ + u] ) * K[0, (i*n_virt + s) * n_ex + i*n_virt + u+ 2*n_ex] * K[1, i*n_virt + s + n_ex]

												elif ((t == s) and (v == s) and (u != s) and (u != t) and (w == u)):

													L3[(i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (8 * g[i, n_occ + u, n_occ + s, n_occ + u] ) * K[0, (i*n_virt + s) * n_ex + i*n_virt + u+ 2*n_ex] * K[1, i*n_virt + u + n_ex]

												elif ((t == s) and (v == s) and (u != s) and (u != t) and (w != s) and (w != t) and (w != u) and (w != v)):

													L3[(i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, n_occ + u, n_occ + s, n_occ + w] + 4 * g[i, n_occ + w, n_occ + s, n_occ + u] ) * K[0, (i*n_virt + s) * n_ex + i*n_virt + u+ 2*n_ex] * K[1, i*n_virt + w + n_ex]

												elif ((t != s) and (v == s) and (u == s) and (w == s)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (8 * g[i, n_occ + s, n_occ + s, n_occ + t] ) * K[0, (i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] * K[1, i*n_virt + s + n_ex]

												elif ((t != s) and (v == s) and (u == s) and (w == t)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * F[i, n_occ + s] + 4 * g[i, n_occ + s, n_occ + t, n_occ + t] + 4 * g[i, n_occ + t, n_occ + s, n_occ + t] + -4 * g[i, i, i, n_occ + s] ) * K[0, (i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] * K[1, i*n_virt + t + n_ex]

												elif ((t != s) and (v == s) and (u == s) and (w != s) and (w != t) and (w != u) and (w != v)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, n_occ + s, n_occ + t, n_occ + w] + 4 * g[i, n_occ + w, n_occ + s, n_occ + t] ) * K[0, (i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] * K[1, i*n_virt + w + n_ex]

												elif ((t != s) and (v == s) and (u == t) and (w == s)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * F[i, n_occ + s] + -8 * g[i, n_occ + s, n_occ + s, n_occ + s] + 4 * g[i, n_occ + t, n_occ + s, n_occ + t] + 4 * g[i, n_occ + s, n_occ + t, n_occ + t] + 4 * g[i, i, i, n_occ + s] ) * K[0, (i*n_virt + s) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, i*n_virt + s + n_ex]

												elif ((t != s) and (v == s) and (u == t) and (w == t)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-8 * F[i, n_occ + t] + -4 * g[i, i, i, n_occ + t] + -4 * g[i, n_occ + t, n_occ + s, n_occ + s] + -4 * g[i, n_occ + s, n_occ + s, n_occ + t] + 8 * g[i, n_occ + t, n_occ + t, n_occ + t] ) * K[0, (i*n_virt + s) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, i*n_virt + t + n_ex]

												elif ((t != s) and (v == s) and (u == t) and (w != s) and (w != t) and (w != u) and (w != v)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * F[i, n_occ + w] + -4 * g[i, n_occ + w, n_occ + s, n_occ + s] + -4 * g[i, n_occ + s, n_occ + s, n_occ + w] + 4 * g[i, n_occ + t, n_occ + t, n_occ + w] + 4 * g[i, n_occ + w, n_occ + t, n_occ + t] ) * K[0, (i*n_virt + s) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, i*n_virt + w + n_ex]

												elif ((t != s) and (v == t) and (u == t) and (w == s)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-8 * g[i, n_occ + s, n_occ + s, n_occ + t] ) * K[0, (i*n_virt + t) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, i*n_virt + s + n_ex]

												elif ((t != s) and (v == t) and (u == t) and (w == t)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, i, i, n_occ + s] + -4 * g[i, n_occ + t, n_occ + s, n_occ + t] + -4 * g[i, n_occ + s, n_occ + t, n_occ + t] ) * K[0, (i*n_virt + t) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, i*n_virt + t + n_ex]

												elif ((t != s) and (v == t) and (u == t) and (w != s) and (w != t) and (w != u) and (w != v)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, n_occ + w, n_occ + s, n_occ + t] + -4 * g[i, n_occ + s, n_occ + t, n_occ + w] ) * K[0, (i*n_virt + t) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, i*n_virt + w + n_ex]

												elif ((t != s) and (v != s) and (v != t) and (v != u) and (u == t) and (w == s)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-8 * g[i, n_occ + s, n_occ + s, n_occ + v] ) * K[0, (i*n_virt + v) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, i*n_virt + s + n_ex]

												elif ((t != s) and (v != s) and (v != t) and (v != u) and (u == t) and (w == t)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, n_occ + t, n_occ + s, n_occ + v] + -4 * g[i, n_occ + s, n_occ + t, n_occ + v] ) * K[0, (i*n_virt + v) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, i*n_virt + t + n_ex]

												elif ((t != s) and (v != s) and (v != t) and (v != u) and (u == t) and (w == v)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, i, i, n_occ + s] + -4 * g[i, n_occ + v, n_occ + s, n_occ + v] + -4 * g[i, n_occ + s, n_occ + v, n_occ + v] ) * K[0, (i*n_virt + v) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, i*n_virt + v + n_ex]

												elif ((t != s) and (v != s) and (v != t) and (v != u) and (u == t) and (w != s) and (w != t) and (w != u) and (w != v)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, n_occ + w, n_occ + s, n_occ + v] + -4 * g[i, n_occ + s, n_occ + v, n_occ + w] ) * K[0, (i*n_virt + v) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, i*n_virt + w + n_ex]

												elif ((t != s) and (v == s) and (u != s) and (u != t) and (w == s)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, n_occ + u, n_occ + s, n_occ + t] + 4 * g[i, n_occ + s, n_occ + t, n_occ + u] ) * K[0, (i*n_virt + s) * n_ex + i*n_virt + u+ 2*n_ex] * K[1, i*n_virt + s + n_ex]

												elif ((t != s) and (v == s) and (u != s) and (u != t) and (w == t)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * F[i, n_occ + u] + 4 * g[i, n_occ + u, n_occ + t, n_occ + t] + 4 * g[i, n_occ + t, n_occ + t, n_occ + u] + -4 * g[i, i, i, n_occ + u] ) * K[0, (i*n_virt + s) * n_ex + i*n_virt + u+ 2*n_ex] * K[1, i*n_virt + t + n_ex]

												elif ((t != s) and (v == s) and (u != s) and (u != t) and (w == u)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (8 * g[i, n_occ + u, n_occ + t, n_occ + u] ) * K[0, (i*n_virt + s) * n_ex + i*n_virt + u+ 2*n_ex] * K[1, i*n_virt + u + n_ex]

												elif ((t != s) and (v == s) and (u != s) and (u != t) and (w != s) and (w != t) and (w != u) and (w != v)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, n_occ + u, n_occ + t, n_occ + w] + 4 * g[i, n_occ + w, n_occ + t, n_occ + u] ) * K[0, (i*n_virt + s) * n_ex + i*n_virt + u+ 2*n_ex] * K[1, i*n_virt + w + n_ex]

											elif ((j == i) and (m == i) and (k == i) and (n != i) and (n != j) and (n != k) and (n != m)):

												if ((t == s) and (v == s) and (u == s) and (w == s)):

													L3[(i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * F[n, n_occ + s] ) * K[0, (i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] * K[1, n*n_virt + s + n_ex]

												elif ((t == s) and (v != s) and (v != t) and (v != u) and (u == s) and (w == s)):

													L3[(i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[n, n_occ + s, n_occ + s, n_occ + v] ) * K[0, (i*n_virt + v) * n_ex + i*n_virt + s+ 2*n_ex] * K[1, n*n_virt + s + n_ex]

												elif ((t == s) and (v != s) and (v != t) and (v != u) and (u == s) and (w == v)):

													L3[(i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (8 * g[i, n, i, n_occ + s] + -4 * g[i, i, n, n_occ + s] + -8 * g[n, n_occ + v, n_occ + s, n_occ + v] + 4 * g[n, n_occ + s, n_occ + v, n_occ + v] ) * K[0, (i*n_virt + v) * n_ex + i*n_virt + s+ 2*n_ex] * K[1, n*n_virt + v + n_ex]

												elif ((t == s) and (v != s) and (v != t) and (v != u) and (u == s) and (w != s) and (w != t) and (w != u) and (w != v)):

													L3[(i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[n, n_occ + s, n_occ + v, n_occ + w] + -8 * g[n, n_occ + w, n_occ + s, n_occ + v] ) * K[0, (i*n_virt + v) * n_ex + i*n_virt + s+ 2*n_ex] * K[1, n*n_virt + w + n_ex]

												elif ((t == s) and (v == s) and (u != s) and (u != t) and (w == s)):

													L3[(i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * F[n, n_occ + u] + 8 * g[n, n_occ + s, n_occ + s, n_occ + u] + -4 * g[n, n_occ + u, n_occ + s, n_occ + s] + 4 * g[i, i, n, n_occ + u] + -8 * g[i, n, i, n_occ + u] ) * K[0, (i*n_virt + s) * n_ex + i*n_virt + u+ 2*n_ex] * K[1, n*n_virt + s + n_ex]

												elif ((t == s) and (v == s) and (u != s) and (u != t) and (w == u)):

													L3[(i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[n, n_occ + u, n_occ + s, n_occ + u] ) * K[0, (i*n_virt + s) * n_ex + i*n_virt + u+ 2*n_ex] * K[1, n*n_virt + u + n_ex]

												elif ((t == s) and (v == s) and (u != s) and (u != t) and (w != s) and (w != t) and (w != u) and (w != v)):

													L3[(i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[n, n_occ + u, n_occ + s, n_occ + w] + 8 * g[n, n_occ + w, n_occ + s, n_occ + u] ) * K[0, (i*n_virt + s) * n_ex + i*n_virt + u+ 2*n_ex] * K[1, n*n_virt + w + n_ex]

												elif ((t != s) and (v == s) and (u == s) and (w == s)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[n, n_occ + s, n_occ + s, n_occ + t] ) * K[0, (i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] * K[1, n*n_virt + s + n_ex]

												elif ((t != s) and (v == s) and (u == s) and (w == t)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * F[n, n_occ + s] + 8 * g[n, n_occ + t, n_occ + s, n_occ + t] + -4 * g[n, n_occ + s, n_occ + t, n_occ + t] + 4 * g[i, i, n, n_occ + s] + -8 * g[i, n, i, n_occ + s] ) * K[0, (i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] * K[1, n*n_virt + t + n_ex]

												elif ((t != s) and (v == s) and (u == s) and (w != s) and (w != t) and (w != u) and (w != v)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[n, n_occ + s, n_occ + t, n_occ + w] + 8 * g[n, n_occ + w, n_occ + s, n_occ + t] ) * K[0, (i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] * K[1, n*n_virt + w + n_ex]

												elif ((t != s) and (v == s) and (u == t) and (w == s)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (8 * g[i, n, i, n_occ + s] + -4 * g[i, i, n, n_occ + s] + -4 * g[n, n_occ + s, n_occ + s, n_occ + s] + -4 * g[n, n_occ + t, n_occ + s, n_occ + t] + 8 * g[n, n_occ + s, n_occ + t, n_occ + t] ) * K[0, (i*n_virt + s) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, n*n_virt + s + n_ex]

												elif ((t != s) and (v == s) and (u == t) and (w == t)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * F[n, n_occ + t] + 4 * g[n, n_occ + s, n_occ + s, n_occ + t] + -8 * g[n, n_occ + t, n_occ + s, n_occ + s] + 4 * g[i, i, n, n_occ + t] + 4 * g[n, n_occ + t, n_occ + t, n_occ + t] + -8 * g[i, n, i, n_occ + t] ) * K[0, (i*n_virt + s) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, n*n_virt + t + n_ex]

												elif ((t != s) and (v == s) and (u == t) and (w != s) and (w != t) and (w != u) and (w != v)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[n, n_occ + s, n_occ + s, n_occ + w] + -8 * g[n, n_occ + w, n_occ + s, n_occ + s] + -4 * g[n, n_occ + t, n_occ + t, n_occ + w] + 8 * g[n, n_occ + w, n_occ + t, n_occ + t] ) * K[0, (i*n_virt + s) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, n*n_virt + w + n_ex]

												elif ((t != s) and (v == t) and (u == t) and (w == s)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[n, n_occ + s, n_occ + s, n_occ + t] ) * K[0, (i*n_virt + t) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, n*n_virt + s + n_ex]

												elif ((t != s) and (v == t) and (u == t) and (w == t)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (8 * g[i, n, i, n_occ + s] + -4 * g[i, i, n, n_occ + s] + -8 * g[n, n_occ + t, n_occ + s, n_occ + t] + 4 * g[n, n_occ + s, n_occ + t, n_occ + t] ) * K[0, (i*n_virt + t) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, n*n_virt + t + n_ex]

												elif ((t != s) and (v == t) and (u == t) and (w != s) and (w != t) and (w != u) and (w != v)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[n, n_occ + s, n_occ + t, n_occ + w] + -8 * g[n, n_occ + w, n_occ + s, n_occ + t] ) * K[0, (i*n_virt + t) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, n*n_virt + w + n_ex]

												elif ((t != s) and (v != s) and (v != t) and (v != u) and (u == t) and (w == s)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[n, n_occ + s, n_occ + s, n_occ + v] ) * K[0, (i*n_virt + v) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, n*n_virt + s + n_ex]

												elif ((t != s) and (v != s) and (v != t) and (v != u) and (u == t) and (w == t)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[n, n_occ + s, n_occ + t, n_occ + v] + -8 * g[n, n_occ + t, n_occ + s, n_occ + v] ) * K[0, (i*n_virt + v) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, n*n_virt + t + n_ex]

												elif ((t != s) and (v != s) and (v != t) and (v != u) and (u == t) and (w == v)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (8 * g[i, n, i, n_occ + s] + -4 * g[i, i, n, n_occ + s] + -8 * g[n, n_occ + v, n_occ + s, n_occ + v] + 4 * g[n, n_occ + s, n_occ + v, n_occ + v] ) * K[0, (i*n_virt + v) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, n*n_virt + v + n_ex]

												elif ((t != s) and (v != s) and (v != t) and (v != u) and (u == t) and (w != s) and (w != t) and (w != u) and (w != v)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[n, n_occ + s, n_occ + v, n_occ + w] + -8 * g[n, n_occ + w, n_occ + s, n_occ + v] ) * K[0, (i*n_virt + v) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, n*n_virt + w + n_ex]

												elif ((t != s) and (v == s) and (u != s) and (u != t) and (w == s)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (8 * g[n, n_occ + s, n_occ + t, n_occ + u] + -4 * g[n, n_occ + u, n_occ + s, n_occ + t] ) * K[0, (i*n_virt + s) * n_ex + i*n_virt + u+ 2*n_ex] * K[1, n*n_virt + s + n_ex]

												elif ((t != s) and (v == s) and (u != s) and (u != t) and (w == t)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * F[n, n_occ + u] + 8 * g[n, n_occ + t, n_occ + t, n_occ + u] + -4 * g[n, n_occ + u, n_occ + t, n_occ + t] + 4 * g[i, i, n, n_occ + u] + -8 * g[i, n, i, n_occ + u] ) * K[0, (i*n_virt + s) * n_ex + i*n_virt + u+ 2*n_ex] * K[1, n*n_virt + t + n_ex]

												elif ((t != s) and (v == s) and (u != s) and (u != t) and (w == u)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[n, n_occ + u, n_occ + t, n_occ + u] ) * K[0, (i*n_virt + s) * n_ex + i*n_virt + u+ 2*n_ex] * K[1, n*n_virt + u + n_ex]

												elif ((t != s) and (v == s) and (u != s) and (u != t) and (w != s) and (w != t) and (w != u) and (w != v)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[n, n_occ + u, n_occ + t, n_occ + w] + 8 * g[n, n_occ + w, n_occ + t, n_occ + u] ) * K[0, (i*n_virt + s) * n_ex + i*n_virt + u+ 2*n_ex] * K[1, n*n_virt + w + n_ex]

											elif ((j == i) and (m != i) and (m != j) and (m != k) and (k == i) and (n == i)):

												if ((t == s) and (v == s) and (u == s) and (w == s)):

													L3[(i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (8 * g[i, m, i, n_occ + s] ) * K[0, (m*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] * K[1, i*n_virt + s + n_ex]

												elif ((t == s) and (v == s) and (u == s) and (w != s) and (w != t) and (w != u) and (w != v)):

													L3[(i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, m, i, n_occ + w] ) * K[0, (m*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] * K[1, i*n_virt + w + n_ex]

												elif ((t == s) and (v != s) and (v != t) and (v != u) and (u == s) and (w == v)):

													L3[(i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, m, i, n_occ + s] ) * K[0, (m*n_virt + v) * n_ex + i*n_virt + s+ 2*n_ex] * K[1, i*n_virt + v + n_ex]

												elif ((t != s) and (v == s) and (u == t) and (w == s)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (8 * g[i, m, i, n_occ + s] ) * K[0, (m*n_virt + s) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, i*n_virt + s + n_ex]

												elif ((t != s) and (v == s) and (u == t) and (w == t)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, m, i, n_occ + t] ) * K[0, (m*n_virt + s) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, i*n_virt + t + n_ex]

												elif ((t != s) and (v == s) and (u == t) and (w != s) and (w != t) and (w != u) and (w != v)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, m, i, n_occ + w] ) * K[0, (m*n_virt + s) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, i*n_virt + w + n_ex]

												elif ((t != s) and (v == t) and (u == t) and (w == t)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, m, i, n_occ + s] ) * K[0, (m*n_virt + t) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, i*n_virt + t + n_ex]

												elif ((t != s) and (v != s) and (v != t) and (v != u) and (u == t) and (w == v)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, m, i, n_occ + s] ) * K[0, (m*n_virt + v) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, i*n_virt + v + n_ex]

											elif ((j == i) and (m != i) and (m != j) and (m != k) and (k == i) and (n == m)):

												if ((t == s) and (v == s) and (u == s) and (w == s)):

													L3[(i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, n_occ + s, m, m] + -4 * g[i, n_occ + s, n_occ + s, n_occ + s] + 4 * g[i, m, m, n_occ + s] ) * K[0, (m*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] * K[1, m*n_virt + s + n_ex]

												elif ((t == s) and (v == s) and (u == s) and (w != s) and (w != t) and (w != u) and (w != v)):

													L3[(i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (8 * g[i, m, m, n_occ + w] + -4 * g[i, n_occ + w, m, m] + -8 * g[i, n_occ + s, n_occ + s, n_occ + w] + 4 * g[i, n_occ + w, n_occ + s, n_occ + s] ) * K[0, (m*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] * K[1, m*n_virt + w + n_ex]

												elif ((t == s) and (v != s) and (v != t) and (v != u) and (u == s) and (w == s)):

													L3[(i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, n_occ + s, n_occ + s, n_occ + v] ) * K[0, (m*n_virt + v) * n_ex + i*n_virt + s+ 2*n_ex] * K[1, m*n_virt + s + n_ex]

												elif ((t == s) and (v != s) and (v != t) and (v != u) and (u == s) and (w == v)):

													L3[(i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, m, m, n_occ + s] + 8 * g[i, n_occ + s, m, m] + 4 * g[i, n_occ + v, n_occ + s, n_occ + v] + -8 * g[i, n_occ + s, n_occ + v, n_occ + v] ) * K[0, (m*n_virt + v) * n_ex + i*n_virt + s+ 2*n_ex] * K[1, m*n_virt + v + n_ex]

												elif ((t == s) and (v != s) and (v != t) and (v != u) and (u == s) and (w != s) and (w != t) and (w != u) and (w != v)):

													L3[(i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-8 * g[i, n_occ + s, n_occ + v, n_occ + w] + 4 * g[i, n_occ + w, n_occ + s, n_occ + v] ) * K[0, (m*n_virt + v) * n_ex + i*n_virt + s+ 2*n_ex] * K[1, m*n_virt + w + n_ex]

												elif ((t != s) and (v == s) and (u == t) and (w == s)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, n_occ + s, m, m] + -4 * g[i, n_occ + s, n_occ + s, n_occ + s] + 4 * g[i, m, m, n_occ + s] ) * K[0, (m*n_virt + s) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, m*n_virt + s + n_ex]

												elif ((t != s) and (v == s) and (u == t) and (w == t)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (8 * g[i, m, m, n_occ + t] + -4 * g[i, n_occ + t, m, m] + -8 * g[i, n_occ + s, n_occ + s, n_occ + t] + 4 * g[i, n_occ + t, n_occ + s, n_occ + s] ) * K[0, (m*n_virt + s) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, m*n_virt + t + n_ex]

												elif ((t != s) and (v == s) and (u == t) and (w != s) and (w != t) and (w != u) and (w != v)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (8 * g[i, m, m, n_occ + w] + -4 * g[i, n_occ + w, m, m] + -8 * g[i, n_occ + s, n_occ + s, n_occ + w] + 4 * g[i, n_occ + w, n_occ + s, n_occ + s] ) * K[0, (m*n_virt + s) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, m*n_virt + w + n_ex]

												elif ((t != s) and (v == t) and (u == t) and (w == s)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, n_occ + s, n_occ + s, n_occ + t] ) * K[0, (m*n_virt + t) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, m*n_virt + s + n_ex]

												elif ((t != s) and (v == t) and (u == t) and (w == t)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, m, m, n_occ + s] + 8 * g[i, n_occ + s, m, m] + 4 * g[i, n_occ + t, n_occ + s, n_occ + t] + -8 * g[i, n_occ + s, n_occ + t, n_occ + t] ) * K[0, (m*n_virt + t) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, m*n_virt + t + n_ex]

												elif ((t != s) and (v == t) and (u == t) and (w != s) and (w != t) and (w != u) and (w != v)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-8 * g[i, n_occ + s, n_occ + t, n_occ + w] + 4 * g[i, n_occ + w, n_occ + s, n_occ + t] ) * K[0, (m*n_virt + t) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, m*n_virt + w + n_ex]

												elif ((t != s) and (v != s) and (v != t) and (v != u) and (u == t) and (w == s)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, n_occ + s, n_occ + s, n_occ + v] ) * K[0, (m*n_virt + v) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, m*n_virt + s + n_ex]

												elif ((t != s) and (v != s) and (v != t) and (v != u) and (u == t) and (w == t)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-8 * g[i, n_occ + s, n_occ + t, n_occ + v] + 4 * g[i, n_occ + t, n_occ + s, n_occ + v] ) * K[0, (m*n_virt + v) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, m*n_virt + t + n_ex]

												elif ((t != s) and (v != s) and (v != t) and (v != u) and (u == t) and (w == v)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, m, m, n_occ + s] + 8 * g[i, n_occ + s, m, m] + 4 * g[i, n_occ + v, n_occ + s, n_occ + v] + -8 * g[i, n_occ + s, n_occ + v, n_occ + v] ) * K[0, (m*n_virt + v) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, m*n_virt + v + n_ex]

												elif ((t != s) and (v != s) and (v != t) and (v != u) and (u == t) and (w != s) and (w != t) and (w != u) and (w != v)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-8 * g[i, n_occ + s, n_occ + v, n_occ + w] + 4 * g[i, n_occ + w, n_occ + s, n_occ + v] ) * K[0, (m*n_virt + v) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, m*n_virt + w + n_ex]

											elif ((j == i) and (m != i) and (m != j) and (m != k) and (k == i) and (n != i) and (n != j) and (n != k) and (n != m)):

												if ((t == s) and (v == s) and (u == s) and (w == s)):

													L3[(i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, m, n, n_occ + s] + 4 * g[i, n_occ + s, m, n] ) * K[0, (m*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] * K[1, n*n_virt + s + n_ex]

												elif ((t == s) and (v == s) and (u == s) and (w != s) and (w != t) and (w != u) and (w != v)):

													L3[(i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (8 * g[i, m, n, n_occ + w] + -4 * g[i, n_occ + w, m, n] ) * K[0, (m*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] * K[1, n*n_virt + w + n_ex]

												elif ((t == s) and (v != s) and (v != t) and (v != u) and (u == s) and (w == v)):

													L3[(i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, m, n, n_occ + s] + 8 * g[i, n_occ + s, m, n] ) * K[0, (m*n_virt + v) * n_ex + i*n_virt + s+ 2*n_ex] * K[1, n*n_virt + v + n_ex]

												elif ((t != s) and (v == s) and (u == t) and (w == s)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, m, n, n_occ + s] + 4 * g[i, n_occ + s, m, n] ) * K[0, (m*n_virt + s) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, n*n_virt + s + n_ex]

												elif ((t != s) and (v == s) and (u == t) and (w == t)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (8 * g[i, m, n, n_occ + t] + -4 * g[i, n_occ + t, m, n] ) * K[0, (m*n_virt + s) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, n*n_virt + t + n_ex]

												elif ((t != s) and (v == s) and (u == t) and (w != s) and (w != t) and (w != u) and (w != v)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (8 * g[i, m, n, n_occ + w] + -4 * g[i, n_occ + w, m, n] ) * K[0, (m*n_virt + s) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, n*n_virt + w + n_ex]

												elif ((t != s) and (v == t) and (u == t) and (w == t)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, m, n, n_occ + s] + 8 * g[i, n_occ + s, m, n] ) * K[0, (m*n_virt + t) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, n*n_virt + t + n_ex]

												elif ((t != s) and (v != s) and (v != t) and (v != u) and (u == t) and (w == v)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, m, n, n_occ + s] + 8 * g[i, n_occ + s, m, n] ) * K[0, (m*n_virt + v) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, n*n_virt + v + n_ex]

											elif ((j == i) and (m == i) and (k != i) and (k != j) and (n == i)):

												if ((t == s) and (v == s) and (u == s) and (w == s)):

													L3[(i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * F[k, n_occ + s] + -4 * g[i, i, k, n_occ + s] + 4 * g[k, n_occ + s, n_occ + s, n_occ + s] + -4 * g[i, k, i, n_occ + s] ) * K[0, (i*n_virt + s) * n_ex + k*n_virt + s+ 2*n_ex] * K[1, i*n_virt + s + n_ex]

												elif ((t == s) and (v == s) and (u == s) and (w != s) and (w != t) and (w != u) and (w != v)):

													L3[(i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * F[k, n_occ + w] + 8 * g[k, n_occ + s, n_occ + s, n_occ + w] + -4 * g[k, n_occ + w, n_occ + s, n_occ + s] + 4 * g[i, i, k, n_occ + w] + -8 * g[i, k, i, n_occ + w] ) * K[0, (i*n_virt + s) * n_ex + k*n_virt + s+ 2*n_ex] * K[1, i*n_virt + w + n_ex]

												elif ((t == s) and (v == s) and (u != s) and (u != t) and (w == s)):

													L3[(i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, k, i, n_occ + u] + -8 * g[i, i, k, n_occ + u] + -4 * g[k, n_occ + s, n_occ + s, n_occ + u] + 8 * g[k, n_occ + u, n_occ + s, n_occ + s] ) * K[0, (i*n_virt + s) * n_ex + k*n_virt + u+ 2*n_ex] * K[1, i*n_virt + s + n_ex]

												elif ((t == s) and (v == s) and (u != s) and (u != t) and (w == u)):

													L3[(i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[k, n_occ + u, n_occ + s, n_occ + u] ) * K[0, (i*n_virt + s) * n_ex + k*n_virt + u+ 2*n_ex] * K[1, i*n_virt + u + n_ex]

												elif ((t == s) and (v == s) and (u != s) and (u != t) and (w != s) and (w != t) and (w != u) and (w != v)):

													L3[(i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (8 * g[k, n_occ + u, n_occ + s, n_occ + w] + -4 * g[k, n_occ + w, n_occ + s, n_occ + u] ) * K[0, (i*n_virt + s) * n_ex + k*n_virt + u+ 2*n_ex] * K[1, i*n_virt + w + n_ex]

												elif ((t != s) and (v == s) and (u == s) and (w == s)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[k, n_occ + s, n_occ + s, n_occ + t] ) * K[0, (i*n_virt + s) * n_ex + k*n_virt + s+ 2*n_ex] * K[1, i*n_virt + s + n_ex]

												elif ((t != s) and (v == s) and (u == s) and (w == t)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, k, i, n_occ + s] + -8 * g[i, i, k, n_occ + s] + -4 * g[k, n_occ + t, n_occ + s, n_occ + t] + 8 * g[k, n_occ + s, n_occ + t, n_occ + t] ) * K[0, (i*n_virt + s) * n_ex + k*n_virt + s+ 2*n_ex] * K[1, i*n_virt + t + n_ex]

												elif ((t != s) and (v == s) and (u == s) and (w != s) and (w != t) and (w != u) and (w != v)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (8 * g[k, n_occ + s, n_occ + t, n_occ + w] + -4 * g[k, n_occ + w, n_occ + s, n_occ + t] ) * K[0, (i*n_virt + s) * n_ex + k*n_virt + s+ 2*n_ex] * K[1, i*n_virt + w + n_ex]

												elif ((t != s) and (v == s) and (u == t) and (w == s)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * F[k, n_occ + s] + 8 * g[k, n_occ + t, n_occ + s, n_occ + t] + -4 * g[k, n_occ + s, n_occ + t, n_occ + t] + 4 * g[i, i, k, n_occ + s] + -8 * g[i, k, i, n_occ + s] ) * K[0, (i*n_virt + s) * n_ex + k*n_virt + t+ 2*n_ex] * K[1, i*n_virt + s + n_ex]

												elif ((t != s) and (v == s) and (u == t) and (w == t)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * F[k, n_occ + t] + -4 * g[i, i, k, n_occ + t] + 4 * g[k, n_occ + t, n_occ + t, n_occ + t] + -4 * g[i, k, i, n_occ + t] ) * K[0, (i*n_virt + s) * n_ex + k*n_virt + t+ 2*n_ex] * K[1, i*n_virt + t + n_ex]

												elif ((t != s) and (v == s) and (u == t) and (w != s) and (w != t) and (w != u) and (w != v)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * F[k, n_occ + w] + 8 * g[k, n_occ + t, n_occ + t, n_occ + w] + -4 * g[k, n_occ + w, n_occ + t, n_occ + t] + 4 * g[i, i, k, n_occ + w] + -8 * g[i, k, i, n_occ + w] ) * K[0, (i*n_virt + s) * n_ex + k*n_virt + t+ 2*n_ex] * K[1, i*n_virt + w + n_ex]

												elif ((t != s) and (v == s) and (u != s) and (u != t) and (w == s)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[k, n_occ + s, n_occ + t, n_occ + u] + 8 * g[k, n_occ + u, n_occ + s, n_occ + t] ) * K[0, (i*n_virt + s) * n_ex + k*n_virt + u+ 2*n_ex] * K[1, i*n_virt + s + n_ex]

												elif ((t != s) and (v == s) and (u != s) and (u != t) and (w == t)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, k, i, n_occ + u] + -8 * g[i, i, k, n_occ + u] + -4 * g[k, n_occ + t, n_occ + t, n_occ + u] + 8 * g[k, n_occ + u, n_occ + t, n_occ + t] ) * K[0, (i*n_virt + s) * n_ex + k*n_virt + u+ 2*n_ex] * K[1, i*n_virt + t + n_ex]

												elif ((t != s) and (v == s) and (u != s) and (u != t) and (w == u)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[k, n_occ + u, n_occ + t, n_occ + u] ) * K[0, (i*n_virt + s) * n_ex + k*n_virt + u+ 2*n_ex] * K[1, i*n_virt + u + n_ex]

												elif ((t != s) and (v == s) and (u != s) and (u != t) and (w != s) and (w != t) and (w != u) and (w != v)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (8 * g[k, n_occ + u, n_occ + t, n_occ + w] + -4 * g[k, n_occ + w, n_occ + t, n_occ + u] ) * K[0, (i*n_virt + s) * n_ex + k*n_virt + u+ 2*n_ex] * K[1, i*n_virt + w + n_ex]

											elif ((j == i) and (m == i) and (k != i) and (k != j) and (n == k)):

												if ((t == s) and (v == s) and (u == s) and (w == s)):

													L3[(i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-8 * g[i, k, k, n_occ + s] ) * K[0, (i*n_virt + s) * n_ex + k*n_virt + s+ 2*n_ex] * K[1, k*n_virt + s + n_ex]

												elif ((t == s) and (v == s) and (u == s) and (w != s) and (w != t) and (w != u) and (w != v)):

													L3[(i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, k, k, n_occ + w] ) * K[0, (i*n_virt + s) * n_ex + k*n_virt + s+ 2*n_ex] * K[1, k*n_virt + w + n_ex]

												elif ((t == s) and (v == s) and (u != s) and (u != t) and (w == s)):

													L3[(i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, k, k, n_occ + u] ) * K[0, (i*n_virt + s) * n_ex + k*n_virt + u+ 2*n_ex] * K[1, k*n_virt + s + n_ex]

												elif ((t != s) and (v == s) and (u == s) and (w == t)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, k, k, n_occ + s] ) * K[0, (i*n_virt + s) * n_ex + k*n_virt + s+ 2*n_ex] * K[1, k*n_virt + t + n_ex]

												elif ((t != s) and (v == s) and (u == t) and (w == s)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, k, k, n_occ + s] ) * K[0, (i*n_virt + s) * n_ex + k*n_virt + t+ 2*n_ex] * K[1, k*n_virt + s + n_ex]

												elif ((t != s) and (v == s) and (u == t) and (w == t)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-8 * g[i, k, k, n_occ + t] ) * K[0, (i*n_virt + s) * n_ex + k*n_virt + t+ 2*n_ex] * K[1, k*n_virt + t + n_ex]

												elif ((t != s) and (v == s) and (u == t) and (w != s) and (w != t) and (w != u) and (w != v)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, k, k, n_occ + w] ) * K[0, (i*n_virt + s) * n_ex + k*n_virt + t+ 2*n_ex] * K[1, k*n_virt + w + n_ex]

												elif ((t != s) and (v == s) and (u != s) and (u != t) and (w == t)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, k, k, n_occ + u] ) * K[0, (i*n_virt + s) * n_ex + k*n_virt + u+ 2*n_ex] * K[1, k*n_virt + t + n_ex]

											elif ((j == i) and (m == i) and (k != i) and (k != j) and (n != i) and (n != j) and (n != k) and (n != m)):

												if ((t == s) and (v == s) and (u == s) and (w == s)):

													L3[(i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, n, k, n_occ + s] + -4 * g[i, k, n, n_occ + s] ) * K[0, (i*n_virt + s) * n_ex + k*n_virt + s+ 2*n_ex] * K[1, n*n_virt + s + n_ex]

												elif ((t == s) and (v == s) and (u == s) and (w != s) and (w != t) and (w != u) and (w != v)):

													L3[(i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-8 * g[i, k, n, n_occ + w] + 4 * g[i, n, k, n_occ + w] ) * K[0, (i*n_virt + s) * n_ex + k*n_virt + s+ 2*n_ex] * K[1, n*n_virt + w + n_ex]

												elif ((t == s) and (v == s) and (u != s) and (u != t) and (w == s)):

													L3[(i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, k, n, n_occ + u] + -8 * g[i, n, k, n_occ + u] ) * K[0, (i*n_virt + s) * n_ex + k*n_virt + u+ 2*n_ex] * K[1, n*n_virt + s + n_ex]

												elif ((t != s) and (v == s) and (u == s) and (w == t)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, k, n, n_occ + s] + -8 * g[i, n, k, n_occ + s] ) * K[0, (i*n_virt + s) * n_ex + k*n_virt + s+ 2*n_ex] * K[1, n*n_virt + t + n_ex]

												elif ((t != s) and (v == s) and (u == t) and (w == s)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-8 * g[i, k, n, n_occ + s] + 4 * g[i, n, k, n_occ + s] ) * K[0, (i*n_virt + s) * n_ex + k*n_virt + t+ 2*n_ex] * K[1, n*n_virt + s + n_ex]

												elif ((t != s) and (v == s) and (u == t) and (w == t)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, n, k, n_occ + t] + -4 * g[i, k, n, n_occ + t] ) * K[0, (i*n_virt + s) * n_ex + k*n_virt + t+ 2*n_ex] * K[1, n*n_virt + t + n_ex]

												elif ((t != s) and (v == s) and (u == t) and (w != s) and (w != t) and (w != u) and (w != v)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-8 * g[i, k, n, n_occ + w] + 4 * g[i, n, k, n_occ + w] ) * K[0, (i*n_virt + s) * n_ex + k*n_virt + t+ 2*n_ex] * K[1, n*n_virt + w + n_ex]

												elif ((t != s) and (v == s) and (u != s) and (u != t) and (w == t)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, k, n, n_occ + u] + -8 * g[i, n, k, n_occ + u] ) * K[0, (i*n_virt + s) * n_ex + k*n_virt + u+ 2*n_ex] * K[1, n*n_virt + t + n_ex]

											elif ((j != i) and (m == i) and (k == i) and (n == i)):

												if ((t == s) and (v == s) and (u == s) and (w == s)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-8 * g[i, j, i, n_occ + s] ) * K[0, (i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] * K[1, i*n_virt + s + n_ex]

												elif ((t == s) and (v == s) and (u == s) and (w != s) and (w != t) and (w != u) and (w != v)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, j, i, n_occ + w] ) * K[0, (i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] * K[1, i*n_virt + w + n_ex]

												elif ((t == s) and (v == s) and (u != s) and (u != t) and (w == s)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, j, i, n_occ + u] ) * K[0, (i*n_virt + s) * n_ex + i*n_virt + u+ 2*n_ex] * K[1, i*n_virt + s + n_ex]

												elif ((t != s) and (v == s) and (u == s) and (w == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, j, i, n_occ + s] ) * K[0, (i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] * K[1, i*n_virt + t + n_ex]

												elif ((t != s) and (v == s) and (u == t) and (w == s)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, j, i, n_occ + s] ) * K[0, (i*n_virt + s) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, i*n_virt + s + n_ex]

												elif ((t != s) and (v == s) and (u == t) and (w == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-8 * g[i, j, i, n_occ + t] ) * K[0, (i*n_virt + s) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, i*n_virt + t + n_ex]

												elif ((t != s) and (v == s) and (u == t) and (w != s) and (w != t) and (w != u) and (w != v)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, j, i, n_occ + w] ) * K[0, (i*n_virt + s) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, i*n_virt + w + n_ex]

												elif ((t != s) and (v == s) and (u != s) and (u != t) and (w == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, j, i, n_occ + u] ) * K[0, (i*n_virt + s) * n_ex + i*n_virt + u+ 2*n_ex] * K[1, i*n_virt + t + n_ex]

											elif ((j != i) and (m == i) and (k == i) and (n == j)):

												if ((t == s) and (v == s) and (u == s) and (w == s)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * F[i, n_occ + s] + -4 * g[i, n_occ + s, j, j] + 4 * g[i, n_occ + s, n_occ + s, n_occ + s] + -4 * g[i, j, j, n_occ + s] ) * K[0, (i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] * K[1, j*n_virt + s + n_ex]

												elif ((t == s) and (v == s) and (u == s) and (w != s) and (w != t) and (w != u) and (w != v)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * F[i, n_occ + w] + 8 * g[i, n_occ + s, n_occ + s, n_occ + w] + -4 * g[i, n_occ + w, n_occ + s, n_occ + s] + 4 * g[i, n_occ + w, j, j] + -8 * g[i, j, j, n_occ + w] ) * K[0, (i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] * K[1, j*n_virt + w + n_ex]

												elif ((t == s) and (v == s) and (u != s) and (u != t) and (w == s)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, j, j, n_occ + u] + -8 * g[i, n_occ + u, j, j] + -4 * g[i, n_occ + s, n_occ + s, n_occ + u] + 8 * g[i, n_occ + u, n_occ + s, n_occ + s] ) * K[0, (i*n_virt + s) * n_ex + i*n_virt + u+ 2*n_ex] * K[1, j*n_virt + s + n_ex]

												elif ((t == s) and (v == s) and (u != s) and (u != t) and (w == u)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, n_occ + u, n_occ + s, n_occ + u] ) * K[0, (i*n_virt + s) * n_ex + i*n_virt + u+ 2*n_ex] * K[1, j*n_virt + u + n_ex]

												elif ((t == s) and (v == s) and (u != s) and (u != t) and (w != s) and (w != t) and (w != u) and (w != v)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (8 * g[i, n_occ + u, n_occ + s, n_occ + w] + -4 * g[i, n_occ + w, n_occ + s, n_occ + u] ) * K[0, (i*n_virt + s) * n_ex + i*n_virt + u+ 2*n_ex] * K[1, j*n_virt + w + n_ex]

												elif ((t != s) and (v == s) and (u == s) and (w == s)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, n_occ + s, n_occ + s, n_occ + t] ) * K[0, (i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] * K[1, j*n_virt + s + n_ex]

												elif ((t != s) and (v == s) and (u == s) and (w == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, j, j, n_occ + s] + -8 * g[i, n_occ + s, j, j] + -4 * g[i, n_occ + t, n_occ + s, n_occ + t] + 8 * g[i, n_occ + s, n_occ + t, n_occ + t] ) * K[0, (i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] * K[1, j*n_virt + t + n_ex]

												elif ((t != s) and (v == s) and (u == s) and (w != s) and (w != t) and (w != u) and (w != v)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (8 * g[i, n_occ + s, n_occ + t, n_occ + w] + -4 * g[i, n_occ + w, n_occ + s, n_occ + t] ) * K[0, (i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] * K[1, j*n_virt + w + n_ex]

												elif ((t != s) and (v == s) and (u == t) and (w == s)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * F[i, n_occ + s] + 8 * g[i, n_occ + t, n_occ + s, n_occ + t] + -4 * g[i, n_occ + s, n_occ + t, n_occ + t] + 4 * g[i, n_occ + s, j, j] + -8 * g[i, j, j, n_occ + s] ) * K[0, (i*n_virt + s) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, j*n_virt + s + n_ex]

												elif ((t != s) and (v == s) and (u == t) and (w == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * F[i, n_occ + t] + -4 * g[i, n_occ + t, j, j] + 4 * g[i, n_occ + t, n_occ + t, n_occ + t] + -4 * g[i, j, j, n_occ + t] ) * K[0, (i*n_virt + s) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, j*n_virt + t + n_ex]

												elif ((t != s) and (v == s) and (u == t) and (w != s) and (w != t) and (w != u) and (w != v)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * F[i, n_occ + w] + 8 * g[i, n_occ + t, n_occ + t, n_occ + w] + -4 * g[i, n_occ + w, n_occ + t, n_occ + t] + 4 * g[i, n_occ + w, j, j] + -8 * g[i, j, j, n_occ + w] ) * K[0, (i*n_virt + s) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, j*n_virt + w + n_ex]

												elif ((t != s) and (v == s) and (u != s) and (u != t) and (w == s)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, n_occ + s, n_occ + t, n_occ + u] + 8 * g[i, n_occ + u, n_occ + s, n_occ + t] ) * K[0, (i*n_virt + s) * n_ex + i*n_virt + u+ 2*n_ex] * K[1, j*n_virt + s + n_ex]

												elif ((t != s) and (v == s) and (u != s) and (u != t) and (w == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, j, j, n_occ + u] + -8 * g[i, n_occ + u, j, j] + -4 * g[i, n_occ + t, n_occ + t, n_occ + u] + 8 * g[i, n_occ + u, n_occ + t, n_occ + t] ) * K[0, (i*n_virt + s) * n_ex + i*n_virt + u+ 2*n_ex] * K[1, j*n_virt + t + n_ex]

												elif ((t != s) and (v == s) and (u != s) and (u != t) and (w == u)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, n_occ + u, n_occ + t, n_occ + u] ) * K[0, (i*n_virt + s) * n_ex + i*n_virt + u+ 2*n_ex] * K[1, j*n_virt + u + n_ex]

												elif ((t != s) and (v == s) and (u != s) and (u != t) and (w != s) and (w != t) and (w != u) and (w != v)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (8 * g[i, n_occ + u, n_occ + t, n_occ + w] + -4 * g[i, n_occ + w, n_occ + t, n_occ + u] ) * K[0, (i*n_virt + s) * n_ex + i*n_virt + u+ 2*n_ex] * K[1, j*n_virt + w + n_ex]

											elif ((j != i) and (m == i) and (k == i) and (n != i) and (n != j) and (n != k) and (n != m)):

												if ((t == s) and (v == s) and (u == s) and (w == s)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, n_occ + s, j, n] + -4 * g[i, j, n, n_occ + s] ) * K[0, (i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] * K[1, n*n_virt + s + n_ex]

												elif ((t == s) and (v == s) and (u == s) and (w != s) and (w != t) and (w != u) and (w != v)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-8 * g[i, j, n, n_occ + w] + 4 * g[i, n_occ + w, j, n] ) * K[0, (i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] * K[1, n*n_virt + w + n_ex]

												elif ((t == s) and (v == s) and (u != s) and (u != t) and (w == s)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, j, n, n_occ + u] + -8 * g[i, n_occ + u, j, n] ) * K[0, (i*n_virt + s) * n_ex + i*n_virt + u+ 2*n_ex] * K[1, n*n_virt + s + n_ex]

												elif ((t != s) and (v == s) and (u == s) and (w == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, j, n, n_occ + s] + -8 * g[i, n_occ + s, j, n] ) * K[0, (i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] * K[1, n*n_virt + t + n_ex]

												elif ((t != s) and (v == s) and (u == t) and (w == s)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-8 * g[i, j, n, n_occ + s] + 4 * g[i, n_occ + s, j, n] ) * K[0, (i*n_virt + s) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, n*n_virt + s + n_ex]

												elif ((t != s) and (v == s) and (u == t) and (w == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, n_occ + t, j, n] + -4 * g[i, j, n, n_occ + t] ) * K[0, (i*n_virt + s) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, n*n_virt + t + n_ex]

												elif ((t != s) and (v == s) and (u == t) and (w != s) and (w != t) and (w != u) and (w != v)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-8 * g[i, j, n, n_occ + w] + 4 * g[i, n_occ + w, j, n] ) * K[0, (i*n_virt + s) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, n*n_virt + w + n_ex]

												elif ((t != s) and (v == s) and (u != s) and (u != t) and (w == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, j, n, n_occ + u] + -8 * g[i, n_occ + u, j, n] ) * K[0, (i*n_virt + s) * n_ex + i*n_virt + u+ 2*n_ex] * K[1, n*n_virt + t + n_ex]

											elif ((j != i) and (m == i) and (k == j) and (n == i)):

												if ((t == s) and (v == s) and (u == s) and (w == s)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * F[i, n_occ + s] + -4 * g[i, n_occ + s, j, j] + -4 * g[i, n_occ + s, n_occ + s, n_occ + s] + 8 * g[i, i, i, n_occ + s] + -4 * g[i, j, j, n_occ + s] ) * K[0, (i*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, i*n_virt + s + n_ex]

												elif ((t == s) and (v == s) and (u == s) and (w != s) and (w != t) and (w != u) and (w != v)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, j, j, n_occ + w] + -8 * g[i, n_occ + w, j, j] + -8 * g[i, n_occ + s, n_occ + s, n_occ + w] + 4 * g[i, i, i, n_occ + w] + 4 * g[i, n_occ + w, n_occ + s, n_occ + s] ) * K[0, (i*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, i*n_virt + w + n_ex]

												elif ((t == s) and (v != s) and (v != t) and (v != u) and (u == s) and (w == s)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-8 * g[i, n_occ + s, n_occ + s, n_occ + v] ) * K[0, (i*n_virt + v) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, i*n_virt + s + n_ex]

												elif ((t == s) and (v != s) and (v != t) and (v != u) and (u == s) and (w == v)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, i, i, n_occ + s] + -4 * g[i, n_occ + v, n_occ + s, n_occ + v] + -4 * g[i, n_occ + s, n_occ + v, n_occ + v] ) * K[0, (i*n_virt + v) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, i*n_virt + v + n_ex]

												elif ((t == s) and (v != s) and (v != t) and (v != u) and (u == s) and (w != s) and (w != t) and (w != u) and (w != v)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, n_occ + w, n_occ + s, n_occ + v] + -4 * g[i, n_occ + s, n_occ + v, n_occ + w] ) * K[0, (i*n_virt + v) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, i*n_virt + w + n_ex]

												elif ((t == s) and (v == s) and (u != s) and (u != t) and (w == s)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * F[i, n_occ + u] + 8 * g[i, n_occ + s, n_occ + s, n_occ + u] + -4 * g[i, n_occ + u, n_occ + s, n_occ + s] + 4 * g[i, n_occ + u, j, j] + -8 * g[i, j, j, n_occ + u] ) * K[0, (i*n_virt + s) * n_ex + j*n_virt + u+ 2*n_ex] * K[1, i*n_virt + s + n_ex]

												elif ((t == s) and (v == s) and (u != s) and (u != t) and (w == u)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, n_occ + u, n_occ + s, n_occ + u] ) * K[0, (i*n_virt + s) * n_ex + j*n_virt + u+ 2*n_ex] * K[1, i*n_virt + u + n_ex]

												elif ((t == s) and (v == s) and (u != s) and (u != t) and (w != s) and (w != t) and (w != u) and (w != v)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, n_occ + u, n_occ + s, n_occ + w] + 8 * g[i, n_occ + w, n_occ + s, n_occ + u] ) * K[0, (i*n_virt + s) * n_ex + j*n_virt + u+ 2*n_ex] * K[1, i*n_virt + w + n_ex]

												elif ((t != s) and (v == s) and (u == s) and (w == s)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, n_occ + s, n_occ + s, n_occ + t] ) * K[0, (i*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, i*n_virt + s + n_ex]

												elif ((t != s) and (v == s) and (u == s) and (w == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * F[i, n_occ + s] + 8 * g[i, n_occ + t, n_occ + s, n_occ + t] + -4 * g[i, n_occ + s, n_occ + t, n_occ + t] + 4 * g[i, n_occ + s, j, j] + -8 * g[i, j, j, n_occ + s] ) * K[0, (i*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, i*n_virt + t + n_ex]

												elif ((t != s) and (v == s) and (u == s) and (w != s) and (w != t) and (w != u) and (w != v)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, n_occ + s, n_occ + t, n_occ + w] + 8 * g[i, n_occ + w, n_occ + s, n_occ + t] ) * K[0, (i*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, i*n_virt + w + n_ex]

												elif ((t != s) and (v == s) and (u == t) and (w == s)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, j, j, n_occ + s] + -8 * g[i, n_occ + s, j, j] + -8 * g[i, n_occ + s, n_occ + s, n_occ + s] + -4 * g[i, n_occ + t, n_occ + s, n_occ + t] + 8 * g[i, n_occ + s, n_occ + t, n_occ + t] + 8 * g[i, i, i, n_occ + s] ) * K[0, (i*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, i*n_virt + s + n_ex]

												elif ((t != s) and (v == s) and (u == t) and (w == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * F[i, n_occ + t] + -4 * g[i, n_occ + t, j, j] + -4 * g[i, n_occ + t, n_occ + s, n_occ + s] + -4 * g[i, n_occ + s, n_occ + s, n_occ + t] + 4 * g[i, n_occ + t, n_occ + t, n_occ + t] + 4 * g[i, i, i, n_occ + t] + -4 * g[i, j, j, n_occ + t] ) * K[0, (i*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, i*n_virt + t + n_ex]

												elif ((t != s) and (v == s) and (u == t) and (w != s) and (w != t) and (w != u) and (w != v)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, j, j, n_occ + w] + -8 * g[i, n_occ + w, j, j] + -4 * g[i, n_occ + w, n_occ + s, n_occ + s] + -4 * g[i, n_occ + s, n_occ + s, n_occ + w] + -4 * g[i, n_occ + t, n_occ + t, n_occ + w] + 8 * g[i, n_occ + w, n_occ + t, n_occ + t] + 4 * g[i, i, i, n_occ + w] ) * K[0, (i*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, i*n_virt + w + n_ex]

												elif ((t != s) and (v == t) and (u == t) and (w == s)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-8 * g[i, n_occ + s, n_occ + s, n_occ + t] ) * K[0, (i*n_virt + t) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, i*n_virt + s + n_ex]

												elif ((t != s) and (v == t) and (u == t) and (w == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, i, i, n_occ + s] + -4 * g[i, n_occ + t, n_occ + s, n_occ + t] + -4 * g[i, n_occ + s, n_occ + t, n_occ + t] ) * K[0, (i*n_virt + t) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, i*n_virt + t + n_ex]

												elif ((t != s) and (v == t) and (u == t) and (w != s) and (w != t) and (w != u) and (w != v)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, n_occ + w, n_occ + s, n_occ + t] + -4 * g[i, n_occ + s, n_occ + t, n_occ + w] ) * K[0, (i*n_virt + t) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, i*n_virt + w + n_ex]

												elif ((t != s) and (v != s) and (v != t) and (v != u) and (u == t) and (w == s)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-8 * g[i, n_occ + s, n_occ + s, n_occ + v] ) * K[0, (i*n_virt + v) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, i*n_virt + s + n_ex]

												elif ((t != s) and (v != s) and (v != t) and (v != u) and (u == t) and (w == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, n_occ + t, n_occ + s, n_occ + v] + -4 * g[i, n_occ + s, n_occ + t, n_occ + v] ) * K[0, (i*n_virt + v) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, i*n_virt + t + n_ex]

												elif ((t != s) and (v != s) and (v != t) and (v != u) and (u == t) and (w == v)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, i, i, n_occ + s] + -4 * g[i, n_occ + v, n_occ + s, n_occ + v] + -4 * g[i, n_occ + s, n_occ + v, n_occ + v] ) * K[0, (i*n_virt + v) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, i*n_virt + v + n_ex]

												elif ((t != s) and (v != s) and (v != t) and (v != u) and (u == t) and (w != s) and (w != t) and (w != u) and (w != v)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, n_occ + w, n_occ + s, n_occ + v] + -4 * g[i, n_occ + s, n_occ + v, n_occ + w] ) * K[0, (i*n_virt + v) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, i*n_virt + w + n_ex]

												elif ((t != s) and (v == s) and (u != s) and (u != t) and (w == s)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (8 * g[i, n_occ + s, n_occ + t, n_occ + u] + -4 * g[i, n_occ + u, n_occ + s, n_occ + t] ) * K[0, (i*n_virt + s) * n_ex + j*n_virt + u+ 2*n_ex] * K[1, i*n_virt + s + n_ex]

												elif ((t != s) and (v == s) and (u != s) and (u != t) and (w == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * F[i, n_occ + u] + 8 * g[i, n_occ + t, n_occ + t, n_occ + u] + -4 * g[i, n_occ + u, n_occ + t, n_occ + t] + 4 * g[i, n_occ + u, j, j] + -8 * g[i, j, j, n_occ + u] ) * K[0, (i*n_virt + s) * n_ex + j*n_virt + u+ 2*n_ex] * K[1, i*n_virt + t + n_ex]

												elif ((t != s) and (v == s) and (u != s) and (u != t) and (w == u)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, n_occ + u, n_occ + t, n_occ + u] ) * K[0, (i*n_virt + s) * n_ex + j*n_virt + u+ 2*n_ex] * K[1, i*n_virt + u + n_ex]

												elif ((t != s) and (v == s) and (u != s) and (u != t) and (w != s) and (w != t) and (w != u) and (w != v)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, n_occ + u, n_occ + t, n_occ + w] + 8 * g[i, n_occ + w, n_occ + t, n_occ + u] ) * K[0, (i*n_virt + s) * n_ex + j*n_virt + u+ 2*n_ex] * K[1, i*n_virt + w + n_ex]

											elif ((j != i) and (m == i) and (k == j) and (n == j)):

												if ((t == s) and (v == s) and (u == s) and (w == s)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-8 * F[j, n_occ + s] + 4 * g[i, j, i, n_occ + s] + 4 * g[i, i, j, n_occ + s] + 4 * g[j, n_occ + s, n_occ + s, n_occ + s] + -8 * g[j, j, j, n_occ + s] ) * K[0, (i*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, j*n_virt + s + n_ex]

												elif ((t == s) and (v == s) and (u == s) and (w != s) and (w != t) and (w != u) and (w != v)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * F[j, n_occ + w] + 8 * g[j, n_occ + s, n_occ + s, n_occ + w] + -4 * g[j, n_occ + w, n_occ + s, n_occ + s] + 8 * g[i, i, j, n_occ + w] + -4 * g[i, j, i, n_occ + w] + -4 * g[j, j, j, n_occ + w] ) * K[0, (i*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, j*n_virt + w + n_ex]

												elif ((t == s) and (v != s) and (v != t) and (v != u) and (u == s) and (w == s)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[j, n_occ + s, n_occ + s, n_occ + v] ) * K[0, (i*n_virt + v) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, j*n_virt + s + n_ex]

												elif ((t == s) and (v != s) and (v != t) and (v != u) and (u == s) and (w == v)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (8 * g[i, j, i, n_occ + s] + -4 * g[i, i, j, n_occ + s] + -8 * g[j, n_occ + v, n_occ + s, n_occ + v] + 4 * g[j, n_occ + s, n_occ + v, n_occ + v] ) * K[0, (i*n_virt + v) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, j*n_virt + v + n_ex]

												elif ((t == s) and (v != s) and (v != t) and (v != u) and (u == s) and (w != s) and (w != t) and (w != u) and (w != v)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[j, n_occ + s, n_occ + v, n_occ + w] + -8 * g[j, n_occ + w, n_occ + s, n_occ + v] ) * K[0, (i*n_virt + v) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, j*n_virt + w + n_ex]

												elif ((t == s) and (v == s) and (u != s) and (u != t) and (w == s)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * F[j, n_occ + u] + 4 * g[j, n_occ + u, n_occ + s, n_occ + s] + 4 * g[j, n_occ + s, n_occ + s, n_occ + u] + -4 * g[j, j, j, n_occ + u] ) * K[0, (i*n_virt + s) * n_ex + j*n_virt + u+ 2*n_ex] * K[1, j*n_virt + s + n_ex]

												elif ((t == s) and (v == s) and (u != s) and (u != t) and (w == u)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (8 * g[j, n_occ + u, n_occ + s, n_occ + u] ) * K[0, (i*n_virt + s) * n_ex + j*n_virt + u+ 2*n_ex] * K[1, j*n_virt + u + n_ex]

												elif ((t == s) and (v == s) and (u != s) and (u != t) and (w != s) and (w != t) and (w != u) and (w != v)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[j, n_occ + u, n_occ + s, n_occ + w] + 4 * g[j, n_occ + w, n_occ + s, n_occ + u] ) * K[0, (i*n_virt + s) * n_ex + j*n_virt + u+ 2*n_ex] * K[1, j*n_virt + w + n_ex]

												elif ((t != s) and (v == s) and (u == s) and (w == s)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (8 * g[j, n_occ + s, n_occ + s, n_occ + t] ) * K[0, (i*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, j*n_virt + s + n_ex]

												elif ((t != s) and (v == s) and (u == s) and (w == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * F[j, n_occ + s] + 4 * g[j, n_occ + s, n_occ + t, n_occ + t] + 4 * g[j, n_occ + t, n_occ + s, n_occ + t] + -4 * g[j, j, j, n_occ + s] ) * K[0, (i*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, j*n_virt + t + n_ex]

												elif ((t != s) and (v == s) and (u == s) and (w != s) and (w != t) and (w != u) and (w != v)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[j, n_occ + s, n_occ + t, n_occ + w] + 4 * g[j, n_occ + w, n_occ + s, n_occ + t] ) * K[0, (i*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, j*n_virt + w + n_ex]

												elif ((t != s) and (v == s) and (u == t) and (w == s)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * F[j, n_occ + s] + 4 * g[i, j, i, n_occ + s] + 4 * g[i, i, j, n_occ + s] + -4 * g[j, n_occ + s, n_occ + s, n_occ + s] + 4 * g[j, n_occ + t, n_occ + s, n_occ + t] + 4 * g[j, n_occ + s, n_occ + t, n_occ + t] + -4 * g[j, j, j, n_occ + s] ) * K[0, (i*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, j*n_virt + s + n_ex]

												elif ((t != s) and (v == s) and (u == t) and (w == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-8 * F[j, n_occ + t] + -4 * g[i, j, i, n_occ + t] + 8 * g[i, i, j, n_occ + t] + 4 * g[j, n_occ + s, n_occ + s, n_occ + t] + -8 * g[j, n_occ + t, n_occ + s, n_occ + s] + 8 * g[j, n_occ + t, n_occ + t, n_occ + t] + -8 * g[j, j, j, n_occ + t] ) * K[0, (i*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, j*n_virt + t + n_ex]

												elif ((t != s) and (v == s) and (u == t) and (w != s) and (w != t) and (w != u) and (w != v)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * F[j, n_occ + w] + 4 * g[j, n_occ + s, n_occ + s, n_occ + w] + -8 * g[j, n_occ + w, n_occ + s, n_occ + s] + 4 * g[j, n_occ + t, n_occ + t, n_occ + w] + 4 * g[j, n_occ + w, n_occ + t, n_occ + t] + 8 * g[i, i, j, n_occ + w] + -4 * g[i, j, i, n_occ + w] + -4 * g[j, j, j, n_occ + w] ) * K[0, (i*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, j*n_virt + w + n_ex]

												elif ((t != s) and (v == t) and (u == t) and (w == s)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[j, n_occ + s, n_occ + s, n_occ + t] ) * K[0, (i*n_virt + t) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, j*n_virt + s + n_ex]

												elif ((t != s) and (v == t) and (u == t) and (w == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (8 * g[i, j, i, n_occ + s] + -4 * g[i, i, j, n_occ + s] + -8 * g[j, n_occ + t, n_occ + s, n_occ + t] + 4 * g[j, n_occ + s, n_occ + t, n_occ + t] ) * K[0, (i*n_virt + t) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, j*n_virt + t + n_ex]

												elif ((t != s) and (v == t) and (u == t) and (w != s) and (w != t) and (w != u) and (w != v)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[j, n_occ + s, n_occ + t, n_occ + w] + -8 * g[j, n_occ + w, n_occ + s, n_occ + t] ) * K[0, (i*n_virt + t) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, j*n_virt + w + n_ex]

												elif ((t != s) and (v != s) and (v != t) and (v != u) and (u == t) and (w == s)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[j, n_occ + s, n_occ + s, n_occ + v] ) * K[0, (i*n_virt + v) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, j*n_virt + s + n_ex]

												elif ((t != s) and (v != s) and (v != t) and (v != u) and (u == t) and (w == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[j, n_occ + s, n_occ + t, n_occ + v] + -8 * g[j, n_occ + t, n_occ + s, n_occ + v] ) * K[0, (i*n_virt + v) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, j*n_virt + t + n_ex]

												elif ((t != s) and (v != s) and (v != t) and (v != u) and (u == t) and (w == v)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (8 * g[i, j, i, n_occ + s] + -4 * g[i, i, j, n_occ + s] + -8 * g[j, n_occ + v, n_occ + s, n_occ + v] + 4 * g[j, n_occ + s, n_occ + v, n_occ + v] ) * K[0, (i*n_virt + v) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, j*n_virt + v + n_ex]

												elif ((t != s) and (v != s) and (v != t) and (v != u) and (u == t) and (w != s) and (w != t) and (w != u) and (w != v)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[j, n_occ + s, n_occ + v, n_occ + w] + -8 * g[j, n_occ + w, n_occ + s, n_occ + v] ) * K[0, (i*n_virt + v) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, j*n_virt + w + n_ex]

												elif ((t != s) and (v == s) and (u != s) and (u != t) and (w == s)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[j, n_occ + u, n_occ + s, n_occ + t] + 4 * g[j, n_occ + s, n_occ + t, n_occ + u] ) * K[0, (i*n_virt + s) * n_ex + j*n_virt + u+ 2*n_ex] * K[1, j*n_virt + s + n_ex]

												elif ((t != s) and (v == s) and (u != s) and (u != t) and (w == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * F[j, n_occ + u] + 4 * g[j, n_occ + u, n_occ + t, n_occ + t] + 4 * g[j, n_occ + t, n_occ + t, n_occ + u] + -4 * g[j, j, j, n_occ + u] ) * K[0, (i*n_virt + s) * n_ex + j*n_virt + u+ 2*n_ex] * K[1, j*n_virt + t + n_ex]

												elif ((t != s) and (v == s) and (u != s) and (u != t) and (w == u)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (8 * g[j, n_occ + u, n_occ + t, n_occ + u] ) * K[0, (i*n_virt + s) * n_ex + j*n_virt + u+ 2*n_ex] * K[1, j*n_virt + u + n_ex]

												elif ((t != s) and (v == s) and (u != s) and (u != t) and (w != s) and (w != t) and (w != u) and (w != v)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[j, n_occ + u, n_occ + t, n_occ + w] + 4 * g[j, n_occ + w, n_occ + t, n_occ + u] ) * K[0, (i*n_virt + s) * n_ex + j*n_virt + u+ 2*n_ex] * K[1, j*n_virt + w + n_ex]

											elif ((j != i) and (m == i) and (k == j) and (n != i) and (n != j) and (n != k) and (n != m)):

												if ((t == s) and (v == s) and (u == s) and (w == s)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * F[n, n_occ + s] + 4 * g[i, n, i, n_occ + s] + 4 * g[i, i, n, n_occ + s] + -4 * g[j, j, n, n_occ + s] + -4 * g[j, n, j, n_occ + s] ) * K[0, (i*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, n*n_virt + s + n_ex]

												elif ((t == s) and (v == s) and (u == s) and (w != s) and (w != t) and (w != u) and (w != v)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[j, n, j, n_occ + w] + -8 * g[j, j, n, n_occ + w] + -4 * g[i, n, i, n_occ + w] + 8 * g[i, i, n, n_occ + w] ) * K[0, (i*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, n*n_virt + w + n_ex]

												elif ((t == s) and (v != s) and (v != t) and (v != u) and (u == s) and (w == s)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[n, n_occ + s, n_occ + s, n_occ + v] ) * K[0, (i*n_virt + v) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, n*n_virt + s + n_ex]

												elif ((t == s) and (v != s) and (v != t) and (v != u) and (u == s) and (w == v)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (8 * g[i, n, i, n_occ + s] + -4 * g[i, i, n, n_occ + s] + -8 * g[n, n_occ + v, n_occ + s, n_occ + v] + 4 * g[n, n_occ + s, n_occ + v, n_occ + v] ) * K[0, (i*n_virt + v) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, n*n_virt + v + n_ex]

												elif ((t == s) and (v != s) and (v != t) and (v != u) and (u == s) and (w != s) and (w != t) and (w != u) and (w != v)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[n, n_occ + s, n_occ + v, n_occ + w] + -8 * g[n, n_occ + w, n_occ + s, n_occ + v] ) * K[0, (i*n_virt + v) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, n*n_virt + w + n_ex]

												elif ((t == s) and (v == s) and (u != s) and (u != t) and (w == s)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * F[n, n_occ + u] + 8 * g[n, n_occ + s, n_occ + s, n_occ + u] + -4 * g[n, n_occ + u, n_occ + s, n_occ + s] + 4 * g[j, j, n, n_occ + u] + -8 * g[j, n, j, n_occ + u] ) * K[0, (i*n_virt + s) * n_ex + j*n_virt + u+ 2*n_ex] * K[1, n*n_virt + s + n_ex]

												elif ((t == s) and (v == s) and (u != s) and (u != t) and (w == u)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[n, n_occ + u, n_occ + s, n_occ + u] ) * K[0, (i*n_virt + s) * n_ex + j*n_virt + u+ 2*n_ex] * K[1, n*n_virt + u + n_ex]

												elif ((t == s) and (v == s) and (u != s) and (u != t) and (w != s) and (w != t) and (w != u) and (w != v)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[n, n_occ + u, n_occ + s, n_occ + w] + 8 * g[n, n_occ + w, n_occ + s, n_occ + u] ) * K[0, (i*n_virt + s) * n_ex + j*n_virt + u+ 2*n_ex] * K[1, n*n_virt + w + n_ex]

												elif ((t != s) and (v == s) and (u == s) and (w == s)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[n, n_occ + s, n_occ + s, n_occ + t] ) * K[0, (i*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, n*n_virt + s + n_ex]

												elif ((t != s) and (v == s) and (u == s) and (w == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * F[n, n_occ + s] + 8 * g[n, n_occ + t, n_occ + s, n_occ + t] + -4 * g[n, n_occ + s, n_occ + t, n_occ + t] + 4 * g[j, j, n, n_occ + s] + -8 * g[j, n, j, n_occ + s] ) * K[0, (i*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, n*n_virt + t + n_ex]

												elif ((t != s) and (v == s) and (u == s) and (w != s) and (w != t) and (w != u) and (w != v)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[n, n_occ + s, n_occ + t, n_occ + w] + 8 * g[n, n_occ + w, n_occ + s, n_occ + t] ) * K[0, (i*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, n*n_virt + w + n_ex]

												elif ((t != s) and (v == s) and (u == t) and (w == s)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, n, i, n_occ + s] + 4 * g[j, n, j, n_occ + s] + -8 * g[j, j, n, n_occ + s] + -4 * g[n, n_occ + s, n_occ + s, n_occ + s] + -4 * g[n, n_occ + t, n_occ + s, n_occ + t] + 8 * g[n, n_occ + s, n_occ + t, n_occ + t] + 4 * g[i, i, n, n_occ + s] ) * K[0, (i*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, n*n_virt + s + n_ex]

												elif ((t != s) and (v == s) and (u == t) and (w == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * F[n, n_occ + t] + 4 * g[n, n_occ + s, n_occ + s, n_occ + t] + -4 * g[j, j, n, n_occ + t] + -8 * g[n, n_occ + t, n_occ + s, n_occ + s] + 4 * g[n, n_occ + t, n_occ + t, n_occ + t] + 8 * g[i, i, n, n_occ + t] + -4 * g[i, n, i, n_occ + t] + -4 * g[j, n, j, n_occ + t] ) * K[0, (i*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, n*n_virt + t + n_ex]

												elif ((t != s) and (v == s) and (u == t) and (w != s) and (w != t) and (w != u) and (w != v)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[j, n, j, n_occ + w] + 4 * g[n, n_occ + s, n_occ + s, n_occ + w] + -8 * g[j, j, n, n_occ + w] + -8 * g[n, n_occ + w, n_occ + s, n_occ + s] + -4 * g[n, n_occ + t, n_occ + t, n_occ + w] + 8 * g[n, n_occ + w, n_occ + t, n_occ + t] + -4 * g[i, n, i, n_occ + w] + 8 * g[i, i, n, n_occ + w] ) * K[0, (i*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, n*n_virt + w + n_ex]

												elif ((t != s) and (v == t) and (u == t) and (w == s)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[n, n_occ + s, n_occ + s, n_occ + t] ) * K[0, (i*n_virt + t) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, n*n_virt + s + n_ex]

												elif ((t != s) and (v == t) and (u == t) and (w == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (8 * g[i, n, i, n_occ + s] + -4 * g[i, i, n, n_occ + s] + -8 * g[n, n_occ + t, n_occ + s, n_occ + t] + 4 * g[n, n_occ + s, n_occ + t, n_occ + t] ) * K[0, (i*n_virt + t) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, n*n_virt + t + n_ex]

												elif ((t != s) and (v == t) and (u == t) and (w != s) and (w != t) and (w != u) and (w != v)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[n, n_occ + s, n_occ + t, n_occ + w] + -8 * g[n, n_occ + w, n_occ + s, n_occ + t] ) * K[0, (i*n_virt + t) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, n*n_virt + w + n_ex]

												elif ((t != s) and (v != s) and (v != t) and (v != u) and (u == t) and (w == s)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[n, n_occ + s, n_occ + s, n_occ + v] ) * K[0, (i*n_virt + v) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, n*n_virt + s + n_ex]

												elif ((t != s) and (v != s) and (v != t) and (v != u) and (u == t) and (w == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[n, n_occ + s, n_occ + t, n_occ + v] + -8 * g[n, n_occ + t, n_occ + s, n_occ + v] ) * K[0, (i*n_virt + v) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, n*n_virt + t + n_ex]

												elif ((t != s) and (v != s) and (v != t) and (v != u) and (u == t) and (w == v)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (8 * g[i, n, i, n_occ + s] + -4 * g[i, i, n, n_occ + s] + -8 * g[n, n_occ + v, n_occ + s, n_occ + v] + 4 * g[n, n_occ + s, n_occ + v, n_occ + v] ) * K[0, (i*n_virt + v) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, n*n_virt + v + n_ex]

												elif ((t != s) and (v != s) and (v != t) and (v != u) and (u == t) and (w != s) and (w != t) and (w != u) and (w != v)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[n, n_occ + s, n_occ + v, n_occ + w] + -8 * g[n, n_occ + w, n_occ + s, n_occ + v] ) * K[0, (i*n_virt + v) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, n*n_virt + w + n_ex]

												elif ((t != s) and (v == s) and (u != s) and (u != t) and (w == s)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (8 * g[n, n_occ + s, n_occ + t, n_occ + u] + -4 * g[n, n_occ + u, n_occ + s, n_occ + t] ) * K[0, (i*n_virt + s) * n_ex + j*n_virt + u+ 2*n_ex] * K[1, n*n_virt + s + n_ex]

												elif ((t != s) and (v == s) and (u != s) and (u != t) and (w == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * F[n, n_occ + u] + 8 * g[n, n_occ + t, n_occ + t, n_occ + u] + -4 * g[n, n_occ + u, n_occ + t, n_occ + t] + 4 * g[j, j, n, n_occ + u] + -8 * g[j, n, j, n_occ + u] ) * K[0, (i*n_virt + s) * n_ex + j*n_virt + u+ 2*n_ex] * K[1, n*n_virt + t + n_ex]

												elif ((t != s) and (v == s) and (u != s) and (u != t) and (w == u)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[n, n_occ + u, n_occ + t, n_occ + u] ) * K[0, (i*n_virt + s) * n_ex + j*n_virt + u+ 2*n_ex] * K[1, n*n_virt + u + n_ex]

												elif ((t != s) and (v == s) and (u != s) and (u != t) and (w != s) and (w != t) and (w != u) and (w != v)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[n, n_occ + u, n_occ + t, n_occ + w] + 8 * g[n, n_occ + w, n_occ + t, n_occ + u] ) * K[0, (i*n_virt + s) * n_ex + j*n_virt + u+ 2*n_ex] * K[1, n*n_virt + w + n_ex]

											elif ((j != i) and (m == j) and (k == j) and (n == i)):

												if ((t == s) and (v == s) and (u == s) and (w == s)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (8 * g[i, j, i, n_occ + s] ) * K[0, (j*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, i*n_virt + s + n_ex]

												elif ((t == s) and (v == s) and (u == s) and (w != s) and (w != t) and (w != u) and (w != v)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, j, i, n_occ + w] ) * K[0, (j*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, i*n_virt + w + n_ex]

												elif ((t == s) and (v != s) and (v != t) and (v != u) and (u == s) and (w == v)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, j, i, n_occ + s] ) * K[0, (j*n_virt + v) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, i*n_virt + v + n_ex]

												elif ((t != s) and (v == s) and (u == t) and (w == s)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (8 * g[i, j, i, n_occ + s] ) * K[0, (j*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, i*n_virt + s + n_ex]

												elif ((t != s) and (v == s) and (u == t) and (w == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, j, i, n_occ + t] ) * K[0, (j*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, i*n_virt + t + n_ex]

												elif ((t != s) and (v == s) and (u == t) and (w != s) and (w != t) and (w != u) and (w != v)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, j, i, n_occ + w] ) * K[0, (j*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, i*n_virt + w + n_ex]

												elif ((t != s) and (v == t) and (u == t) and (w == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, j, i, n_occ + s] ) * K[0, (j*n_virt + t) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, i*n_virt + t + n_ex]

												elif ((t != s) and (v != s) and (v != t) and (v != u) and (u == t) and (w == v)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, j, i, n_occ + s] ) * K[0, (j*n_virt + v) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, i*n_virt + v + n_ex]

											elif ((j != i) and (m == j) and (k == j) and (n == j)):

												if ((t == s) and (v == s) and (u == s) and (w == s)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, n_occ + s, j, j] + -4 * g[i, n_occ + s, n_occ + s, n_occ + s] + 4 * g[i, j, j, n_occ + s] ) * K[0, (j*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, j*n_virt + s + n_ex]

												elif ((t == s) and (v == s) and (u == s) and (w != s) and (w != t) and (w != u) and (w != v)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (8 * g[i, j, j, n_occ + w] + -4 * g[i, n_occ + w, j, j] + -8 * g[i, n_occ + s, n_occ + s, n_occ + w] + 4 * g[i, n_occ + w, n_occ + s, n_occ + s] ) * K[0, (j*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, j*n_virt + w + n_ex]

												elif ((t == s) and (v != s) and (v != t) and (v != u) and (u == s) and (w == s)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, n_occ + s, n_occ + s, n_occ + v] ) * K[0, (j*n_virt + v) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, j*n_virt + s + n_ex]

												elif ((t == s) and (v != s) and (v != t) and (v != u) and (u == s) and (w == v)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, j, j, n_occ + s] + 8 * g[i, n_occ + s, j, j] + 4 * g[i, n_occ + v, n_occ + s, n_occ + v] + -8 * g[i, n_occ + s, n_occ + v, n_occ + v] ) * K[0, (j*n_virt + v) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, j*n_virt + v + n_ex]

												elif ((t == s) and (v != s) and (v != t) and (v != u) and (u == s) and (w != s) and (w != t) and (w != u) and (w != v)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-8 * g[i, n_occ + s, n_occ + v, n_occ + w] + 4 * g[i, n_occ + w, n_occ + s, n_occ + v] ) * K[0, (j*n_virt + v) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, j*n_virt + w + n_ex]

												elif ((t != s) and (v == s) and (u == t) and (w == s)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, n_occ + s, j, j] + -4 * g[i, n_occ + s, n_occ + s, n_occ + s] + 4 * g[i, j, j, n_occ + s] ) * K[0, (j*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, j*n_virt + s + n_ex]

												elif ((t != s) and (v == s) and (u == t) and (w == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (8 * g[i, j, j, n_occ + t] + -4 * g[i, n_occ + t, j, j] + -8 * g[i, n_occ + s, n_occ + s, n_occ + t] + 4 * g[i, n_occ + t, n_occ + s, n_occ + s] ) * K[0, (j*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, j*n_virt + t + n_ex]

												elif ((t != s) and (v == s) and (u == t) and (w != s) and (w != t) and (w != u) and (w != v)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (8 * g[i, j, j, n_occ + w] + -4 * g[i, n_occ + w, j, j] + -8 * g[i, n_occ + s, n_occ + s, n_occ + w] + 4 * g[i, n_occ + w, n_occ + s, n_occ + s] ) * K[0, (j*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, j*n_virt + w + n_ex]

												elif ((t != s) and (v == t) and (u == t) and (w == s)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, n_occ + s, n_occ + s, n_occ + t] ) * K[0, (j*n_virt + t) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, j*n_virt + s + n_ex]

												elif ((t != s) and (v == t) and (u == t) and (w == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, j, j, n_occ + s] + 8 * g[i, n_occ + s, j, j] + 4 * g[i, n_occ + t, n_occ + s, n_occ + t] + -8 * g[i, n_occ + s, n_occ + t, n_occ + t] ) * K[0, (j*n_virt + t) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, j*n_virt + t + n_ex]

												elif ((t != s) and (v == t) and (u == t) and (w != s) and (w != t) and (w != u) and (w != v)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-8 * g[i, n_occ + s, n_occ + t, n_occ + w] + 4 * g[i, n_occ + w, n_occ + s, n_occ + t] ) * K[0, (j*n_virt + t) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, j*n_virt + w + n_ex]

												elif ((t != s) and (v != s) and (v != t) and (v != u) and (u == t) and (w == s)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, n_occ + s, n_occ + s, n_occ + v] ) * K[0, (j*n_virt + v) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, j*n_virt + s + n_ex]

												elif ((t != s) and (v != s) and (v != t) and (v != u) and (u == t) and (w == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-8 * g[i, n_occ + s, n_occ + t, n_occ + v] + 4 * g[i, n_occ + t, n_occ + s, n_occ + v] ) * K[0, (j*n_virt + v) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, j*n_virt + t + n_ex]

												elif ((t != s) and (v != s) and (v != t) and (v != u) and (u == t) and (w == v)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, j, j, n_occ + s] + 8 * g[i, n_occ + s, j, j] + 4 * g[i, n_occ + v, n_occ + s, n_occ + v] + -8 * g[i, n_occ + s, n_occ + v, n_occ + v] ) * K[0, (j*n_virt + v) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, j*n_virt + v + n_ex]

												elif ((t != s) and (v != s) and (v != t) and (v != u) and (u == t) and (w != s) and (w != t) and (w != u) and (w != v)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-8 * g[i, n_occ + s, n_occ + v, n_occ + w] + 4 * g[i, n_occ + w, n_occ + s, n_occ + v] ) * K[0, (j*n_virt + v) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, j*n_virt + w + n_ex]

											elif ((j != i) and (m == j) and (k == j) and (n != i) and (n != j) and (n != k) and (n != m)):

												if ((t == s) and (v == s) and (u == s) and (w == s)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, j, n, n_occ + s] + 4 * g[i, n_occ + s, j, n] ) * K[0, (j*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, n*n_virt + s + n_ex]

												elif ((t == s) and (v == s) and (u == s) and (w != s) and (w != t) and (w != u) and (w != v)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (8 * g[i, j, n, n_occ + w] + -4 * g[i, n_occ + w, j, n] ) * K[0, (j*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, n*n_virt + w + n_ex]

												elif ((t == s) and (v != s) and (v != t) and (v != u) and (u == s) and (w == v)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, j, n, n_occ + s] + 8 * g[i, n_occ + s, j, n] ) * K[0, (j*n_virt + v) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, n*n_virt + v + n_ex]

												elif ((t != s) and (v == s) and (u == t) and (w == s)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, j, n, n_occ + s] + 4 * g[i, n_occ + s, j, n] ) * K[0, (j*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, n*n_virt + s + n_ex]

												elif ((t != s) and (v == s) and (u == t) and (w == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (8 * g[i, j, n, n_occ + t] + -4 * g[i, n_occ + t, j, n] ) * K[0, (j*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, n*n_virt + t + n_ex]

												elif ((t != s) and (v == s) and (u == t) and (w != s) and (w != t) and (w != u) and (w != v)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (8 * g[i, j, n, n_occ + w] + -4 * g[i, n_occ + w, j, n] ) * K[0, (j*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, n*n_virt + w + n_ex]

												elif ((t != s) and (v == t) and (u == t) and (w == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, j, n, n_occ + s] + 8 * g[i, n_occ + s, j, n] ) * K[0, (j*n_virt + t) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, n*n_virt + t + n_ex]

												elif ((t != s) and (v != s) and (v != t) and (v != u) and (u == t) and (w == v)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, j, n, n_occ + s] + 8 * g[i, n_occ + s, j, n] ) * K[0, (j*n_virt + v) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, n*n_virt + v + n_ex]

											elif ((j != i) and (m != i) and (m != j) and (m != k) and (k == j) and (n == i)):

												if ((t == s) and (v == s) and (u == s) and (w == s)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (8 * g[i, m, i, n_occ + s] ) * K[0, (m*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, i*n_virt + s + n_ex]

												elif ((t == s) and (v == s) and (u == s) and (w != s) and (w != t) and (w != u) and (w != v)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, m, i, n_occ + w] ) * K[0, (m*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, i*n_virt + w + n_ex]

												elif ((t == s) and (v != s) and (v != t) and (v != u) and (u == s) and (w == v)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, m, i, n_occ + s] ) * K[0, (m*n_virt + v) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, i*n_virt + v + n_ex]

												elif ((t != s) and (v == s) and (u == t) and (w == s)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (8 * g[i, m, i, n_occ + s] ) * K[0, (m*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, i*n_virt + s + n_ex]

												elif ((t != s) and (v == s) and (u == t) and (w == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, m, i, n_occ + t] ) * K[0, (m*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, i*n_virt + t + n_ex]

												elif ((t != s) and (v == s) and (u == t) and (w != s) and (w != t) and (w != u) and (w != v)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, m, i, n_occ + w] ) * K[0, (m*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, i*n_virt + w + n_ex]

												elif ((t != s) and (v == t) and (u == t) and (w == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, m, i, n_occ + s] ) * K[0, (m*n_virt + t) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, i*n_virt + t + n_ex]

												elif ((t != s) and (v != s) and (v != t) and (v != u) and (u == t) and (w == v)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, m, i, n_occ + s] ) * K[0, (m*n_virt + v) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, i*n_virt + v + n_ex]

											elif ((j != i) and (m != i) and (m != j) and (m != k) and (k == j) and (n == j)):

												if ((t == s) and (v == s) and (u == s) and (w == s)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, m, j, n_occ + s] + 4 * g[i, n_occ + s, j, m] ) * K[0, (m*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, j*n_virt + s + n_ex]

												elif ((t == s) and (v == s) and (u == s) and (w != s) and (w != t) and (w != u) and (w != v)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (8 * g[i, m, j, n_occ + w] + -4 * g[i, n_occ + w, j, m] ) * K[0, (m*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, j*n_virt + w + n_ex]

												elif ((t == s) and (v != s) and (v != t) and (v != u) and (u == s) and (w == v)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, m, j, n_occ + s] + 8 * g[i, n_occ + s, j, m] ) * K[0, (m*n_virt + v) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, j*n_virt + v + n_ex]

												elif ((t != s) and (v == s) and (u == t) and (w == s)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, m, j, n_occ + s] + 4 * g[i, n_occ + s, j, m] ) * K[0, (m*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, j*n_virt + s + n_ex]

												elif ((t != s) and (v == s) and (u == t) and (w == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (8 * g[i, m, j, n_occ + t] + -4 * g[i, n_occ + t, j, m] ) * K[0, (m*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, j*n_virt + t + n_ex]

												elif ((t != s) and (v == s) and (u == t) and (w != s) and (w != t) and (w != u) and (w != v)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (8 * g[i, m, j, n_occ + w] + -4 * g[i, n_occ + w, j, m] ) * K[0, (m*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, j*n_virt + w + n_ex]

												elif ((t != s) and (v == t) and (u == t) and (w == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, m, j, n_occ + s] + 8 * g[i, n_occ + s, j, m] ) * K[0, (m*n_virt + t) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, j*n_virt + t + n_ex]

												elif ((t != s) and (v != s) and (v != t) and (v != u) and (u == t) and (w == v)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, m, j, n_occ + s] + 8 * g[i, n_occ + s, j, m] ) * K[0, (m*n_virt + v) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, j*n_virt + v + n_ex]

											elif ((j != i) and (m != i) and (m != j) and (m != k) and (k == j) and (n == m)):

												if ((t == s) and (v == s) and (u == s) and (w == s)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, n_occ + s, m, m] + -4 * g[i, n_occ + s, n_occ + s, n_occ + s] + 4 * g[i, m, m, n_occ + s] ) * K[0, (m*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, m*n_virt + s + n_ex]

												elif ((t == s) and (v == s) and (u == s) and (w != s) and (w != t) and (w != u) and (w != v)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (8 * g[i, m, m, n_occ + w] + -4 * g[i, n_occ + w, m, m] + -8 * g[i, n_occ + s, n_occ + s, n_occ + w] + 4 * g[i, n_occ + w, n_occ + s, n_occ + s] ) * K[0, (m*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, m*n_virt + w + n_ex]

												elif ((t == s) and (v != s) and (v != t) and (v != u) and (u == s) and (w == s)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, n_occ + s, n_occ + s, n_occ + v] ) * K[0, (m*n_virt + v) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, m*n_virt + s + n_ex]

												elif ((t == s) and (v != s) and (v != t) and (v != u) and (u == s) and (w == v)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, m, m, n_occ + s] + 8 * g[i, n_occ + s, m, m] + 4 * g[i, n_occ + v, n_occ + s, n_occ + v] + -8 * g[i, n_occ + s, n_occ + v, n_occ + v] ) * K[0, (m*n_virt + v) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, m*n_virt + v + n_ex]

												elif ((t == s) and (v != s) and (v != t) and (v != u) and (u == s) and (w != s) and (w != t) and (w != u) and (w != v)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-8 * g[i, n_occ + s, n_occ + v, n_occ + w] + 4 * g[i, n_occ + w, n_occ + s, n_occ + v] ) * K[0, (m*n_virt + v) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, m*n_virt + w + n_ex]

												elif ((t != s) and (v == s) and (u == t) and (w == s)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, n_occ + s, m, m] + -4 * g[i, n_occ + s, n_occ + s, n_occ + s] + 4 * g[i, m, m, n_occ + s] ) * K[0, (m*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, m*n_virt + s + n_ex]

												elif ((t != s) and (v == s) and (u == t) and (w == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (8 * g[i, m, m, n_occ + t] + -4 * g[i, n_occ + t, m, m] + -8 * g[i, n_occ + s, n_occ + s, n_occ + t] + 4 * g[i, n_occ + t, n_occ + s, n_occ + s] ) * K[0, (m*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, m*n_virt + t + n_ex]

												elif ((t != s) and (v == s) and (u == t) and (w != s) and (w != t) and (w != u) and (w != v)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (8 * g[i, m, m, n_occ + w] + -4 * g[i, n_occ + w, m, m] + -8 * g[i, n_occ + s, n_occ + s, n_occ + w] + 4 * g[i, n_occ + w, n_occ + s, n_occ + s] ) * K[0, (m*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, m*n_virt + w + n_ex]

												elif ((t != s) and (v == t) and (u == t) and (w == s)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, n_occ + s, n_occ + s, n_occ + t] ) * K[0, (m*n_virt + t) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, m*n_virt + s + n_ex]

												elif ((t != s) and (v == t) and (u == t) and (w == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, m, m, n_occ + s] + 8 * g[i, n_occ + s, m, m] + 4 * g[i, n_occ + t, n_occ + s, n_occ + t] + -8 * g[i, n_occ + s, n_occ + t, n_occ + t] ) * K[0, (m*n_virt + t) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, m*n_virt + t + n_ex]

												elif ((t != s) and (v == t) and (u == t) and (w != s) and (w != t) and (w != u) and (w != v)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-8 * g[i, n_occ + s, n_occ + t, n_occ + w] + 4 * g[i, n_occ + w, n_occ + s, n_occ + t] ) * K[0, (m*n_virt + t) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, m*n_virt + w + n_ex]

												elif ((t != s) and (v != s) and (v != t) and (v != u) and (u == t) and (w == s)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, n_occ + s, n_occ + s, n_occ + v] ) * K[0, (m*n_virt + v) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, m*n_virt + s + n_ex]

												elif ((t != s) and (v != s) and (v != t) and (v != u) and (u == t) and (w == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-8 * g[i, n_occ + s, n_occ + t, n_occ + v] + 4 * g[i, n_occ + t, n_occ + s, n_occ + v] ) * K[0, (m*n_virt + v) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, m*n_virt + t + n_ex]

												elif ((t != s) and (v != s) and (v != t) and (v != u) and (u == t) and (w == v)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, m, m, n_occ + s] + 8 * g[i, n_occ + s, m, m] + 4 * g[i, n_occ + v, n_occ + s, n_occ + v] + -8 * g[i, n_occ + s, n_occ + v, n_occ + v] ) * K[0, (m*n_virt + v) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, m*n_virt + v + n_ex]

												elif ((t != s) and (v != s) and (v != t) and (v != u) and (u == t) and (w != s) and (w != t) and (w != u) and (w != v)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-8 * g[i, n_occ + s, n_occ + v, n_occ + w] + 4 * g[i, n_occ + w, n_occ + s, n_occ + v] ) * K[0, (m*n_virt + v) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, m*n_virt + w + n_ex]

											elif ((j != i) and (m != i) and (m != j) and (m != k) and (k == j) and (n != i) and (n != j) and (n != k) and (n != m)):

												if ((t == s) and (v == s) and (u == s) and (w == s)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, m, n, n_occ + s] + 4 * g[i, n_occ + s, m, n] ) * K[0, (m*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, n*n_virt + s + n_ex]

												elif ((t == s) and (v == s) and (u == s) and (w != s) and (w != t) and (w != u) and (w != v)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (8 * g[i, m, n, n_occ + w] + -4 * g[i, n_occ + w, m, n] ) * K[0, (m*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, n*n_virt + w + n_ex]

												elif ((t == s) and (v != s) and (v != t) and (v != u) and (u == s) and (w == v)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, m, n, n_occ + s] + 8 * g[i, n_occ + s, m, n] ) * K[0, (m*n_virt + v) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, n*n_virt + v + n_ex]

												elif ((t != s) and (v == s) and (u == t) and (w == s)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, m, n, n_occ + s] + 4 * g[i, n_occ + s, m, n] ) * K[0, (m*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, n*n_virt + s + n_ex]

												elif ((t != s) and (v == s) and (u == t) and (w == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (8 * g[i, m, n, n_occ + t] + -4 * g[i, n_occ + t, m, n] ) * K[0, (m*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, n*n_virt + t + n_ex]

												elif ((t != s) and (v == s) and (u == t) and (w != s) and (w != t) and (w != u) and (w != v)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (8 * g[i, m, n, n_occ + w] + -4 * g[i, n_occ + w, m, n] ) * K[0, (m*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, n*n_virt + w + n_ex]

												elif ((t != s) and (v == t) and (u == t) and (w == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, m, n, n_occ + s] + 8 * g[i, n_occ + s, m, n] ) * K[0, (m*n_virt + t) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, n*n_virt + t + n_ex]

												elif ((t != s) and (v != s) and (v != t) and (v != u) and (u == t) and (w == v)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, m, n, n_occ + s] + 8 * g[i, n_occ + s, m, n] ) * K[0, (m*n_virt + v) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, n*n_virt + v + n_ex]

											elif ((j != i) and (m == i) and (k != i) and (k != j) and (n == i)):

												if ((t == s) and (v == s) and (u == s) and (w == s)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, j, k, n_occ + s] + -4 * g[i, n_occ + s, j, k] ) * K[0, (i*n_virt + s) * n_ex + k*n_virt + s+ 2*n_ex] * K[1, i*n_virt + s + n_ex]

												elif ((t == s) and (v == s) and (u == s) and (w != s) and (w != t) and (w != u) and (w != v)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, j, k, n_occ + w] + -8 * g[i, n_occ + w, j, k] ) * K[0, (i*n_virt + s) * n_ex + k*n_virt + s+ 2*n_ex] * K[1, i*n_virt + w + n_ex]

												elif ((t == s) and (v == s) and (u != s) and (u != t) and (w == s)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-8 * g[i, j, k, n_occ + u] + 4 * g[i, n_occ + u, j, k] ) * K[0, (i*n_virt + s) * n_ex + k*n_virt + u+ 2*n_ex] * K[1, i*n_virt + s + n_ex]

												elif ((t != s) and (v == s) and (u == s) and (w == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-8 * g[i, j, k, n_occ + s] + 4 * g[i, n_occ + s, j, k] ) * K[0, (i*n_virt + s) * n_ex + k*n_virt + s+ 2*n_ex] * K[1, i*n_virt + t + n_ex]

												elif ((t != s) and (v == s) and (u == t) and (w == s)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, j, k, n_occ + s] + -8 * g[i, n_occ + s, j, k] ) * K[0, (i*n_virt + s) * n_ex + k*n_virt + t+ 2*n_ex] * K[1, i*n_virt + s + n_ex]

												elif ((t != s) and (v == s) and (u == t) and (w == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, j, k, n_occ + t] + -4 * g[i, n_occ + t, j, k] ) * K[0, (i*n_virt + s) * n_ex + k*n_virt + t+ 2*n_ex] * K[1, i*n_virt + t + n_ex]

												elif ((t != s) and (v == s) and (u == t) and (w != s) and (w != t) and (w != u) and (w != v)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, j, k, n_occ + w] + -8 * g[i, n_occ + w, j, k] ) * K[0, (i*n_virt + s) * n_ex + k*n_virt + t+ 2*n_ex] * K[1, i*n_virt + w + n_ex]

												elif ((t != s) and (v == s) and (u != s) and (u != t) and (w == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-8 * g[i, j, k, n_occ + u] + 4 * g[i, n_occ + u, j, k] ) * K[0, (i*n_virt + s) * n_ex + k*n_virt + u+ 2*n_ex] * K[1, i*n_virt + t + n_ex]

											elif ((j != i) and (m == i) and (k != i) and (k != j) and (n == j)):

												if ((t == s) and (v == s) and (u == s) and (w == s)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * F[k, n_occ + s] + -4 * g[j, j, k, n_occ + s] + 4 * g[k, n_occ + s, n_occ + s, n_occ + s] + -4 * g[j, k, j, n_occ + s] ) * K[0, (i*n_virt + s) * n_ex + k*n_virt + s+ 2*n_ex] * K[1, j*n_virt + s + n_ex]

												elif ((t == s) and (v == s) and (u == s) and (w != s) and (w != t) and (w != u) and (w != v)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * F[k, n_occ + w] + 8 * g[k, n_occ + s, n_occ + s, n_occ + w] + -4 * g[k, n_occ + w, n_occ + s, n_occ + s] + 4 * g[j, j, k, n_occ + w] + -8 * g[j, k, j, n_occ + w] ) * K[0, (i*n_virt + s) * n_ex + k*n_virt + s+ 2*n_ex] * K[1, j*n_virt + w + n_ex]

												elif ((t == s) and (v == s) and (u != s) and (u != t) and (w == s)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[j, k, j, n_occ + u] + -8 * g[j, j, k, n_occ + u] + -4 * g[k, n_occ + s, n_occ + s, n_occ + u] + 8 * g[k, n_occ + u, n_occ + s, n_occ + s] ) * K[0, (i*n_virt + s) * n_ex + k*n_virt + u+ 2*n_ex] * K[1, j*n_virt + s + n_ex]

												elif ((t == s) and (v == s) and (u != s) and (u != t) and (w == u)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[k, n_occ + u, n_occ + s, n_occ + u] ) * K[0, (i*n_virt + s) * n_ex + k*n_virt + u+ 2*n_ex] * K[1, j*n_virt + u + n_ex]

												elif ((t == s) and (v == s) and (u != s) and (u != t) and (w != s) and (w != t) and (w != u) and (w != v)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (8 * g[k, n_occ + u, n_occ + s, n_occ + w] + -4 * g[k, n_occ + w, n_occ + s, n_occ + u] ) * K[0, (i*n_virt + s) * n_ex + k*n_virt + u+ 2*n_ex] * K[1, j*n_virt + w + n_ex]

												elif ((t != s) and (v == s) and (u == s) and (w == s)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[k, n_occ + s, n_occ + s, n_occ + t] ) * K[0, (i*n_virt + s) * n_ex + k*n_virt + s+ 2*n_ex] * K[1, j*n_virt + s + n_ex]

												elif ((t != s) and (v == s) and (u == s) and (w == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[j, k, j, n_occ + s] + -8 * g[j, j, k, n_occ + s] + -4 * g[k, n_occ + t, n_occ + s, n_occ + t] + 8 * g[k, n_occ + s, n_occ + t, n_occ + t] ) * K[0, (i*n_virt + s) * n_ex + k*n_virt + s+ 2*n_ex] * K[1, j*n_virt + t + n_ex]

												elif ((t != s) and (v == s) and (u == s) and (w != s) and (w != t) and (w != u) and (w != v)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (8 * g[k, n_occ + s, n_occ + t, n_occ + w] + -4 * g[k, n_occ + w, n_occ + s, n_occ + t] ) * K[0, (i*n_virt + s) * n_ex + k*n_virt + s+ 2*n_ex] * K[1, j*n_virt + w + n_ex]

												elif ((t != s) and (v == s) and (u == t) and (w == s)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * F[k, n_occ + s] + 8 * g[k, n_occ + t, n_occ + s, n_occ + t] + -4 * g[k, n_occ + s, n_occ + t, n_occ + t] + 4 * g[j, j, k, n_occ + s] + -8 * g[j, k, j, n_occ + s] ) * K[0, (i*n_virt + s) * n_ex + k*n_virt + t+ 2*n_ex] * K[1, j*n_virt + s + n_ex]

												elif ((t != s) and (v == s) and (u == t) and (w == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * F[k, n_occ + t] + -4 * g[j, j, k, n_occ + t] + 4 * g[k, n_occ + t, n_occ + t, n_occ + t] + -4 * g[j, k, j, n_occ + t] ) * K[0, (i*n_virt + s) * n_ex + k*n_virt + t+ 2*n_ex] * K[1, j*n_virt + t + n_ex]

												elif ((t != s) and (v == s) and (u == t) and (w != s) and (w != t) and (w != u) and (w != v)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * F[k, n_occ + w] + 8 * g[k, n_occ + t, n_occ + t, n_occ + w] + -4 * g[k, n_occ + w, n_occ + t, n_occ + t] + 4 * g[j, j, k, n_occ + w] + -8 * g[j, k, j, n_occ + w] ) * K[0, (i*n_virt + s) * n_ex + k*n_virt + t+ 2*n_ex] * K[1, j*n_virt + w + n_ex]

												elif ((t != s) and (v == s) and (u != s) and (u != t) and (w == s)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[k, n_occ + s, n_occ + t, n_occ + u] + 8 * g[k, n_occ + u, n_occ + s, n_occ + t] ) * K[0, (i*n_virt + s) * n_ex + k*n_virt + u+ 2*n_ex] * K[1, j*n_virt + s + n_ex]

												elif ((t != s) and (v == s) and (u != s) and (u != t) and (w == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[j, k, j, n_occ + u] + -8 * g[j, j, k, n_occ + u] + -4 * g[k, n_occ + t, n_occ + t, n_occ + u] + 8 * g[k, n_occ + u, n_occ + t, n_occ + t] ) * K[0, (i*n_virt + s) * n_ex + k*n_virt + u+ 2*n_ex] * K[1, j*n_virt + t + n_ex]

												elif ((t != s) and (v == s) and (u != s) and (u != t) and (w == u)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[k, n_occ + u, n_occ + t, n_occ + u] ) * K[0, (i*n_virt + s) * n_ex + k*n_virt + u+ 2*n_ex] * K[1, j*n_virt + u + n_ex]

												elif ((t != s) and (v == s) and (u != s) and (u != t) and (w != s) and (w != t) and (w != u) and (w != v)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (8 * g[k, n_occ + u, n_occ + t, n_occ + w] + -4 * g[k, n_occ + w, n_occ + t, n_occ + u] ) * K[0, (i*n_virt + s) * n_ex + k*n_virt + u+ 2*n_ex] * K[1, j*n_virt + w + n_ex]

											elif ((j != i) and (m == i) and (k != i) and (k != j) and (n == k)):

												if ((t == s) and (v == s) and (u == s) and (w == s)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-8 * g[j, k, k, n_occ + s] ) * K[0, (i*n_virt + s) * n_ex + k*n_virt + s+ 2*n_ex] * K[1, k*n_virt + s + n_ex]

												elif ((t == s) and (v == s) and (u == s) and (w != s) and (w != t) and (w != u) and (w != v)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[j, k, k, n_occ + w] ) * K[0, (i*n_virt + s) * n_ex + k*n_virt + s+ 2*n_ex] * K[1, k*n_virt + w + n_ex]

												elif ((t == s) and (v == s) and (u != s) and (u != t) and (w == s)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[j, k, k, n_occ + u] ) * K[0, (i*n_virt + s) * n_ex + k*n_virt + u+ 2*n_ex] * K[1, k*n_virt + s + n_ex]

												elif ((t != s) and (v == s) and (u == s) and (w == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[j, k, k, n_occ + s] ) * K[0, (i*n_virt + s) * n_ex + k*n_virt + s+ 2*n_ex] * K[1, k*n_virt + t + n_ex]

												elif ((t != s) and (v == s) and (u == t) and (w == s)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[j, k, k, n_occ + s] ) * K[0, (i*n_virt + s) * n_ex + k*n_virt + t+ 2*n_ex] * K[1, k*n_virt + s + n_ex]

												elif ((t != s) and (v == s) and (u == t) and (w == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-8 * g[j, k, k, n_occ + t] ) * K[0, (i*n_virt + s) * n_ex + k*n_virt + t+ 2*n_ex] * K[1, k*n_virt + t + n_ex]

												elif ((t != s) and (v == s) and (u == t) and (w != s) and (w != t) and (w != u) and (w != v)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[j, k, k, n_occ + w] ) * K[0, (i*n_virt + s) * n_ex + k*n_virt + t+ 2*n_ex] * K[1, k*n_virt + w + n_ex]

												elif ((t != s) and (v == s) and (u != s) and (u != t) and (w == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[j, k, k, n_occ + u] ) * K[0, (i*n_virt + s) * n_ex + k*n_virt + u+ 2*n_ex] * K[1, k*n_virt + t + n_ex]

											elif ((j != i) and (m == i) and (k != i) and (k != j) and (n != i) and (n != j) and (n != k) and (n != m)):

												if ((t == s) and (v == s) and (u == s) and (w == s)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[j, n, k, n_occ + s] + -4 * g[j, k, n, n_occ + s] ) * K[0, (i*n_virt + s) * n_ex + k*n_virt + s+ 2*n_ex] * K[1, n*n_virt + s + n_ex]

												elif ((t == s) and (v == s) and (u == s) and (w != s) and (w != t) and (w != u) and (w != v)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-8 * g[j, k, n, n_occ + w] + 4 * g[j, n, k, n_occ + w] ) * K[0, (i*n_virt + s) * n_ex + k*n_virt + s+ 2*n_ex] * K[1, n*n_virt + w + n_ex]

												elif ((t == s) and (v == s) and (u != s) and (u != t) and (w == s)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[j, k, n, n_occ + u] + -8 * g[j, n, k, n_occ + u] ) * K[0, (i*n_virt + s) * n_ex + k*n_virt + u+ 2*n_ex] * K[1, n*n_virt + s + n_ex]

												elif ((t != s) and (v == s) and (u == s) and (w == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[j, k, n, n_occ + s] + -8 * g[j, n, k, n_occ + s] ) * K[0, (i*n_virt + s) * n_ex + k*n_virt + s+ 2*n_ex] * K[1, n*n_virt + t + n_ex]

												elif ((t != s) and (v == s) and (u == t) and (w == s)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-8 * g[j, k, n, n_occ + s] + 4 * g[j, n, k, n_occ + s] ) * K[0, (i*n_virt + s) * n_ex + k*n_virt + t+ 2*n_ex] * K[1, n*n_virt + s + n_ex]

												elif ((t != s) and (v == s) and (u == t) and (w == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[j, n, k, n_occ + t] + -4 * g[j, k, n, n_occ + t] ) * K[0, (i*n_virt + s) * n_ex + k*n_virt + t+ 2*n_ex] * K[1, n*n_virt + t + n_ex]

												elif ((t != s) and (v == s) and (u == t) and (w != s) and (w != t) and (w != u) and (w != v)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-8 * g[j, k, n, n_occ + w] + 4 * g[j, n, k, n_occ + w] ) * K[0, (i*n_virt + s) * n_ex + k*n_virt + t+ 2*n_ex] * K[1, n*n_virt + w + n_ex]

												elif ((t != s) and (v == s) and (u != s) and (u != t) and (w == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[j, k, n, n_occ + u] + -8 * g[j, n, k, n_occ + u] ) * K[0, (i*n_virt + s) * n_ex + k*n_virt + u+ 2*n_ex] * K[1, n*n_virt + t + n_ex]

	# This operator combination: {'a': 3, 'b': 1, 'c': 1}
	for i in range(n_occ):
		for j in range(n_occ):
			for m in range(n_occ):
				for k in range(n_occ):
					for s in range(n_virt):
						for t in range(n_virt):
							for v in range(n_virt):
								for u in range(n_virt):

									if ((j == i) and (m == i) and (k == i)):

										if ((t == s) and (v == s) and (u == s)):

											L3[i*n_virt + s] += (-4 * g[i, n_occ + s, i, n_occ + s] ) * K[0, i*n_virt + s] * K[1, (i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex]

										elif ((t == s) and (v != s) and (v != t) and (v != u) and (u == s)):

											L3[i*n_virt + s] += (-4 * g[i, n_occ + s, i, n_occ + v] ) * K[0, i*n_virt + s] * K[1, (i*n_virt + v) * n_ex + i*n_virt + s+ 2*n_ex]

										elif ((t != s) and (v == s) and (u == s)):

											L3[i*n_virt + s] += (-4 * g[i, n_occ + s, i, n_occ + t] ) * K[0, i*n_virt + t] * K[1, (i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex]

										elif ((t != s) and (v == t) and (u == s)):

											L3[i*n_virt + s] += (-4 * g[i, n_occ + t, i, n_occ + t] ) * K[0, i*n_virt + t] * K[1, (i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex]

										elif ((t != s) and (v != s) and (v != t) and (v != u) and (u == s)):

											L3[i*n_virt + s] += (-4 * g[i, n_occ + t, i, n_occ + v] ) * K[0, i*n_virt + t] * K[1, (i*n_virt + v) * n_ex + i*n_virt + s+ 2*n_ex]

									elif ((j == i) and (m != i) and (m != j) and (m != k) and (k == i)):

										if ((t == s) and (v == s) and (u == s)):

											L3[i*n_virt + s] += (-4 * g[i, n_occ + s, m, n_occ + s] ) * K[0, i*n_virt + s] * K[1, (m*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex]

										elif ((t == s) and (v != s) and (v != t) and (v != u) and (u == s)):

											L3[i*n_virt + s] += (-8 * g[i, n_occ + s, m, n_occ + v] + 4 * g[i, n_occ + v, m, n_occ + s] ) * K[0, i*n_virt + s] * K[1, (m*n_virt + v) * n_ex + i*n_virt + s+ 2*n_ex]

										elif ((t != s) and (v == s) and (u == s)):

											L3[i*n_virt + s] += (4 * g[i, n_occ + s, m, n_occ + t] + -8 * g[i, n_occ + t, m, n_occ + s] ) * K[0, i*n_virt + t] * K[1, (m*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex]

										elif ((t != s) and (v == t) and (u == s)):

											L3[i*n_virt + s] += (-4 * g[i, n_occ + t, m, n_occ + t] ) * K[0, i*n_virt + t] * K[1, (m*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex]

										elif ((t != s) and (v != s) and (v != t) and (v != u) and (u == s)):

											L3[i*n_virt + s] += (-8 * g[i, n_occ + t, m, n_occ + v] + 4 * g[i, n_occ + v, m, n_occ + t] ) * K[0, i*n_virt + t] * K[1, (m*n_virt + v) * n_ex + i*n_virt + s+ 2*n_ex]

									elif ((j != i) and (m == i) and (k == i)):

										if ((t == s) and (v == s) and (u == s)):

											L3[i*n_virt + s] += (-4 * g[i, n_occ + s, j, n_occ + s] ) * K[0, j*n_virt + s] * K[1, (i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex]

										elif ((t == s) and (v != s) and (v != t) and (v != u) and (u == s)):

											L3[i*n_virt + s] += (4 * g[i, n_occ + s, j, n_occ + v] + -8 * g[i, n_occ + v, j, n_occ + s] ) * K[0, j*n_virt + s] * K[1, (i*n_virt + v) * n_ex + i*n_virt + s+ 2*n_ex]

										elif ((t != s) and (v == s) and (u == s)):

											L3[i*n_virt + s] += (-8 * g[i, n_occ + s, j, n_occ + t] + 4 * g[i, n_occ + t, j, n_occ + s] ) * K[0, j*n_virt + t] * K[1, (i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex]

										elif ((t != s) and (v == t) and (u == s)):

											L3[i*n_virt + s] += (-4 * g[i, n_occ + t, j, n_occ + t] ) * K[0, j*n_virt + t] * K[1, (i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex]

										elif ((t != s) and (v != s) and (v != t) and (v != u) and (u == s)):

											L3[i*n_virt + s] += (4 * g[i, n_occ + t, j, n_occ + v] + -8 * g[i, n_occ + v, j, n_occ + t] ) * K[0, j*n_virt + t] * K[1, (i*n_virt + v) * n_ex + i*n_virt + s+ 2*n_ex]

									elif ((j != i) and (m == j) and (k == i)):

										if ((t == s) and (v == s) and (u == s)):

											L3[i*n_virt + s] += (-4 * g[j, n_occ + s, j, n_occ + s] ) * K[0, j*n_virt + s] * K[1, (j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex]

										elif ((t == s) and (v != s) and (v != t) and (v != u) and (u == s)):

											L3[i*n_virt + s] += (-4 * g[j, n_occ + s, j, n_occ + v] ) * K[0, j*n_virt + s] * K[1, (j*n_virt + v) * n_ex + i*n_virt + s+ 2*n_ex]

										elif ((t != s) and (v == s) and (u == s)):

											L3[i*n_virt + s] += (-4 * g[j, n_occ + s, j, n_occ + t] ) * K[0, j*n_virt + t] * K[1, (j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex]

										elif ((t != s) and (v == t) and (u == s)):

											L3[i*n_virt + s] += (-4 * g[j, n_occ + t, j, n_occ + t] ) * K[0, j*n_virt + t] * K[1, (j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex]

										elif ((t != s) and (v != s) and (v != t) and (v != u) and (u == s)):

											L3[i*n_virt + s] += (-4 * g[j, n_occ + t, j, n_occ + v] ) * K[0, j*n_virt + t] * K[1, (j*n_virt + v) * n_ex + i*n_virt + s+ 2*n_ex]

									elif ((j != i) and (m != i) and (m != j) and (m != k) and (k == i)):

										if ((t == s) and (v == s) and (u == s)):

											L3[i*n_virt + s] += (-4 * g[j, n_occ + s, m, n_occ + s] ) * K[0, j*n_virt + s] * K[1, (m*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex]

										elif ((t == s) and (v != s) and (v != t) and (v != u) and (u == s)):

											L3[i*n_virt + s] += (-8 * g[j, n_occ + s, m, n_occ + v] + 4 * g[j, n_occ + v, m, n_occ + s] ) * K[0, j*n_virt + s] * K[1, (m*n_virt + v) * n_ex + i*n_virt + s+ 2*n_ex]

										elif ((t != s) and (v == s) and (u == s)):

											L3[i*n_virt + s] += (4 * g[j, n_occ + s, m, n_occ + t] + -8 * g[j, n_occ + t, m, n_occ + s] ) * K[0, j*n_virt + t] * K[1, (m*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex]

										elif ((t != s) and (v == t) and (u == s)):

											L3[i*n_virt + s] += (-4 * g[j, n_occ + t, m, n_occ + t] ) * K[0, j*n_virt + t] * K[1, (m*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex]

										elif ((t != s) and (v != s) and (v != t) and (v != u) and (u == s)):

											L3[i*n_virt + s] += (-8 * g[j, n_occ + t, m, n_occ + v] + 4 * g[j, n_occ + v, m, n_occ + t] ) * K[0, j*n_virt + t] * K[1, (m*n_virt + v) * n_ex + i*n_virt + s+ 2*n_ex]

	# This operator combination: {'a': 3, 'b': 1, 'c': 2}
	for i in range(n_occ):
		for j in range(n_occ):
			for m in range(n_occ):
				for k in range(n_occ):
					for s in range(n_virt):
						for t in range(n_virt):
							for v in range(n_virt):
								for u in range(n_virt):

									if ((j == i) and (m == i) and (k == i)):

										if ((t == s) and (v == s) and (u == s)):

											L3[i*n_virt + s + n_ex] += (-4 * F[i, i] + 4 * F[n_occ + s, n_occ + s] + -4 * g[i, i, n_occ + s, n_occ + s] + 8 * g[i, n_occ + s, i, n_occ + s] ) * K[0, i*n_virt + s] * K[1, (i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex]

										elif ((t == s) and (v == s) and (u != s) and (u != t)):

											L3[i*n_virt + s + n_ex] += (4 * F[n_occ + s, n_occ + u] + -4 * g[i, i, n_occ + s, n_occ + u] + 8 * g[i, n_occ + s, i, n_occ + u] ) * K[0, i*n_virt + s] * K[1, (i*n_virt + s) * n_ex + i*n_virt + u+ 2*n_ex]

										elif ((t != s) and (v == s) and (u == s)):

											L3[i*n_virt + s + n_ex] += (4 * F[n_occ + s, n_occ + t] + -4 * g[i, i, n_occ + s, n_occ + t] + 8 * g[i, n_occ + s, i, n_occ + t] ) * K[0, i*n_virt + t] * K[1, (i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex]

										elif ((t != s) and (v == s) and (u == t)):

											L3[i*n_virt + s + n_ex] += (-4 * F[i, i] + 4 * F[n_occ + t, n_occ + t] + -4 * g[i, i, n_occ + t, n_occ + t] + 8 * g[i, n_occ + t, i, n_occ + t] ) * K[0, i*n_virt + t] * K[1, (i*n_virt + s) * n_ex + i*n_virt + t+ 2*n_ex]

										elif ((t != s) and (v == s) and (u != s) and (u != t)):

											L3[i*n_virt + s + n_ex] += (4 * F[n_occ + t, n_occ + u] + -4 * g[i, i, n_occ + t, n_occ + u] + 8 * g[i, n_occ + t, i, n_occ + u] ) * K[0, i*n_virt + t] * K[1, (i*n_virt + s) * n_ex + i*n_virt + u+ 2*n_ex]

									elif ((j == i) and (m == i) and (k != i) and (k != j)):

										if ((t == s) and (v == s) and (u == s)):

											L3[i*n_virt + s + n_ex] += (-4 * F[i, k] + 8 * g[i, n_occ + s, k, n_occ + s] + -4 * g[i, k, n_occ + s, n_occ + s] ) * K[0, i*n_virt + s] * K[1, (i*n_virt + s) * n_ex + k*n_virt + s+ 2*n_ex]

										elif ((t == s) and (v == s) and (u != s) and (u != t)):

											L3[i*n_virt + s + n_ex] += (-4 * g[i, k, n_occ + s, n_occ + u] + 8 * g[i, n_occ + s, k, n_occ + u] ) * K[0, i*n_virt + s] * K[1, (i*n_virt + s) * n_ex + k*n_virt + u+ 2*n_ex]

										elif ((t != s) and (v == s) and (u == s)):

											L3[i*n_virt + s + n_ex] += (-4 * g[i, k, n_occ + s, n_occ + t] + 8 * g[i, n_occ + t, k, n_occ + s] ) * K[0, i*n_virt + t] * K[1, (i*n_virt + s) * n_ex + k*n_virt + s+ 2*n_ex]

										elif ((t != s) and (v == s) and (u == t)):

											L3[i*n_virt + s + n_ex] += (-4 * F[i, k] + 8 * g[i, n_occ + t, k, n_occ + t] + -4 * g[i, k, n_occ + t, n_occ + t] ) * K[0, i*n_virt + t] * K[1, (i*n_virt + s) * n_ex + k*n_virt + t+ 2*n_ex]

										elif ((t != s) and (v == s) and (u != s) and (u != t)):

											L3[i*n_virt + s + n_ex] += (-4 * g[i, k, n_occ + t, n_occ + u] + 8 * g[i, n_occ + t, k, n_occ + u] ) * K[0, i*n_virt + t] * K[1, (i*n_virt + s) * n_ex + k*n_virt + u+ 2*n_ex]

									elif ((j != i) and (m == i) and (k == i)):

										if ((t == s) and (v == s) and (u == s)):

											L3[i*n_virt + s + n_ex] += (-4 * F[i, j] + 8 * g[i, n_occ + s, j, n_occ + s] + -4 * g[i, j, n_occ + s, n_occ + s] ) * K[0, j*n_virt + s] * K[1, (i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex]

										elif ((t == s) and (v == s) and (u != s) and (u != t)):

											L3[i*n_virt + s + n_ex] += (-4 * g[i, j, n_occ + s, n_occ + u] + 8 * g[i, n_occ + u, j, n_occ + s] ) * K[0, j*n_virt + s] * K[1, (i*n_virt + s) * n_ex + i*n_virt + u+ 2*n_ex]

										elif ((t != s) and (v == s) and (u == s)):

											L3[i*n_virt + s + n_ex] += (-4 * g[i, j, n_occ + s, n_occ + t] + 8 * g[i, n_occ + s, j, n_occ + t] ) * K[0, j*n_virt + t] * K[1, (i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex]

										elif ((t != s) and (v == s) and (u == t)):

											L3[i*n_virt + s + n_ex] += (-4 * F[i, j] + 8 * g[i, n_occ + t, j, n_occ + t] + -4 * g[i, j, n_occ + t, n_occ + t] ) * K[0, j*n_virt + t] * K[1, (i*n_virt + s) * n_ex + i*n_virt + t+ 2*n_ex]

										elif ((t != s) and (v == s) and (u != s) and (u != t)):

											L3[i*n_virt + s + n_ex] += (-4 * g[i, j, n_occ + t, n_occ + u] + 8 * g[i, n_occ + u, j, n_occ + t] ) * K[0, j*n_virt + t] * K[1, (i*n_virt + s) * n_ex + i*n_virt + u+ 2*n_ex]

									elif ((j != i) and (m == i) and (k == j)):

										if ((t == s) and (v == s) and (u == s)):

											L3[i*n_virt + s + n_ex] += (4 * F[n_occ + s, n_occ + s] + -4 * F[j, j] + 8 * g[j, n_occ + s, j, n_occ + s] + -4 * g[j, j, n_occ + s, n_occ + s] ) * K[0, j*n_virt + s] * K[1, (i*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex]

										elif ((t == s) and (v == s) and (u != s) and (u != t)):

											L3[i*n_virt + s + n_ex] += (4 * F[n_occ + s, n_occ + u] + -4 * g[j, j, n_occ + s, n_occ + u] + 8 * g[j, n_occ + s, j, n_occ + u] ) * K[0, j*n_virt + s] * K[1, (i*n_virt + s) * n_ex + j*n_virt + u+ 2*n_ex]

										elif ((t != s) and (v == s) and (u == s)):

											L3[i*n_virt + s + n_ex] += (4 * F[n_occ + s, n_occ + t] + -4 * g[j, j, n_occ + s, n_occ + t] + 8 * g[j, n_occ + s, j, n_occ + t] ) * K[0, j*n_virt + t] * K[1, (i*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex]

										elif ((t != s) and (v == s) and (u == t)):

											L3[i*n_virt + s + n_ex] += (4 * F[n_occ + t, n_occ + t] + -4 * F[j, j] + -4 * g[j, j, n_occ + t, n_occ + t] + 8 * g[j, n_occ + t, j, n_occ + t] ) * K[0, j*n_virt + t] * K[1, (i*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex]

										elif ((t != s) and (v == s) and (u != s) and (u != t)):

											L3[i*n_virt + s + n_ex] += (4 * F[n_occ + t, n_occ + u] + -4 * g[j, j, n_occ + t, n_occ + u] + 8 * g[j, n_occ + t, j, n_occ + u] ) * K[0, j*n_virt + t] * K[1, (i*n_virt + s) * n_ex + j*n_virt + u+ 2*n_ex]

									elif ((j != i) and (m == i) and (k != i) and (k != j)):

										if ((t == s) and (v == s) and (u == s)):

											L3[i*n_virt + s + n_ex] += (-4 * F[j, k] + 8 * g[j, n_occ + s, k, n_occ + s] + -4 * g[j, k, n_occ + s, n_occ + s] ) * K[0, j*n_virt + s] * K[1, (i*n_virt + s) * n_ex + k*n_virt + s+ 2*n_ex]

										elif ((t == s) and (v == s) and (u != s) and (u != t)):

											L3[i*n_virt + s + n_ex] += (-4 * g[j, k, n_occ + s, n_occ + u] + 8 * g[j, n_occ + s, k, n_occ + u] ) * K[0, j*n_virt + s] * K[1, (i*n_virt + s) * n_ex + k*n_virt + u+ 2*n_ex]

										elif ((t != s) and (v == s) and (u == s)):

											L3[i*n_virt + s + n_ex] += (-4 * g[j, k, n_occ + s, n_occ + t] + 8 * g[j, n_occ + t, k, n_occ + s] ) * K[0, j*n_virt + t] * K[1, (i*n_virt + s) * n_ex + k*n_virt + s+ 2*n_ex]

										elif ((t != s) and (v == s) and (u == t)):

											L3[i*n_virt + s + n_ex] += (-4 * F[j, k] + 8 * g[j, n_occ + t, k, n_occ + t] + -4 * g[j, k, n_occ + t, n_occ + t] ) * K[0, j*n_virt + t] * K[1, (i*n_virt + s) * n_ex + k*n_virt + t+ 2*n_ex]

										elif ((t != s) and (v == s) and (u != s) and (u != t)):

											L3[i*n_virt + s + n_ex] += (-4 * g[j, k, n_occ + t, n_occ + u] + 8 * g[j, n_occ + t, k, n_occ + u] ) * K[0, j*n_virt + t] * K[1, (i*n_virt + s) * n_ex + k*n_virt + u+ 2*n_ex]

	# This operator combination: {'a': 3, 'b': 1, 'c': 3}
	for j in range(n_occ):
		for i in range(n_occ):
			for k in range(n_occ):
				for n in range(n_occ):
					for m in range(n_occ):
						for t in range(n_virt):
							for s in range(n_virt):
								for u in range(n_virt):
									for w in range(n_virt):
										for v in range(n_virt):

											if ((j == i) and (k == i) and (n == i) and (m == i)):

												if ((t == s) and (u == s) and (w != s) and (w != t) and (w != u) and (w != v) and (v == s)):

													L3[(i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * F[i, n_occ + w] + -4 * g[i, n_occ + s, n_occ + s, n_occ + w] + -4 * g[i, n_occ + w, n_occ + s, n_occ + s] + 4 * g[i, i, i, n_occ + w] ) * K[0, i*n_virt + s] * K[1, (i*n_virt + w) * n_ex + i*n_virt + s+ 2*n_ex]

												elif ((t == s) and (u == s) and (w == s) and (v != s) and (v != t) and (v != u)):

													L3[(i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (8 * g[i, n_occ + s, n_occ + s, n_occ + v] ) * K[0, i*n_virt + s] * K[1, (i*n_virt + s) * n_ex + i*n_virt + v+ 2*n_ex]

												elif ((t == s) and (u != s) and (u != t) and (w == u) and (v == s)):

													L3[(i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-8 * g[i, n_occ + u, n_occ + s, n_occ + u] ) * K[0, i*n_virt + u] * K[1, (i*n_virt + u) * n_ex + i*n_virt + s+ 2*n_ex]

												elif ((t == s) and (u != s) and (u != t) and (w != s) and (w != t) and (w != u) and (w != v) and (v == s)):

													L3[(i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, n_occ + u, n_occ + s, n_occ + w] + -4 * g[i, n_occ + w, n_occ + s, n_occ + u] ) * K[0, i*n_virt + u] * K[1, (i*n_virt + w) * n_ex + i*n_virt + s+ 2*n_ex]

												elif ((t == s) and (u != s) and (u != t) and (w == s) and (v == u)):

													L3[(i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * F[i, n_occ + s] + 4 * g[i, n_occ + u, n_occ + s, n_occ + u] + 4 * g[i, n_occ + s, n_occ + u, n_occ + u] + -4 * g[i, i, i, n_occ + s] ) * K[0, i*n_virt + u] * K[1, (i*n_virt + s) * n_ex + i*n_virt + u+ 2*n_ex]

												elif ((t == s) and (u != s) and (u != t) and (w == s) and (v != s) and (v != t) and (v != u)):

													L3[(i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, n_occ + u, n_occ + s, n_occ + v] + 4 * g[i, n_occ + s, n_occ + u, n_occ + v] ) * K[0, i*n_virt + u] * K[1, (i*n_virt + s) * n_ex + i*n_virt + v+ 2*n_ex]

												elif ((t != s) and (u == s) and (w == s) and (v == s)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * F[i, n_occ + t] + 4 * g[i, n_occ + s, n_occ + s, n_occ + t] + 4 * g[i, n_occ + t, n_occ + s, n_occ + s] + -4 * g[i, i, i, n_occ + t] ) * K[0, i*n_virt + s] * K[1, (i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex]

												elif ((t != s) and (u == s) and (w == s) and (v == t)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * F[i, n_occ + s] + 4 * g[i, n_occ + s, n_occ + t, n_occ + t] + 4 * g[i, n_occ + t, n_occ + s, n_occ + t] + -8 * g[i, n_occ + s, n_occ + s, n_occ + s] + 4 * g[i, i, i, n_occ + s] ) * K[0, i*n_virt + s] * K[1, (i*n_virt + s) * n_ex + i*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u == s) and (w == t) and (v == t)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * F[i, n_occ + t] + -4 * g[i, n_occ + s, n_occ + s, n_occ + t] + -4 * g[i, n_occ + t, n_occ + s, n_occ + s] + 4 * g[i, i, i, n_occ + t] ) * K[0, i*n_virt + s] * K[1, (i*n_virt + t) * n_ex + i*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u == s) and (w != s) and (w != t) and (w != u) and (w != v) and (v == t)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * F[i, n_occ + w] + -4 * g[i, n_occ + s, n_occ + s, n_occ + w] + -4 * g[i, n_occ + w, n_occ + s, n_occ + s] + 4 * g[i, i, i, n_occ + w] ) * K[0, i*n_virt + s] * K[1, (i*n_virt + w) * n_ex + i*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u == s) and (w == s) and (v != s) and (v != t) and (v != u)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, n_occ + s, n_occ + t, n_occ + v] + 4 * g[i, n_occ + t, n_occ + s, n_occ + v] ) * K[0, i*n_virt + s] * K[1, (i*n_virt + s) * n_ex + i*n_virt + v+ 2*n_ex]

												elif ((t != s) and (u == t) and (w == s) and (v == s)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (8 * g[i, n_occ + t, n_occ + s, n_occ + t] ) * K[0, i*n_virt + t] * K[1, (i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex]

												elif ((t != s) and (u == t) and (w == s) and (v == t)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * F[i, n_occ + t] + 8 * g[i, n_occ + t, n_occ + t, n_occ + t] + -4 * g[i, n_occ + t, n_occ + s, n_occ + s] + -4 * g[i, n_occ + s, n_occ + s, n_occ + t] + -4 * g[i, i, i, n_occ + t] ) * K[0, i*n_virt + t] * K[1, (i*n_virt + s) * n_ex + i*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u == t) and (w == t) and (v == t)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-8 * g[i, n_occ + t, n_occ + s, n_occ + t] ) * K[0, i*n_virt + t] * K[1, (i*n_virt + t) * n_ex + i*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u == t) and (w != s) and (w != t) and (w != u) and (w != v) and (v == t)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, n_occ + t, n_occ + s, n_occ + w] + -4 * g[i, n_occ + w, n_occ + s, n_occ + t] ) * K[0, i*n_virt + t] * K[1, (i*n_virt + w) * n_ex + i*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u == t) and (w == s) and (v != s) and (v != t) and (v != u)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (8 * g[i, n_occ + t, n_occ + t, n_occ + v] ) * K[0, i*n_virt + t] * K[1, (i*n_virt + s) * n_ex + i*n_virt + v+ 2*n_ex]

												elif ((t != s) and (u != s) and (u != t) and (w == s) and (v == s)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, n_occ + u, n_occ + s, n_occ + t] + 4 * g[i, n_occ + t, n_occ + s, n_occ + u] ) * K[0, i*n_virt + u] * K[1, (i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex]

												elif ((t != s) and (u != s) and (u != t) and (w == s) and (v == t)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, n_occ + u, n_occ + t, n_occ + t] + 4 * g[i, n_occ + t, n_occ + t, n_occ + u] + -4 * g[i, n_occ + u, n_occ + s, n_occ + s] + -4 * g[i, n_occ + s, n_occ + s, n_occ + u] ) * K[0, i*n_virt + u] * K[1, (i*n_virt + s) * n_ex + i*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u != s) and (u != t) and (w == t) and (v == t)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, n_occ + u, n_occ + s, n_occ + t] + -4 * g[i, n_occ + t, n_occ + s, n_occ + u] ) * K[0, i*n_virt + u] * K[1, (i*n_virt + t) * n_ex + i*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u != s) and (u != t) and (w == u) and (v == t)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-8 * g[i, n_occ + u, n_occ + s, n_occ + u] ) * K[0, i*n_virt + u] * K[1, (i*n_virt + u) * n_ex + i*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u != s) and (u != t) and (w != s) and (w != t) and (w != u) and (w != v) and (v == t)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, n_occ + u, n_occ + s, n_occ + w] + -4 * g[i, n_occ + w, n_occ + s, n_occ + u] ) * K[0, i*n_virt + u] * K[1, (i*n_virt + w) * n_ex + i*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u != s) and (u != t) and (w == s) and (v == u)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * F[i, n_occ + t] + 4 * g[i, n_occ + u, n_occ + t, n_occ + u] + 4 * g[i, n_occ + t, n_occ + u, n_occ + u] + -4 * g[i, i, i, n_occ + t] ) * K[0, i*n_virt + u] * K[1, (i*n_virt + s) * n_ex + i*n_virt + u+ 2*n_ex]

												elif ((t != s) and (u != s) and (u != t) and (w == s) and (v != s) and (v != t) and (v != u)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, n_occ + u, n_occ + t, n_occ + v] + 4 * g[i, n_occ + t, n_occ + u, n_occ + v] ) * K[0, i*n_virt + u] * K[1, (i*n_virt + s) * n_ex + i*n_virt + v+ 2*n_ex]

											elif ((j == i) and (k == i) and (n != i) and (n != j) and (n != k) and (n != m) and (m == i)):

												if ((t == s) and (u == s) and (w == s) and (v == s)):

													L3[(i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * F[n, n_occ + s] + 4 * g[i, i, n, n_occ + s] + -4 * g[n, n_occ + s, n_occ + s, n_occ + s] + 4 * g[i, n, i, n_occ + s] ) * K[0, i*n_virt + s] * K[1, (n*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex]

												elif ((t == s) and (u == s) and (w != s) and (w != t) and (w != u) and (w != v) and (v == s)):

													L3[(i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, n, i, n_occ + w] + 8 * g[i, i, n, n_occ + w] + 4 * g[n, n_occ + s, n_occ + s, n_occ + w] + -8 * g[n, n_occ + w, n_occ + s, n_occ + s] ) * K[0, i*n_virt + s] * K[1, (n*n_virt + w) * n_ex + i*n_virt + s+ 2*n_ex]

												elif ((t == s) and (u != s) and (u != t) and (w == s) and (v == s)):

													L3[(i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * F[n, n_occ + u] + -8 * g[n, n_occ + s, n_occ + s, n_occ + u] + 4 * g[n, n_occ + u, n_occ + s, n_occ + s] + -4 * g[i, i, n, n_occ + u] + 8 * g[i, n, i, n_occ + u] ) * K[0, i*n_virt + u] * K[1, (n*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex]

												elif ((t == s) and (u != s) and (u != t) and (w == u) and (v == s)):

													L3[(i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[n, n_occ + u, n_occ + s, n_occ + u] ) * K[0, i*n_virt + u] * K[1, (n*n_virt + u) * n_ex + i*n_virt + s+ 2*n_ex]

												elif ((t == s) and (u != s) and (u != t) and (w != s) and (w != t) and (w != u) and (w != v) and (v == s)):

													L3[(i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[n, n_occ + u, n_occ + s, n_occ + w] + -8 * g[n, n_occ + w, n_occ + s, n_occ + u] ) * K[0, i*n_virt + u] * K[1, (n*n_virt + w) * n_ex + i*n_virt + s+ 2*n_ex]

												elif ((t != s) and (u == s) and (w == s) and (v == t)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * F[n, n_occ + s] + 4 * g[i, i, n, n_occ + s] + -4 * g[n, n_occ + s, n_occ + s, n_occ + s] + 4 * g[i, n, i, n_occ + s] ) * K[0, i*n_virt + s] * K[1, (n*n_virt + s) * n_ex + i*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u == s) and (w == t) and (v == t)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, n, i, n_occ + t] + 8 * g[i, i, n, n_occ + t] + 4 * g[n, n_occ + s, n_occ + s, n_occ + t] + -8 * g[n, n_occ + t, n_occ + s, n_occ + s] ) * K[0, i*n_virt + s] * K[1, (n*n_virt + t) * n_ex + i*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u == s) and (w != s) and (w != t) and (w != u) and (w != v) and (v == t)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, n, i, n_occ + w] + 8 * g[i, i, n, n_occ + w] + 4 * g[n, n_occ + s, n_occ + s, n_occ + w] + -8 * g[n, n_occ + w, n_occ + s, n_occ + s] ) * K[0, i*n_virt + s] * K[1, (n*n_virt + w) * n_ex + i*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u == t) and (w == s) and (v == t)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * F[n, n_occ + t] + -8 * g[n, n_occ + s, n_occ + s, n_occ + t] + 4 * g[n, n_occ + t, n_occ + s, n_occ + s] + -4 * g[i, i, n, n_occ + t] + 8 * g[i, n, i, n_occ + t] ) * K[0, i*n_virt + t] * K[1, (n*n_virt + s) * n_ex + i*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u == t) and (w == t) and (v == t)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[n, n_occ + t, n_occ + s, n_occ + t] ) * K[0, i*n_virt + t] * K[1, (n*n_virt + t) * n_ex + i*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u == t) and (w != s) and (w != t) and (w != u) and (w != v) and (v == t)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[n, n_occ + t, n_occ + s, n_occ + w] + -8 * g[n, n_occ + w, n_occ + s, n_occ + t] ) * K[0, i*n_virt + t] * K[1, (n*n_virt + w) * n_ex + i*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u != s) and (u != t) and (w == s) and (v == t)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * F[n, n_occ + u] + -8 * g[n, n_occ + s, n_occ + s, n_occ + u] + 4 * g[n, n_occ + u, n_occ + s, n_occ + s] + -4 * g[i, i, n, n_occ + u] + 8 * g[i, n, i, n_occ + u] ) * K[0, i*n_virt + u] * K[1, (n*n_virt + s) * n_ex + i*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u != s) and (u != t) and (w == t) and (v == t)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-8 * g[n, n_occ + t, n_occ + s, n_occ + u] + 4 * g[n, n_occ + u, n_occ + s, n_occ + t] ) * K[0, i*n_virt + u] * K[1, (n*n_virt + t) * n_ex + i*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u != s) and (u != t) and (w == u) and (v == t)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[n, n_occ + u, n_occ + s, n_occ + u] ) * K[0, i*n_virt + u] * K[1, (n*n_virt + u) * n_ex + i*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u != s) and (u != t) and (w != s) and (w != t) and (w != u) and (w != v) and (v == t)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[n, n_occ + u, n_occ + s, n_occ + w] + -8 * g[n, n_occ + w, n_occ + s, n_occ + u] ) * K[0, i*n_virt + u] * K[1, (n*n_virt + w) * n_ex + i*n_virt + t+ 2*n_ex]

											elif ((j == i) and (k == i) and (n == i) and (m != i) and (m != j) and (m != k)):

												if ((t == s) and (u == s) and (w == s) and (v == s)):

													L3[(i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-8 * g[i, m, i, n_occ + s] ) * K[0, i*n_virt + s] * K[1, (i*n_virt + s) * n_ex + m*n_virt + s+ 2*n_ex]

												elif ((t == s) and (u != s) and (u != t) and (w == s) and (v == s)):

													L3[(i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, m, i, n_occ + u] ) * K[0, i*n_virt + u] * K[1, (i*n_virt + s) * n_ex + m*n_virt + s+ 2*n_ex]

												elif ((t == s) and (u != s) and (u != t) and (w == s) and (v == u)):

													L3[(i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, m, i, n_occ + s] ) * K[0, i*n_virt + u] * K[1, (i*n_virt + s) * n_ex + m*n_virt + u+ 2*n_ex]

												elif ((t != s) and (u == s) and (w == s) and (v == s)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, m, i, n_occ + t] ) * K[0, i*n_virt + s] * K[1, (i*n_virt + s) * n_ex + m*n_virt + s+ 2*n_ex]

												elif ((t != s) and (u == s) and (w == s) and (v == t)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, m, i, n_occ + s] ) * K[0, i*n_virt + s] * K[1, (i*n_virt + s) * n_ex + m*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u == t) and (w == s) and (v == t)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-8 * g[i, m, i, n_occ + t] ) * K[0, i*n_virt + t] * K[1, (i*n_virt + s) * n_ex + m*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u != s) and (u != t) and (w == s) and (v == t)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, m, i, n_occ + u] ) * K[0, i*n_virt + u] * K[1, (i*n_virt + s) * n_ex + m*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u != s) and (u != t) and (w == s) and (v == u)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, m, i, n_occ + t] ) * K[0, i*n_virt + u] * K[1, (i*n_virt + s) * n_ex + m*n_virt + u+ 2*n_ex]

											elif ((j == i) and (k != i) and (k != j) and (n == i) and (m == i)):

												if ((t == s) and (u == s) and (w != s) and (w != t) and (w != u) and (w != v) and (v == s)):

													L3[(i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * F[k, n_occ + w] + -8 * g[k, n_occ + s, n_occ + s, n_occ + w] + 4 * g[k, n_occ + w, n_occ + s, n_occ + s] + -4 * g[i, i, k, n_occ + w] + 8 * g[i, k, i, n_occ + w] ) * K[0, k*n_virt + s] * K[1, (i*n_virt + w) * n_ex + i*n_virt + s+ 2*n_ex]

												elif ((t == s) and (u == s) and (w == s) and (v != s) and (v != t) and (v != u)):

													L3[(i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[k, n_occ + s, n_occ + s, n_occ + v] ) * K[0, k*n_virt + s] * K[1, (i*n_virt + s) * n_ex + i*n_virt + v+ 2*n_ex]

												elif ((t == s) and (u != s) and (u != t) and (w == u) and (v == s)):

													L3[(i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[k, n_occ + u, n_occ + s, n_occ + u] ) * K[0, k*n_virt + u] * K[1, (i*n_virt + u) * n_ex + i*n_virt + s+ 2*n_ex]

												elif ((t == s) and (u != s) and (u != t) and (w != s) and (w != t) and (w != u) and (w != v) and (v == s)):

													L3[(i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-8 * g[k, n_occ + u, n_occ + s, n_occ + w] + 4 * g[k, n_occ + w, n_occ + s, n_occ + u] ) * K[0, k*n_virt + u] * K[1, (i*n_virt + w) * n_ex + i*n_virt + s+ 2*n_ex]

												elif ((t == s) and (u != s) and (u != t) and (w == s) and (v == u)):

													L3[(i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * F[k, n_occ + s] + 8 * g[k, n_occ + u, n_occ + s, n_occ + u] + -4 * g[k, n_occ + s, n_occ + u, n_occ + u] + 4 * g[i, i, k, n_occ + s] + -8 * g[i, k, i, n_occ + s] ) * K[0, k*n_virt + u] * K[1, (i*n_virt + s) * n_ex + i*n_virt + u+ 2*n_ex]

												elif ((t == s) and (u != s) and (u != t) and (w == s) and (v != s) and (v != t) and (v != u)):

													L3[(i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[k, n_occ + s, n_occ + u, n_occ + v] + 8 * g[k, n_occ + u, n_occ + s, n_occ + v] ) * K[0, k*n_virt + u] * K[1, (i*n_virt + s) * n_ex + i*n_virt + v+ 2*n_ex]

												elif ((t != s) and (u == s) and (w == s) and (v == s)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * F[k, n_occ + t] + 8 * g[k, n_occ + s, n_occ + s, n_occ + t] + -4 * g[k, n_occ + t, n_occ + s, n_occ + s] + 4 * g[i, i, k, n_occ + t] + -8 * g[i, k, i, n_occ + t] ) * K[0, k*n_virt + s] * K[1, (i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex]

												elif ((t != s) and (u == s) and (w == s) and (v == t)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * F[k, n_occ + s] + -4 * g[k, n_occ + t, n_occ + s, n_occ + t] + 8 * g[k, n_occ + s, n_occ + t, n_occ + t] + -4 * g[i, i, k, n_occ + s] + -4 * g[k, n_occ + s, n_occ + s, n_occ + s] + 8 * g[i, k, i, n_occ + s] ) * K[0, k*n_virt + s] * K[1, (i*n_virt + s) * n_ex + i*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u == s) and (w == t) and (v == t)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * F[k, n_occ + t] + -8 * g[k, n_occ + s, n_occ + s, n_occ + t] + 4 * g[k, n_occ + t, n_occ + s, n_occ + s] + -4 * g[i, i, k, n_occ + t] + 8 * g[i, k, i, n_occ + t] ) * K[0, k*n_virt + s] * K[1, (i*n_virt + t) * n_ex + i*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u == s) and (w != s) and (w != t) and (w != u) and (w != v) and (v == t)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * F[k, n_occ + w] + -8 * g[k, n_occ + s, n_occ + s, n_occ + w] + 4 * g[k, n_occ + w, n_occ + s, n_occ + s] + -4 * g[i, i, k, n_occ + w] + 8 * g[i, k, i, n_occ + w] ) * K[0, k*n_virt + s] * K[1, (i*n_virt + w) * n_ex + i*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u == s) and (w == s) and (v != s) and (v != t) and (v != u)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (8 * g[k, n_occ + s, n_occ + t, n_occ + v] + -4 * g[k, n_occ + t, n_occ + s, n_occ + v] ) * K[0, k*n_virt + s] * K[1, (i*n_virt + s) * n_ex + i*n_virt + v+ 2*n_ex]

												elif ((t != s) and (u == t) and (w == s) and (v == s)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[k, n_occ + t, n_occ + s, n_occ + t] ) * K[0, k*n_virt + t] * K[1, (i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex]

												elif ((t != s) and (u == t) and (w == s) and (v == t)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * F[k, n_occ + t] + 4 * g[k, n_occ + t, n_occ + t, n_occ + t] + -8 * g[i, k, i, n_occ + t] + 4 * g[k, n_occ + s, n_occ + s, n_occ + t] + -8 * g[k, n_occ + t, n_occ + s, n_occ + s] + 4 * g[i, i, k, n_occ + t] ) * K[0, k*n_virt + t] * K[1, (i*n_virt + s) * n_ex + i*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u == t) and (w == t) and (v == t)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[k, n_occ + t, n_occ + s, n_occ + t] ) * K[0, k*n_virt + t] * K[1, (i*n_virt + t) * n_ex + i*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u == t) and (w != s) and (w != t) and (w != u) and (w != v) and (v == t)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-8 * g[k, n_occ + t, n_occ + s, n_occ + w] + 4 * g[k, n_occ + w, n_occ + s, n_occ + t] ) * K[0, k*n_virt + t] * K[1, (i*n_virt + w) * n_ex + i*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u == t) and (w == s) and (v != s) and (v != t) and (v != u)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[k, n_occ + t, n_occ + t, n_occ + v] ) * K[0, k*n_virt + t] * K[1, (i*n_virt + s) * n_ex + i*n_virt + v+ 2*n_ex]

												elif ((t != s) and (u != s) and (u != t) and (w == s) and (v == s)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[k, n_occ + t, n_occ + s, n_occ + u] + 8 * g[k, n_occ + u, n_occ + s, n_occ + t] ) * K[0, k*n_virt + u] * K[1, (i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex]

												elif ((t != s) and (u != s) and (u != t) and (w == s) and (v == t)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[k, n_occ + t, n_occ + t, n_occ + u] + 8 * g[k, n_occ + u, n_occ + t, n_occ + t] + 4 * g[k, n_occ + s, n_occ + s, n_occ + u] + -8 * g[k, n_occ + u, n_occ + s, n_occ + s] ) * K[0, k*n_virt + u] * K[1, (i*n_virt + s) * n_ex + i*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u != s) and (u != t) and (w == t) and (v == t)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[k, n_occ + t, n_occ + s, n_occ + u] + -8 * g[k, n_occ + u, n_occ + s, n_occ + t] ) * K[0, k*n_virt + u] * K[1, (i*n_virt + t) * n_ex + i*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u != s) and (u != t) and (w == u) and (v == t)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[k, n_occ + u, n_occ + s, n_occ + u] ) * K[0, k*n_virt + u] * K[1, (i*n_virt + u) * n_ex + i*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u != s) and (u != t) and (w != s) and (w != t) and (w != u) and (w != v) and (v == t)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-8 * g[k, n_occ + u, n_occ + s, n_occ + w] + 4 * g[k, n_occ + w, n_occ + s, n_occ + u] ) * K[0, k*n_virt + u] * K[1, (i*n_virt + w) * n_ex + i*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u != s) and (u != t) and (w == s) and (v == u)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * F[k, n_occ + t] + 8 * g[k, n_occ + u, n_occ + t, n_occ + u] + -4 * g[k, n_occ + t, n_occ + u, n_occ + u] + 4 * g[i, i, k, n_occ + t] + -8 * g[i, k, i, n_occ + t] ) * K[0, k*n_virt + u] * K[1, (i*n_virt + s) * n_ex + i*n_virt + u+ 2*n_ex]

												elif ((t != s) and (u != s) and (u != t) and (w == s) and (v != s) and (v != t) and (v != u)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[k, n_occ + t, n_occ + u, n_occ + v] + 8 * g[k, n_occ + u, n_occ + t, n_occ + v] ) * K[0, k*n_virt + u] * K[1, (i*n_virt + s) * n_ex + i*n_virt + v+ 2*n_ex]

											elif ((j == i) and (k != i) and (k != j) and (n == k) and (m == i)):

												if ((t == s) and (u == s) and (w == s) and (v == s)):

													L3[(i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (8 * g[i, k, k, n_occ + s] ) * K[0, k*n_virt + s] * K[1, (k*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex]

												elif ((t == s) and (u == s) and (w != s) and (w != t) and (w != u) and (w != v) and (v == s)):

													L3[(i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, k, k, n_occ + w] ) * K[0, k*n_virt + s] * K[1, (k*n_virt + w) * n_ex + i*n_virt + s+ 2*n_ex]

												elif ((t == s) and (u != s) and (u != t) and (w == s) and (v == s)):

													L3[(i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, k, k, n_occ + u] ) * K[0, k*n_virt + u] * K[1, (k*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex]

												elif ((t != s) and (u == s) and (w == s) and (v == t)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (8 * g[i, k, k, n_occ + s] ) * K[0, k*n_virt + s] * K[1, (k*n_virt + s) * n_ex + i*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u == s) and (w == t) and (v == t)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, k, k, n_occ + t] ) * K[0, k*n_virt + s] * K[1, (k*n_virt + t) * n_ex + i*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u == s) and (w != s) and (w != t) and (w != u) and (w != v) and (v == t)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, k, k, n_occ + w] ) * K[0, k*n_virt + s] * K[1, (k*n_virt + w) * n_ex + i*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u == t) and (w == s) and (v == t)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, k, k, n_occ + t] ) * K[0, k*n_virt + t] * K[1, (k*n_virt + s) * n_ex + i*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u != s) and (u != t) and (w == s) and (v == t)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, k, k, n_occ + u] ) * K[0, k*n_virt + u] * K[1, (k*n_virt + s) * n_ex + i*n_virt + t+ 2*n_ex]

											elif ((j == i) and (k != i) and (k != j) and (n != i) and (n != j) and (n != k) and (n != m) and (m == i)):

												if ((t == s) and (u == s) and (w == s) and (v == s)):

													L3[(i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, n, k, n_occ + s] + 4 * g[i, k, n, n_occ + s] ) * K[0, k*n_virt + s] * K[1, (n*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex]

												elif ((t == s) and (u == s) and (w != s) and (w != t) and (w != u) and (w != v) and (v == s)):

													L3[(i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (8 * g[i, k, n, n_occ + w] + -4 * g[i, n, k, n_occ + w] ) * K[0, k*n_virt + s] * K[1, (n*n_virt + w) * n_ex + i*n_virt + s+ 2*n_ex]

												elif ((t == s) and (u != s) and (u != t) and (w == s) and (v == s)):

													L3[(i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, k, n, n_occ + u] + 8 * g[i, n, k, n_occ + u] ) * K[0, k*n_virt + u] * K[1, (n*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex]

												elif ((t != s) and (u == s) and (w == s) and (v == t)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, n, k, n_occ + s] + 4 * g[i, k, n, n_occ + s] ) * K[0, k*n_virt + s] * K[1, (n*n_virt + s) * n_ex + i*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u == s) and (w == t) and (v == t)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (8 * g[i, k, n, n_occ + t] + -4 * g[i, n, k, n_occ + t] ) * K[0, k*n_virt + s] * K[1, (n*n_virt + t) * n_ex + i*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u == s) and (w != s) and (w != t) and (w != u) and (w != v) and (v == t)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (8 * g[i, k, n, n_occ + w] + -4 * g[i, n, k, n_occ + w] ) * K[0, k*n_virt + s] * K[1, (n*n_virt + w) * n_ex + i*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u == t) and (w == s) and (v == t)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, k, n, n_occ + t] + 8 * g[i, n, k, n_occ + t] ) * K[0, k*n_virt + t] * K[1, (n*n_virt + s) * n_ex + i*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u != s) and (u != t) and (w == s) and (v == t)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, k, n, n_occ + u] + 8 * g[i, n, k, n_occ + u] ) * K[0, k*n_virt + u] * K[1, (n*n_virt + s) * n_ex + i*n_virt + t+ 2*n_ex]

											elif ((j == i) and (k != i) and (k != j) and (n == i) and (m == k)):

												if ((t == s) and (u == s) and (w == s) and (v == s)):

													L3[(i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * F[i, n_occ + s] + 4 * g[i, n_occ + s, n_occ + s, n_occ + s] + -4 * g[i, n_occ + s, k, k] + -4 * g[i, k, k, n_occ + s] ) * K[0, k*n_virt + s] * K[1, (i*n_virt + s) * n_ex + k*n_virt + s+ 2*n_ex]

												elif ((t == s) and (u == s) and (w == s) and (v != s) and (v != t) and (v != u)):

													L3[(i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, n_occ + s, n_occ + s, n_occ + v] ) * K[0, k*n_virt + s] * K[1, (i*n_virt + s) * n_ex + k*n_virt + v+ 2*n_ex]

												elif ((t == s) and (u != s) and (u != t) and (w == s) and (v == s)):

													L3[(i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * F[i, n_occ + u] + 8 * g[i, n_occ + s, n_occ + s, n_occ + u] + -4 * g[i, n_occ + u, n_occ + s, n_occ + s] + 4 * g[i, n_occ + u, k, k] + -8 * g[i, k, k, n_occ + u] ) * K[0, k*n_virt + u] * K[1, (i*n_virt + s) * n_ex + k*n_virt + s+ 2*n_ex]

												elif ((t == s) and (u != s) and (u != t) and (w == s) and (v == u)):

													L3[(i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, n_occ + u, n_occ + s, n_occ + u] + 8 * g[i, n_occ + s, n_occ + u, n_occ + u] + 4 * g[i, k, k, n_occ + s] + -8 * g[i, n_occ + s, k, k] ) * K[0, k*n_virt + u] * K[1, (i*n_virt + s) * n_ex + k*n_virt + u+ 2*n_ex]

												elif ((t == s) and (u != s) and (u != t) and (w == s) and (v != s) and (v != t) and (v != u)):

													L3[(i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (8 * g[i, n_occ + s, n_occ + u, n_occ + v] + -4 * g[i, n_occ + u, n_occ + s, n_occ + v] ) * K[0, k*n_virt + u] * K[1, (i*n_virt + s) * n_ex + k*n_virt + v+ 2*n_ex]

												elif ((t != s) and (u == s) and (w == s) and (v == s)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, n_occ + s, n_occ + s, n_occ + t] + 8 * g[i, n_occ + t, n_occ + s, n_occ + s] + 4 * g[i, k, k, n_occ + t] + -8 * g[i, n_occ + t, k, k] ) * K[0, k*n_virt + s] * K[1, (i*n_virt + s) * n_ex + k*n_virt + s+ 2*n_ex]

												elif ((t != s) and (u == s) and (w == s) and (v == t)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * F[i, n_occ + s] + 8 * g[i, n_occ + t, n_occ + s, n_occ + t] + -4 * g[i, n_occ + s, n_occ + t, n_occ + t] + 4 * g[i, n_occ + s, k, k] + -8 * g[i, k, k, n_occ + s] ) * K[0, k*n_virt + s] * K[1, (i*n_virt + s) * n_ex + k*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u == s) and (w == s) and (v != s) and (v != t) and (v != u)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, n_occ + s, n_occ + t, n_occ + v] + 8 * g[i, n_occ + t, n_occ + s, n_occ + v] ) * K[0, k*n_virt + s] * K[1, (i*n_virt + s) * n_ex + k*n_virt + v+ 2*n_ex]

												elif ((t != s) and (u == t) and (w == s) and (v == s)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, n_occ + t, n_occ + s, n_occ + t] ) * K[0, k*n_virt + t] * K[1, (i*n_virt + s) * n_ex + k*n_virt + s+ 2*n_ex]

												elif ((t != s) and (u == t) and (w == s) and (v == t)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * F[i, n_occ + t] + 4 * g[i, n_occ + t, n_occ + t, n_occ + t] + -4 * g[i, n_occ + t, k, k] + -4 * g[i, k, k, n_occ + t] ) * K[0, k*n_virt + t] * K[1, (i*n_virt + s) * n_ex + k*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u == t) and (w == s) and (v != s) and (v != t) and (v != u)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, n_occ + t, n_occ + t, n_occ + v] ) * K[0, k*n_virt + t] * K[1, (i*n_virt + s) * n_ex + k*n_virt + v+ 2*n_ex]

												elif ((t != s) and (u != s) and (u != t) and (w == s) and (v == s)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (8 * g[i, n_occ + t, n_occ + s, n_occ + u] + -4 * g[i, n_occ + u, n_occ + s, n_occ + t] ) * K[0, k*n_virt + u] * K[1, (i*n_virt + s) * n_ex + k*n_virt + s+ 2*n_ex]

												elif ((t != s) and (u != s) and (u != t) and (w == s) and (v == t)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * F[i, n_occ + u] + 8 * g[i, n_occ + t, n_occ + t, n_occ + u] + -4 * g[i, n_occ + u, n_occ + t, n_occ + t] + 4 * g[i, n_occ + u, k, k] + -8 * g[i, k, k, n_occ + u] ) * K[0, k*n_virt + u] * K[1, (i*n_virt + s) * n_ex + k*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u != s) and (u != t) and (w == s) and (v == u)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, n_occ + u, n_occ + t, n_occ + u] + 8 * g[i, n_occ + t, n_occ + u, n_occ + u] + 4 * g[i, k, k, n_occ + t] + -8 * g[i, n_occ + t, k, k] ) * K[0, k*n_virt + u] * K[1, (i*n_virt + s) * n_ex + k*n_virt + u+ 2*n_ex]

												elif ((t != s) and (u != s) and (u != t) and (w == s) and (v != s) and (v != t) and (v != u)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (8 * g[i, n_occ + t, n_occ + u, n_occ + v] + -4 * g[i, n_occ + u, n_occ + t, n_occ + v] ) * K[0, k*n_virt + u] * K[1, (i*n_virt + s) * n_ex + k*n_virt + v+ 2*n_ex]

											elif ((j == i) and (k != i) and (k != j) and (n == i) and (m != i) and (m != j) and (m != k)):

												if ((t == s) and (u == s) and (w == s) and (v == s)):

													L3[(i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, m, k, n_occ + s] + -4 * g[i, n_occ + s, k, m] ) * K[0, k*n_virt + s] * K[1, (i*n_virt + s) * n_ex + m*n_virt + s+ 2*n_ex]

												elif ((t == s) and (u != s) and (u != t) and (w == s) and (v == s)):

													L3[(i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-8 * g[i, m, k, n_occ + u] + 4 * g[i, n_occ + u, k, m] ) * K[0, k*n_virt + u] * K[1, (i*n_virt + s) * n_ex + m*n_virt + s+ 2*n_ex]

												elif ((t == s) and (u != s) and (u != t) and (w == s) and (v == u)):

													L3[(i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, m, k, n_occ + s] + -8 * g[i, n_occ + s, k, m] ) * K[0, k*n_virt + u] * K[1, (i*n_virt + s) * n_ex + m*n_virt + u+ 2*n_ex]

												elif ((t != s) and (u == s) and (w == s) and (v == s)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, m, k, n_occ + t] + -8 * g[i, n_occ + t, k, m] ) * K[0, k*n_virt + s] * K[1, (i*n_virt + s) * n_ex + m*n_virt + s+ 2*n_ex]

												elif ((t != s) and (u == s) and (w == s) and (v == t)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-8 * g[i, m, k, n_occ + s] + 4 * g[i, n_occ + s, k, m] ) * K[0, k*n_virt + s] * K[1, (i*n_virt + s) * n_ex + m*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u == t) and (w == s) and (v == t)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, m, k, n_occ + t] + -4 * g[i, n_occ + t, k, m] ) * K[0, k*n_virt + t] * K[1, (i*n_virt + s) * n_ex + m*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u != s) and (u != t) and (w == s) and (v == t)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-8 * g[i, m, k, n_occ + u] + 4 * g[i, n_occ + u, k, m] ) * K[0, k*n_virt + u] * K[1, (i*n_virt + s) * n_ex + m*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u != s) and (u != t) and (w == s) and (v == u)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, m, k, n_occ + t] + -8 * g[i, n_occ + t, k, m] ) * K[0, k*n_virt + u] * K[1, (i*n_virt + s) * n_ex + m*n_virt + u+ 2*n_ex]

											elif ((j != i) and (k == i) and (n == i) and (m == i)):

												if ((t == s) and (u == s) and (w == s) and (v == s)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * F[j, n_occ + s] + 4 * g[j, n_occ + s, n_occ + s, n_occ + s] + -4 * g[i, i, j, n_occ + s] + -4 * g[i, j, i, n_occ + s] ) * K[0, i*n_virt + s] * K[1, (i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex]

												elif ((t == s) and (u == s) and (w == s) and (v != s) and (v != t) and (v != u)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[j, n_occ + s, n_occ + s, n_occ + v] ) * K[0, i*n_virt + s] * K[1, (i*n_virt + s) * n_ex + i*n_virt + v+ 2*n_ex]

												elif ((t == s) and (u != s) and (u != t) and (w == s) and (v == s)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * F[j, n_occ + u] + 8 * g[j, n_occ + s, n_occ + s, n_occ + u] + -4 * g[j, n_occ + u, n_occ + s, n_occ + s] + 4 * g[i, i, j, n_occ + u] + -8 * g[i, j, i, n_occ + u] ) * K[0, i*n_virt + u] * K[1, (i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex]

												elif ((t == s) and (u != s) and (u != t) and (w == s) and (v == u)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[j, n_occ + u, n_occ + s, n_occ + u] + 8 * g[j, n_occ + s, n_occ + u, n_occ + u] + 4 * g[i, j, i, n_occ + s] + -8 * g[i, i, j, n_occ + s] ) * K[0, i*n_virt + u] * K[1, (i*n_virt + s) * n_ex + i*n_virt + u+ 2*n_ex]

												elif ((t == s) and (u != s) and (u != t) and (w == s) and (v != s) and (v != t) and (v != u)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (8 * g[j, n_occ + s, n_occ + u, n_occ + v] + -4 * g[j, n_occ + u, n_occ + s, n_occ + v] ) * K[0, i*n_virt + u] * K[1, (i*n_virt + s) * n_ex + i*n_virt + v+ 2*n_ex]

												elif ((t != s) and (u == s) and (w == s) and (v == s)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[j, n_occ + s, n_occ + s, n_occ + t] + 8 * g[j, n_occ + t, n_occ + s, n_occ + s] + 4 * g[i, j, i, n_occ + t] + -8 * g[i, i, j, n_occ + t] ) * K[0, i*n_virt + s] * K[1, (i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex]

												elif ((t != s) and (u == s) and (w == s) and (v == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * F[j, n_occ + s] + 8 * g[j, n_occ + t, n_occ + s, n_occ + t] + -4 * g[j, n_occ + s, n_occ + t, n_occ + t] + 4 * g[i, i, j, n_occ + s] + -8 * g[i, j, i, n_occ + s] ) * K[0, i*n_virt + s] * K[1, (i*n_virt + s) * n_ex + i*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u == s) and (w == s) and (v != s) and (v != t) and (v != u)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[j, n_occ + s, n_occ + t, n_occ + v] + 8 * g[j, n_occ + t, n_occ + s, n_occ + v] ) * K[0, i*n_virt + s] * K[1, (i*n_virt + s) * n_ex + i*n_virt + v+ 2*n_ex]

												elif ((t != s) and (u == t) and (w == s) and (v == s)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[j, n_occ + t, n_occ + s, n_occ + t] ) * K[0, i*n_virt + t] * K[1, (i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex]

												elif ((t != s) and (u == t) and (w == s) and (v == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * F[j, n_occ + t] + 4 * g[j, n_occ + t, n_occ + t, n_occ + t] + -4 * g[i, i, j, n_occ + t] + -4 * g[i, j, i, n_occ + t] ) * K[0, i*n_virt + t] * K[1, (i*n_virt + s) * n_ex + i*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u == t) and (w == s) and (v != s) and (v != t) and (v != u)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[j, n_occ + t, n_occ + t, n_occ + v] ) * K[0, i*n_virt + t] * K[1, (i*n_virt + s) * n_ex + i*n_virt + v+ 2*n_ex]

												elif ((t != s) and (u != s) and (u != t) and (w == s) and (v == s)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (8 * g[j, n_occ + t, n_occ + s, n_occ + u] + -4 * g[j, n_occ + u, n_occ + s, n_occ + t] ) * K[0, i*n_virt + u] * K[1, (i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex]

												elif ((t != s) and (u != s) and (u != t) and (w == s) and (v == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * F[j, n_occ + u] + 8 * g[j, n_occ + t, n_occ + t, n_occ + u] + -4 * g[j, n_occ + u, n_occ + t, n_occ + t] + 4 * g[i, i, j, n_occ + u] + -8 * g[i, j, i, n_occ + u] ) * K[0, i*n_virt + u] * K[1, (i*n_virt + s) * n_ex + i*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u != s) and (u != t) and (w == s) and (v == u)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[j, n_occ + u, n_occ + t, n_occ + u] + 8 * g[j, n_occ + t, n_occ + u, n_occ + u] + 4 * g[i, j, i, n_occ + t] + -8 * g[i, i, j, n_occ + t] ) * K[0, i*n_virt + u] * K[1, (i*n_virt + s) * n_ex + i*n_virt + u+ 2*n_ex]

												elif ((t != s) and (u != s) and (u != t) and (w == s) and (v != s) and (v != t) and (v != u)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (8 * g[j, n_occ + t, n_occ + u, n_occ + v] + -4 * g[j, n_occ + u, n_occ + t, n_occ + v] ) * K[0, i*n_virt + u] * K[1, (i*n_virt + s) * n_ex + i*n_virt + v+ 2*n_ex]

											elif ((j != i) and (k == i) and (n == i) and (m == j)):

												if ((t == s) and (u == s) and (w == s) and (v == s)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * F[i, n_occ + s] + -4 * g[i, j, j, n_occ + s] + 8 * g[i, i, i, n_occ + s] + -4 * g[i, n_occ + s, j, j] + -4 * g[i, n_occ + s, n_occ + s, n_occ + s] ) * K[0, i*n_virt + s] * K[1, (i*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex]

												elif ((t == s) and (u == s) and (w != s) and (w != t) and (w != u) and (w != v) and (v == s)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * F[i, n_occ + w] + -4 * g[i, n_occ + s, n_occ + s, n_occ + w] + -4 * g[i, n_occ + w, n_occ + s, n_occ + s] + 4 * g[i, i, i, n_occ + w] ) * K[0, i*n_virt + s] * K[1, (i*n_virt + w) * n_ex + j*n_virt + s+ 2*n_ex]

												elif ((t == s) and (u == s) and (w == s) and (v != s) and (v != t) and (v != u)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, n_occ + s, n_occ + s, n_occ + v] ) * K[0, i*n_virt + s] * K[1, (i*n_virt + s) * n_ex + j*n_virt + v+ 2*n_ex]

												elif ((t == s) and (u != s) and (u != t) and (w == s) and (v == s)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * F[i, n_occ + u] + -8 * g[i, n_occ + s, n_occ + s, n_occ + u] + 4 * g[i, n_occ + u, n_occ + s, n_occ + s] + 4 * g[i, i, i, n_occ + u] + -8 * g[i, n_occ + u, j, j] + 4 * g[i, j, j, n_occ + u] ) * K[0, i*n_virt + u] * K[1, (i*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex]

												elif ((t == s) and (u != s) and (u != t) and (w == u) and (v == s)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-8 * g[i, n_occ + u, n_occ + s, n_occ + u] ) * K[0, i*n_virt + u] * K[1, (i*n_virt + u) * n_ex + j*n_virt + s+ 2*n_ex]

												elif ((t == s) and (u != s) and (u != t) and (w != s) and (w != t) and (w != u) and (w != v) and (v == s)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, n_occ + u, n_occ + s, n_occ + w] + -4 * g[i, n_occ + w, n_occ + s, n_occ + u] ) * K[0, i*n_virt + u] * K[1, (i*n_virt + w) * n_ex + j*n_virt + s+ 2*n_ex]

												elif ((t == s) and (u != s) and (u != t) and (w == s) and (v == u)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * F[i, n_occ + s] + 8 * g[i, n_occ + u, n_occ + s, n_occ + u] + -4 * g[i, n_occ + s, n_occ + u, n_occ + u] + 4 * g[i, n_occ + s, j, j] + -8 * g[i, j, j, n_occ + s] ) * K[0, i*n_virt + u] * K[1, (i*n_virt + s) * n_ex + j*n_virt + u+ 2*n_ex]

												elif ((t == s) and (u != s) and (u != t) and (w == s) and (v != s) and (v != t) and (v != u)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, n_occ + s, n_occ + u, n_occ + v] + 8 * g[i, n_occ + u, n_occ + s, n_occ + v] ) * K[0, i*n_virt + u] * K[1, (i*n_virt + s) * n_ex + j*n_virt + v+ 2*n_ex]

												elif ((t != s) and (u == s) and (w == s) and (v == s)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * F[i, n_occ + t] + 8 * g[i, n_occ + s, n_occ + s, n_occ + t] + -4 * g[i, n_occ + t, n_occ + s, n_occ + s] + 4 * g[i, n_occ + t, j, j] + -8 * g[i, j, j, n_occ + t] ) * K[0, i*n_virt + s] * K[1, (i*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex]

												elif ((t != s) and (u == s) and (w == s) and (v == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (8 * F[i, n_occ + s] + -4 * g[i, n_occ + t, n_occ + s, n_occ + t] + 8 * g[i, n_occ + s, n_occ + t, n_occ + t] + -8 * g[i, n_occ + s, j, j] + 4 * g[i, j, j, n_occ + s] + -8 * g[i, n_occ + s, n_occ + s, n_occ + s] + 8 * g[i, i, i, n_occ + s] ) * K[0, i*n_virt + s] * K[1, (i*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u == s) and (w == t) and (v == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * F[i, n_occ + t] + -4 * g[i, n_occ + s, n_occ + s, n_occ + t] + -4 * g[i, n_occ + t, n_occ + s, n_occ + s] + 4 * g[i, i, i, n_occ + t] ) * K[0, i*n_virt + s] * K[1, (i*n_virt + t) * n_ex + j*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u == s) and (w != s) and (w != t) and (w != u) and (w != v) and (v == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * F[i, n_occ + w] + -4 * g[i, n_occ + s, n_occ + s, n_occ + w] + -4 * g[i, n_occ + w, n_occ + s, n_occ + s] + 4 * g[i, i, i, n_occ + w] ) * K[0, i*n_virt + s] * K[1, (i*n_virt + w) * n_ex + j*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u == s) and (w == s) and (v != s) and (v != t) and (v != u)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (8 * g[i, n_occ + s, n_occ + t, n_occ + v] + -4 * g[i, n_occ + t, n_occ + s, n_occ + v] ) * K[0, i*n_virt + s] * K[1, (i*n_virt + s) * n_ex + j*n_virt + v+ 2*n_ex]

												elif ((t != s) and (u == t) and (w == s) and (v == s)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, n_occ + t, n_occ + s, n_occ + t] ) * K[0, i*n_virt + t] * K[1, (i*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex]

												elif ((t != s) and (u == t) and (w == s) and (v == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, n_occ + t, n_occ + t, n_occ + t] + -4 * g[i, j, j, n_occ + t] + 4 * g[i, i, i, n_occ + t] + -4 * g[i, n_occ + t, n_occ + s, n_occ + s] + -4 * g[i, n_occ + s, n_occ + s, n_occ + t] + -4 * g[i, n_occ + t, j, j] ) * K[0, i*n_virt + t] * K[1, (i*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u == t) and (w == t) and (v == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-8 * g[i, n_occ + t, n_occ + s, n_occ + t] ) * K[0, i*n_virt + t] * K[1, (i*n_virt + t) * n_ex + j*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u == t) and (w != s) and (w != t) and (w != u) and (w != v) and (v == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, n_occ + t, n_occ + s, n_occ + w] + -4 * g[i, n_occ + w, n_occ + s, n_occ + t] ) * K[0, i*n_virt + t] * K[1, (i*n_virt + w) * n_ex + j*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u == t) and (w == s) and (v != s) and (v != t) and (v != u)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, n_occ + t, n_occ + t, n_occ + v] ) * K[0, i*n_virt + t] * K[1, (i*n_virt + s) * n_ex + j*n_virt + v+ 2*n_ex]

												elif ((t != s) and (u != s) and (u != t) and (w == s) and (v == s)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, n_occ + t, n_occ + s, n_occ + u] + 8 * g[i, n_occ + u, n_occ + s, n_occ + t] ) * K[0, i*n_virt + u] * K[1, (i*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex]

												elif ((t != s) and (u != s) and (u != t) and (w == s) and (v == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * F[i, n_occ + u] + -4 * g[i, n_occ + t, n_occ + t, n_occ + u] + 8 * g[i, n_occ + u, n_occ + t, n_occ + t] + -4 * g[i, n_occ + u, n_occ + s, n_occ + s] + -4 * g[i, n_occ + s, n_occ + s, n_occ + u] + 4 * g[i, i, i, n_occ + u] + -8 * g[i, n_occ + u, j, j] + 4 * g[i, j, j, n_occ + u] ) * K[0, i*n_virt + u] * K[1, (i*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u != s) and (u != t) and (w == t) and (v == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, n_occ + u, n_occ + s, n_occ + t] + -4 * g[i, n_occ + t, n_occ + s, n_occ + u] ) * K[0, i*n_virt + u] * K[1, (i*n_virt + t) * n_ex + j*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u != s) and (u != t) and (w == u) and (v == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-8 * g[i, n_occ + u, n_occ + s, n_occ + u] ) * K[0, i*n_virt + u] * K[1, (i*n_virt + u) * n_ex + j*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u != s) and (u != t) and (w != s) and (w != t) and (w != u) and (w != v) and (v == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, n_occ + u, n_occ + s, n_occ + w] + -4 * g[i, n_occ + w, n_occ + s, n_occ + u] ) * K[0, i*n_virt + u] * K[1, (i*n_virt + w) * n_ex + j*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u != s) and (u != t) and (w == s) and (v == u)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * F[i, n_occ + t] + 8 * g[i, n_occ + u, n_occ + t, n_occ + u] + -4 * g[i, n_occ + t, n_occ + u, n_occ + u] + 4 * g[i, n_occ + t, j, j] + -8 * g[i, j, j, n_occ + t] ) * K[0, i*n_virt + u] * K[1, (i*n_virt + s) * n_ex + j*n_virt + u+ 2*n_ex]

												elif ((t != s) and (u != s) and (u != t) and (w == s) and (v != s) and (v != t) and (v != u)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, n_occ + t, n_occ + u, n_occ + v] + 8 * g[i, n_occ + u, n_occ + t, n_occ + v] ) * K[0, i*n_virt + u] * K[1, (i*n_virt + s) * n_ex + j*n_virt + v+ 2*n_ex]

											elif ((j != i) and (k == i) and (n == j) and (m == j)):

												if ((t == s) and (u == s) and (w == s) and (v == s)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * F[j, n_occ + s] + 4 * g[i, i, j, n_occ + s] + -4 * g[j, n_occ + s, n_occ + s, n_occ + s] + 4 * g[i, j, i, n_occ + s] ) * K[0, i*n_virt + s] * K[1, (j*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex]

												elif ((t == s) and (u == s) and (w != s) and (w != t) and (w != u) and (w != v) and (v == s)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, j, i, n_occ + w] + 8 * g[i, i, j, n_occ + w] + 4 * g[j, n_occ + s, n_occ + s, n_occ + w] + -8 * g[j, n_occ + w, n_occ + s, n_occ + s] ) * K[0, i*n_virt + s] * K[1, (j*n_virt + w) * n_ex + j*n_virt + s+ 2*n_ex]

												elif ((t == s) and (u != s) and (u != t) and (w == s) and (v == s)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * F[j, n_occ + u] + -8 * g[j, n_occ + s, n_occ + s, n_occ + u] + 4 * g[j, n_occ + u, n_occ + s, n_occ + s] + -4 * g[i, i, j, n_occ + u] + 8 * g[i, j, i, n_occ + u] ) * K[0, i*n_virt + u] * K[1, (j*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex]

												elif ((t == s) and (u != s) and (u != t) and (w == u) and (v == s)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[j, n_occ + u, n_occ + s, n_occ + u] ) * K[0, i*n_virt + u] * K[1, (j*n_virt + u) * n_ex + j*n_virt + s+ 2*n_ex]

												elif ((t == s) and (u != s) and (u != t) and (w != s) and (w != t) and (w != u) and (w != v) and (v == s)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[j, n_occ + u, n_occ + s, n_occ + w] + -8 * g[j, n_occ + w, n_occ + s, n_occ + u] ) * K[0, i*n_virt + u] * K[1, (j*n_virt + w) * n_ex + j*n_virt + s+ 2*n_ex]

												elif ((t != s) and (u == s) and (w == s) and (v == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * F[j, n_occ + s] + 4 * g[i, i, j, n_occ + s] + -4 * g[j, n_occ + s, n_occ + s, n_occ + s] + 4 * g[i, j, i, n_occ + s] ) * K[0, i*n_virt + s] * K[1, (j*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u == s) and (w == t) and (v == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, j, i, n_occ + t] + 8 * g[i, i, j, n_occ + t] + 4 * g[j, n_occ + s, n_occ + s, n_occ + t] + -8 * g[j, n_occ + t, n_occ + s, n_occ + s] ) * K[0, i*n_virt + s] * K[1, (j*n_virt + t) * n_ex + j*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u == s) and (w != s) and (w != t) and (w != u) and (w != v) and (v == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, j, i, n_occ + w] + 8 * g[i, i, j, n_occ + w] + 4 * g[j, n_occ + s, n_occ + s, n_occ + w] + -8 * g[j, n_occ + w, n_occ + s, n_occ + s] ) * K[0, i*n_virt + s] * K[1, (j*n_virt + w) * n_ex + j*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u == t) and (w == s) and (v == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * F[j, n_occ + t] + -8 * g[j, n_occ + s, n_occ + s, n_occ + t] + 4 * g[j, n_occ + t, n_occ + s, n_occ + s] + -4 * g[i, i, j, n_occ + t] + 8 * g[i, j, i, n_occ + t] ) * K[0, i*n_virt + t] * K[1, (j*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u == t) and (w == t) and (v == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[j, n_occ + t, n_occ + s, n_occ + t] ) * K[0, i*n_virt + t] * K[1, (j*n_virt + t) * n_ex + j*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u == t) and (w != s) and (w != t) and (w != u) and (w != v) and (v == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[j, n_occ + t, n_occ + s, n_occ + w] + -8 * g[j, n_occ + w, n_occ + s, n_occ + t] ) * K[0, i*n_virt + t] * K[1, (j*n_virt + w) * n_ex + j*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u != s) and (u != t) and (w == s) and (v == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * F[j, n_occ + u] + -8 * g[j, n_occ + s, n_occ + s, n_occ + u] + 4 * g[j, n_occ + u, n_occ + s, n_occ + s] + -4 * g[i, i, j, n_occ + u] + 8 * g[i, j, i, n_occ + u] ) * K[0, i*n_virt + u] * K[1, (j*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u != s) and (u != t) and (w == t) and (v == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-8 * g[j, n_occ + t, n_occ + s, n_occ + u] + 4 * g[j, n_occ + u, n_occ + s, n_occ + t] ) * K[0, i*n_virt + u] * K[1, (j*n_virt + t) * n_ex + j*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u != s) and (u != t) and (w == u) and (v == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[j, n_occ + u, n_occ + s, n_occ + u] ) * K[0, i*n_virt + u] * K[1, (j*n_virt + u) * n_ex + j*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u != s) and (u != t) and (w != s) and (w != t) and (w != u) and (w != v) and (v == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[j, n_occ + u, n_occ + s, n_occ + w] + -8 * g[j, n_occ + w, n_occ + s, n_occ + u] ) * K[0, i*n_virt + u] * K[1, (j*n_virt + w) * n_ex + j*n_virt + t+ 2*n_ex]

											elif ((j != i) and (k == i) and (n != i) and (n != j) and (n != k) and (n != m) and (m == j)):

												if ((t == s) and (u == s) and (w == s) and (v == s)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * F[n, n_occ + s] + 4 * g[i, i, n, n_occ + s] + -4 * g[n, n_occ + s, n_occ + s, n_occ + s] + 4 * g[i, n, i, n_occ + s] ) * K[0, i*n_virt + s] * K[1, (n*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex]

												elif ((t == s) and (u == s) and (w != s) and (w != t) and (w != u) and (w != v) and (v == s)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, n, i, n_occ + w] + 8 * g[i, i, n, n_occ + w] + 4 * g[n, n_occ + s, n_occ + s, n_occ + w] + -8 * g[n, n_occ + w, n_occ + s, n_occ + s] ) * K[0, i*n_virt + s] * K[1, (n*n_virt + w) * n_ex + j*n_virt + s+ 2*n_ex]

												elif ((t == s) and (u != s) and (u != t) and (w == s) and (v == s)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * F[n, n_occ + u] + -8 * g[n, n_occ + s, n_occ + s, n_occ + u] + 4 * g[n, n_occ + u, n_occ + s, n_occ + s] + -4 * g[i, i, n, n_occ + u] + 8 * g[i, n, i, n_occ + u] ) * K[0, i*n_virt + u] * K[1, (n*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex]

												elif ((t == s) and (u != s) and (u != t) and (w == u) and (v == s)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[n, n_occ + u, n_occ + s, n_occ + u] ) * K[0, i*n_virt + u] * K[1, (n*n_virt + u) * n_ex + j*n_virt + s+ 2*n_ex]

												elif ((t == s) and (u != s) and (u != t) and (w != s) and (w != t) and (w != u) and (w != v) and (v == s)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[n, n_occ + u, n_occ + s, n_occ + w] + -8 * g[n, n_occ + w, n_occ + s, n_occ + u] ) * K[0, i*n_virt + u] * K[1, (n*n_virt + w) * n_ex + j*n_virt + s+ 2*n_ex]

												elif ((t != s) and (u == s) and (w == s) and (v == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * F[n, n_occ + s] + 4 * g[i, i, n, n_occ + s] + -4 * g[n, n_occ + s, n_occ + s, n_occ + s] + 4 * g[i, n, i, n_occ + s] ) * K[0, i*n_virt + s] * K[1, (n*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u == s) and (w == t) and (v == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, n, i, n_occ + t] + 8 * g[i, i, n, n_occ + t] + 4 * g[n, n_occ + s, n_occ + s, n_occ + t] + -8 * g[n, n_occ + t, n_occ + s, n_occ + s] ) * K[0, i*n_virt + s] * K[1, (n*n_virt + t) * n_ex + j*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u == s) and (w != s) and (w != t) and (w != u) and (w != v) and (v == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, n, i, n_occ + w] + 8 * g[i, i, n, n_occ + w] + 4 * g[n, n_occ + s, n_occ + s, n_occ + w] + -8 * g[n, n_occ + w, n_occ + s, n_occ + s] ) * K[0, i*n_virt + s] * K[1, (n*n_virt + w) * n_ex + j*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u == t) and (w == s) and (v == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * F[n, n_occ + t] + -8 * g[n, n_occ + s, n_occ + s, n_occ + t] + 4 * g[n, n_occ + t, n_occ + s, n_occ + s] + -4 * g[i, i, n, n_occ + t] + 8 * g[i, n, i, n_occ + t] ) * K[0, i*n_virt + t] * K[1, (n*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u == t) and (w == t) and (v == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[n, n_occ + t, n_occ + s, n_occ + t] ) * K[0, i*n_virt + t] * K[1, (n*n_virt + t) * n_ex + j*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u == t) and (w != s) and (w != t) and (w != u) and (w != v) and (v == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[n, n_occ + t, n_occ + s, n_occ + w] + -8 * g[n, n_occ + w, n_occ + s, n_occ + t] ) * K[0, i*n_virt + t] * K[1, (n*n_virt + w) * n_ex + j*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u != s) and (u != t) and (w == s) and (v == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * F[n, n_occ + u] + -8 * g[n, n_occ + s, n_occ + s, n_occ + u] + 4 * g[n, n_occ + u, n_occ + s, n_occ + s] + -4 * g[i, i, n, n_occ + u] + 8 * g[i, n, i, n_occ + u] ) * K[0, i*n_virt + u] * K[1, (n*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u != s) and (u != t) and (w == t) and (v == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-8 * g[n, n_occ + t, n_occ + s, n_occ + u] + 4 * g[n, n_occ + u, n_occ + s, n_occ + t] ) * K[0, i*n_virt + u] * K[1, (n*n_virt + t) * n_ex + j*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u != s) and (u != t) and (w == u) and (v == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[n, n_occ + u, n_occ + s, n_occ + u] ) * K[0, i*n_virt + u] * K[1, (n*n_virt + u) * n_ex + j*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u != s) and (u != t) and (w != s) and (w != t) and (w != u) and (w != v) and (v == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[n, n_occ + u, n_occ + s, n_occ + w] + -8 * g[n, n_occ + w, n_occ + s, n_occ + u] ) * K[0, i*n_virt + u] * K[1, (n*n_virt + w) * n_ex + j*n_virt + t+ 2*n_ex]

											elif ((j != i) and (k == i) and (n == i) and (m != i) and (m != j) and (m != k)):

												if ((t == s) and (u == s) and (w == s) and (v == s)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, n_occ + s, j, m] + -4 * g[i, m, j, n_occ + s] ) * K[0, i*n_virt + s] * K[1, (i*n_virt + s) * n_ex + m*n_virt + s+ 2*n_ex]

												elif ((t == s) and (u != s) and (u != t) and (w == s) and (v == s)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, m, j, n_occ + u] + -8 * g[i, n_occ + u, j, m] ) * K[0, i*n_virt + u] * K[1, (i*n_virt + s) * n_ex + m*n_virt + s+ 2*n_ex]

												elif ((t == s) and (u != s) and (u != t) and (w == s) and (v == u)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-8 * g[i, m, j, n_occ + s] + 4 * g[i, n_occ + s, j, m] ) * K[0, i*n_virt + u] * K[1, (i*n_virt + s) * n_ex + m*n_virt + u+ 2*n_ex]

												elif ((t != s) and (u == s) and (w == s) and (v == s)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-8 * g[i, m, j, n_occ + t] + 4 * g[i, n_occ + t, j, m] ) * K[0, i*n_virt + s] * K[1, (i*n_virt + s) * n_ex + m*n_virt + s+ 2*n_ex]

												elif ((t != s) and (u == s) and (w == s) and (v == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, m, j, n_occ + s] + -8 * g[i, n_occ + s, j, m] ) * K[0, i*n_virt + s] * K[1, (i*n_virt + s) * n_ex + m*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u == t) and (w == s) and (v == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, n_occ + t, j, m] + -4 * g[i, m, j, n_occ + t] ) * K[0, i*n_virt + t] * K[1, (i*n_virt + s) * n_ex + m*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u != s) and (u != t) and (w == s) and (v == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, m, j, n_occ + u] + -8 * g[i, n_occ + u, j, m] ) * K[0, i*n_virt + u] * K[1, (i*n_virt + s) * n_ex + m*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u != s) and (u != t) and (w == s) and (v == u)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-8 * g[i, m, j, n_occ + t] + 4 * g[i, n_occ + t, j, m] ) * K[0, i*n_virt + u] * K[1, (i*n_virt + s) * n_ex + m*n_virt + u+ 2*n_ex]

											elif ((j != i) and (k == j) and (n == i) and (m == i)):

												if ((t == s) and (u == s) and (w == s) and (v == s)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-8 * g[i, j, j, n_occ + s] ) * K[0, j*n_virt + s] * K[1, (i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex]

												elif ((t == s) and (u != s) and (u != t) and (w == s) and (v == s)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, j, j, n_occ + u] ) * K[0, j*n_virt + u] * K[1, (i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex]

												elif ((t == s) and (u != s) and (u != t) and (w == s) and (v == u)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, j, j, n_occ + s] ) * K[0, j*n_virt + u] * K[1, (i*n_virt + s) * n_ex + i*n_virt + u+ 2*n_ex]

												elif ((t != s) and (u == s) and (w == s) and (v == s)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, j, j, n_occ + t] ) * K[0, j*n_virt + s] * K[1, (i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex]

												elif ((t != s) and (u == s) and (w == s) and (v == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, j, j, n_occ + s] ) * K[0, j*n_virt + s] * K[1, (i*n_virt + s) * n_ex + i*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u == t) and (w == s) and (v == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-8 * g[i, j, j, n_occ + t] ) * K[0, j*n_virt + t] * K[1, (i*n_virt + s) * n_ex + i*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u != s) and (u != t) and (w == s) and (v == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, j, j, n_occ + u] ) * K[0, j*n_virt + u] * K[1, (i*n_virt + s) * n_ex + i*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u != s) and (u != t) and (w == s) and (v == u)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, j, j, n_occ + t] ) * K[0, j*n_virt + u] * K[1, (i*n_virt + s) * n_ex + i*n_virt + u+ 2*n_ex]

											elif ((j != i) and (k == j) and (n == i) and (m == j)):

												if ((t == s) and (u == s) and (w == s) and (v == s)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * F[j, n_occ + s] + 4 * g[j, n_occ + s, n_occ + s, n_occ + s] + -8 * g[j, j, j, n_occ + s] + 4 * g[i, j, i, n_occ + s] + 4 * g[i, i, j, n_occ + s] ) * K[0, j*n_virt + s] * K[1, (i*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex]

												elif ((t == s) and (u == s) and (w != s) and (w != t) and (w != u) and (w != v) and (v == s)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * F[j, n_occ + w] + -8 * g[j, n_occ + s, n_occ + s, n_occ + w] + 4 * g[j, n_occ + w, n_occ + s, n_occ + s] + -4 * g[i, i, j, n_occ + w] + 8 * g[i, j, i, n_occ + w] ) * K[0, j*n_virt + s] * K[1, (i*n_virt + w) * n_ex + j*n_virt + s+ 2*n_ex]

												elif ((t == s) and (u == s) and (w == s) and (v != s) and (v != t) and (v != u)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (8 * g[j, n_occ + s, n_occ + s, n_occ + v] ) * K[0, j*n_virt + s] * K[1, (i*n_virt + s) * n_ex + j*n_virt + v+ 2*n_ex]

												elif ((t == s) and (u != s) and (u != t) and (w == s) and (v == s)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * F[j, n_occ + u] + 8 * g[j, n_occ + s, n_occ + s, n_occ + u] + -4 * g[j, n_occ + u, n_occ + s, n_occ + s] + 8 * g[i, i, j, n_occ + u] + -4 * g[i, j, i, n_occ + u] + -4 * g[j, j, j, n_occ + u] ) * K[0, j*n_virt + u] * K[1, (i*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex]

												elif ((t == s) and (u != s) and (u != t) and (w == u) and (v == s)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[j, n_occ + u, n_occ + s, n_occ + u] ) * K[0, j*n_virt + u] * K[1, (i*n_virt + u) * n_ex + j*n_virt + s+ 2*n_ex]

												elif ((t == s) and (u != s) and (u != t) and (w != s) and (w != t) and (w != u) and (w != v) and (v == s)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-8 * g[j, n_occ + u, n_occ + s, n_occ + w] + 4 * g[j, n_occ + w, n_occ + s, n_occ + u] ) * K[0, j*n_virt + u] * K[1, (i*n_virt + w) * n_ex + j*n_virt + s+ 2*n_ex]

												elif ((t == s) and (u != s) and (u != t) and (w == s) and (v == u)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * F[j, n_occ + s] + 4 * g[j, n_occ + u, n_occ + s, n_occ + u] + 4 * g[j, n_occ + s, n_occ + u, n_occ + u] + -4 * g[j, j, j, n_occ + s] ) * K[0, j*n_virt + u] * K[1, (i*n_virt + s) * n_ex + j*n_virt + u+ 2*n_ex]

												elif ((t == s) and (u != s) and (u != t) and (w == s) and (v != s) and (v != t) and (v != u)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[j, n_occ + u, n_occ + s, n_occ + v] + 4 * g[j, n_occ + s, n_occ + u, n_occ + v] ) * K[0, j*n_virt + u] * K[1, (i*n_virt + s) * n_ex + j*n_virt + v+ 2*n_ex]

												elif ((t != s) and (u == s) and (w == s) and (v == s)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * F[j, n_occ + t] + 4 * g[j, n_occ + s, n_occ + s, n_occ + t] + 4 * g[j, n_occ + t, n_occ + s, n_occ + s] + -4 * g[j, j, j, n_occ + t] ) * K[0, j*n_virt + s] * K[1, (i*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex]

												elif ((t != s) and (u == s) and (w == s) and (v == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[j, n_occ + s, n_occ + t, n_occ + t] + 4 * g[j, n_occ + t, n_occ + s, n_occ + t] + 4 * g[i, i, j, n_occ + s] + -4 * g[j, j, j, n_occ + s] + -4 * g[j, n_occ + s, n_occ + s, n_occ + s] + 4 * g[i, j, i, n_occ + s] ) * K[0, j*n_virt + s] * K[1, (i*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u == s) and (w == t) and (v == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * F[j, n_occ + t] + -8 * g[j, n_occ + s, n_occ + s, n_occ + t] + 4 * g[j, n_occ + t, n_occ + s, n_occ + s] + -4 * g[i, i, j, n_occ + t] + 8 * g[i, j, i, n_occ + t] ) * K[0, j*n_virt + s] * K[1, (i*n_virt + t) * n_ex + j*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u == s) and (w != s) and (w != t) and (w != u) and (w != v) and (v == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * F[j, n_occ + w] + -8 * g[j, n_occ + s, n_occ + s, n_occ + w] + 4 * g[j, n_occ + w, n_occ + s, n_occ + s] + -4 * g[i, i, j, n_occ + w] + 8 * g[i, j, i, n_occ + w] ) * K[0, j*n_virt + s] * K[1, (i*n_virt + w) * n_ex + j*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u == s) and (w == s) and (v != s) and (v != t) and (v != u)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[j, n_occ + s, n_occ + t, n_occ + v] + 4 * g[j, n_occ + t, n_occ + s, n_occ + v] ) * K[0, j*n_virt + s] * K[1, (i*n_virt + s) * n_ex + j*n_virt + v+ 2*n_ex]

												elif ((t != s) and (u == t) and (w == s) and (v == s)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (8 * g[j, n_occ + t, n_occ + s, n_occ + t] ) * K[0, j*n_virt + t] * K[1, (i*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex]

												elif ((t != s) and (u == t) and (w == s) and (v == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-8 * F[j, n_occ + t] + 8 * g[j, n_occ + t, n_occ + t, n_occ + t] + 4 * g[j, n_occ + s, n_occ + s, n_occ + t] + -8 * g[j, n_occ + t, n_occ + s, n_occ + s] + -4 * g[i, j, i, n_occ + t] + 8 * g[i, i, j, n_occ + t] + -8 * g[j, j, j, n_occ + t] ) * K[0, j*n_virt + t] * K[1, (i*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u == t) and (w == t) and (v == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[j, n_occ + t, n_occ + s, n_occ + t] ) * K[0, j*n_virt + t] * K[1, (i*n_virt + t) * n_ex + j*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u == t) and (w != s) and (w != t) and (w != u) and (w != v) and (v == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-8 * g[j, n_occ + t, n_occ + s, n_occ + w] + 4 * g[j, n_occ + w, n_occ + s, n_occ + t] ) * K[0, j*n_virt + t] * K[1, (i*n_virt + w) * n_ex + j*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u == t) and (w == s) and (v != s) and (v != t) and (v != u)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (8 * g[j, n_occ + t, n_occ + t, n_occ + v] ) * K[0, j*n_virt + t] * K[1, (i*n_virt + s) * n_ex + j*n_virt + v+ 2*n_ex]

												elif ((t != s) and (u != s) and (u != t) and (w == s) and (v == s)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[j, n_occ + u, n_occ + s, n_occ + t] + 4 * g[j, n_occ + t, n_occ + s, n_occ + u] ) * K[0, j*n_virt + u] * K[1, (i*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex]

												elif ((t != s) and (u != s) and (u != t) and (w == s) and (v == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * F[j, n_occ + u] + 4 * g[j, n_occ + u, n_occ + t, n_occ + t] + 4 * g[j, n_occ + t, n_occ + t, n_occ + u] + 4 * g[j, n_occ + s, n_occ + s, n_occ + u] + -8 * g[j, n_occ + u, n_occ + s, n_occ + s] + 8 * g[i, i, j, n_occ + u] + -4 * g[i, j, i, n_occ + u] + -4 * g[j, j, j, n_occ + u] ) * K[0, j*n_virt + u] * K[1, (i*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u != s) and (u != t) and (w == t) and (v == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[j, n_occ + t, n_occ + s, n_occ + u] + -8 * g[j, n_occ + u, n_occ + s, n_occ + t] ) * K[0, j*n_virt + u] * K[1, (i*n_virt + t) * n_ex + j*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u != s) and (u != t) and (w == u) and (v == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[j, n_occ + u, n_occ + s, n_occ + u] ) * K[0, j*n_virt + u] * K[1, (i*n_virt + u) * n_ex + j*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u != s) and (u != t) and (w != s) and (w != t) and (w != u) and (w != v) and (v == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-8 * g[j, n_occ + u, n_occ + s, n_occ + w] + 4 * g[j, n_occ + w, n_occ + s, n_occ + u] ) * K[0, j*n_virt + u] * K[1, (i*n_virt + w) * n_ex + j*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u != s) and (u != t) and (w == s) and (v == u)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * F[j, n_occ + t] + 4 * g[j, n_occ + u, n_occ + t, n_occ + u] + 4 * g[j, n_occ + t, n_occ + u, n_occ + u] + -4 * g[j, j, j, n_occ + t] ) * K[0, j*n_virt + u] * K[1, (i*n_virt + s) * n_ex + j*n_virt + u+ 2*n_ex]

												elif ((t != s) and (u != s) and (u != t) and (w == s) and (v != s) and (v != t) and (v != u)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[j, n_occ + u, n_occ + t, n_occ + v] + 4 * g[j, n_occ + t, n_occ + u, n_occ + v] ) * K[0, j*n_virt + u] * K[1, (i*n_virt + s) * n_ex + j*n_virt + v+ 2*n_ex]

											elif ((j != i) and (k == j) and (n == j) and (m == j)):

												if ((t == s) and (u == s) and (w == s) and (v == s)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (8 * g[i, j, j, n_occ + s] ) * K[0, j*n_virt + s] * K[1, (j*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex]

												elif ((t == s) and (u == s) and (w != s) and (w != t) and (w != u) and (w != v) and (v == s)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, j, j, n_occ + w] ) * K[0, j*n_virt + s] * K[1, (j*n_virt + w) * n_ex + j*n_virt + s+ 2*n_ex]

												elif ((t == s) and (u != s) and (u != t) and (w == s) and (v == s)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, j, j, n_occ + u] ) * K[0, j*n_virt + u] * K[1, (j*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex]

												elif ((t != s) and (u == s) and (w == s) and (v == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (8 * g[i, j, j, n_occ + s] ) * K[0, j*n_virt + s] * K[1, (j*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u == s) and (w == t) and (v == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, j, j, n_occ + t] ) * K[0, j*n_virt + s] * K[1, (j*n_virt + t) * n_ex + j*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u == s) and (w != s) and (w != t) and (w != u) and (w != v) and (v == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, j, j, n_occ + w] ) * K[0, j*n_virt + s] * K[1, (j*n_virt + w) * n_ex + j*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u == t) and (w == s) and (v == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, j, j, n_occ + t] ) * K[0, j*n_virt + t] * K[1, (j*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u != s) and (u != t) and (w == s) and (v == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, j, j, n_occ + u] ) * K[0, j*n_virt + u] * K[1, (j*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex]

											elif ((j != i) and (k == j) and (n != i) and (n != j) and (n != k) and (n != m) and (m == j)):

												if ((t == s) and (u == s) and (w == s) and (v == s)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, n, j, n_occ + s] + 4 * g[i, j, n, n_occ + s] ) * K[0, j*n_virt + s] * K[1, (n*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex]

												elif ((t == s) and (u == s) and (w != s) and (w != t) and (w != u) and (w != v) and (v == s)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (8 * g[i, j, n, n_occ + w] + -4 * g[i, n, j, n_occ + w] ) * K[0, j*n_virt + s] * K[1, (n*n_virt + w) * n_ex + j*n_virt + s+ 2*n_ex]

												elif ((t == s) and (u != s) and (u != t) and (w == s) and (v == s)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, j, n, n_occ + u] + 8 * g[i, n, j, n_occ + u] ) * K[0, j*n_virt + u] * K[1, (n*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex]

												elif ((t != s) and (u == s) and (w == s) and (v == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, n, j, n_occ + s] + 4 * g[i, j, n, n_occ + s] ) * K[0, j*n_virt + s] * K[1, (n*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u == s) and (w == t) and (v == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (8 * g[i, j, n, n_occ + t] + -4 * g[i, n, j, n_occ + t] ) * K[0, j*n_virt + s] * K[1, (n*n_virt + t) * n_ex + j*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u == s) and (w != s) and (w != t) and (w != u) and (w != v) and (v == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (8 * g[i, j, n, n_occ + w] + -4 * g[i, n, j, n_occ + w] ) * K[0, j*n_virt + s] * K[1, (n*n_virt + w) * n_ex + j*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u == t) and (w == s) and (v == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, j, n, n_occ + t] + 8 * g[i, n, j, n_occ + t] ) * K[0, j*n_virt + t] * K[1, (n*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u != s) and (u != t) and (w == s) and (v == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, j, n, n_occ + u] + 8 * g[i, n, j, n_occ + u] ) * K[0, j*n_virt + u] * K[1, (n*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex]

											elif ((j != i) and (k == j) and (n == i) and (m != i) and (m != j) and (m != k)):

												if ((t == s) and (u == s) and (w == s) and (v == s)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-8 * g[j, m, j, n_occ + s] ) * K[0, j*n_virt + s] * K[1, (i*n_virt + s) * n_ex + m*n_virt + s+ 2*n_ex]

												elif ((t == s) and (u != s) and (u != t) and (w == s) and (v == s)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[j, m, j, n_occ + u] ) * K[0, j*n_virt + u] * K[1, (i*n_virt + s) * n_ex + m*n_virt + s+ 2*n_ex]

												elif ((t == s) and (u != s) and (u != t) and (w == s) and (v == u)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[j, m, j, n_occ + s] ) * K[0, j*n_virt + u] * K[1, (i*n_virt + s) * n_ex + m*n_virt + u+ 2*n_ex]

												elif ((t != s) and (u == s) and (w == s) and (v == s)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[j, m, j, n_occ + t] ) * K[0, j*n_virt + s] * K[1, (i*n_virt + s) * n_ex + m*n_virt + s+ 2*n_ex]

												elif ((t != s) and (u == s) and (w == s) and (v == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[j, m, j, n_occ + s] ) * K[0, j*n_virt + s] * K[1, (i*n_virt + s) * n_ex + m*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u == t) and (w == s) and (v == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-8 * g[j, m, j, n_occ + t] ) * K[0, j*n_virt + t] * K[1, (i*n_virt + s) * n_ex + m*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u != s) and (u != t) and (w == s) and (v == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[j, m, j, n_occ + u] ) * K[0, j*n_virt + u] * K[1, (i*n_virt + s) * n_ex + m*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u != s) and (u != t) and (w == s) and (v == u)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[j, m, j, n_occ + t] ) * K[0, j*n_virt + u] * K[1, (i*n_virt + s) * n_ex + m*n_virt + u+ 2*n_ex]

											elif ((j != i) and (k != i) and (k != j) and (n == i) and (m == i)):

												if ((t == s) and (u == s) and (w == s) and (v == s)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, j, k, n_occ + s] + -4 * g[i, k, j, n_occ + s] ) * K[0, k*n_virt + s] * K[1, (i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex]

												elif ((t == s) and (u != s) and (u != t) and (w == s) and (v == s)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-8 * g[i, j, k, n_occ + u] + 4 * g[i, k, j, n_occ + u] ) * K[0, k*n_virt + u] * K[1, (i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex]

												elif ((t == s) and (u != s) and (u != t) and (w == s) and (v == u)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, j, k, n_occ + s] + -8 * g[i, k, j, n_occ + s] ) * K[0, k*n_virt + u] * K[1, (i*n_virt + s) * n_ex + i*n_virt + u+ 2*n_ex]

												elif ((t != s) and (u == s) and (w == s) and (v == s)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, j, k, n_occ + t] + -8 * g[i, k, j, n_occ + t] ) * K[0, k*n_virt + s] * K[1, (i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex]

												elif ((t != s) and (u == s) and (w == s) and (v == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-8 * g[i, j, k, n_occ + s] + 4 * g[i, k, j, n_occ + s] ) * K[0, k*n_virt + s] * K[1, (i*n_virt + s) * n_ex + i*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u == t) and (w == s) and (v == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, j, k, n_occ + t] + -4 * g[i, k, j, n_occ + t] ) * K[0, k*n_virt + t] * K[1, (i*n_virt + s) * n_ex + i*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u != s) and (u != t) and (w == s) and (v == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-8 * g[i, j, k, n_occ + u] + 4 * g[i, k, j, n_occ + u] ) * K[0, k*n_virt + u] * K[1, (i*n_virt + s) * n_ex + i*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u != s) and (u != t) and (w == s) and (v == u)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, j, k, n_occ + t] + -8 * g[i, k, j, n_occ + t] ) * K[0, k*n_virt + u] * K[1, (i*n_virt + s) * n_ex + i*n_virt + u+ 2*n_ex]

											elif ((j != i) and (k != i) and (k != j) and (n == i) and (m == j)):

												if ((t == s) and (u == s) and (w == s) and (v == s)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[j, k, j, n_occ + s] + 4 * g[i, i, k, n_occ + s] + 4 * g[i, k, i, n_occ + s] + -4 * g[j, j, k, n_occ + s] ) * K[0, k*n_virt + s] * K[1, (i*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex]

												elif ((t == s) and (u == s) and (w != s) and (w != t) and (w != u) and (w != v) and (v == s)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * F[k, n_occ + w] + -8 * g[k, n_occ + s, n_occ + s, n_occ + w] + 4 * g[k, n_occ + w, n_occ + s, n_occ + s] + -4 * g[i, i, k, n_occ + w] + 8 * g[i, k, i, n_occ + w] ) * K[0, k*n_virt + s] * K[1, (i*n_virt + w) * n_ex + j*n_virt + s+ 2*n_ex]

												elif ((t == s) and (u == s) and (w == s) and (v != s) and (v != t) and (v != u)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[k, n_occ + s, n_occ + s, n_occ + v] ) * K[0, k*n_virt + s] * K[1, (i*n_virt + s) * n_ex + j*n_virt + v+ 2*n_ex]

												elif ((t == s) and (u != s) and (u != t) and (w == s) and (v == s)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, k, i, n_occ + u] + 8 * g[i, i, k, n_occ + u] + 4 * g[j, k, j, n_occ + u] + -8 * g[j, j, k, n_occ + u] ) * K[0, k*n_virt + u] * K[1, (i*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex]

												elif ((t == s) and (u != s) and (u != t) and (w == u) and (v == s)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[k, n_occ + u, n_occ + s, n_occ + u] ) * K[0, k*n_virt + u] * K[1, (i*n_virt + u) * n_ex + j*n_virt + s+ 2*n_ex]

												elif ((t == s) and (u != s) and (u != t) and (w != s) and (w != t) and (w != u) and (w != v) and (v == s)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-8 * g[k, n_occ + u, n_occ + s, n_occ + w] + 4 * g[k, n_occ + w, n_occ + s, n_occ + u] ) * K[0, k*n_virt + u] * K[1, (i*n_virt + w) * n_ex + j*n_virt + s+ 2*n_ex]

												elif ((t == s) and (u != s) and (u != t) and (w == s) and (v == u)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * F[k, n_occ + s] + 8 * g[k, n_occ + u, n_occ + s, n_occ + u] + -4 * g[k, n_occ + s, n_occ + u, n_occ + u] + 4 * g[j, j, k, n_occ + s] + -8 * g[j, k, j, n_occ + s] ) * K[0, k*n_virt + u] * K[1, (i*n_virt + s) * n_ex + j*n_virt + u+ 2*n_ex]

												elif ((t == s) and (u != s) and (u != t) and (w == s) and (v != s) and (v != t) and (v != u)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[k, n_occ + s, n_occ + u, n_occ + v] + 8 * g[k, n_occ + u, n_occ + s, n_occ + v] ) * K[0, k*n_virt + u] * K[1, (i*n_virt + s) * n_ex + j*n_virt + v+ 2*n_ex]

												elif ((t != s) and (u == s) and (w == s) and (v == s)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * F[k, n_occ + t] + 8 * g[k, n_occ + s, n_occ + s, n_occ + t] + -4 * g[k, n_occ + t, n_occ + s, n_occ + s] + 4 * g[j, j, k, n_occ + t] + -8 * g[j, k, j, n_occ + t] ) * K[0, k*n_virt + s] * K[1, (i*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex]

												elif ((t != s) and (u == s) and (w == s) and (v == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * F[k, n_occ + s] + -4 * g[k, n_occ + t, n_occ + s, n_occ + t] + 8 * g[k, n_occ + s, n_occ + t, n_occ + t] + 4 * g[i, i, k, n_occ + s] + -4 * g[k, n_occ + s, n_occ + s, n_occ + s] + 4 * g[i, k, i, n_occ + s] + -8 * g[j, j, k, n_occ + s] + 4 * g[j, k, j, n_occ + s] ) * K[0, k*n_virt + s] * K[1, (i*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u == s) and (w == t) and (v == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * F[k, n_occ + t] + -8 * g[k, n_occ + s, n_occ + s, n_occ + t] + 4 * g[k, n_occ + t, n_occ + s, n_occ + s] + -4 * g[i, i, k, n_occ + t] + 8 * g[i, k, i, n_occ + t] ) * K[0, k*n_virt + s] * K[1, (i*n_virt + t) * n_ex + j*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u == s) and (w != s) and (w != t) and (w != u) and (w != v) and (v == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * F[k, n_occ + w] + -8 * g[k, n_occ + s, n_occ + s, n_occ + w] + 4 * g[k, n_occ + w, n_occ + s, n_occ + s] + -4 * g[i, i, k, n_occ + w] + 8 * g[i, k, i, n_occ + w] ) * K[0, k*n_virt + s] * K[1, (i*n_virt + w) * n_ex + j*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u == s) and (w == s) and (v != s) and (v != t) and (v != u)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (8 * g[k, n_occ + s, n_occ + t, n_occ + v] + -4 * g[k, n_occ + t, n_occ + s, n_occ + v] ) * K[0, k*n_virt + s] * K[1, (i*n_virt + s) * n_ex + j*n_virt + v+ 2*n_ex]

												elif ((t != s) and (u == t) and (w == s) and (v == s)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[k, n_occ + t, n_occ + s, n_occ + t] ) * K[0, k*n_virt + t] * K[1, (i*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex]

												elif ((t != s) and (u == t) and (w == s) and (v == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * F[k, n_occ + t] + 4 * g[k, n_occ + t, n_occ + t, n_occ + t] + 4 * g[k, n_occ + s, n_occ + s, n_occ + t] + -8 * g[k, n_occ + t, n_occ + s, n_occ + s] + -4 * g[j, j, k, n_occ + t] + 8 * g[i, i, k, n_occ + t] + -4 * g[i, k, i, n_occ + t] + -4 * g[j, k, j, n_occ + t] ) * K[0, k*n_virt + t] * K[1, (i*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u == t) and (w == t) and (v == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[k, n_occ + t, n_occ + s, n_occ + t] ) * K[0, k*n_virt + t] * K[1, (i*n_virt + t) * n_ex + j*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u == t) and (w != s) and (w != t) and (w != u) and (w != v) and (v == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-8 * g[k, n_occ + t, n_occ + s, n_occ + w] + 4 * g[k, n_occ + w, n_occ + s, n_occ + t] ) * K[0, k*n_virt + t] * K[1, (i*n_virt + w) * n_ex + j*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u == t) and (w == s) and (v != s) and (v != t) and (v != u)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[k, n_occ + t, n_occ + t, n_occ + v] ) * K[0, k*n_virt + t] * K[1, (i*n_virt + s) * n_ex + j*n_virt + v+ 2*n_ex]

												elif ((t != s) and (u != s) and (u != t) and (w == s) and (v == s)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[k, n_occ + t, n_occ + s, n_occ + u] + 8 * g[k, n_occ + u, n_occ + s, n_occ + t] ) * K[0, k*n_virt + u] * K[1, (i*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex]

												elif ((t != s) and (u != s) and (u != t) and (w == s) and (v == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[k, n_occ + t, n_occ + t, n_occ + u] + 8 * g[k, n_occ + u, n_occ + t, n_occ + t] + -4 * g[i, k, i, n_occ + u] + 8 * g[i, i, k, n_occ + u] + 4 * g[k, n_occ + s, n_occ + s, n_occ + u] + -8 * g[k, n_occ + u, n_occ + s, n_occ + s] + 4 * g[j, k, j, n_occ + u] + -8 * g[j, j, k, n_occ + u] ) * K[0, k*n_virt + u] * K[1, (i*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u != s) and (u != t) and (w == t) and (v == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[k, n_occ + t, n_occ + s, n_occ + u] + -8 * g[k, n_occ + u, n_occ + s, n_occ + t] ) * K[0, k*n_virt + u] * K[1, (i*n_virt + t) * n_ex + j*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u != s) and (u != t) and (w == u) and (v == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[k, n_occ + u, n_occ + s, n_occ + u] ) * K[0, k*n_virt + u] * K[1, (i*n_virt + u) * n_ex + j*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u != s) and (u != t) and (w != s) and (w != t) and (w != u) and (w != v) and (v == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-8 * g[k, n_occ + u, n_occ + s, n_occ + w] + 4 * g[k, n_occ + w, n_occ + s, n_occ + u] ) * K[0, k*n_virt + u] * K[1, (i*n_virt + w) * n_ex + j*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u != s) and (u != t) and (w == s) and (v == u)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * F[k, n_occ + t] + 8 * g[k, n_occ + u, n_occ + t, n_occ + u] + -4 * g[k, n_occ + t, n_occ + u, n_occ + u] + 4 * g[j, j, k, n_occ + t] + -8 * g[j, k, j, n_occ + t] ) * K[0, k*n_virt + u] * K[1, (i*n_virt + s) * n_ex + j*n_virt + u+ 2*n_ex]

												elif ((t != s) and (u != s) and (u != t) and (w == s) and (v != s) and (v != t) and (v != u)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[k, n_occ + t, n_occ + u, n_occ + v] + 8 * g[k, n_occ + u, n_occ + t, n_occ + v] ) * K[0, k*n_virt + u] * K[1, (i*n_virt + s) * n_ex + j*n_virt + v+ 2*n_ex]

											elif ((j != i) and (k != i) and (k != j) and (n == j) and (m == j)):

												if ((t == s) and (u == s) and (w == s) and (v == s)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, j, k, n_occ + s] + 4 * g[i, k, j, n_occ + s] ) * K[0, k*n_virt + s] * K[1, (j*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex]

												elif ((t == s) and (u == s) and (w != s) and (w != t) and (w != u) and (w != v) and (v == s)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, j, k, n_occ + w] + 8 * g[i, k, j, n_occ + w] ) * K[0, k*n_virt + s] * K[1, (j*n_virt + w) * n_ex + j*n_virt + s+ 2*n_ex]

												elif ((t == s) and (u != s) and (u != t) and (w == s) and (v == s)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (8 * g[i, j, k, n_occ + u] + -4 * g[i, k, j, n_occ + u] ) * K[0, k*n_virt + u] * K[1, (j*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex]

												elif ((t != s) and (u == s) and (w == s) and (v == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, j, k, n_occ + s] + 4 * g[i, k, j, n_occ + s] ) * K[0, k*n_virt + s] * K[1, (j*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u == s) and (w == t) and (v == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, j, k, n_occ + t] + 8 * g[i, k, j, n_occ + t] ) * K[0, k*n_virt + s] * K[1, (j*n_virt + t) * n_ex + j*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u == s) and (w != s) and (w != t) and (w != u) and (w != v) and (v == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, j, k, n_occ + w] + 8 * g[i, k, j, n_occ + w] ) * K[0, k*n_virt + s] * K[1, (j*n_virt + w) * n_ex + j*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u == t) and (w == s) and (v == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (8 * g[i, j, k, n_occ + t] + -4 * g[i, k, j, n_occ + t] ) * K[0, k*n_virt + t] * K[1, (j*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u != s) and (u != t) and (w == s) and (v == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (8 * g[i, j, k, n_occ + u] + -4 * g[i, k, j, n_occ + u] ) * K[0, k*n_virt + u] * K[1, (j*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex]

											elif ((j != i) and (k != i) and (k != j) and (n == k) and (m == j)):

												if ((t == s) and (u == s) and (w == s) and (v == s)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (8 * g[i, k, k, n_occ + s] ) * K[0, k*n_virt + s] * K[1, (k*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex]

												elif ((t == s) and (u == s) and (w != s) and (w != t) and (w != u) and (w != v) and (v == s)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, k, k, n_occ + w] ) * K[0, k*n_virt + s] * K[1, (k*n_virt + w) * n_ex + j*n_virt + s+ 2*n_ex]

												elif ((t == s) and (u != s) and (u != t) and (w == s) and (v == s)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, k, k, n_occ + u] ) * K[0, k*n_virt + u] * K[1, (k*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex]

												elif ((t != s) and (u == s) and (w == s) and (v == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (8 * g[i, k, k, n_occ + s] ) * K[0, k*n_virt + s] * K[1, (k*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u == s) and (w == t) and (v == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, k, k, n_occ + t] ) * K[0, k*n_virt + s] * K[1, (k*n_virt + t) * n_ex + j*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u == s) and (w != s) and (w != t) and (w != u) and (w != v) and (v == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, k, k, n_occ + w] ) * K[0, k*n_virt + s] * K[1, (k*n_virt + w) * n_ex + j*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u == t) and (w == s) and (v == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, k, k, n_occ + t] ) * K[0, k*n_virt + t] * K[1, (k*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u != s) and (u != t) and (w == s) and (v == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, k, k, n_occ + u] ) * K[0, k*n_virt + u] * K[1, (k*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex]

											elif ((j != i) and (k != i) and (k != j) and (n != i) and (n != j) and (n != k) and (n != m) and (m == j)):

												if ((t == s) and (u == s) and (w == s) and (v == s)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, n, k, n_occ + s] + 4 * g[i, k, n, n_occ + s] ) * K[0, k*n_virt + s] * K[1, (n*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex]

												elif ((t == s) and (u == s) and (w != s) and (w != t) and (w != u) and (w != v) and (v == s)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (8 * g[i, k, n, n_occ + w] + -4 * g[i, n, k, n_occ + w] ) * K[0, k*n_virt + s] * K[1, (n*n_virt + w) * n_ex + j*n_virt + s+ 2*n_ex]

												elif ((t == s) and (u != s) and (u != t) and (w == s) and (v == s)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, k, n, n_occ + u] + 8 * g[i, n, k, n_occ + u] ) * K[0, k*n_virt + u] * K[1, (n*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex]

												elif ((t != s) and (u == s) and (w == s) and (v == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, n, k, n_occ + s] + 4 * g[i, k, n, n_occ + s] ) * K[0, k*n_virt + s] * K[1, (n*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u == s) and (w == t) and (v == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (8 * g[i, k, n, n_occ + t] + -4 * g[i, n, k, n_occ + t] ) * K[0, k*n_virt + s] * K[1, (n*n_virt + t) * n_ex + j*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u == s) and (w != s) and (w != t) and (w != u) and (w != v) and (v == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (8 * g[i, k, n, n_occ + w] + -4 * g[i, n, k, n_occ + w] ) * K[0, k*n_virt + s] * K[1, (n*n_virt + w) * n_ex + j*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u == t) and (w == s) and (v == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, k, n, n_occ + t] + 8 * g[i, n, k, n_occ + t] ) * K[0, k*n_virt + t] * K[1, (n*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u != s) and (u != t) and (w == s) and (v == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, k, n, n_occ + u] + 8 * g[i, n, k, n_occ + u] ) * K[0, k*n_virt + u] * K[1, (n*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex]

											elif ((j != i) and (k != i) and (k != j) and (n == i) and (m == k)):

												if ((t == s) and (u == s) and (w == s) and (v == s)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * F[j, n_occ + s] + 4 * g[j, n_occ + s, n_occ + s, n_occ + s] + -4 * g[j, n_occ + s, k, k] + -4 * g[j, k, k, n_occ + s] ) * K[0, k*n_virt + s] * K[1, (i*n_virt + s) * n_ex + k*n_virt + s+ 2*n_ex]

												elif ((t == s) and (u == s) and (w == s) and (v != s) and (v != t) and (v != u)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[j, n_occ + s, n_occ + s, n_occ + v] ) * K[0, k*n_virt + s] * K[1, (i*n_virt + s) * n_ex + k*n_virt + v+ 2*n_ex]

												elif ((t == s) and (u != s) and (u != t) and (w == s) and (v == s)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * F[j, n_occ + u] + 8 * g[j, n_occ + s, n_occ + s, n_occ + u] + -4 * g[j, n_occ + u, n_occ + s, n_occ + s] + 4 * g[j, n_occ + u, k, k] + -8 * g[j, k, k, n_occ + u] ) * K[0, k*n_virt + u] * K[1, (i*n_virt + s) * n_ex + k*n_virt + s+ 2*n_ex]

												elif ((t == s) and (u != s) and (u != t) and (w == s) and (v == u)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[j, n_occ + u, n_occ + s, n_occ + u] + 8 * g[j, n_occ + s, n_occ + u, n_occ + u] + 4 * g[j, k, k, n_occ + s] + -8 * g[j, n_occ + s, k, k] ) * K[0, k*n_virt + u] * K[1, (i*n_virt + s) * n_ex + k*n_virt + u+ 2*n_ex]

												elif ((t == s) and (u != s) and (u != t) and (w == s) and (v != s) and (v != t) and (v != u)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (8 * g[j, n_occ + s, n_occ + u, n_occ + v] + -4 * g[j, n_occ + u, n_occ + s, n_occ + v] ) * K[0, k*n_virt + u] * K[1, (i*n_virt + s) * n_ex + k*n_virt + v+ 2*n_ex]

												elif ((t != s) and (u == s) and (w == s) and (v == s)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[j, n_occ + s, n_occ + s, n_occ + t] + 8 * g[j, n_occ + t, n_occ + s, n_occ + s] + 4 * g[j, k, k, n_occ + t] + -8 * g[j, n_occ + t, k, k] ) * K[0, k*n_virt + s] * K[1, (i*n_virt + s) * n_ex + k*n_virt + s+ 2*n_ex]

												elif ((t != s) and (u == s) and (w == s) and (v == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * F[j, n_occ + s] + 8 * g[j, n_occ + t, n_occ + s, n_occ + t] + -4 * g[j, n_occ + s, n_occ + t, n_occ + t] + 4 * g[j, n_occ + s, k, k] + -8 * g[j, k, k, n_occ + s] ) * K[0, k*n_virt + s] * K[1, (i*n_virt + s) * n_ex + k*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u == s) and (w == s) and (v != s) and (v != t) and (v != u)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[j, n_occ + s, n_occ + t, n_occ + v] + 8 * g[j, n_occ + t, n_occ + s, n_occ + v] ) * K[0, k*n_virt + s] * K[1, (i*n_virt + s) * n_ex + k*n_virt + v+ 2*n_ex]

												elif ((t != s) and (u == t) and (w == s) and (v == s)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[j, n_occ + t, n_occ + s, n_occ + t] ) * K[0, k*n_virt + t] * K[1, (i*n_virt + s) * n_ex + k*n_virt + s+ 2*n_ex]

												elif ((t != s) and (u == t) and (w == s) and (v == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * F[j, n_occ + t] + 4 * g[j, n_occ + t, n_occ + t, n_occ + t] + -4 * g[j, n_occ + t, k, k] + -4 * g[j, k, k, n_occ + t] ) * K[0, k*n_virt + t] * K[1, (i*n_virt + s) * n_ex + k*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u == t) and (w == s) and (v != s) and (v != t) and (v != u)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[j, n_occ + t, n_occ + t, n_occ + v] ) * K[0, k*n_virt + t] * K[1, (i*n_virt + s) * n_ex + k*n_virt + v+ 2*n_ex]

												elif ((t != s) and (u != s) and (u != t) and (w == s) and (v == s)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (8 * g[j, n_occ + t, n_occ + s, n_occ + u] + -4 * g[j, n_occ + u, n_occ + s, n_occ + t] ) * K[0, k*n_virt + u] * K[1, (i*n_virt + s) * n_ex + k*n_virt + s+ 2*n_ex]

												elif ((t != s) and (u != s) and (u != t) and (w == s) and (v == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * F[j, n_occ + u] + 8 * g[j, n_occ + t, n_occ + t, n_occ + u] + -4 * g[j, n_occ + u, n_occ + t, n_occ + t] + 4 * g[j, n_occ + u, k, k] + -8 * g[j, k, k, n_occ + u] ) * K[0, k*n_virt + u] * K[1, (i*n_virt + s) * n_ex + k*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u != s) and (u != t) and (w == s) and (v == u)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[j, n_occ + u, n_occ + t, n_occ + u] + 8 * g[j, n_occ + t, n_occ + u, n_occ + u] + 4 * g[j, k, k, n_occ + t] + -8 * g[j, n_occ + t, k, k] ) * K[0, k*n_virt + u] * K[1, (i*n_virt + s) * n_ex + k*n_virt + u+ 2*n_ex]

												elif ((t != s) and (u != s) and (u != t) and (w == s) and (v != s) and (v != t) and (v != u)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (8 * g[j, n_occ + t, n_occ + u, n_occ + v] + -4 * g[j, n_occ + u, n_occ + t, n_occ + v] ) * K[0, k*n_virt + u] * K[1, (i*n_virt + s) * n_ex + k*n_virt + v+ 2*n_ex]

											elif ((j != i) and (k != i) and (k != j) and (n == i) and (m != i) and (m != j) and (m != k)):

												if ((t == s) and (u == s) and (w == s) and (v == s)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[j, m, k, n_occ + s] + -4 * g[j, n_occ + s, k, m] ) * K[0, k*n_virt + s] * K[1, (i*n_virt + s) * n_ex + m*n_virt + s+ 2*n_ex]

												elif ((t == s) and (u != s) and (u != t) and (w == s) and (v == s)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-8 * g[j, m, k, n_occ + u] + 4 * g[j, n_occ + u, k, m] ) * K[0, k*n_virt + u] * K[1, (i*n_virt + s) * n_ex + m*n_virt + s+ 2*n_ex]

												elif ((t == s) and (u != s) and (u != t) and (w == s) and (v == u)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[j, m, k, n_occ + s] + -8 * g[j, n_occ + s, k, m] ) * K[0, k*n_virt + u] * K[1, (i*n_virt + s) * n_ex + m*n_virt + u+ 2*n_ex]

												elif ((t != s) and (u == s) and (w == s) and (v == s)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[j, m, k, n_occ + t] + -8 * g[j, n_occ + t, k, m] ) * K[0, k*n_virt + s] * K[1, (i*n_virt + s) * n_ex + m*n_virt + s+ 2*n_ex]

												elif ((t != s) and (u == s) and (w == s) and (v == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-8 * g[j, m, k, n_occ + s] + 4 * g[j, n_occ + s, k, m] ) * K[0, k*n_virt + s] * K[1, (i*n_virt + s) * n_ex + m*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u == t) and (w == s) and (v == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[j, m, k, n_occ + t] + -4 * g[j, n_occ + t, k, m] ) * K[0, k*n_virt + t] * K[1, (i*n_virt + s) * n_ex + m*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u != s) and (u != t) and (w == s) and (v == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-8 * g[j, m, k, n_occ + u] + 4 * g[j, n_occ + u, k, m] ) * K[0, k*n_virt + u] * K[1, (i*n_virt + s) * n_ex + m*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u != s) and (u != t) and (w == s) and (v == u)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[j, m, k, n_occ + t] + -8 * g[j, n_occ + t, k, m] ) * K[0, k*n_virt + u] * K[1, (i*n_virt + s) * n_ex + m*n_virt + u+ 2*n_ex]

	# This operator combination: {'a': 3, 'b': 2, 'c': 1}
	for i in range(n_occ):
		for j in range(n_occ):
			for m in range(n_occ):
				for k in range(n_occ):
					for s in range(n_virt):
						for t in range(n_virt):
							for v in range(n_virt):
								for u in range(n_virt):

									if ((j == i) and (m == i) and (k == i)):

										if ((t == s) and (v == s) and (u == s)):

											L3[i*n_virt + s] += (-4 * F[n_occ + s, n_occ + s] + 4 * F[i, i] + 4 * g[i, i, n_occ + s, n_occ + s] + -8 * g[i, n_occ + s, i, n_occ + s] ) * K[0, i*n_virt + s + n_ex] * K[1, (i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex]

										elif ((t == s) and (v != s) and (v != t) and (v != u) and (u == s)):

											L3[i*n_virt + s] += (-4 * F[n_occ + s, n_occ + v] + 4 * g[i, i, n_occ + s, n_occ + v] + -8 * g[i, n_occ + s, i, n_occ + v] ) * K[0, i*n_virt + s + n_ex] * K[1, (i*n_virt + v) * n_ex + i*n_virt + s+ 2*n_ex]

										elif ((t != s) and (v == s) and (u == s)):

											L3[i*n_virt + s] += (-4 * F[n_occ + s, n_occ + t] + 4 * g[i, i, n_occ + s, n_occ + t] + -8 * g[i, n_occ + s, i, n_occ + t] ) * K[0, i*n_virt + t + n_ex] * K[1, (i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex]

										elif ((t != s) and (v == t) and (u == s)):

											L3[i*n_virt + s] += (4 * F[i, i] + -4 * F[n_occ + t, n_occ + t] + 4 * g[i, i, n_occ + t, n_occ + t] + -8 * g[i, n_occ + t, i, n_occ + t] ) * K[0, i*n_virt + t + n_ex] * K[1, (i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex]

										elif ((t != s) and (v != s) and (v != t) and (v != u) and (u == s)):

											L3[i*n_virt + s] += (-4 * F[n_occ + t, n_occ + v] + 4 * g[i, i, n_occ + t, n_occ + v] + -8 * g[i, n_occ + t, i, n_occ + v] ) * K[0, i*n_virt + t + n_ex] * K[1, (i*n_virt + v) * n_ex + i*n_virt + s+ 2*n_ex]

									elif ((j == i) and (m != i) and (m != j) and (m != k) and (k == i)):

										if ((t == s) and (v == s) and (u == s)):

											L3[i*n_virt + s] += (4 * F[i, m] + -8 * g[i, n_occ + s, m, n_occ + s] + 4 * g[i, m, n_occ + s, n_occ + s] ) * K[0, i*n_virt + s + n_ex] * K[1, (m*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex]

										elif ((t == s) and (v != s) and (v != t) and (v != u) and (u == s)):

											L3[i*n_virt + s] += (4 * g[i, m, n_occ + s, n_occ + v] + -8 * g[i, n_occ + s, m, n_occ + v] ) * K[0, i*n_virt + s + n_ex] * K[1, (m*n_virt + v) * n_ex + i*n_virt + s+ 2*n_ex]

										elif ((t != s) and (v == s) and (u == s)):

											L3[i*n_virt + s] += (4 * g[i, m, n_occ + s, n_occ + t] + -8 * g[i, n_occ + t, m, n_occ + s] ) * K[0, i*n_virt + t + n_ex] * K[1, (m*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex]

										elif ((t != s) and (v == t) and (u == s)):

											L3[i*n_virt + s] += (4 * F[i, m] + -8 * g[i, n_occ + t, m, n_occ + t] + 4 * g[i, m, n_occ + t, n_occ + t] ) * K[0, i*n_virt + t + n_ex] * K[1, (m*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex]

										elif ((t != s) and (v != s) and (v != t) and (v != u) and (u == s)):

											L3[i*n_virt + s] += (4 * g[i, m, n_occ + t, n_occ + v] + -8 * g[i, n_occ + t, m, n_occ + v] ) * K[0, i*n_virt + t + n_ex] * K[1, (m*n_virt + v) * n_ex + i*n_virt + s+ 2*n_ex]

									elif ((j != i) and (m == i) and (k == i)):

										if ((t == s) and (v == s) and (u == s)):

											L3[i*n_virt + s] += (4 * F[i, j] + -8 * g[i, n_occ + s, j, n_occ + s] + 4 * g[i, j, n_occ + s, n_occ + s] ) * K[0, j*n_virt + s + n_ex] * K[1, (i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex]

										elif ((t == s) and (v != s) and (v != t) and (v != u) and (u == s)):

											L3[i*n_virt + s] += (4 * g[i, j, n_occ + s, n_occ + v] + -8 * g[i, n_occ + v, j, n_occ + s] ) * K[0, j*n_virt + s + n_ex] * K[1, (i*n_virt + v) * n_ex + i*n_virt + s+ 2*n_ex]

										elif ((t != s) and (v == s) and (u == s)):

											L3[i*n_virt + s] += (4 * g[i, j, n_occ + s, n_occ + t] + -8 * g[i, n_occ + s, j, n_occ + t] ) * K[0, j*n_virt + t + n_ex] * K[1, (i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex]

										elif ((t != s) and (v == t) and (u == s)):

											L3[i*n_virt + s] += (4 * F[i, j] + -8 * g[i, n_occ + t, j, n_occ + t] + 4 * g[i, j, n_occ + t, n_occ + t] ) * K[0, j*n_virt + t + n_ex] * K[1, (i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex]

										elif ((t != s) and (v != s) and (v != t) and (v != u) and (u == s)):

											L3[i*n_virt + s] += (4 * g[i, j, n_occ + t, n_occ + v] + -8 * g[i, n_occ + v, j, n_occ + t] ) * K[0, j*n_virt + t + n_ex] * K[1, (i*n_virt + v) * n_ex + i*n_virt + s+ 2*n_ex]

									elif ((j != i) and (m == j) and (k == i)):

										if ((t == s) and (v == s) and (u == s)):

											L3[i*n_virt + s] += (-4 * F[n_occ + s, n_occ + s] + 4 * F[j, j] + -8 * g[j, n_occ + s, j, n_occ + s] + 4 * g[j, j, n_occ + s, n_occ + s] ) * K[0, j*n_virt + s + n_ex] * K[1, (j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex]

										elif ((t == s) and (v != s) and (v != t) and (v != u) and (u == s)):

											L3[i*n_virt + s] += (-4 * F[n_occ + s, n_occ + v] + 4 * g[j, j, n_occ + s, n_occ + v] + -8 * g[j, n_occ + s, j, n_occ + v] ) * K[0, j*n_virt + s + n_ex] * K[1, (j*n_virt + v) * n_ex + i*n_virt + s+ 2*n_ex]

										elif ((t != s) and (v == s) and (u == s)):

											L3[i*n_virt + s] += (-4 * F[n_occ + s, n_occ + t] + 4 * g[j, j, n_occ + s, n_occ + t] + -8 * g[j, n_occ + s, j, n_occ + t] ) * K[0, j*n_virt + t + n_ex] * K[1, (j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex]

										elif ((t != s) and (v == t) and (u == s)):

											L3[i*n_virt + s] += (4 * F[j, j] + -4 * F[n_occ + t, n_occ + t] + 4 * g[j, j, n_occ + t, n_occ + t] + -8 * g[j, n_occ + t, j, n_occ + t] ) * K[0, j*n_virt + t + n_ex] * K[1, (j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex]

										elif ((t != s) and (v != s) and (v != t) and (v != u) and (u == s)):

											L3[i*n_virt + s] += (-4 * F[n_occ + t, n_occ + v] + 4 * g[j, j, n_occ + t, n_occ + v] + -8 * g[j, n_occ + t, j, n_occ + v] ) * K[0, j*n_virt + t + n_ex] * K[1, (j*n_virt + v) * n_ex + i*n_virt + s+ 2*n_ex]

									elif ((j != i) and (m != i) and (m != j) and (m != k) and (k == i)):

										if ((t == s) and (v == s) and (u == s)):

											L3[i*n_virt + s] += (4 * F[j, m] + -8 * g[j, n_occ + s, m, n_occ + s] + 4 * g[j, m, n_occ + s, n_occ + s] ) * K[0, j*n_virt + s + n_ex] * K[1, (m*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex]

										elif ((t == s) and (v != s) and (v != t) and (v != u) and (u == s)):

											L3[i*n_virt + s] += (4 * g[j, m, n_occ + s, n_occ + v] + -8 * g[j, n_occ + s, m, n_occ + v] ) * K[0, j*n_virt + s + n_ex] * K[1, (m*n_virt + v) * n_ex + i*n_virt + s+ 2*n_ex]

										elif ((t != s) and (v == s) and (u == s)):

											L3[i*n_virt + s] += (4 * g[j, m, n_occ + s, n_occ + t] + -8 * g[j, n_occ + t, m, n_occ + s] ) * K[0, j*n_virt + t + n_ex] * K[1, (m*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex]

										elif ((t != s) and (v == t) and (u == s)):

											L3[i*n_virt + s] += (4 * F[j, m] + -8 * g[j, n_occ + t, m, n_occ + t] + 4 * g[j, m, n_occ + t, n_occ + t] ) * K[0, j*n_virt + t + n_ex] * K[1, (m*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex]

										elif ((t != s) and (v != s) and (v != t) and (v != u) and (u == s)):

											L3[i*n_virt + s] += (4 * g[j, m, n_occ + t, n_occ + v] + -8 * g[j, n_occ + t, m, n_occ + v] ) * K[0, j*n_virt + t + n_ex] * K[1, (m*n_virt + v) * n_ex + i*n_virt + s+ 2*n_ex]

	# This operator combination: {'a': 3, 'b': 2, 'c': 2}
	for i in range(n_occ):
		for j in range(n_occ):
			for m in range(n_occ):
				for k in range(n_occ):
					for s in range(n_virt):
						for t in range(n_virt):
							for v in range(n_virt):
								for u in range(n_virt):

									if ((j == i) and (m == i) and (k == i)):

										if ((t == s) and (v == s) and (u == s)):

											L3[i*n_virt + s + n_ex] += (4 * g[i, n_occ + s, i, n_occ + s] ) * K[0, i*n_virt + s + n_ex] * K[1, (i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex]

										elif ((t == s) and (v == s) and (u != s) and (u != t)):

											L3[i*n_virt + s + n_ex] += (4 * g[i, n_occ + s, i, n_occ + u] ) * K[0, i*n_virt + s + n_ex] * K[1, (i*n_virt + s) * n_ex + i*n_virt + u+ 2*n_ex]

										elif ((t != s) and (v == s) and (u == s)):

											L3[i*n_virt + s + n_ex] += (4 * g[i, n_occ + s, i, n_occ + t] ) * K[0, i*n_virt + t + n_ex] * K[1, (i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex]

										elif ((t != s) and (v == s) and (u == t)):

											L3[i*n_virt + s + n_ex] += (4 * g[i, n_occ + t, i, n_occ + t] ) * K[0, i*n_virt + t + n_ex] * K[1, (i*n_virt + s) * n_ex + i*n_virt + t+ 2*n_ex]

										elif ((t != s) and (v == s) and (u != s) and (u != t)):

											L3[i*n_virt + s + n_ex] += (4 * g[i, n_occ + t, i, n_occ + u] ) * K[0, i*n_virt + t + n_ex] * K[1, (i*n_virt + s) * n_ex + i*n_virt + u+ 2*n_ex]

									elif ((j == i) and (m == i) and (k != i) and (k != j)):

										if ((t == s) and (v == s) and (u == s)):

											L3[i*n_virt + s + n_ex] += (4 * g[i, n_occ + s, k, n_occ + s] ) * K[0, i*n_virt + s + n_ex] * K[1, (i*n_virt + s) * n_ex + k*n_virt + s+ 2*n_ex]

										elif ((t == s) and (v == s) and (u != s) and (u != t)):

											L3[i*n_virt + s + n_ex] += (8 * g[i, n_occ + s, k, n_occ + u] + -4 * g[i, n_occ + u, k, n_occ + s] ) * K[0, i*n_virt + s + n_ex] * K[1, (i*n_virt + s) * n_ex + k*n_virt + u+ 2*n_ex]

										elif ((t != s) and (v == s) and (u == s)):

											L3[i*n_virt + s + n_ex] += (-4 * g[i, n_occ + s, k, n_occ + t] + 8 * g[i, n_occ + t, k, n_occ + s] ) * K[0, i*n_virt + t + n_ex] * K[1, (i*n_virt + s) * n_ex + k*n_virt + s+ 2*n_ex]

										elif ((t != s) and (v == s) and (u == t)):

											L3[i*n_virt + s + n_ex] += (4 * g[i, n_occ + t, k, n_occ + t] ) * K[0, i*n_virt + t + n_ex] * K[1, (i*n_virt + s) * n_ex + k*n_virt + t+ 2*n_ex]

										elif ((t != s) and (v == s) and (u != s) and (u != t)):

											L3[i*n_virt + s + n_ex] += (8 * g[i, n_occ + t, k, n_occ + u] + -4 * g[i, n_occ + u, k, n_occ + t] ) * K[0, i*n_virt + t + n_ex] * K[1, (i*n_virt + s) * n_ex + k*n_virt + u+ 2*n_ex]

									elif ((j != i) and (m == i) and (k == i)):

										if ((t == s) and (v == s) and (u == s)):

											L3[i*n_virt + s + n_ex] += (4 * g[i, n_occ + s, j, n_occ + s] ) * K[0, j*n_virt + s + n_ex] * K[1, (i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex]

										elif ((t == s) and (v == s) and (u != s) and (u != t)):

											L3[i*n_virt + s + n_ex] += (-4 * g[i, n_occ + s, j, n_occ + u] + 8 * g[i, n_occ + u, j, n_occ + s] ) * K[0, j*n_virt + s + n_ex] * K[1, (i*n_virt + s) * n_ex + i*n_virt + u+ 2*n_ex]

										elif ((t != s) and (v == s) and (u == s)):

											L3[i*n_virt + s + n_ex] += (8 * g[i, n_occ + s, j, n_occ + t] + -4 * g[i, n_occ + t, j, n_occ + s] ) * K[0, j*n_virt + t + n_ex] * K[1, (i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex]

										elif ((t != s) and (v == s) and (u == t)):

											L3[i*n_virt + s + n_ex] += (4 * g[i, n_occ + t, j, n_occ + t] ) * K[0, j*n_virt + t + n_ex] * K[1, (i*n_virt + s) * n_ex + i*n_virt + t+ 2*n_ex]

										elif ((t != s) and (v == s) and (u != s) and (u != t)):

											L3[i*n_virt + s + n_ex] += (-4 * g[i, n_occ + t, j, n_occ + u] + 8 * g[i, n_occ + u, j, n_occ + t] ) * K[0, j*n_virt + t + n_ex] * K[1, (i*n_virt + s) * n_ex + i*n_virt + u+ 2*n_ex]

									elif ((j != i) and (m == i) and (k == j)):

										if ((t == s) and (v == s) and (u == s)):

											L3[i*n_virt + s + n_ex] += (4 * g[j, n_occ + s, j, n_occ + s] ) * K[0, j*n_virt + s + n_ex] * K[1, (i*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex]

										elif ((t == s) and (v == s) and (u != s) and (u != t)):

											L3[i*n_virt + s + n_ex] += (4 * g[j, n_occ + s, j, n_occ + u] ) * K[0, j*n_virt + s + n_ex] * K[1, (i*n_virt + s) * n_ex + j*n_virt + u+ 2*n_ex]

										elif ((t != s) and (v == s) and (u == s)):

											L3[i*n_virt + s + n_ex] += (4 * g[j, n_occ + s, j, n_occ + t] ) * K[0, j*n_virt + t + n_ex] * K[1, (i*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex]

										elif ((t != s) and (v == s) and (u == t)):

											L3[i*n_virt + s + n_ex] += (4 * g[j, n_occ + t, j, n_occ + t] ) * K[0, j*n_virt + t + n_ex] * K[1, (i*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex]

										elif ((t != s) and (v == s) and (u != s) and (u != t)):

											L3[i*n_virt + s + n_ex] += (4 * g[j, n_occ + t, j, n_occ + u] ) * K[0, j*n_virt + t + n_ex] * K[1, (i*n_virt + s) * n_ex + j*n_virt + u+ 2*n_ex]

									elif ((j != i) and (m == i) and (k != i) and (k != j)):

										if ((t == s) and (v == s) and (u == s)):

											L3[i*n_virt + s + n_ex] += (4 * g[j, n_occ + s, k, n_occ + s] ) * K[0, j*n_virt + s + n_ex] * K[1, (i*n_virt + s) * n_ex + k*n_virt + s+ 2*n_ex]

										elif ((t == s) and (v == s) and (u != s) and (u != t)):

											L3[i*n_virt + s + n_ex] += (8 * g[j, n_occ + s, k, n_occ + u] + -4 * g[j, n_occ + u, k, n_occ + s] ) * K[0, j*n_virt + s + n_ex] * K[1, (i*n_virt + s) * n_ex + k*n_virt + u+ 2*n_ex]

										elif ((t != s) and (v == s) and (u == s)):

											L3[i*n_virt + s + n_ex] += (-4 * g[j, n_occ + s, k, n_occ + t] + 8 * g[j, n_occ + t, k, n_occ + s] ) * K[0, j*n_virt + t + n_ex] * K[1, (i*n_virt + s) * n_ex + k*n_virt + s+ 2*n_ex]

										elif ((t != s) and (v == s) and (u == t)):

											L3[i*n_virt + s + n_ex] += (4 * g[j, n_occ + t, k, n_occ + t] ) * K[0, j*n_virt + t + n_ex] * K[1, (i*n_virt + s) * n_ex + k*n_virt + t+ 2*n_ex]

										elif ((t != s) and (v == s) and (u != s) and (u != t)):

											L3[i*n_virt + s + n_ex] += (8 * g[j, n_occ + t, k, n_occ + u] + -4 * g[j, n_occ + u, k, n_occ + t] ) * K[0, j*n_virt + t + n_ex] * K[1, (i*n_virt + s) * n_ex + k*n_virt + u+ 2*n_ex]

	# This operator combination: {'a': 3, 'b': 2, 'c': 3}
	for j in range(n_occ):
		for i in range(n_occ):
			for k in range(n_occ):
				for n in range(n_occ):
					for m in range(n_occ):
						for t in range(n_virt):
							for s in range(n_virt):
								for u in range(n_virt):
									for w in range(n_virt):
										for v in range(n_virt):

											if ((j == i) and (k == i) and (n == i) and (m == i)):

												if ((t == s) and (u == s) and (w != s) and (w != t) and (w != u) and (w != v) and (v == s)):

													L3[(i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-8 * g[i, n_occ + s, n_occ + s, n_occ + w] ) * K[0, i*n_virt + s + n_ex] * K[1, (i*n_virt + w) * n_ex + i*n_virt + s+ 2*n_ex]

												elif ((t == s) and (u == s) and (w == s) and (v != s) and (v != t) and (v != u)):

													L3[(i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * F[i, n_occ + v] + 4 * g[i, n_occ + s, n_occ + s, n_occ + v] + 4 * g[i, n_occ + v, n_occ + s, n_occ + s] + -4 * g[i, i, i, n_occ + v] ) * K[0, i*n_virt + s + n_ex] * K[1, (i*n_virt + s) * n_ex + i*n_virt + v+ 2*n_ex]

												elif ((t == s) and (u != s) and (u != t) and (w == u) and (v == s)):

													L3[(i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * F[i, n_occ + s] + -4 * g[i, n_occ + u, n_occ + s, n_occ + u] + -4 * g[i, n_occ + s, n_occ + u, n_occ + u] + 4 * g[i, i, i, n_occ + s] ) * K[0, i*n_virt + u + n_ex] * K[1, (i*n_virt + u) * n_ex + i*n_virt + s+ 2*n_ex]

												elif ((t == s) and (u != s) and (u != t) and (w != s) and (w != t) and (w != u) and (w != v) and (v == s)):

													L3[(i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, n_occ + u, n_occ + s, n_occ + w] + -4 * g[i, n_occ + s, n_occ + u, n_occ + w] ) * K[0, i*n_virt + u + n_ex] * K[1, (i*n_virt + w) * n_ex + i*n_virt + s+ 2*n_ex]

												elif ((t == s) and (u != s) and (u != t) and (w == s) and (v == u)):

													L3[(i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (8 * g[i, n_occ + u, n_occ + s, n_occ + u] ) * K[0, i*n_virt + u + n_ex] * K[1, (i*n_virt + s) * n_ex + i*n_virt + u+ 2*n_ex]

												elif ((t == s) and (u != s) and (u != t) and (w == s) and (v != s) and (v != t) and (v != u)):

													L3[(i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, n_occ + u, n_occ + s, n_occ + v] + 4 * g[i, n_occ + v, n_occ + s, n_occ + u] ) * K[0, i*n_virt + u + n_ex] * K[1, (i*n_virt + s) * n_ex + i*n_virt + v+ 2*n_ex]

												elif ((t != s) and (u == s) and (w == s) and (v == s)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (8 * g[i, n_occ + s, n_occ + s, n_occ + t] ) * K[0, i*n_virt + s + n_ex] * K[1, (i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex]

												elif ((t != s) and (u == s) and (w == s) and (v == t)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * F[i, n_occ + s] + -8 * g[i, n_occ + s, n_occ + s, n_occ + s] + 4 * g[i, n_occ + s, n_occ + t, n_occ + t] + 4 * g[i, n_occ + t, n_occ + s, n_occ + t] + 4 * g[i, i, i, n_occ + s] ) * K[0, i*n_virt + s + n_ex] * K[1, (i*n_virt + s) * n_ex + i*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u == s) and (w == t) and (v == t)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-8 * g[i, n_occ + s, n_occ + s, n_occ + t] ) * K[0, i*n_virt + s + n_ex] * K[1, (i*n_virt + t) * n_ex + i*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u == s) and (w != s) and (w != t) and (w != u) and (w != v) and (v == t)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-8 * g[i, n_occ + s, n_occ + s, n_occ + w] ) * K[0, i*n_virt + s + n_ex] * K[1, (i*n_virt + w) * n_ex + i*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u == s) and (w == s) and (v != s) and (v != t) and (v != u)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, n_occ + s, n_occ + t, n_occ + v] + 4 * g[i, n_occ + v, n_occ + s, n_occ + t] ) * K[0, i*n_virt + s + n_ex] * K[1, (i*n_virt + s) * n_ex + i*n_virt + v+ 2*n_ex]

												elif ((t != s) and (u == t) and (w == s) and (v == s)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * F[i, n_occ + s] + 4 * g[i, n_occ + t, n_occ + s, n_occ + t] + 4 * g[i, n_occ + s, n_occ + t, n_occ + t] + -4 * g[i, i, i, n_occ + s] ) * K[0, i*n_virt + t + n_ex] * K[1, (i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex]

												elif ((t != s) and (u == t) and (w == s) and (v == t)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * F[i, n_occ + t] + -4 * g[i, n_occ + t, n_occ + s, n_occ + s] + -4 * g[i, n_occ + s, n_occ + s, n_occ + t] + 8 * g[i, n_occ + t, n_occ + t, n_occ + t] + -4 * g[i, i, i, n_occ + t] ) * K[0, i*n_virt + t + n_ex] * K[1, (i*n_virt + s) * n_ex + i*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u == t) and (w == t) and (v == t)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * F[i, n_occ + s] + -4 * g[i, n_occ + t, n_occ + s, n_occ + t] + -4 * g[i, n_occ + s, n_occ + t, n_occ + t] + 4 * g[i, i, i, n_occ + s] ) * K[0, i*n_virt + t + n_ex] * K[1, (i*n_virt + t) * n_ex + i*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u == t) and (w != s) and (w != t) and (w != u) and (w != v) and (v == t)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, n_occ + t, n_occ + s, n_occ + w] + -4 * g[i, n_occ + s, n_occ + t, n_occ + w] ) * K[0, i*n_virt + t + n_ex] * K[1, (i*n_virt + w) * n_ex + i*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u == t) and (w == s) and (v != s) and (v != t) and (v != u)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * F[i, n_occ + v] + 4 * g[i, n_occ + t, n_occ + t, n_occ + v] + 4 * g[i, n_occ + v, n_occ + t, n_occ + t] + -4 * g[i, i, i, n_occ + v] ) * K[0, i*n_virt + t + n_ex] * K[1, (i*n_virt + s) * n_ex + i*n_virt + v+ 2*n_ex]

												elif ((t != s) and (u != s) and (u != t) and (w == s) and (v == s)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, n_occ + u, n_occ + s, n_occ + t] + 4 * g[i, n_occ + s, n_occ + t, n_occ + u] ) * K[0, i*n_virt + u + n_ex] * K[1, (i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex]

												elif ((t != s) and (u != s) and (u != t) and (w == s) and (v == t)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, n_occ + u, n_occ + s, n_occ + s] + -4 * g[i, n_occ + s, n_occ + s, n_occ + u] + 4 * g[i, n_occ + u, n_occ + t, n_occ + t] + 4 * g[i, n_occ + t, n_occ + t, n_occ + u] ) * K[0, i*n_virt + u + n_ex] * K[1, (i*n_virt + s) * n_ex + i*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u != s) and (u != t) and (w == t) and (v == t)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, n_occ + u, n_occ + s, n_occ + t] + -4 * g[i, n_occ + s, n_occ + t, n_occ + u] ) * K[0, i*n_virt + u + n_ex] * K[1, (i*n_virt + t) * n_ex + i*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u != s) and (u != t) and (w == u) and (v == t)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * F[i, n_occ + s] + -4 * g[i, n_occ + u, n_occ + s, n_occ + u] + -4 * g[i, n_occ + s, n_occ + u, n_occ + u] + 4 * g[i, i, i, n_occ + s] ) * K[0, i*n_virt + u + n_ex] * K[1, (i*n_virt + u) * n_ex + i*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u != s) and (u != t) and (w != s) and (w != t) and (w != u) and (w != v) and (v == t)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, n_occ + u, n_occ + s, n_occ + w] + -4 * g[i, n_occ + s, n_occ + u, n_occ + w] ) * K[0, i*n_virt + u + n_ex] * K[1, (i*n_virt + w) * n_ex + i*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u != s) and (u != t) and (w == s) and (v == u)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (8 * g[i, n_occ + u, n_occ + t, n_occ + u] ) * K[0, i*n_virt + u + n_ex] * K[1, (i*n_virt + s) * n_ex + i*n_virt + u+ 2*n_ex]

												elif ((t != s) and (u != s) and (u != t) and (w == s) and (v != s) and (v != t) and (v != u)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, n_occ + u, n_occ + t, n_occ + v] + 4 * g[i, n_occ + v, n_occ + t, n_occ + u] ) * K[0, i*n_virt + u + n_ex] * K[1, (i*n_virt + s) * n_ex + i*n_virt + v+ 2*n_ex]

											elif ((j == i) and (k == i) and (n != i) and (n != j) and (n != k) and (n != m) and (m == i)):

												if ((t == s) and (u == s) and (w == s) and (v == s)):

													L3[(i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (8 * g[i, n, i, n_occ + s] ) * K[0, i*n_virt + s + n_ex] * K[1, (n*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex]

												elif ((t == s) and (u != s) and (u != t) and (w == s) and (v == s)):

													L3[(i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, n, i, n_occ + u] ) * K[0, i*n_virt + u + n_ex] * K[1, (n*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex]

												elif ((t == s) and (u != s) and (u != t) and (w == u) and (v == s)):

													L3[(i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, n, i, n_occ + s] ) * K[0, i*n_virt + u + n_ex] * K[1, (n*n_virt + u) * n_ex + i*n_virt + s+ 2*n_ex]

												elif ((t != s) and (u == s) and (w == s) and (v == t)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (8 * g[i, n, i, n_occ + s] ) * K[0, i*n_virt + s + n_ex] * K[1, (n*n_virt + s) * n_ex + i*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u == t) and (w == s) and (v == t)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, n, i, n_occ + t] ) * K[0, i*n_virt + t + n_ex] * K[1, (n*n_virt + s) * n_ex + i*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u == t) and (w == t) and (v == t)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, n, i, n_occ + s] ) * K[0, i*n_virt + t + n_ex] * K[1, (n*n_virt + t) * n_ex + i*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u != s) and (u != t) and (w == s) and (v == t)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, n, i, n_occ + u] ) * K[0, i*n_virt + u + n_ex] * K[1, (n*n_virt + s) * n_ex + i*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u != s) and (u != t) and (w == u) and (v == t)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, n, i, n_occ + s] ) * K[0, i*n_virt + u + n_ex] * K[1, (n*n_virt + u) * n_ex + i*n_virt + t+ 2*n_ex]

											elif ((j == i) and (k == i) and (n == i) and (m != i) and (m != j) and (m != k)):

												if ((t == s) and (u == s) and (w == s) and (v == s)):

													L3[(i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * F[m, n_occ + s] + -4 * g[i, i, m, n_occ + s] + 4 * g[m, n_occ + s, n_occ + s, n_occ + s] + -4 * g[i, m, i, n_occ + s] ) * K[0, i*n_virt + s + n_ex] * K[1, (i*n_virt + s) * n_ex + m*n_virt + s+ 2*n_ex]

												elif ((t == s) and (u == s) and (w == s) and (v != s) and (v != t) and (v != u)):

													L3[(i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, m, i, n_occ + v] + -8 * g[i, i, m, n_occ + v] + -4 * g[m, n_occ + s, n_occ + s, n_occ + v] + 8 * g[m, n_occ + v, n_occ + s, n_occ + s] ) * K[0, i*n_virt + s + n_ex] * K[1, (i*n_virt + s) * n_ex + m*n_virt + v+ 2*n_ex]

												elif ((t == s) and (u != s) and (u != t) and (w == s) and (v == s)):

													L3[(i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * F[m, n_occ + u] + 8 * g[m, n_occ + s, n_occ + s, n_occ + u] + -4 * g[m, n_occ + u, n_occ + s, n_occ + s] + 4 * g[i, i, m, n_occ + u] + -8 * g[i, m, i, n_occ + u] ) * K[0, i*n_virt + u + n_ex] * K[1, (i*n_virt + s) * n_ex + m*n_virt + s+ 2*n_ex]

												elif ((t == s) and (u != s) and (u != t) and (w == s) and (v == u)):

													L3[(i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[m, n_occ + u, n_occ + s, n_occ + u] ) * K[0, i*n_virt + u + n_ex] * K[1, (i*n_virt + s) * n_ex + m*n_virt + u+ 2*n_ex]

												elif ((t == s) and (u != s) and (u != t) and (w == s) and (v != s) and (v != t) and (v != u)):

													L3[(i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[m, n_occ + u, n_occ + s, n_occ + v] + 8 * g[m, n_occ + v, n_occ + s, n_occ + u] ) * K[0, i*n_virt + u + n_ex] * K[1, (i*n_virt + s) * n_ex + m*n_virt + v+ 2*n_ex]

												elif ((t != s) and (u == s) and (w == s) and (v == s)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[m, n_occ + s, n_occ + s, n_occ + t] ) * K[0, i*n_virt + s + n_ex] * K[1, (i*n_virt + s) * n_ex + m*n_virt + s+ 2*n_ex]

												elif ((t != s) and (u == s) and (w == s) and (v == t)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * F[m, n_occ + s] + 8 * g[m, n_occ + t, n_occ + s, n_occ + t] + -4 * g[m, n_occ + s, n_occ + t, n_occ + t] + 4 * g[i, i, m, n_occ + s] + -8 * g[i, m, i, n_occ + s] ) * K[0, i*n_virt + s + n_ex] * K[1, (i*n_virt + s) * n_ex + m*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u == s) and (w == s) and (v != s) and (v != t) and (v != u)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[m, n_occ + s, n_occ + t, n_occ + v] + 8 * g[m, n_occ + v, n_occ + s, n_occ + t] ) * K[0, i*n_virt + s + n_ex] * K[1, (i*n_virt + s) * n_ex + m*n_virt + v+ 2*n_ex]

												elif ((t != s) and (u == t) and (w == s) and (v == s)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, m, i, n_occ + s] + -8 * g[i, i, m, n_occ + s] + -4 * g[m, n_occ + t, n_occ + s, n_occ + t] + 8 * g[m, n_occ + s, n_occ + t, n_occ + t] ) * K[0, i*n_virt + t + n_ex] * K[1, (i*n_virt + s) * n_ex + m*n_virt + s+ 2*n_ex]

												elif ((t != s) and (u == t) and (w == s) and (v == t)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * F[m, n_occ + t] + -4 * g[i, i, m, n_occ + t] + 4 * g[m, n_occ + t, n_occ + t, n_occ + t] + -4 * g[i, m, i, n_occ + t] ) * K[0, i*n_virt + t + n_ex] * K[1, (i*n_virt + s) * n_ex + m*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u == t) and (w == s) and (v != s) and (v != t) and (v != u)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, m, i, n_occ + v] + -8 * g[i, i, m, n_occ + v] + -4 * g[m, n_occ + t, n_occ + t, n_occ + v] + 8 * g[m, n_occ + v, n_occ + t, n_occ + t] ) * K[0, i*n_virt + t + n_ex] * K[1, (i*n_virt + s) * n_ex + m*n_virt + v+ 2*n_ex]

												elif ((t != s) and (u != s) and (u != t) and (w == s) and (v == s)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (8 * g[m, n_occ + s, n_occ + t, n_occ + u] + -4 * g[m, n_occ + u, n_occ + s, n_occ + t] ) * K[0, i*n_virt + u + n_ex] * K[1, (i*n_virt + s) * n_ex + m*n_virt + s+ 2*n_ex]

												elif ((t != s) and (u != s) and (u != t) and (w == s) and (v == t)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * F[m, n_occ + u] + 8 * g[m, n_occ + t, n_occ + t, n_occ + u] + -4 * g[m, n_occ + u, n_occ + t, n_occ + t] + 4 * g[i, i, m, n_occ + u] + -8 * g[i, m, i, n_occ + u] ) * K[0, i*n_virt + u + n_ex] * K[1, (i*n_virt + s) * n_ex + m*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u != s) and (u != t) and (w == s) and (v == u)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[m, n_occ + u, n_occ + t, n_occ + u] ) * K[0, i*n_virt + u + n_ex] * K[1, (i*n_virt + s) * n_ex + m*n_virt + u+ 2*n_ex]

												elif ((t != s) and (u != s) and (u != t) and (w == s) and (v != s) and (v != t) and (v != u)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[m, n_occ + u, n_occ + t, n_occ + v] + 8 * g[m, n_occ + v, n_occ + t, n_occ + u] ) * K[0, i*n_virt + u + n_ex] * K[1, (i*n_virt + s) * n_ex + m*n_virt + v+ 2*n_ex]

											elif ((j == i) and (k != i) and (k != j) and (n == i) and (m == i)):

												if ((t == s) and (u == s) and (w != s) and (w != t) and (w != u) and (w != v) and (v == s)):

													L3[(i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[k, n_occ + s, n_occ + s, n_occ + w] ) * K[0, k*n_virt + s + n_ex] * K[1, (i*n_virt + w) * n_ex + i*n_virt + s+ 2*n_ex]

												elif ((t == s) and (u == s) and (w == s) and (v != s) and (v != t) and (v != u)):

													L3[(i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * F[k, n_occ + v] + 8 * g[k, n_occ + s, n_occ + s, n_occ + v] + -4 * g[k, n_occ + v, n_occ + s, n_occ + s] + 4 * g[i, i, k, n_occ + v] + -8 * g[i, k, i, n_occ + v] ) * K[0, k*n_virt + s + n_ex] * K[1, (i*n_virt + s) * n_ex + i*n_virt + v+ 2*n_ex]

												elif ((t == s) and (u != s) and (u != t) and (w == u) and (v == s)):

													L3[(i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * F[k, n_occ + s] + -8 * g[k, n_occ + u, n_occ + s, n_occ + u] + 4 * g[k, n_occ + s, n_occ + u, n_occ + u] + -4 * g[i, i, k, n_occ + s] + 8 * g[i, k, i, n_occ + s] ) * K[0, k*n_virt + u + n_ex] * K[1, (i*n_virt + u) * n_ex + i*n_virt + s+ 2*n_ex]

												elif ((t == s) and (u != s) and (u != t) and (w != s) and (w != t) and (w != u) and (w != v) and (v == s)):

													L3[(i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[k, n_occ + s, n_occ + u, n_occ + w] + -8 * g[k, n_occ + u, n_occ + s, n_occ + w] ) * K[0, k*n_virt + u + n_ex] * K[1, (i*n_virt + w) * n_ex + i*n_virt + s+ 2*n_ex]

												elif ((t == s) and (u != s) and (u != t) and (w == s) and (v == u)):

													L3[(i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[k, n_occ + u, n_occ + s, n_occ + u] ) * K[0, k*n_virt + u + n_ex] * K[1, (i*n_virt + s) * n_ex + i*n_virt + u+ 2*n_ex]

												elif ((t == s) and (u != s) and (u != t) and (w == s) and (v != s) and (v != t) and (v != u)):

													L3[(i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (8 * g[k, n_occ + u, n_occ + s, n_occ + v] + -4 * g[k, n_occ + v, n_occ + s, n_occ + u] ) * K[0, k*n_virt + u + n_ex] * K[1, (i*n_virt + s) * n_ex + i*n_virt + v+ 2*n_ex]

												elif ((t != s) and (u == s) and (w == s) and (v == s)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[k, n_occ + s, n_occ + s, n_occ + t] ) * K[0, k*n_virt + s + n_ex] * K[1, (i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex]

												elif ((t != s) and (u == s) and (w == s) and (v == t)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * F[k, n_occ + s] + -4 * g[k, n_occ + s, n_occ + s, n_occ + s] + 8 * g[i, k, i, n_occ + s] + -4 * g[k, n_occ + t, n_occ + s, n_occ + t] + 8 * g[k, n_occ + s, n_occ + t, n_occ + t] + -4 * g[i, i, k, n_occ + s] ) * K[0, k*n_virt + s + n_ex] * K[1, (i*n_virt + s) * n_ex + i*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u == s) and (w == t) and (v == t)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[k, n_occ + s, n_occ + s, n_occ + t] ) * K[0, k*n_virt + s + n_ex] * K[1, (i*n_virt + t) * n_ex + i*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u == s) and (w != s) and (w != t) and (w != u) and (w != v) and (v == t)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[k, n_occ + s, n_occ + s, n_occ + w] ) * K[0, k*n_virt + s + n_ex] * K[1, (i*n_virt + w) * n_ex + i*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u == s) and (w == s) and (v != s) and (v != t) and (v != u)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (8 * g[k, n_occ + s, n_occ + t, n_occ + v] + -4 * g[k, n_occ + v, n_occ + s, n_occ + t] ) * K[0, k*n_virt + s + n_ex] * K[1, (i*n_virt + s) * n_ex + i*n_virt + v+ 2*n_ex]

												elif ((t != s) and (u == t) and (w == s) and (v == s)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * F[k, n_occ + s] + 8 * g[k, n_occ + t, n_occ + s, n_occ + t] + -4 * g[k, n_occ + s, n_occ + t, n_occ + t] + 4 * g[i, i, k, n_occ + s] + -8 * g[i, k, i, n_occ + s] ) * K[0, k*n_virt + t + n_ex] * K[1, (i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex]

												elif ((t != s) and (u == t) and (w == s) and (v == t)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * F[k, n_occ + t] + 4 * g[k, n_occ + s, n_occ + s, n_occ + t] + -8 * g[k, n_occ + t, n_occ + s, n_occ + s] + 4 * g[i, i, k, n_occ + t] + 4 * g[k, n_occ + t, n_occ + t, n_occ + t] + -8 * g[i, k, i, n_occ + t] ) * K[0, k*n_virt + t + n_ex] * K[1, (i*n_virt + s) * n_ex + i*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u == t) and (w == t) and (v == t)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * F[k, n_occ + s] + -8 * g[k, n_occ + t, n_occ + s, n_occ + t] + 4 * g[k, n_occ + s, n_occ + t, n_occ + t] + -4 * g[i, i, k, n_occ + s] + 8 * g[i, k, i, n_occ + s] ) * K[0, k*n_virt + t + n_ex] * K[1, (i*n_virt + t) * n_ex + i*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u == t) and (w != s) and (w != t) and (w != u) and (w != v) and (v == t)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[k, n_occ + s, n_occ + t, n_occ + w] + -8 * g[k, n_occ + t, n_occ + s, n_occ + w] ) * K[0, k*n_virt + t + n_ex] * K[1, (i*n_virt + w) * n_ex + i*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u == t) and (w == s) and (v != s) and (v != t) and (v != u)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * F[k, n_occ + v] + 8 * g[k, n_occ + t, n_occ + t, n_occ + v] + -4 * g[k, n_occ + v, n_occ + t, n_occ + t] + 4 * g[i, i, k, n_occ + v] + -8 * g[i, k, i, n_occ + v] ) * K[0, k*n_virt + t + n_ex] * K[1, (i*n_virt + s) * n_ex + i*n_virt + v+ 2*n_ex]

												elif ((t != s) and (u != s) and (u != t) and (w == s) and (v == s)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[k, n_occ + s, n_occ + t, n_occ + u] + 8 * g[k, n_occ + u, n_occ + s, n_occ + t] ) * K[0, k*n_virt + u + n_ex] * K[1, (i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex]

												elif ((t != s) and (u != s) and (u != t) and (w == s) and (v == t)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[k, n_occ + s, n_occ + s, n_occ + u] + -8 * g[k, n_occ + u, n_occ + s, n_occ + s] + -4 * g[k, n_occ + t, n_occ + t, n_occ + u] + 8 * g[k, n_occ + u, n_occ + t, n_occ + t] ) * K[0, k*n_virt + u + n_ex] * K[1, (i*n_virt + s) * n_ex + i*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u != s) and (u != t) and (w == t) and (v == t)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[k, n_occ + s, n_occ + t, n_occ + u] + -8 * g[k, n_occ + u, n_occ + s, n_occ + t] ) * K[0, k*n_virt + u + n_ex] * K[1, (i*n_virt + t) * n_ex + i*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u != s) and (u != t) and (w == u) and (v == t)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * F[k, n_occ + s] + -8 * g[k, n_occ + u, n_occ + s, n_occ + u] + 4 * g[k, n_occ + s, n_occ + u, n_occ + u] + -4 * g[i, i, k, n_occ + s] + 8 * g[i, k, i, n_occ + s] ) * K[0, k*n_virt + u + n_ex] * K[1, (i*n_virt + u) * n_ex + i*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u != s) and (u != t) and (w != s) and (w != t) and (w != u) and (w != v) and (v == t)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[k, n_occ + s, n_occ + u, n_occ + w] + -8 * g[k, n_occ + u, n_occ + s, n_occ + w] ) * K[0, k*n_virt + u + n_ex] * K[1, (i*n_virt + w) * n_ex + i*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u != s) and (u != t) and (w == s) and (v == u)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[k, n_occ + u, n_occ + t, n_occ + u] ) * K[0, k*n_virt + u + n_ex] * K[1, (i*n_virt + s) * n_ex + i*n_virt + u+ 2*n_ex]

												elif ((t != s) and (u != s) and (u != t) and (w == s) and (v != s) and (v != t) and (v != u)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (8 * g[k, n_occ + u, n_occ + t, n_occ + v] + -4 * g[k, n_occ + v, n_occ + t, n_occ + u] ) * K[0, k*n_virt + u + n_ex] * K[1, (i*n_virt + s) * n_ex + i*n_virt + v+ 2*n_ex]

											elif ((j == i) and (k != i) and (k != j) and (n == k) and (m == i)):

												if ((t == s) and (u == s) and (w == s) and (v == s)):

													L3[(i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * F[i, n_occ + s] + -4 * g[i, n_occ + s, n_occ + s, n_occ + s] + 4 * g[i, n_occ + s, k, k] + 4 * g[i, k, k, n_occ + s] ) * K[0, k*n_virt + s + n_ex] * K[1, (k*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex]

												elif ((t == s) and (u == s) and (w != s) and (w != t) and (w != u) and (w != v) and (v == s)):

													L3[(i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, n_occ + s, n_occ + s, n_occ + w] ) * K[0, k*n_virt + s + n_ex] * K[1, (k*n_virt + w) * n_ex + i*n_virt + s+ 2*n_ex]

												elif ((t == s) and (u != s) and (u != t) and (w == s) and (v == s)):

													L3[(i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * F[i, n_occ + u] + -8 * g[i, n_occ + s, n_occ + s, n_occ + u] + 4 * g[i, n_occ + u, n_occ + s, n_occ + s] + -4 * g[i, n_occ + u, k, k] + 8 * g[i, k, k, n_occ + u] ) * K[0, k*n_virt + u + n_ex] * K[1, (k*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex]

												elif ((t == s) and (u != s) and (u != t) and (w == u) and (v == s)):

													L3[(i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, n_occ + u, n_occ + s, n_occ + u] + -8 * g[i, n_occ + s, n_occ + u, n_occ + u] + -4 * g[i, k, k, n_occ + s] + 8 * g[i, n_occ + s, k, k] ) * K[0, k*n_virt + u + n_ex] * K[1, (k*n_virt + u) * n_ex + i*n_virt + s+ 2*n_ex]

												elif ((t == s) and (u != s) and (u != t) and (w != s) and (w != t) and (w != u) and (w != v) and (v == s)):

													L3[(i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-8 * g[i, n_occ + s, n_occ + u, n_occ + w] + 4 * g[i, n_occ + u, n_occ + s, n_occ + w] ) * K[0, k*n_virt + u + n_ex] * K[1, (k*n_virt + w) * n_ex + i*n_virt + s+ 2*n_ex]

												elif ((t != s) and (u == s) and (w == s) and (v == t)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * F[i, n_occ + s] + -4 * g[i, n_occ + s, n_occ + s, n_occ + s] + 4 * g[i, n_occ + s, k, k] + 4 * g[i, k, k, n_occ + s] ) * K[0, k*n_virt + s + n_ex] * K[1, (k*n_virt + s) * n_ex + i*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u == s) and (w == t) and (v == t)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, n_occ + s, n_occ + s, n_occ + t] ) * K[0, k*n_virt + s + n_ex] * K[1, (k*n_virt + t) * n_ex + i*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u == s) and (w != s) and (w != t) and (w != u) and (w != v) and (v == t)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, n_occ + s, n_occ + s, n_occ + w] ) * K[0, k*n_virt + s + n_ex] * K[1, (k*n_virt + w) * n_ex + i*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u == t) and (w == s) and (v == t)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * F[i, n_occ + t] + -8 * g[i, n_occ + s, n_occ + s, n_occ + t] + 4 * g[i, n_occ + t, n_occ + s, n_occ + s] + -4 * g[i, n_occ + t, k, k] + 8 * g[i, k, k, n_occ + t] ) * K[0, k*n_virt + t + n_ex] * K[1, (k*n_virt + s) * n_ex + i*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u == t) and (w == t) and (v == t)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, n_occ + t, n_occ + s, n_occ + t] + -8 * g[i, n_occ + s, n_occ + t, n_occ + t] + -4 * g[i, k, k, n_occ + s] + 8 * g[i, n_occ + s, k, k] ) * K[0, k*n_virt + t + n_ex] * K[1, (k*n_virt + t) * n_ex + i*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u == t) and (w != s) and (w != t) and (w != u) and (w != v) and (v == t)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-8 * g[i, n_occ + s, n_occ + t, n_occ + w] + 4 * g[i, n_occ + t, n_occ + s, n_occ + w] ) * K[0, k*n_virt + t + n_ex] * K[1, (k*n_virt + w) * n_ex + i*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u != s) and (u != t) and (w == s) and (v == t)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * F[i, n_occ + u] + -8 * g[i, n_occ + s, n_occ + s, n_occ + u] + 4 * g[i, n_occ + u, n_occ + s, n_occ + s] + -4 * g[i, n_occ + u, k, k] + 8 * g[i, k, k, n_occ + u] ) * K[0, k*n_virt + u + n_ex] * K[1, (k*n_virt + s) * n_ex + i*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u != s) and (u != t) and (w == t) and (v == t)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-8 * g[i, n_occ + s, n_occ + t, n_occ + u] + 4 * g[i, n_occ + u, n_occ + s, n_occ + t] ) * K[0, k*n_virt + u + n_ex] * K[1, (k*n_virt + t) * n_ex + i*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u != s) and (u != t) and (w == u) and (v == t)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, n_occ + u, n_occ + s, n_occ + u] + -8 * g[i, n_occ + s, n_occ + u, n_occ + u] + -4 * g[i, k, k, n_occ + s] + 8 * g[i, n_occ + s, k, k] ) * K[0, k*n_virt + u + n_ex] * K[1, (k*n_virt + u) * n_ex + i*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u != s) and (u != t) and (w != s) and (w != t) and (w != u) and (w != v) and (v == t)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-8 * g[i, n_occ + s, n_occ + u, n_occ + w] + 4 * g[i, n_occ + u, n_occ + s, n_occ + w] ) * K[0, k*n_virt + u + n_ex] * K[1, (k*n_virt + w) * n_ex + i*n_virt + t+ 2*n_ex]

											elif ((j == i) and (k != i) and (k != j) and (n != i) and (n != j) and (n != k) and (n != m) and (m == i)):

												if ((t == s) and (u == s) and (w == s) and (v == s)):

													L3[(i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, n, k, n_occ + s] + 4 * g[i, n_occ + s, k, n] ) * K[0, k*n_virt + s + n_ex] * K[1, (n*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex]

												elif ((t == s) and (u != s) and (u != t) and (w == s) and (v == s)):

													L3[(i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (8 * g[i, n, k, n_occ + u] + -4 * g[i, n_occ + u, k, n] ) * K[0, k*n_virt + u + n_ex] * K[1, (n*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex]

												elif ((t == s) and (u != s) and (u != t) and (w == u) and (v == s)):

													L3[(i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, n, k, n_occ + s] + 8 * g[i, n_occ + s, k, n] ) * K[0, k*n_virt + u + n_ex] * K[1, (n*n_virt + u) * n_ex + i*n_virt + s+ 2*n_ex]

												elif ((t != s) and (u == s) and (w == s) and (v == t)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, n, k, n_occ + s] + 4 * g[i, n_occ + s, k, n] ) * K[0, k*n_virt + s + n_ex] * K[1, (n*n_virt + s) * n_ex + i*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u == t) and (w == s) and (v == t)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (8 * g[i, n, k, n_occ + t] + -4 * g[i, n_occ + t, k, n] ) * K[0, k*n_virt + t + n_ex] * K[1, (n*n_virt + s) * n_ex + i*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u == t) and (w == t) and (v == t)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, n, k, n_occ + s] + 8 * g[i, n_occ + s, k, n] ) * K[0, k*n_virt + t + n_ex] * K[1, (n*n_virt + t) * n_ex + i*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u != s) and (u != t) and (w == s) and (v == t)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (8 * g[i, n, k, n_occ + u] + -4 * g[i, n_occ + u, k, n] ) * K[0, k*n_virt + u + n_ex] * K[1, (n*n_virt + s) * n_ex + i*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u != s) and (u != t) and (w == u) and (v == t)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, n, k, n_occ + s] + 8 * g[i, n_occ + s, k, n] ) * K[0, k*n_virt + u + n_ex] * K[1, (n*n_virt + u) * n_ex + i*n_virt + t+ 2*n_ex]

											elif ((j == i) and (k != i) and (k != j) and (n == i) and (m == k)):

												if ((t == s) and (u == s) and (w == s) and (v == s)):

													L3[(i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-8 * g[i, k, k, n_occ + s] ) * K[0, k*n_virt + s + n_ex] * K[1, (i*n_virt + s) * n_ex + k*n_virt + s+ 2*n_ex]

												elif ((t == s) and (u == s) and (w == s) and (v != s) and (v != t) and (v != u)):

													L3[(i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, k, k, n_occ + v] ) * K[0, k*n_virt + s + n_ex] * K[1, (i*n_virt + s) * n_ex + k*n_virt + v+ 2*n_ex]

												elif ((t == s) and (u != s) and (u != t) and (w == s) and (v == s)):

													L3[(i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, k, k, n_occ + u] ) * K[0, k*n_virt + u + n_ex] * K[1, (i*n_virt + s) * n_ex + k*n_virt + s+ 2*n_ex]

												elif ((t != s) and (u == s) and (w == s) and (v == t)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, k, k, n_occ + s] ) * K[0, k*n_virt + s + n_ex] * K[1, (i*n_virt + s) * n_ex + k*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u == t) and (w == s) and (v == s)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, k, k, n_occ + s] ) * K[0, k*n_virt + t + n_ex] * K[1, (i*n_virt + s) * n_ex + k*n_virt + s+ 2*n_ex]

												elif ((t != s) and (u == t) and (w == s) and (v == t)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-8 * g[i, k, k, n_occ + t] ) * K[0, k*n_virt + t + n_ex] * K[1, (i*n_virt + s) * n_ex + k*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u == t) and (w == s) and (v != s) and (v != t) and (v != u)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, k, k, n_occ + v] ) * K[0, k*n_virt + t + n_ex] * K[1, (i*n_virt + s) * n_ex + k*n_virt + v+ 2*n_ex]

												elif ((t != s) and (u != s) and (u != t) and (w == s) and (v == t)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, k, k, n_occ + u] ) * K[0, k*n_virt + u + n_ex] * K[1, (i*n_virt + s) * n_ex + k*n_virt + t+ 2*n_ex]

											elif ((j == i) and (k != i) and (k != j) and (n == i) and (m != i) and (m != j) and (m != k)):

												if ((t == s) and (u == s) and (w == s) and (v == s)):

													L3[(i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, m, k, n_occ + s] + -4 * g[i, k, m, n_occ + s] ) * K[0, k*n_virt + s + n_ex] * K[1, (i*n_virt + s) * n_ex + m*n_virt + s+ 2*n_ex]

												elif ((t == s) and (u == s) and (w == s) and (v != s) and (v != t) and (v != u)):

													L3[(i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-8 * g[i, k, m, n_occ + v] + 4 * g[i, m, k, n_occ + v] ) * K[0, k*n_virt + s + n_ex] * K[1, (i*n_virt + s) * n_ex + m*n_virt + v+ 2*n_ex]

												elif ((t == s) and (u != s) and (u != t) and (w == s) and (v == s)):

													L3[(i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, k, m, n_occ + u] + -8 * g[i, m, k, n_occ + u] ) * K[0, k*n_virt + u + n_ex] * K[1, (i*n_virt + s) * n_ex + m*n_virt + s+ 2*n_ex]

												elif ((t != s) and (u == s) and (w == s) and (v == t)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, k, m, n_occ + s] + -8 * g[i, m, k, n_occ + s] ) * K[0, k*n_virt + s + n_ex] * K[1, (i*n_virt + s) * n_ex + m*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u == t) and (w == s) and (v == s)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-8 * g[i, k, m, n_occ + s] + 4 * g[i, m, k, n_occ + s] ) * K[0, k*n_virt + t + n_ex] * K[1, (i*n_virt + s) * n_ex + m*n_virt + s+ 2*n_ex]

												elif ((t != s) and (u == t) and (w == s) and (v == t)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, m, k, n_occ + t] + -4 * g[i, k, m, n_occ + t] ) * K[0, k*n_virt + t + n_ex] * K[1, (i*n_virt + s) * n_ex + m*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u == t) and (w == s) and (v != s) and (v != t) and (v != u)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-8 * g[i, k, m, n_occ + v] + 4 * g[i, m, k, n_occ + v] ) * K[0, k*n_virt + t + n_ex] * K[1, (i*n_virt + s) * n_ex + m*n_virt + v+ 2*n_ex]

												elif ((t != s) and (u != s) and (u != t) and (w == s) and (v == t)):

													L3[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, k, m, n_occ + u] + -8 * g[i, m, k, n_occ + u] ) * K[0, k*n_virt + u + n_ex] * K[1, (i*n_virt + s) * n_ex + m*n_virt + t+ 2*n_ex]

											elif ((j != i) and (k == i) and (n == i) and (m == i)):

												if ((t == s) and (u == s) and (w == s) and (v == s)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-8 * g[i, j, i, n_occ + s] ) * K[0, i*n_virt + s + n_ex] * K[1, (i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex]

												elif ((t == s) and (u == s) and (w == s) and (v != s) and (v != t) and (v != u)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, j, i, n_occ + v] ) * K[0, i*n_virt + s + n_ex] * K[1, (i*n_virt + s) * n_ex + i*n_virt + v+ 2*n_ex]

												elif ((t == s) and (u != s) and (u != t) and (w == s) and (v == s)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, j, i, n_occ + u] ) * K[0, i*n_virt + u + n_ex] * K[1, (i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex]

												elif ((t != s) and (u == s) and (w == s) and (v == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, j, i, n_occ + s] ) * K[0, i*n_virt + s + n_ex] * K[1, (i*n_virt + s) * n_ex + i*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u == t) and (w == s) and (v == s)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, j, i, n_occ + s] ) * K[0, i*n_virt + t + n_ex] * K[1, (i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex]

												elif ((t != s) and (u == t) and (w == s) and (v == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-8 * g[i, j, i, n_occ + t] ) * K[0, i*n_virt + t + n_ex] * K[1, (i*n_virt + s) * n_ex + i*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u == t) and (w == s) and (v != s) and (v != t) and (v != u)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, j, i, n_occ + v] ) * K[0, i*n_virt + t + n_ex] * K[1, (i*n_virt + s) * n_ex + i*n_virt + v+ 2*n_ex]

												elif ((t != s) and (u != s) and (u != t) and (w == s) and (v == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, j, i, n_occ + u] ) * K[0, i*n_virt + u + n_ex] * K[1, (i*n_virt + s) * n_ex + i*n_virt + t+ 2*n_ex]

											elif ((j != i) and (k == i) and (n == i) and (m == j)):

												if ((t == s) and (u == s) and (w == s) and (v == s)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * F[i, n_occ + s] + -4 * g[i, n_occ + s, n_occ + s, n_occ + s] + 8 * g[i, i, i, n_occ + s] + -4 * g[i, j, j, n_occ + s] + -4 * g[i, n_occ + s, j, j] ) * K[0, i*n_virt + s + n_ex] * K[1, (i*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex]

												elif ((t == s) and (u == s) and (w != s) and (w != t) and (w != u) and (w != v) and (v == s)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-8 * g[i, n_occ + s, n_occ + s, n_occ + w] ) * K[0, i*n_virt + s + n_ex] * K[1, (i*n_virt + w) * n_ex + j*n_virt + s+ 2*n_ex]

												elif ((t == s) and (u == s) and (w == s) and (v != s) and (v != t) and (v != u)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * F[i, n_occ + v] + 8 * g[i, n_occ + s, n_occ + s, n_occ + v] + -4 * g[i, n_occ + v, n_occ + s, n_occ + s] + 4 * g[i, n_occ + v, j, j] + -8 * g[i, j, j, n_occ + v] ) * K[0, i*n_virt + s + n_ex] * K[1, (i*n_virt + s) * n_ex + j*n_virt + v+ 2*n_ex]

												elif ((t == s) and (u != s) and (u != t) and (w == s) and (v == s)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * F[i, n_occ + u] + -8 * g[i, n_occ + s, n_occ + s, n_occ + u] + 4 * g[i, n_occ + u, n_occ + s, n_occ + s] + 4 * g[i, i, i, n_occ + u] + -8 * g[i, n_occ + u, j, j] + 4 * g[i, j, j, n_occ + u] ) * K[0, i*n_virt + u + n_ex] * K[1, (i*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex]

												elif ((t == s) and (u != s) and (u != t) and (w == u) and (v == s)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * F[i, n_occ + s] + -4 * g[i, n_occ + u, n_occ + s, n_occ + u] + -4 * g[i, n_occ + s, n_occ + u, n_occ + u] + 4 * g[i, i, i, n_occ + s] ) * K[0, i*n_virt + u + n_ex] * K[1, (i*n_virt + u) * n_ex + j*n_virt + s+ 2*n_ex]

												elif ((t == s) and (u != s) and (u != t) and (w != s) and (w != t) and (w != u) and (w != v) and (v == s)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, n_occ + u, n_occ + s, n_occ + w] + -4 * g[i, n_occ + s, n_occ + u, n_occ + w] ) * K[0, i*n_virt + u + n_ex] * K[1, (i*n_virt + w) * n_ex + j*n_virt + s+ 2*n_ex]

												elif ((t == s) and (u != s) and (u != t) and (w == s) and (v == u)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, n_occ + u, n_occ + s, n_occ + u] ) * K[0, i*n_virt + u + n_ex] * K[1, (i*n_virt + s) * n_ex + j*n_virt + u+ 2*n_ex]

												elif ((t == s) and (u != s) and (u != t) and (w == s) and (v != s) and (v != t) and (v != u)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (8 * g[i, n_occ + u, n_occ + s, n_occ + v] + -4 * g[i, n_occ + v, n_occ + s, n_occ + u] ) * K[0, i*n_virt + u + n_ex] * K[1, (i*n_virt + s) * n_ex + j*n_virt + v+ 2*n_ex]

												elif ((t != s) and (u == s) and (w == s) and (v == s)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, n_occ + s, n_occ + s, n_occ + t] ) * K[0, i*n_virt + s + n_ex] * K[1, (i*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex]

												elif ((t != s) and (u == s) and (w == s) and (v == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (8 * F[i, n_occ + s] + -8 * g[i, n_occ + s, n_occ + s, n_occ + s] + -4 * g[i, n_occ + t, n_occ + s, n_occ + t] + 8 * g[i, n_occ + s, n_occ + t, n_occ + t] + 4 * g[i, j, j, n_occ + s] + -8 * g[i, n_occ + s, j, j] + 8 * g[i, i, i, n_occ + s] ) * K[0, i*n_virt + s + n_ex] * K[1, (i*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u == s) and (w == t) and (v == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-8 * g[i, n_occ + s, n_occ + s, n_occ + t] ) * K[0, i*n_virt + s + n_ex] * K[1, (i*n_virt + t) * n_ex + j*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u == s) and (w != s) and (w != t) and (w != u) and (w != v) and (v == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-8 * g[i, n_occ + s, n_occ + s, n_occ + w] ) * K[0, i*n_virt + s + n_ex] * K[1, (i*n_virt + w) * n_ex + j*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u == s) and (w == s) and (v != s) and (v != t) and (v != u)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (8 * g[i, n_occ + s, n_occ + t, n_occ + v] + -4 * g[i, n_occ + v, n_occ + s, n_occ + t] ) * K[0, i*n_virt + s + n_ex] * K[1, (i*n_virt + s) * n_ex + j*n_virt + v+ 2*n_ex]

												elif ((t != s) and (u == t) and (w == s) and (v == s)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * F[i, n_occ + s] + 8 * g[i, n_occ + t, n_occ + s, n_occ + t] + -4 * g[i, n_occ + s, n_occ + t, n_occ + t] + 4 * g[i, n_occ + s, j, j] + -8 * g[i, j, j, n_occ + s] ) * K[0, i*n_virt + t + n_ex] * K[1, (i*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex]

												elif ((t != s) and (u == t) and (w == s) and (v == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, n_occ + t, n_occ + s, n_occ + s] + -4 * g[i, n_occ + s, n_occ + s, n_occ + t] + -4 * g[i, n_occ + t, j, j] + 4 * g[i, i, i, n_occ + t] + 4 * g[i, n_occ + t, n_occ + t, n_occ + t] + -4 * g[i, j, j, n_occ + t] ) * K[0, i*n_virt + t + n_ex] * K[1, (i*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u == t) and (w == t) and (v == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * F[i, n_occ + s] + -4 * g[i, n_occ + t, n_occ + s, n_occ + t] + -4 * g[i, n_occ + s, n_occ + t, n_occ + t] + 4 * g[i, i, i, n_occ + s] ) * K[0, i*n_virt + t + n_ex] * K[1, (i*n_virt + t) * n_ex + j*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u == t) and (w != s) and (w != t) and (w != u) and (w != v) and (v == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, n_occ + t, n_occ + s, n_occ + w] + -4 * g[i, n_occ + s, n_occ + t, n_occ + w] ) * K[0, i*n_virt + t + n_ex] * K[1, (i*n_virt + w) * n_ex + j*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u == t) and (w == s) and (v != s) and (v != t) and (v != u)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * F[i, n_occ + v] + 8 * g[i, n_occ + t, n_occ + t, n_occ + v] + -4 * g[i, n_occ + v, n_occ + t, n_occ + t] + 4 * g[i, n_occ + v, j, j] + -8 * g[i, j, j, n_occ + v] ) * K[0, i*n_virt + t + n_ex] * K[1, (i*n_virt + s) * n_ex + j*n_virt + v+ 2*n_ex]

												elif ((t != s) and (u != s) and (u != t) and (w == s) and (v == s)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, n_occ + s, n_occ + t, n_occ + u] + 8 * g[i, n_occ + u, n_occ + s, n_occ + t] ) * K[0, i*n_virt + u + n_ex] * K[1, (i*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex]

												elif ((t != s) and (u != s) and (u != t) and (w == s) and (v == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * F[i, n_occ + u] + -4 * g[i, n_occ + u, n_occ + s, n_occ + s] + -4 * g[i, n_occ + s, n_occ + s, n_occ + u] + -4 * g[i, n_occ + t, n_occ + t, n_occ + u] + 8 * g[i, n_occ + u, n_occ + t, n_occ + t] + 4 * g[i, i, i, n_occ + u] + -8 * g[i, n_occ + u, j, j] + 4 * g[i, j, j, n_occ + u] ) * K[0, i*n_virt + u + n_ex] * K[1, (i*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u != s) and (u != t) and (w == t) and (v == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, n_occ + u, n_occ + s, n_occ + t] + -4 * g[i, n_occ + s, n_occ + t, n_occ + u] ) * K[0, i*n_virt + u + n_ex] * K[1, (i*n_virt + t) * n_ex + j*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u != s) and (u != t) and (w == u) and (v == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * F[i, n_occ + s] + -4 * g[i, n_occ + u, n_occ + s, n_occ + u] + -4 * g[i, n_occ + s, n_occ + u, n_occ + u] + 4 * g[i, i, i, n_occ + s] ) * K[0, i*n_virt + u + n_ex] * K[1, (i*n_virt + u) * n_ex + j*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u != s) and (u != t) and (w != s) and (w != t) and (w != u) and (w != v) and (v == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, n_occ + u, n_occ + s, n_occ + w] + -4 * g[i, n_occ + s, n_occ + u, n_occ + w] ) * K[0, i*n_virt + u + n_ex] * K[1, (i*n_virt + w) * n_ex + j*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u != s) and (u != t) and (w == s) and (v == u)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, n_occ + u, n_occ + t, n_occ + u] ) * K[0, i*n_virt + u + n_ex] * K[1, (i*n_virt + s) * n_ex + j*n_virt + u+ 2*n_ex]

												elif ((t != s) and (u != s) and (u != t) and (w == s) and (v != s) and (v != t) and (v != u)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (8 * g[i, n_occ + u, n_occ + t, n_occ + v] + -4 * g[i, n_occ + v, n_occ + t, n_occ + u] ) * K[0, i*n_virt + u + n_ex] * K[1, (i*n_virt + s) * n_ex + j*n_virt + v+ 2*n_ex]

											elif ((j != i) and (k == i) and (n == j) and (m == j)):

												if ((t == s) and (u == s) and (w == s) and (v == s)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (8 * g[i, j, i, n_occ + s] ) * K[0, i*n_virt + s + n_ex] * K[1, (j*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex]

												elif ((t == s) and (u != s) and (u != t) and (w == s) and (v == s)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, j, i, n_occ + u] ) * K[0, i*n_virt + u + n_ex] * K[1, (j*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex]

												elif ((t == s) and (u != s) and (u != t) and (w == u) and (v == s)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, j, i, n_occ + s] ) * K[0, i*n_virt + u + n_ex] * K[1, (j*n_virt + u) * n_ex + j*n_virt + s+ 2*n_ex]

												elif ((t != s) and (u == s) and (w == s) and (v == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (8 * g[i, j, i, n_occ + s] ) * K[0, i*n_virt + s + n_ex] * K[1, (j*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u == t) and (w == s) and (v == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, j, i, n_occ + t] ) * K[0, i*n_virt + t + n_ex] * K[1, (j*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u == t) and (w == t) and (v == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, j, i, n_occ + s] ) * K[0, i*n_virt + t + n_ex] * K[1, (j*n_virt + t) * n_ex + j*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u != s) and (u != t) and (w == s) and (v == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, j, i, n_occ + u] ) * K[0, i*n_virt + u + n_ex] * K[1, (j*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u != s) and (u != t) and (w == u) and (v == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, j, i, n_occ + s] ) * K[0, i*n_virt + u + n_ex] * K[1, (j*n_virt + u) * n_ex + j*n_virt + t+ 2*n_ex]

											elif ((j != i) and (k == i) and (n != i) and (n != j) and (n != k) and (n != m) and (m == j)):

												if ((t == s) and (u == s) and (w == s) and (v == s)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (8 * g[i, n, i, n_occ + s] ) * K[0, i*n_virt + s + n_ex] * K[1, (n*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex]

												elif ((t == s) and (u != s) and (u != t) and (w == s) and (v == s)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, n, i, n_occ + u] ) * K[0, i*n_virt + u + n_ex] * K[1, (n*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex]

												elif ((t == s) and (u != s) and (u != t) and (w == u) and (v == s)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, n, i, n_occ + s] ) * K[0, i*n_virt + u + n_ex] * K[1, (n*n_virt + u) * n_ex + j*n_virt + s+ 2*n_ex]

												elif ((t != s) and (u == s) and (w == s) and (v == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (8 * g[i, n, i, n_occ + s] ) * K[0, i*n_virt + s + n_ex] * K[1, (n*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u == t) and (w == s) and (v == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, n, i, n_occ + t] ) * K[0, i*n_virt + t + n_ex] * K[1, (n*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u == t) and (w == t) and (v == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, n, i, n_occ + s] ) * K[0, i*n_virt + t + n_ex] * K[1, (n*n_virt + t) * n_ex + j*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u != s) and (u != t) and (w == s) and (v == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, n, i, n_occ + u] ) * K[0, i*n_virt + u + n_ex] * K[1, (n*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u != s) and (u != t) and (w == u) and (v == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, n, i, n_occ + s] ) * K[0, i*n_virt + u + n_ex] * K[1, (n*n_virt + u) * n_ex + j*n_virt + t+ 2*n_ex]

											elif ((j != i) and (k == i) and (n == i) and (m != i) and (m != j) and (m != k)):

												if ((t == s) and (u == s) and (w == s) and (v == s)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, n_occ + s, j, m] + -4 * g[i, j, m, n_occ + s] ) * K[0, i*n_virt + s + n_ex] * K[1, (i*n_virt + s) * n_ex + m*n_virt + s+ 2*n_ex]

												elif ((t == s) and (u == s) and (w == s) and (v != s) and (v != t) and (v != u)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-8 * g[i, j, m, n_occ + v] + 4 * g[i, n_occ + v, j, m] ) * K[0, i*n_virt + s + n_ex] * K[1, (i*n_virt + s) * n_ex + m*n_virt + v+ 2*n_ex]

												elif ((t == s) and (u != s) and (u != t) and (w == s) and (v == s)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, j, m, n_occ + u] + -8 * g[i, n_occ + u, j, m] ) * K[0, i*n_virt + u + n_ex] * K[1, (i*n_virt + s) * n_ex + m*n_virt + s+ 2*n_ex]

												elif ((t != s) and (u == s) and (w == s) and (v == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, j, m, n_occ + s] + -8 * g[i, n_occ + s, j, m] ) * K[0, i*n_virt + s + n_ex] * K[1, (i*n_virt + s) * n_ex + m*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u == t) and (w == s) and (v == s)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-8 * g[i, j, m, n_occ + s] + 4 * g[i, n_occ + s, j, m] ) * K[0, i*n_virt + t + n_ex] * K[1, (i*n_virt + s) * n_ex + m*n_virt + s+ 2*n_ex]

												elif ((t != s) and (u == t) and (w == s) and (v == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, n_occ + t, j, m] + -4 * g[i, j, m, n_occ + t] ) * K[0, i*n_virt + t + n_ex] * K[1, (i*n_virt + s) * n_ex + m*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u == t) and (w == s) and (v != s) and (v != t) and (v != u)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-8 * g[i, j, m, n_occ + v] + 4 * g[i, n_occ + v, j, m] ) * K[0, i*n_virt + t + n_ex] * K[1, (i*n_virt + s) * n_ex + m*n_virt + v+ 2*n_ex]

												elif ((t != s) and (u != s) and (u != t) and (w == s) and (v == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, j, m, n_occ + u] + -8 * g[i, n_occ + u, j, m] ) * K[0, i*n_virt + u + n_ex] * K[1, (i*n_virt + s) * n_ex + m*n_virt + t+ 2*n_ex]

											elif ((j != i) and (k == j) and (n == i) and (m == i)):

												if ((t == s) and (u == s) and (w == s) and (v == s)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * F[i, n_occ + s] + -4 * g[i, n_occ + s, j, j] + 4 * g[i, n_occ + s, n_occ + s, n_occ + s] + -4 * g[i, j, j, n_occ + s] ) * K[0, j*n_virt + s + n_ex] * K[1, (i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex]

												elif ((t == s) and (u == s) and (w == s) and (v != s) and (v != t) and (v != u)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, j, j, n_occ + v] + -8 * g[i, n_occ + v, j, j] + -4 * g[i, n_occ + s, n_occ + s, n_occ + v] + 8 * g[i, n_occ + v, n_occ + s, n_occ + s] ) * K[0, j*n_virt + s + n_ex] * K[1, (i*n_virt + s) * n_ex + i*n_virt + v+ 2*n_ex]

												elif ((t == s) and (u != s) and (u != t) and (w == s) and (v == s)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * F[i, n_occ + u] + 8 * g[i, n_occ + s, n_occ + s, n_occ + u] + -4 * g[i, n_occ + u, n_occ + s, n_occ + s] + 4 * g[i, n_occ + u, j, j] + -8 * g[i, j, j, n_occ + u] ) * K[0, j*n_virt + u + n_ex] * K[1, (i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex]

												elif ((t == s) and (u != s) and (u != t) and (w == s) and (v == u)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, n_occ + u, n_occ + s, n_occ + u] ) * K[0, j*n_virt + u + n_ex] * K[1, (i*n_virt + s) * n_ex + i*n_virt + u+ 2*n_ex]

												elif ((t == s) and (u != s) and (u != t) and (w == s) and (v != s) and (v != t) and (v != u)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, n_occ + u, n_occ + s, n_occ + v] + 8 * g[i, n_occ + v, n_occ + s, n_occ + u] ) * K[0, j*n_virt + u + n_ex] * K[1, (i*n_virt + s) * n_ex + i*n_virt + v+ 2*n_ex]

												elif ((t != s) and (u == s) and (w == s) and (v == s)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, n_occ + s, n_occ + s, n_occ + t] ) * K[0, j*n_virt + s + n_ex] * K[1, (i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex]

												elif ((t != s) and (u == s) and (w == s) and (v == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * F[i, n_occ + s] + 8 * g[i, n_occ + t, n_occ + s, n_occ + t] + -4 * g[i, n_occ + s, n_occ + t, n_occ + t] + 4 * g[i, n_occ + s, j, j] + -8 * g[i, j, j, n_occ + s] ) * K[0, j*n_virt + s + n_ex] * K[1, (i*n_virt + s) * n_ex + i*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u == s) and (w == s) and (v != s) and (v != t) and (v != u)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, n_occ + s, n_occ + t, n_occ + v] + 8 * g[i, n_occ + v, n_occ + s, n_occ + t] ) * K[0, j*n_virt + s + n_ex] * K[1, (i*n_virt + s) * n_ex + i*n_virt + v+ 2*n_ex]

												elif ((t != s) and (u == t) and (w == s) and (v == s)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, j, j, n_occ + s] + -8 * g[i, n_occ + s, j, j] + -4 * g[i, n_occ + t, n_occ + s, n_occ + t] + 8 * g[i, n_occ + s, n_occ + t, n_occ + t] ) * K[0, j*n_virt + t + n_ex] * K[1, (i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex]

												elif ((t != s) and (u == t) and (w == s) and (v == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * F[i, n_occ + t] + -4 * g[i, n_occ + t, j, j] + 4 * g[i, n_occ + t, n_occ + t, n_occ + t] + -4 * g[i, j, j, n_occ + t] ) * K[0, j*n_virt + t + n_ex] * K[1, (i*n_virt + s) * n_ex + i*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u == t) and (w == s) and (v != s) and (v != t) and (v != u)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, j, j, n_occ + v] + -8 * g[i, n_occ + v, j, j] + -4 * g[i, n_occ + t, n_occ + t, n_occ + v] + 8 * g[i, n_occ + v, n_occ + t, n_occ + t] ) * K[0, j*n_virt + t + n_ex] * K[1, (i*n_virt + s) * n_ex + i*n_virt + v+ 2*n_ex]

												elif ((t != s) and (u != s) and (u != t) and (w == s) and (v == s)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (8 * g[i, n_occ + s, n_occ + t, n_occ + u] + -4 * g[i, n_occ + u, n_occ + s, n_occ + t] ) * K[0, j*n_virt + u + n_ex] * K[1, (i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex]

												elif ((t != s) and (u != s) and (u != t) and (w == s) and (v == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * F[i, n_occ + u] + 8 * g[i, n_occ + t, n_occ + t, n_occ + u] + -4 * g[i, n_occ + u, n_occ + t, n_occ + t] + 4 * g[i, n_occ + u, j, j] + -8 * g[i, j, j, n_occ + u] ) * K[0, j*n_virt + u + n_ex] * K[1, (i*n_virt + s) * n_ex + i*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u != s) and (u != t) and (w == s) and (v == u)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, n_occ + u, n_occ + t, n_occ + u] ) * K[0, j*n_virt + u + n_ex] * K[1, (i*n_virt + s) * n_ex + i*n_virt + u+ 2*n_ex]

												elif ((t != s) and (u != s) and (u != t) and (w == s) and (v != s) and (v != t) and (v != u)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, n_occ + u, n_occ + t, n_occ + v] + 8 * g[i, n_occ + v, n_occ + t, n_occ + u] ) * K[0, j*n_virt + u + n_ex] * K[1, (i*n_virt + s) * n_ex + i*n_virt + v+ 2*n_ex]

											elif ((j != i) and (k == j) and (n == i) and (m == j)):

												if ((t == s) and (u == s) and (w == s) and (v == s)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * F[j, n_occ + s] + 4 * g[i, j, i, n_occ + s] + -8 * g[j, j, j, n_occ + s] + 4 * g[i, i, j, n_occ + s] + 4 * g[j, n_occ + s, n_occ + s, n_occ + s] ) * K[0, j*n_virt + s + n_ex] * K[1, (i*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex]

												elif ((t == s) and (u == s) and (w != s) and (w != t) and (w != u) and (w != v) and (v == s)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[j, n_occ + s, n_occ + s, n_occ + w] ) * K[0, j*n_virt + s + n_ex] * K[1, (i*n_virt + w) * n_ex + j*n_virt + s+ 2*n_ex]

												elif ((t == s) and (u == s) and (w == s) and (v != s) and (v != t) and (v != u)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * F[j, n_occ + v] + 4 * g[j, n_occ + s, n_occ + s, n_occ + v] + 4 * g[j, n_occ + v, n_occ + s, n_occ + s] + -4 * g[j, j, j, n_occ + v] ) * K[0, j*n_virt + s + n_ex] * K[1, (i*n_virt + s) * n_ex + j*n_virt + v+ 2*n_ex]

												elif ((t == s) and (u != s) and (u != t) and (w == s) and (v == s)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * F[j, n_occ + u] + 8 * g[j, n_occ + s, n_occ + s, n_occ + u] + -4 * g[j, n_occ + u, n_occ + s, n_occ + s] + 8 * g[i, i, j, n_occ + u] + -4 * g[i, j, i, n_occ + u] + -4 * g[j, j, j, n_occ + u] ) * K[0, j*n_virt + u + n_ex] * K[1, (i*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex]

												elif ((t == s) and (u != s) and (u != t) and (w == u) and (v == s)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * F[j, n_occ + s] + -8 * g[j, n_occ + u, n_occ + s, n_occ + u] + 4 * g[j, n_occ + s, n_occ + u, n_occ + u] + -4 * g[i, i, j, n_occ + s] + 8 * g[i, j, i, n_occ + s] ) * K[0, j*n_virt + u + n_ex] * K[1, (i*n_virt + u) * n_ex + j*n_virt + s+ 2*n_ex]

												elif ((t == s) and (u != s) and (u != t) and (w != s) and (w != t) and (w != u) and (w != v) and (v == s)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[j, n_occ + s, n_occ + u, n_occ + w] + -8 * g[j, n_occ + u, n_occ + s, n_occ + w] ) * K[0, j*n_virt + u + n_ex] * K[1, (i*n_virt + w) * n_ex + j*n_virt + s+ 2*n_ex]

												elif ((t == s) and (u != s) and (u != t) and (w == s) and (v == u)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (8 * g[j, n_occ + u, n_occ + s, n_occ + u] ) * K[0, j*n_virt + u + n_ex] * K[1, (i*n_virt + s) * n_ex + j*n_virt + u+ 2*n_ex]

												elif ((t == s) and (u != s) and (u != t) and (w == s) and (v != s) and (v != t) and (v != u)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[j, n_occ + u, n_occ + s, n_occ + v] + 4 * g[j, n_occ + v, n_occ + s, n_occ + u] ) * K[0, j*n_virt + u + n_ex] * K[1, (i*n_virt + s) * n_ex + j*n_virt + v+ 2*n_ex]

												elif ((t != s) and (u == s) and (w == s) and (v == s)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (8 * g[j, n_occ + s, n_occ + s, n_occ + t] ) * K[0, j*n_virt + s + n_ex] * K[1, (i*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex]

												elif ((t != s) and (u == s) and (w == s) and (v == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[j, n_occ + s, n_occ + s, n_occ + s] + 4 * g[i, j, i, n_occ + s] + -4 * g[j, j, j, n_occ + s] + 4 * g[j, n_occ + s, n_occ + t, n_occ + t] + 4 * g[j, n_occ + t, n_occ + s, n_occ + t] + 4 * g[i, i, j, n_occ + s] ) * K[0, j*n_virt + s + n_ex] * K[1, (i*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u == s) and (w == t) and (v == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[j, n_occ + s, n_occ + s, n_occ + t] ) * K[0, j*n_virt + s + n_ex] * K[1, (i*n_virt + t) * n_ex + j*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u == s) and (w != s) and (w != t) and (w != u) and (w != v) and (v == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[j, n_occ + s, n_occ + s, n_occ + w] ) * K[0, j*n_virt + s + n_ex] * K[1, (i*n_virt + w) * n_ex + j*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u == s) and (w == s) and (v != s) and (v != t) and (v != u)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[j, n_occ + s, n_occ + t, n_occ + v] + 4 * g[j, n_occ + v, n_occ + s, n_occ + t] ) * K[0, j*n_virt + s + n_ex] * K[1, (i*n_virt + s) * n_ex + j*n_virt + v+ 2*n_ex]

												elif ((t != s) and (u == t) and (w == s) and (v == s)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * F[j, n_occ + s] + 4 * g[j, n_occ + t, n_occ + s, n_occ + t] + 4 * g[j, n_occ + s, n_occ + t, n_occ + t] + -4 * g[j, j, j, n_occ + s] ) * K[0, j*n_virt + t + n_ex] * K[1, (i*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex]

												elif ((t != s) and (u == t) and (w == s) and (v == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-8 * F[j, n_occ + t] + 4 * g[j, n_occ + s, n_occ + s, n_occ + t] + -8 * g[j, n_occ + t, n_occ + s, n_occ + s] + 8 * g[i, i, j, n_occ + t] + -4 * g[i, j, i, n_occ + t] + 8 * g[j, n_occ + t, n_occ + t, n_occ + t] + -8 * g[j, j, j, n_occ + t] ) * K[0, j*n_virt + t + n_ex] * K[1, (i*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u == t) and (w == t) and (v == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * F[j, n_occ + s] + -8 * g[j, n_occ + t, n_occ + s, n_occ + t] + 4 * g[j, n_occ + s, n_occ + t, n_occ + t] + -4 * g[i, i, j, n_occ + s] + 8 * g[i, j, i, n_occ + s] ) * K[0, j*n_virt + t + n_ex] * K[1, (i*n_virt + t) * n_ex + j*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u == t) and (w != s) and (w != t) and (w != u) and (w != v) and (v == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[j, n_occ + s, n_occ + t, n_occ + w] + -8 * g[j, n_occ + t, n_occ + s, n_occ + w] ) * K[0, j*n_virt + t + n_ex] * K[1, (i*n_virt + w) * n_ex + j*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u == t) and (w == s) and (v != s) and (v != t) and (v != u)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * F[j, n_occ + v] + 4 * g[j, n_occ + t, n_occ + t, n_occ + v] + 4 * g[j, n_occ + v, n_occ + t, n_occ + t] + -4 * g[j, j, j, n_occ + v] ) * K[0, j*n_virt + t + n_ex] * K[1, (i*n_virt + s) * n_ex + j*n_virt + v+ 2*n_ex]

												elif ((t != s) and (u != s) and (u != t) and (w == s) and (v == s)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[j, n_occ + u, n_occ + s, n_occ + t] + 4 * g[j, n_occ + s, n_occ + t, n_occ + u] ) * K[0, j*n_virt + u + n_ex] * K[1, (i*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex]

												elif ((t != s) and (u != s) and (u != t) and (w == s) and (v == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * F[j, n_occ + u] + 4 * g[j, n_occ + s, n_occ + s, n_occ + u] + -8 * g[j, n_occ + u, n_occ + s, n_occ + s] + 4 * g[j, n_occ + u, n_occ + t, n_occ + t] + 4 * g[j, n_occ + t, n_occ + t, n_occ + u] + 8 * g[i, i, j, n_occ + u] + -4 * g[i, j, i, n_occ + u] + -4 * g[j, j, j, n_occ + u] ) * K[0, j*n_virt + u + n_ex] * K[1, (i*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u != s) and (u != t) and (w == t) and (v == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[j, n_occ + s, n_occ + t, n_occ + u] + -8 * g[j, n_occ + u, n_occ + s, n_occ + t] ) * K[0, j*n_virt + u + n_ex] * K[1, (i*n_virt + t) * n_ex + j*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u != s) and (u != t) and (w == u) and (v == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * F[j, n_occ + s] + -8 * g[j, n_occ + u, n_occ + s, n_occ + u] + 4 * g[j, n_occ + s, n_occ + u, n_occ + u] + -4 * g[i, i, j, n_occ + s] + 8 * g[i, j, i, n_occ + s] ) * K[0, j*n_virt + u + n_ex] * K[1, (i*n_virt + u) * n_ex + j*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u != s) and (u != t) and (w != s) and (w != t) and (w != u) and (w != v) and (v == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[j, n_occ + s, n_occ + u, n_occ + w] + -8 * g[j, n_occ + u, n_occ + s, n_occ + w] ) * K[0, j*n_virt + u + n_ex] * K[1, (i*n_virt + w) * n_ex + j*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u != s) and (u != t) and (w == s) and (v == u)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (8 * g[j, n_occ + u, n_occ + t, n_occ + u] ) * K[0, j*n_virt + u + n_ex] * K[1, (i*n_virt + s) * n_ex + j*n_virt + u+ 2*n_ex]

												elif ((t != s) and (u != s) and (u != t) and (w == s) and (v != s) and (v != t) and (v != u)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[j, n_occ + u, n_occ + t, n_occ + v] + 4 * g[j, n_occ + v, n_occ + t, n_occ + u] ) * K[0, j*n_virt + u + n_ex] * K[1, (i*n_virt + s) * n_ex + j*n_virt + v+ 2*n_ex]

											elif ((j != i) and (k == j) and (n == j) and (m == j)):

												if ((t == s) and (u == s) and (w == s) and (v == s)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * F[i, n_occ + s] + -4 * g[i, n_occ + s, n_occ + s, n_occ + s] + 4 * g[i, n_occ + s, j, j] + 4 * g[i, j, j, n_occ + s] ) * K[0, j*n_virt + s + n_ex] * K[1, (j*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex]

												elif ((t == s) and (u == s) and (w != s) and (w != t) and (w != u) and (w != v) and (v == s)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, n_occ + s, n_occ + s, n_occ + w] ) * K[0, j*n_virt + s + n_ex] * K[1, (j*n_virt + w) * n_ex + j*n_virt + s+ 2*n_ex]

												elif ((t == s) and (u != s) and (u != t) and (w == s) and (v == s)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * F[i, n_occ + u] + -8 * g[i, n_occ + s, n_occ + s, n_occ + u] + 4 * g[i, n_occ + u, n_occ + s, n_occ + s] + -4 * g[i, n_occ + u, j, j] + 8 * g[i, j, j, n_occ + u] ) * K[0, j*n_virt + u + n_ex] * K[1, (j*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex]

												elif ((t == s) and (u != s) and (u != t) and (w == u) and (v == s)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, n_occ + u, n_occ + s, n_occ + u] + -8 * g[i, n_occ + s, n_occ + u, n_occ + u] + -4 * g[i, j, j, n_occ + s] + 8 * g[i, n_occ + s, j, j] ) * K[0, j*n_virt + u + n_ex] * K[1, (j*n_virt + u) * n_ex + j*n_virt + s+ 2*n_ex]

												elif ((t == s) and (u != s) and (u != t) and (w != s) and (w != t) and (w != u) and (w != v) and (v == s)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-8 * g[i, n_occ + s, n_occ + u, n_occ + w] + 4 * g[i, n_occ + u, n_occ + s, n_occ + w] ) * K[0, j*n_virt + u + n_ex] * K[1, (j*n_virt + w) * n_ex + j*n_virt + s+ 2*n_ex]

												elif ((t != s) and (u == s) and (w == s) and (v == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * F[i, n_occ + s] + -4 * g[i, n_occ + s, n_occ + s, n_occ + s] + 4 * g[i, n_occ + s, j, j] + 4 * g[i, j, j, n_occ + s] ) * K[0, j*n_virt + s + n_ex] * K[1, (j*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u == s) and (w == t) and (v == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, n_occ + s, n_occ + s, n_occ + t] ) * K[0, j*n_virt + s + n_ex] * K[1, (j*n_virt + t) * n_ex + j*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u == s) and (w != s) and (w != t) and (w != u) and (w != v) and (v == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, n_occ + s, n_occ + s, n_occ + w] ) * K[0, j*n_virt + s + n_ex] * K[1, (j*n_virt + w) * n_ex + j*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u == t) and (w == s) and (v == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * F[i, n_occ + t] + -8 * g[i, n_occ + s, n_occ + s, n_occ + t] + 4 * g[i, n_occ + t, n_occ + s, n_occ + s] + -4 * g[i, n_occ + t, j, j] + 8 * g[i, j, j, n_occ + t] ) * K[0, j*n_virt + t + n_ex] * K[1, (j*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u == t) and (w == t) and (v == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, n_occ + t, n_occ + s, n_occ + t] + -8 * g[i, n_occ + s, n_occ + t, n_occ + t] + -4 * g[i, j, j, n_occ + s] + 8 * g[i, n_occ + s, j, j] ) * K[0, j*n_virt + t + n_ex] * K[1, (j*n_virt + t) * n_ex + j*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u == t) and (w != s) and (w != t) and (w != u) and (w != v) and (v == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-8 * g[i, n_occ + s, n_occ + t, n_occ + w] + 4 * g[i, n_occ + t, n_occ + s, n_occ + w] ) * K[0, j*n_virt + t + n_ex] * K[1, (j*n_virt + w) * n_ex + j*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u != s) and (u != t) and (w == s) and (v == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * F[i, n_occ + u] + -8 * g[i, n_occ + s, n_occ + s, n_occ + u] + 4 * g[i, n_occ + u, n_occ + s, n_occ + s] + -4 * g[i, n_occ + u, j, j] + 8 * g[i, j, j, n_occ + u] ) * K[0, j*n_virt + u + n_ex] * K[1, (j*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u != s) and (u != t) and (w == t) and (v == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-8 * g[i, n_occ + s, n_occ + t, n_occ + u] + 4 * g[i, n_occ + u, n_occ + s, n_occ + t] ) * K[0, j*n_virt + u + n_ex] * K[1, (j*n_virt + t) * n_ex + j*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u != s) and (u != t) and (w == u) and (v == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, n_occ + u, n_occ + s, n_occ + u] + -8 * g[i, n_occ + s, n_occ + u, n_occ + u] + -4 * g[i, j, j, n_occ + s] + 8 * g[i, n_occ + s, j, j] ) * K[0, j*n_virt + u + n_ex] * K[1, (j*n_virt + u) * n_ex + j*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u != s) and (u != t) and (w != s) and (w != t) and (w != u) and (w != v) and (v == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-8 * g[i, n_occ + s, n_occ + u, n_occ + w] + 4 * g[i, n_occ + u, n_occ + s, n_occ + w] ) * K[0, j*n_virt + u + n_ex] * K[1, (j*n_virt + w) * n_ex + j*n_virt + t+ 2*n_ex]

											elif ((j != i) and (k == j) and (n != i) and (n != j) and (n != k) and (n != m) and (m == j)):

												if ((t == s) and (u == s) and (w == s) and (v == s)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, n, j, n_occ + s] + 4 * g[i, n_occ + s, j, n] ) * K[0, j*n_virt + s + n_ex] * K[1, (n*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex]

												elif ((t == s) and (u != s) and (u != t) and (w == s) and (v == s)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (8 * g[i, n, j, n_occ + u] + -4 * g[i, n_occ + u, j, n] ) * K[0, j*n_virt + u + n_ex] * K[1, (n*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex]

												elif ((t == s) and (u != s) and (u != t) and (w == u) and (v == s)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, n, j, n_occ + s] + 8 * g[i, n_occ + s, j, n] ) * K[0, j*n_virt + u + n_ex] * K[1, (n*n_virt + u) * n_ex + j*n_virt + s+ 2*n_ex]

												elif ((t != s) and (u == s) and (w == s) and (v == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, n, j, n_occ + s] + 4 * g[i, n_occ + s, j, n] ) * K[0, j*n_virt + s + n_ex] * K[1, (n*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u == t) and (w == s) and (v == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (8 * g[i, n, j, n_occ + t] + -4 * g[i, n_occ + t, j, n] ) * K[0, j*n_virt + t + n_ex] * K[1, (n*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u == t) and (w == t) and (v == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, n, j, n_occ + s] + 8 * g[i, n_occ + s, j, n] ) * K[0, j*n_virt + t + n_ex] * K[1, (n*n_virt + t) * n_ex + j*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u != s) and (u != t) and (w == s) and (v == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (8 * g[i, n, j, n_occ + u] + -4 * g[i, n_occ + u, j, n] ) * K[0, j*n_virt + u + n_ex] * K[1, (n*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u != s) and (u != t) and (w == u) and (v == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, n, j, n_occ + s] + 8 * g[i, n_occ + s, j, n] ) * K[0, j*n_virt + u + n_ex] * K[1, (n*n_virt + u) * n_ex + j*n_virt + t+ 2*n_ex]

											elif ((j != i) and (k == j) and (n == i) and (m != i) and (m != j) and (m != k)):

												if ((t == s) and (u == s) and (w == s) and (v == s)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * F[m, n_occ + s] + -4 * g[j, j, m, n_occ + s] + 4 * g[m, n_occ + s, n_occ + s, n_occ + s] + -4 * g[j, m, j, n_occ + s] ) * K[0, j*n_virt + s + n_ex] * K[1, (i*n_virt + s) * n_ex + m*n_virt + s+ 2*n_ex]

												elif ((t == s) and (u == s) and (w == s) and (v != s) and (v != t) and (v != u)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[j, m, j, n_occ + v] + -8 * g[j, j, m, n_occ + v] + -4 * g[m, n_occ + s, n_occ + s, n_occ + v] + 8 * g[m, n_occ + v, n_occ + s, n_occ + s] ) * K[0, j*n_virt + s + n_ex] * K[1, (i*n_virt + s) * n_ex + m*n_virt + v+ 2*n_ex]

												elif ((t == s) and (u != s) and (u != t) and (w == s) and (v == s)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * F[m, n_occ + u] + 8 * g[m, n_occ + s, n_occ + s, n_occ + u] + -4 * g[m, n_occ + u, n_occ + s, n_occ + s] + 4 * g[j, j, m, n_occ + u] + -8 * g[j, m, j, n_occ + u] ) * K[0, j*n_virt + u + n_ex] * K[1, (i*n_virt + s) * n_ex + m*n_virt + s+ 2*n_ex]

												elif ((t == s) and (u != s) and (u != t) and (w == s) and (v == u)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[m, n_occ + u, n_occ + s, n_occ + u] ) * K[0, j*n_virt + u + n_ex] * K[1, (i*n_virt + s) * n_ex + m*n_virt + u+ 2*n_ex]

												elif ((t == s) and (u != s) and (u != t) and (w == s) and (v != s) and (v != t) and (v != u)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[m, n_occ + u, n_occ + s, n_occ + v] + 8 * g[m, n_occ + v, n_occ + s, n_occ + u] ) * K[0, j*n_virt + u + n_ex] * K[1, (i*n_virt + s) * n_ex + m*n_virt + v+ 2*n_ex]

												elif ((t != s) and (u == s) and (w == s) and (v == s)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[m, n_occ + s, n_occ + s, n_occ + t] ) * K[0, j*n_virt + s + n_ex] * K[1, (i*n_virt + s) * n_ex + m*n_virt + s+ 2*n_ex]

												elif ((t != s) and (u == s) and (w == s) and (v == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * F[m, n_occ + s] + 8 * g[m, n_occ + t, n_occ + s, n_occ + t] + -4 * g[m, n_occ + s, n_occ + t, n_occ + t] + 4 * g[j, j, m, n_occ + s] + -8 * g[j, m, j, n_occ + s] ) * K[0, j*n_virt + s + n_ex] * K[1, (i*n_virt + s) * n_ex + m*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u == s) and (w == s) and (v != s) and (v != t) and (v != u)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[m, n_occ + s, n_occ + t, n_occ + v] + 8 * g[m, n_occ + v, n_occ + s, n_occ + t] ) * K[0, j*n_virt + s + n_ex] * K[1, (i*n_virt + s) * n_ex + m*n_virt + v+ 2*n_ex]

												elif ((t != s) and (u == t) and (w == s) and (v == s)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[j, m, j, n_occ + s] + -8 * g[j, j, m, n_occ + s] + -4 * g[m, n_occ + t, n_occ + s, n_occ + t] + 8 * g[m, n_occ + s, n_occ + t, n_occ + t] ) * K[0, j*n_virt + t + n_ex] * K[1, (i*n_virt + s) * n_ex + m*n_virt + s+ 2*n_ex]

												elif ((t != s) and (u == t) and (w == s) and (v == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * F[m, n_occ + t] + -4 * g[j, j, m, n_occ + t] + 4 * g[m, n_occ + t, n_occ + t, n_occ + t] + -4 * g[j, m, j, n_occ + t] ) * K[0, j*n_virt + t + n_ex] * K[1, (i*n_virt + s) * n_ex + m*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u == t) and (w == s) and (v != s) and (v != t) and (v != u)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[j, m, j, n_occ + v] + -8 * g[j, j, m, n_occ + v] + -4 * g[m, n_occ + t, n_occ + t, n_occ + v] + 8 * g[m, n_occ + v, n_occ + t, n_occ + t] ) * K[0, j*n_virt + t + n_ex] * K[1, (i*n_virt + s) * n_ex + m*n_virt + v+ 2*n_ex]

												elif ((t != s) and (u != s) and (u != t) and (w == s) and (v == s)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (8 * g[m, n_occ + s, n_occ + t, n_occ + u] + -4 * g[m, n_occ + u, n_occ + s, n_occ + t] ) * K[0, j*n_virt + u + n_ex] * K[1, (i*n_virt + s) * n_ex + m*n_virt + s+ 2*n_ex]

												elif ((t != s) and (u != s) and (u != t) and (w == s) and (v == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * F[m, n_occ + u] + 8 * g[m, n_occ + t, n_occ + t, n_occ + u] + -4 * g[m, n_occ + u, n_occ + t, n_occ + t] + 4 * g[j, j, m, n_occ + u] + -8 * g[j, m, j, n_occ + u] ) * K[0, j*n_virt + u + n_ex] * K[1, (i*n_virt + s) * n_ex + m*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u != s) and (u != t) and (w == s) and (v == u)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[m, n_occ + u, n_occ + t, n_occ + u] ) * K[0, j*n_virt + u + n_ex] * K[1, (i*n_virt + s) * n_ex + m*n_virt + u+ 2*n_ex]

												elif ((t != s) and (u != s) and (u != t) and (w == s) and (v != s) and (v != t) and (v != u)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[m, n_occ + u, n_occ + t, n_occ + v] + 8 * g[m, n_occ + v, n_occ + t, n_occ + u] ) * K[0, j*n_virt + u + n_ex] * K[1, (i*n_virt + s) * n_ex + m*n_virt + v+ 2*n_ex]

											elif ((j != i) and (k != i) and (k != j) and (n == i) and (m == i)):

												if ((t == s) and (u == s) and (w == s) and (v == s)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, j, k, n_occ + s] + -4 * g[i, n_occ + s, j, k] ) * K[0, k*n_virt + s + n_ex] * K[1, (i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex]

												elif ((t == s) and (u == s) and (w == s) and (v != s) and (v != t) and (v != u)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, j, k, n_occ + v] + -8 * g[i, n_occ + v, j, k] ) * K[0, k*n_virt + s + n_ex] * K[1, (i*n_virt + s) * n_ex + i*n_virt + v+ 2*n_ex]

												elif ((t == s) and (u != s) and (u != t) and (w == s) and (v == s)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-8 * g[i, j, k, n_occ + u] + 4 * g[i, n_occ + u, j, k] ) * K[0, k*n_virt + u + n_ex] * K[1, (i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex]

												elif ((t != s) and (u == s) and (w == s) and (v == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-8 * g[i, j, k, n_occ + s] + 4 * g[i, n_occ + s, j, k] ) * K[0, k*n_virt + s + n_ex] * K[1, (i*n_virt + s) * n_ex + i*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u == t) and (w == s) and (v == s)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, j, k, n_occ + s] + -8 * g[i, n_occ + s, j, k] ) * K[0, k*n_virt + t + n_ex] * K[1, (i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex]

												elif ((t != s) and (u == t) and (w == s) and (v == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, j, k, n_occ + t] + -4 * g[i, n_occ + t, j, k] ) * K[0, k*n_virt + t + n_ex] * K[1, (i*n_virt + s) * n_ex + i*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u == t) and (w == s) and (v != s) and (v != t) and (v != u)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, j, k, n_occ + v] + -8 * g[i, n_occ + v, j, k] ) * K[0, k*n_virt + t + n_ex] * K[1, (i*n_virt + s) * n_ex + i*n_virt + v+ 2*n_ex]

												elif ((t != s) and (u != s) and (u != t) and (w == s) and (v == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-8 * g[i, j, k, n_occ + u] + 4 * g[i, n_occ + u, j, k] ) * K[0, k*n_virt + u + n_ex] * K[1, (i*n_virt + s) * n_ex + i*n_virt + t+ 2*n_ex]

											elif ((j != i) and (k != i) and (k != j) and (n == i) and (m == j)):

												if ((t == s) and (u == s) and (w == s) and (v == s)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, k, i, n_occ + s] + -4 * g[j, j, k, n_occ + s] + -4 * g[j, k, j, n_occ + s] + 4 * g[i, i, k, n_occ + s] ) * K[0, k*n_virt + s + n_ex] * K[1, (i*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex]

												elif ((t == s) and (u == s) and (w != s) and (w != t) and (w != u) and (w != v) and (v == s)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[k, n_occ + s, n_occ + s, n_occ + w] ) * K[0, k*n_virt + s + n_ex] * K[1, (i*n_virt + w) * n_ex + j*n_virt + s+ 2*n_ex]

												elif ((t == s) and (u == s) and (w == s) and (v != s) and (v != t) and (v != u)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * F[k, n_occ + v] + 8 * g[k, n_occ + s, n_occ + s, n_occ + v] + -4 * g[k, n_occ + v, n_occ + s, n_occ + s] + 4 * g[j, j, k, n_occ + v] + -8 * g[j, k, j, n_occ + v] ) * K[0, k*n_virt + s + n_ex] * K[1, (i*n_virt + s) * n_ex + j*n_virt + v+ 2*n_ex]

												elif ((t == s) and (u != s) and (u != t) and (w == s) and (v == s)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[j, k, j, n_occ + u] + -8 * g[j, j, k, n_occ + u] + -4 * g[i, k, i, n_occ + u] + 8 * g[i, i, k, n_occ + u] ) * K[0, k*n_virt + u + n_ex] * K[1, (i*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex]

												elif ((t == s) and (u != s) and (u != t) and (w == u) and (v == s)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * F[k, n_occ + s] + -8 * g[k, n_occ + u, n_occ + s, n_occ + u] + 4 * g[k, n_occ + s, n_occ + u, n_occ + u] + -4 * g[i, i, k, n_occ + s] + 8 * g[i, k, i, n_occ + s] ) * K[0, k*n_virt + u + n_ex] * K[1, (i*n_virt + u) * n_ex + j*n_virt + s+ 2*n_ex]

												elif ((t == s) and (u != s) and (u != t) and (w != s) and (w != t) and (w != u) and (w != v) and (v == s)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[k, n_occ + s, n_occ + u, n_occ + w] + -8 * g[k, n_occ + u, n_occ + s, n_occ + w] ) * K[0, k*n_virt + u + n_ex] * K[1, (i*n_virt + w) * n_ex + j*n_virt + s+ 2*n_ex]

												elif ((t == s) and (u != s) and (u != t) and (w == s) and (v == u)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[k, n_occ + u, n_occ + s, n_occ + u] ) * K[0, k*n_virt + u + n_ex] * K[1, (i*n_virt + s) * n_ex + j*n_virt + u+ 2*n_ex]

												elif ((t == s) and (u != s) and (u != t) and (w == s) and (v != s) and (v != t) and (v != u)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (8 * g[k, n_occ + u, n_occ + s, n_occ + v] + -4 * g[k, n_occ + v, n_occ + s, n_occ + u] ) * K[0, k*n_virt + u + n_ex] * K[1, (i*n_virt + s) * n_ex + j*n_virt + v+ 2*n_ex]

												elif ((t != s) and (u == s) and (w == s) and (v == s)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[k, n_occ + s, n_occ + s, n_occ + t] ) * K[0, k*n_virt + s + n_ex] * K[1, (i*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex]

												elif ((t != s) and (u == s) and (w == s) and (v == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * F[k, n_occ + s] + -4 * g[k, n_occ + s, n_occ + s, n_occ + s] + -4 * g[k, n_occ + t, n_occ + s, n_occ + t] + 8 * g[k, n_occ + s, n_occ + t, n_occ + t] + 4 * g[i, i, k, n_occ + s] + 4 * g[i, k, i, n_occ + s] + -8 * g[j, j, k, n_occ + s] + 4 * g[j, k, j, n_occ + s] ) * K[0, k*n_virt + s + n_ex] * K[1, (i*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u == s) and (w == t) and (v == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[k, n_occ + s, n_occ + s, n_occ + t] ) * K[0, k*n_virt + s + n_ex] * K[1, (i*n_virt + t) * n_ex + j*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u == s) and (w != s) and (w != t) and (w != u) and (w != v) and (v == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[k, n_occ + s, n_occ + s, n_occ + w] ) * K[0, k*n_virt + s + n_ex] * K[1, (i*n_virt + w) * n_ex + j*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u == s) and (w == s) and (v != s) and (v != t) and (v != u)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (8 * g[k, n_occ + s, n_occ + t, n_occ + v] + -4 * g[k, n_occ + v, n_occ + s, n_occ + t] ) * K[0, k*n_virt + s + n_ex] * K[1, (i*n_virt + s) * n_ex + j*n_virt + v+ 2*n_ex]

												elif ((t != s) and (u == t) and (w == s) and (v == s)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * F[k, n_occ + s] + 8 * g[k, n_occ + t, n_occ + s, n_occ + t] + -4 * g[k, n_occ + s, n_occ + t, n_occ + t] + 4 * g[j, j, k, n_occ + s] + -8 * g[j, k, j, n_occ + s] ) * K[0, k*n_virt + t + n_ex] * K[1, (i*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex]

												elif ((t != s) and (u == t) and (w == s) and (v == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * F[k, n_occ + t] + 4 * g[k, n_occ + s, n_occ + s, n_occ + t] + -8 * g[k, n_occ + t, n_occ + s, n_occ + s] + -4 * g[j, j, k, n_occ + t] + 4 * g[k, n_occ + t, n_occ + t, n_occ + t] + 8 * g[i, i, k, n_occ + t] + -4 * g[i, k, i, n_occ + t] + -4 * g[j, k, j, n_occ + t] ) * K[0, k*n_virt + t + n_ex] * K[1, (i*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u == t) and (w == t) and (v == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * F[k, n_occ + s] + -8 * g[k, n_occ + t, n_occ + s, n_occ + t] + 4 * g[k, n_occ + s, n_occ + t, n_occ + t] + -4 * g[i, i, k, n_occ + s] + 8 * g[i, k, i, n_occ + s] ) * K[0, k*n_virt + t + n_ex] * K[1, (i*n_virt + t) * n_ex + j*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u == t) and (w != s) and (w != t) and (w != u) and (w != v) and (v == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[k, n_occ + s, n_occ + t, n_occ + w] + -8 * g[k, n_occ + t, n_occ + s, n_occ + w] ) * K[0, k*n_virt + t + n_ex] * K[1, (i*n_virt + w) * n_ex + j*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u == t) and (w == s) and (v != s) and (v != t) and (v != u)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * F[k, n_occ + v] + 8 * g[k, n_occ + t, n_occ + t, n_occ + v] + -4 * g[k, n_occ + v, n_occ + t, n_occ + t] + 4 * g[j, j, k, n_occ + v] + -8 * g[j, k, j, n_occ + v] ) * K[0, k*n_virt + t + n_ex] * K[1, (i*n_virt + s) * n_ex + j*n_virt + v+ 2*n_ex]

												elif ((t != s) and (u != s) and (u != t) and (w == s) and (v == s)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[k, n_occ + s, n_occ + t, n_occ + u] + 8 * g[k, n_occ + u, n_occ + s, n_occ + t] ) * K[0, k*n_virt + u + n_ex] * K[1, (i*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex]

												elif ((t != s) and (u != s) and (u != t) and (w == s) and (v == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[k, n_occ + s, n_occ + s, n_occ + u] + -8 * g[k, n_occ + u, n_occ + s, n_occ + s] + 4 * g[j, k, j, n_occ + u] + -8 * g[j, j, k, n_occ + u] + -4 * g[k, n_occ + t, n_occ + t, n_occ + u] + 8 * g[k, n_occ + u, n_occ + t, n_occ + t] + -4 * g[i, k, i, n_occ + u] + 8 * g[i, i, k, n_occ + u] ) * K[0, k*n_virt + u + n_ex] * K[1, (i*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u != s) and (u != t) and (w == t) and (v == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[k, n_occ + s, n_occ + t, n_occ + u] + -8 * g[k, n_occ + u, n_occ + s, n_occ + t] ) * K[0, k*n_virt + u + n_ex] * K[1, (i*n_virt + t) * n_ex + j*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u != s) and (u != t) and (w == u) and (v == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * F[k, n_occ + s] + -8 * g[k, n_occ + u, n_occ + s, n_occ + u] + 4 * g[k, n_occ + s, n_occ + u, n_occ + u] + -4 * g[i, i, k, n_occ + s] + 8 * g[i, k, i, n_occ + s] ) * K[0, k*n_virt + u + n_ex] * K[1, (i*n_virt + u) * n_ex + j*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u != s) and (u != t) and (w != s) and (w != t) and (w != u) and (w != v) and (v == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[k, n_occ + s, n_occ + u, n_occ + w] + -8 * g[k, n_occ + u, n_occ + s, n_occ + w] ) * K[0, k*n_virt + u + n_ex] * K[1, (i*n_virt + w) * n_ex + j*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u != s) and (u != t) and (w == s) and (v == u)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[k, n_occ + u, n_occ + t, n_occ + u] ) * K[0, k*n_virt + u + n_ex] * K[1, (i*n_virt + s) * n_ex + j*n_virt + u+ 2*n_ex]

												elif ((t != s) and (u != s) and (u != t) and (w == s) and (v != s) and (v != t) and (v != u)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (8 * g[k, n_occ + u, n_occ + t, n_occ + v] + -4 * g[k, n_occ + v, n_occ + t, n_occ + u] ) * K[0, k*n_virt + u + n_ex] * K[1, (i*n_virt + s) * n_ex + j*n_virt + v+ 2*n_ex]

											elif ((j != i) and (k != i) and (k != j) and (n == j) and (m == j)):

												if ((t == s) and (u == s) and (w == s) and (v == s)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, j, k, n_occ + s] + 4 * g[i, n_occ + s, j, k] ) * K[0, k*n_virt + s + n_ex] * K[1, (j*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex]

												elif ((t == s) and (u != s) and (u != t) and (w == s) and (v == s)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (8 * g[i, j, k, n_occ + u] + -4 * g[i, n_occ + u, j, k] ) * K[0, k*n_virt + u + n_ex] * K[1, (j*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex]

												elif ((t == s) and (u != s) and (u != t) and (w == u) and (v == s)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, j, k, n_occ + s] + 8 * g[i, n_occ + s, j, k] ) * K[0, k*n_virt + u + n_ex] * K[1, (j*n_virt + u) * n_ex + j*n_virt + s+ 2*n_ex]

												elif ((t != s) and (u == s) and (w == s) and (v == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, j, k, n_occ + s] + 4 * g[i, n_occ + s, j, k] ) * K[0, k*n_virt + s + n_ex] * K[1, (j*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u == t) and (w == s) and (v == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (8 * g[i, j, k, n_occ + t] + -4 * g[i, n_occ + t, j, k] ) * K[0, k*n_virt + t + n_ex] * K[1, (j*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u == t) and (w == t) and (v == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, j, k, n_occ + s] + 8 * g[i, n_occ + s, j, k] ) * K[0, k*n_virt + t + n_ex] * K[1, (j*n_virt + t) * n_ex + j*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u != s) and (u != t) and (w == s) and (v == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (8 * g[i, j, k, n_occ + u] + -4 * g[i, n_occ + u, j, k] ) * K[0, k*n_virt + u + n_ex] * K[1, (j*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u != s) and (u != t) and (w == u) and (v == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, j, k, n_occ + s] + 8 * g[i, n_occ + s, j, k] ) * K[0, k*n_virt + u + n_ex] * K[1, (j*n_virt + u) * n_ex + j*n_virt + t+ 2*n_ex]

											elif ((j != i) and (k != i) and (k != j) and (n == k) and (m == j)):

												if ((t == s) and (u == s) and (w == s) and (v == s)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * F[i, n_occ + s] + -4 * g[i, n_occ + s, n_occ + s, n_occ + s] + 4 * g[i, n_occ + s, k, k] + 4 * g[i, k, k, n_occ + s] ) * K[0, k*n_virt + s + n_ex] * K[1, (k*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex]

												elif ((t == s) and (u == s) and (w != s) and (w != t) and (w != u) and (w != v) and (v == s)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, n_occ + s, n_occ + s, n_occ + w] ) * K[0, k*n_virt + s + n_ex] * K[1, (k*n_virt + w) * n_ex + j*n_virt + s+ 2*n_ex]

												elif ((t == s) and (u != s) and (u != t) and (w == s) and (v == s)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * F[i, n_occ + u] + -8 * g[i, n_occ + s, n_occ + s, n_occ + u] + 4 * g[i, n_occ + u, n_occ + s, n_occ + s] + -4 * g[i, n_occ + u, k, k] + 8 * g[i, k, k, n_occ + u] ) * K[0, k*n_virt + u + n_ex] * K[1, (k*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex]

												elif ((t == s) and (u != s) and (u != t) and (w == u) and (v == s)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, n_occ + u, n_occ + s, n_occ + u] + -8 * g[i, n_occ + s, n_occ + u, n_occ + u] + -4 * g[i, k, k, n_occ + s] + 8 * g[i, n_occ + s, k, k] ) * K[0, k*n_virt + u + n_ex] * K[1, (k*n_virt + u) * n_ex + j*n_virt + s+ 2*n_ex]

												elif ((t == s) and (u != s) and (u != t) and (w != s) and (w != t) and (w != u) and (w != v) and (v == s)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-8 * g[i, n_occ + s, n_occ + u, n_occ + w] + 4 * g[i, n_occ + u, n_occ + s, n_occ + w] ) * K[0, k*n_virt + u + n_ex] * K[1, (k*n_virt + w) * n_ex + j*n_virt + s+ 2*n_ex]

												elif ((t != s) and (u == s) and (w == s) and (v == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * F[i, n_occ + s] + -4 * g[i, n_occ + s, n_occ + s, n_occ + s] + 4 * g[i, n_occ + s, k, k] + 4 * g[i, k, k, n_occ + s] ) * K[0, k*n_virt + s + n_ex] * K[1, (k*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u == s) and (w == t) and (v == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, n_occ + s, n_occ + s, n_occ + t] ) * K[0, k*n_virt + s + n_ex] * K[1, (k*n_virt + t) * n_ex + j*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u == s) and (w != s) and (w != t) and (w != u) and (w != v) and (v == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, n_occ + s, n_occ + s, n_occ + w] ) * K[0, k*n_virt + s + n_ex] * K[1, (k*n_virt + w) * n_ex + j*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u == t) and (w == s) and (v == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * F[i, n_occ + t] + -8 * g[i, n_occ + s, n_occ + s, n_occ + t] + 4 * g[i, n_occ + t, n_occ + s, n_occ + s] + -4 * g[i, n_occ + t, k, k] + 8 * g[i, k, k, n_occ + t] ) * K[0, k*n_virt + t + n_ex] * K[1, (k*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u == t) and (w == t) and (v == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, n_occ + t, n_occ + s, n_occ + t] + -8 * g[i, n_occ + s, n_occ + t, n_occ + t] + -4 * g[i, k, k, n_occ + s] + 8 * g[i, n_occ + s, k, k] ) * K[0, k*n_virt + t + n_ex] * K[1, (k*n_virt + t) * n_ex + j*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u == t) and (w != s) and (w != t) and (w != u) and (w != v) and (v == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-8 * g[i, n_occ + s, n_occ + t, n_occ + w] + 4 * g[i, n_occ + t, n_occ + s, n_occ + w] ) * K[0, k*n_virt + t + n_ex] * K[1, (k*n_virt + w) * n_ex + j*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u != s) and (u != t) and (w == s) and (v == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * F[i, n_occ + u] + -8 * g[i, n_occ + s, n_occ + s, n_occ + u] + 4 * g[i, n_occ + u, n_occ + s, n_occ + s] + -4 * g[i, n_occ + u, k, k] + 8 * g[i, k, k, n_occ + u] ) * K[0, k*n_virt + u + n_ex] * K[1, (k*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u != s) and (u != t) and (w == t) and (v == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-8 * g[i, n_occ + s, n_occ + t, n_occ + u] + 4 * g[i, n_occ + u, n_occ + s, n_occ + t] ) * K[0, k*n_virt + u + n_ex] * K[1, (k*n_virt + t) * n_ex + j*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u != s) and (u != t) and (w == u) and (v == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, n_occ + u, n_occ + s, n_occ + u] + -8 * g[i, n_occ + s, n_occ + u, n_occ + u] + -4 * g[i, k, k, n_occ + s] + 8 * g[i, n_occ + s, k, k] ) * K[0, k*n_virt + u + n_ex] * K[1, (k*n_virt + u) * n_ex + j*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u != s) and (u != t) and (w != s) and (w != t) and (w != u) and (w != v) and (v == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-8 * g[i, n_occ + s, n_occ + u, n_occ + w] + 4 * g[i, n_occ + u, n_occ + s, n_occ + w] ) * K[0, k*n_virt + u + n_ex] * K[1, (k*n_virt + w) * n_ex + j*n_virt + t+ 2*n_ex]

											elif ((j != i) and (k != i) and (k != j) and (n != i) and (n != j) and (n != k) and (n != m) and (m == j)):

												if ((t == s) and (u == s) and (w == s) and (v == s)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, n, k, n_occ + s] + 4 * g[i, n_occ + s, k, n] ) * K[0, k*n_virt + s + n_ex] * K[1, (n*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex]

												elif ((t == s) and (u != s) and (u != t) and (w == s) and (v == s)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (8 * g[i, n, k, n_occ + u] + -4 * g[i, n_occ + u, k, n] ) * K[0, k*n_virt + u + n_ex] * K[1, (n*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex]

												elif ((t == s) and (u != s) and (u != t) and (w == u) and (v == s)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, n, k, n_occ + s] + 8 * g[i, n_occ + s, k, n] ) * K[0, k*n_virt + u + n_ex] * K[1, (n*n_virt + u) * n_ex + j*n_virt + s+ 2*n_ex]

												elif ((t != s) and (u == s) and (w == s) and (v == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, n, k, n_occ + s] + 4 * g[i, n_occ + s, k, n] ) * K[0, k*n_virt + s + n_ex] * K[1, (n*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u == t) and (w == s) and (v == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (8 * g[i, n, k, n_occ + t] + -4 * g[i, n_occ + t, k, n] ) * K[0, k*n_virt + t + n_ex] * K[1, (n*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u == t) and (w == t) and (v == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, n, k, n_occ + s] + 8 * g[i, n_occ + s, k, n] ) * K[0, k*n_virt + t + n_ex] * K[1, (n*n_virt + t) * n_ex + j*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u != s) and (u != t) and (w == s) and (v == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (8 * g[i, n, k, n_occ + u] + -4 * g[i, n_occ + u, k, n] ) * K[0, k*n_virt + u + n_ex] * K[1, (n*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u != s) and (u != t) and (w == u) and (v == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, n, k, n_occ + s] + 8 * g[i, n_occ + s, k, n] ) * K[0, k*n_virt + u + n_ex] * K[1, (n*n_virt + u) * n_ex + j*n_virt + t+ 2*n_ex]

											elif ((j != i) and (k != i) and (k != j) and (n == i) and (m == k)):

												if ((t == s) and (u == s) and (w == s) and (v == s)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-8 * g[j, k, k, n_occ + s] ) * K[0, k*n_virt + s + n_ex] * K[1, (i*n_virt + s) * n_ex + k*n_virt + s+ 2*n_ex]

												elif ((t == s) and (u == s) and (w == s) and (v != s) and (v != t) and (v != u)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[j, k, k, n_occ + v] ) * K[0, k*n_virt + s + n_ex] * K[1, (i*n_virt + s) * n_ex + k*n_virt + v+ 2*n_ex]

												elif ((t == s) and (u != s) and (u != t) and (w == s) and (v == s)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[j, k, k, n_occ + u] ) * K[0, k*n_virt + u + n_ex] * K[1, (i*n_virt + s) * n_ex + k*n_virt + s+ 2*n_ex]

												elif ((t != s) and (u == s) and (w == s) and (v == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[j, k, k, n_occ + s] ) * K[0, k*n_virt + s + n_ex] * K[1, (i*n_virt + s) * n_ex + k*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u == t) and (w == s) and (v == s)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[j, k, k, n_occ + s] ) * K[0, k*n_virt + t + n_ex] * K[1, (i*n_virt + s) * n_ex + k*n_virt + s+ 2*n_ex]

												elif ((t != s) and (u == t) and (w == s) and (v == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-8 * g[j, k, k, n_occ + t] ) * K[0, k*n_virt + t + n_ex] * K[1, (i*n_virt + s) * n_ex + k*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u == t) and (w == s) and (v != s) and (v != t) and (v != u)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[j, k, k, n_occ + v] ) * K[0, k*n_virt + t + n_ex] * K[1, (i*n_virt + s) * n_ex + k*n_virt + v+ 2*n_ex]

												elif ((t != s) and (u != s) and (u != t) and (w == s) and (v == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[j, k, k, n_occ + u] ) * K[0, k*n_virt + u + n_ex] * K[1, (i*n_virt + s) * n_ex + k*n_virt + t+ 2*n_ex]

											elif ((j != i) and (k != i) and (k != j) and (n == i) and (m != i) and (m != j) and (m != k)):

												if ((t == s) and (u == s) and (w == s) and (v == s)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[j, m, k, n_occ + s] + -4 * g[j, k, m, n_occ + s] ) * K[0, k*n_virt + s + n_ex] * K[1, (i*n_virt + s) * n_ex + m*n_virt + s+ 2*n_ex]

												elif ((t == s) and (u == s) and (w == s) and (v != s) and (v != t) and (v != u)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-8 * g[j, k, m, n_occ + v] + 4 * g[j, m, k, n_occ + v] ) * K[0, k*n_virt + s + n_ex] * K[1, (i*n_virt + s) * n_ex + m*n_virt + v+ 2*n_ex]

												elif ((t == s) and (u != s) and (u != t) and (w == s) and (v == s)):

													L3[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[j, k, m, n_occ + u] + -8 * g[j, m, k, n_occ + u] ) * K[0, k*n_virt + u + n_ex] * K[1, (i*n_virt + s) * n_ex + m*n_virt + s+ 2*n_ex]

												elif ((t != s) and (u == s) and (w == s) and (v == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[j, k, m, n_occ + s] + -8 * g[j, m, k, n_occ + s] ) * K[0, k*n_virt + s + n_ex] * K[1, (i*n_virt + s) * n_ex + m*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u == t) and (w == s) and (v == s)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-8 * g[j, k, m, n_occ + s] + 4 * g[j, m, k, n_occ + s] ) * K[0, k*n_virt + t + n_ex] * K[1, (i*n_virt + s) * n_ex + m*n_virt + s+ 2*n_ex]

												elif ((t != s) and (u == t) and (w == s) and (v == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[j, m, k, n_occ + t] + -4 * g[j, k, m, n_occ + t] ) * K[0, k*n_virt + t + n_ex] * K[1, (i*n_virt + s) * n_ex + m*n_virt + t+ 2*n_ex]

												elif ((t != s) and (u == t) and (w == s) and (v != s) and (v != t) and (v != u)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-8 * g[j, k, m, n_occ + v] + 4 * g[j, m, k, n_occ + v] ) * K[0, k*n_virt + t + n_ex] * K[1, (i*n_virt + s) * n_ex + m*n_virt + v+ 2*n_ex]

												elif ((t != s) and (u != s) and (u != t) and (w == s) and (v == t)):

													L3[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[j, k, m, n_occ + u] + -8 * g[j, m, k, n_occ + u] ) * K[0, k*n_virt + u + n_ex] * K[1, (i*n_virt + s) * n_ex + m*n_virt + t+ 2*n_ex]

	# This operator combination: {'a': 3, 'b': 3, 'c': 1}
	for i in range(n_occ):
		for k in range(n_occ):
			for j in range(n_occ):
				for n in range(n_occ):
					for m in range(n_occ):
						for s in range(n_virt):
							for u in range(n_virt):
								for t in range(n_virt):
									for w in range(n_virt):
										for v in range(n_virt):

											if ((k == i) and (j == i) and (n == i) and (m == i)):

												if ((u == s) and (t == s) and (w == s) and (v == s)):

													L3[i*n_virt + s] += (-16 * g[i, i, i, n_occ + s] + 16 * g[i, n_occ + s, n_occ + s, n_occ + s] ) * K[0, (i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] * K[1, (i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex]

												elif ((u == s) and (t == s) and (w != s) and (w != t) and (w != u) and (w != v) and (v == s)):

													L3[i*n_virt + s] += (-4 * g[i, i, i, n_occ + w] + 4 * g[i, n_occ + w, n_occ + s, n_occ + s] + 4 * g[i, n_occ + s, n_occ + s, n_occ + w] ) * K[0, (i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] * K[1, (i*n_virt + w) * n_ex + i*n_virt + s+ 2*n_ex]

												elif ((u == s) and (t == s) and (w == s) and (v != s) and (v != t) and (v != u)):

													L3[i*n_virt + s] += (8 * g[i, n_occ + s, n_occ + s, n_occ + v] ) * K[0, (i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] * K[1, (i*n_virt + s) * n_ex + i*n_virt + v+ 2*n_ex]

												elif ((u != s) and (u != t) and (t == s) and (w == s) and (v == s)):

													L3[i*n_virt + s] += (4 * F[i, n_occ + u] + 4 * g[i, n_occ + u, n_occ + s, n_occ + s] + 4 * g[i, n_occ + s, n_occ + s, n_occ + u] + -4 * g[i, i, i, n_occ + u] ) * K[0, (i*n_virt + u) * n_ex + i*n_virt + s+ 2*n_ex] * K[1, (i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex]

												elif ((u != s) and (u != t) and (t == s) and (w == s) and (v == u)):

													L3[i*n_virt + s] += (-4 * F[i, n_occ + s] + -12 * g[i, i, i, n_occ + s] + 4 * g[i, n_occ + u, n_occ + s, n_occ + u] + 4 * g[i, n_occ + s, n_occ + u, n_occ + u] + 8 * g[i, n_occ + s, n_occ + s, n_occ + s] ) * K[0, (i*n_virt + u) * n_ex + i*n_virt + s+ 2*n_ex] * K[1, (i*n_virt + s) * n_ex + i*n_virt + u+ 2*n_ex]

												elif ((u != s) and (u != t) and (t == s) and (w == u) and (v == u)):

													L3[i*n_virt + s] += (-4 * g[i, i, i, n_occ + u] + 4 * g[i, n_occ + u, n_occ + s, n_occ + s] + 4 * g[i, n_occ + s, n_occ + s, n_occ + u] ) * K[0, (i*n_virt + u) * n_ex + i*n_virt + s+ 2*n_ex] * K[1, (i*n_virt + u) * n_ex + i*n_virt + u+ 2*n_ex]

												elif ((u != s) and (u != t) and (t == s) and (w != s) and (w != t) and (w != u) and (w != v) and (v == u)):

													L3[i*n_virt + s] += (-4 * g[i, i, i, n_occ + w] + 4 * g[i, n_occ + w, n_occ + s, n_occ + s] + 4 * g[i, n_occ + s, n_occ + s, n_occ + w] ) * K[0, (i*n_virt + u) * n_ex + i*n_virt + s+ 2*n_ex] * K[1, (i*n_virt + w) * n_ex + i*n_virt + u+ 2*n_ex]

												elif ((u != s) and (u != t) and (t == s) and (w == s) and (v != s) and (v != t) and (v != u)):

													L3[i*n_virt + s] += (4 * g[i, n_occ + u, n_occ + s, n_occ + v] + 4 * g[i, n_occ + s, n_occ + u, n_occ + v] ) * K[0, (i*n_virt + u) * n_ex + i*n_virt + s+ 2*n_ex] * K[1, (i*n_virt + s) * n_ex + i*n_virt + v+ 2*n_ex]

												elif ((u == s) and (t != s) and (w == s) and (v == s)):

													L3[i*n_virt + s] += (8 * g[i, n_occ + s, n_occ + s, n_occ + t] ) * K[0, (i*n_virt + s) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, (i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex]

												elif ((u == s) and (t != s) and (w == t) and (v == s)):

													L3[i*n_virt + s] += (-12 * g[i, i, i, n_occ + s] + 8 * g[i, n_occ + s, n_occ + s, n_occ + s] + 4 * g[i, n_occ + t, n_occ + s, n_occ + t] + 4 * g[i, n_occ + s, n_occ + t, n_occ + t] ) * K[0, (i*n_virt + s) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, (i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex]

												elif ((u == s) and (t != s) and (w != s) and (w != t) and (w != u) and (w != v) and (v == s)):

													L3[i*n_virt + s] += (4 * g[i, n_occ + w, n_occ + s, n_occ + t] + 4 * g[i, n_occ + s, n_occ + t, n_occ + w] ) * K[0, (i*n_virt + s) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, (i*n_virt + w) * n_ex + i*n_virt + s+ 2*n_ex]

												elif ((u == s) and (t != s) and (w == t) and (v == t)):

													L3[i*n_virt + s] += (8 * g[i, n_occ + s, n_occ + s, n_occ + t] ) * K[0, (i*n_virt + s) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, (i*n_virt + t) * n_ex + i*n_virt + t+ 2*n_ex]

												elif ((u == s) and (t != s) and (w == t) and (v != s) and (v != t) and (v != u)):

													L3[i*n_virt + s] += (8 * g[i, n_occ + s, n_occ + s, n_occ + v] ) * K[0, (i*n_virt + s) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, (i*n_virt + t) * n_ex + i*n_virt + v+ 2*n_ex]

												elif ((u == t) and (t != s) and (w == t) and (v == s)):

													L3[i*n_virt + s] += (4 * F[i, n_occ + t] + 4 * g[i, n_occ + t, n_occ + s, n_occ + s] + 4 * g[i, n_occ + s, n_occ + s, n_occ + t] + -4 * g[i, i, i, n_occ + t] ) * K[0, (i*n_virt + t) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, (i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex]

												elif ((u == t) and (t != s) and (w == s) and (v == t)):

													L3[i*n_virt + s] += (8 * g[i, n_occ + s, n_occ + s, n_occ + t] ) * K[0, (i*n_virt + t) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, (i*n_virt + s) * n_ex + i*n_virt + t+ 2*n_ex]

												elif ((u == t) and (t != s) and (w == t) and (v == t)):

													L3[i*n_virt + s] += (-4 * F[i, n_occ + s] + -8 * g[i, i, i, n_occ + s] + 8 * g[i, n_occ + t, n_occ + s, n_occ + t] + 8 * g[i, n_occ + s, n_occ + t, n_occ + t] ) * K[0, (i*n_virt + t) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, (i*n_virt + t) * n_ex + i*n_virt + t+ 2*n_ex]

												elif ((u == t) and (t != s) and (w != s) and (w != t) and (w != u) and (w != v) and (v == t)):

													L3[i*n_virt + s] += (4 * g[i, n_occ + w, n_occ + s, n_occ + t] + 4 * g[i, n_occ + s, n_occ + t, n_occ + w] ) * K[0, (i*n_virt + t) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, (i*n_virt + w) * n_ex + i*n_virt + t+ 2*n_ex]

												elif ((u == t) and (t != s) and (w == t) and (v != s) and (v != t) and (v != u)):

													L3[i*n_virt + s] += (4 * g[i, n_occ + t, n_occ + s, n_occ + v] + 4 * g[i, n_occ + s, n_occ + t, n_occ + v] ) * K[0, (i*n_virt + t) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, (i*n_virt + t) * n_ex + i*n_virt + v+ 2*n_ex]

												elif ((u != s) and (u != t) and (t != s) and (w == t) and (v == s)):

													L3[i*n_virt + s] += (4 * F[i, n_occ + u] + 4 * g[i, n_occ + u, n_occ + s, n_occ + s] + 4 * g[i, n_occ + s, n_occ + s, n_occ + u] + -4 * g[i, i, i, n_occ + u] ) * K[0, (i*n_virt + u) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, (i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex]

												elif ((u != s) and (u != t) and (t != s) and (w == t) and (v == t)):

													L3[i*n_virt + s] += (4 * g[i, n_occ + u, n_occ + s, n_occ + t] + 4 * g[i, n_occ + s, n_occ + t, n_occ + u] ) * K[0, (i*n_virt + u) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, (i*n_virt + t) * n_ex + i*n_virt + t+ 2*n_ex]

												elif ((u != s) and (u != t) and (t != s) and (w == s) and (v == u)):

													L3[i*n_virt + s] += (8 * g[i, n_occ + s, n_occ + s, n_occ + t] ) * K[0, (i*n_virt + u) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, (i*n_virt + s) * n_ex + i*n_virt + u+ 2*n_ex]

												elif ((u != s) and (u != t) and (t != s) and (w == t) and (v == u)):

													L3[i*n_virt + s] += (-4 * F[i, n_occ + s] + -8 * g[i, i, i, n_occ + s] + 4 * g[i, n_occ + u, n_occ + s, n_occ + u] + 4 * g[i, n_occ + s, n_occ + u, n_occ + u] + 4 * g[i, n_occ + t, n_occ + s, n_occ + t] + 4 * g[i, n_occ + s, n_occ + t, n_occ + t] ) * K[0, (i*n_virt + u) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, (i*n_virt + t) * n_ex + i*n_virt + u+ 2*n_ex]

												elif ((u != s) and (u != t) and (t != s) and (w == u) and (v == u)):

													L3[i*n_virt + s] += (4 * g[i, n_occ + u, n_occ + s, n_occ + t] + 4 * g[i, n_occ + s, n_occ + t, n_occ + u] ) * K[0, (i*n_virt + u) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, (i*n_virt + u) * n_ex + i*n_virt + u+ 2*n_ex]

												elif ((u != s) and (u != t) and (t != s) and (w != s) and (w != t) and (w != u) and (w != v) and (v == u)):

													L3[i*n_virt + s] += (4 * g[i, n_occ + w, n_occ + s, n_occ + t] + 4 * g[i, n_occ + s, n_occ + t, n_occ + w] ) * K[0, (i*n_virt + u) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, (i*n_virt + w) * n_ex + i*n_virt + u+ 2*n_ex]

												elif ((u != s) and (u != t) and (t != s) and (w == t) and (v != s) and (v != t) and (v != u)):

													L3[i*n_virt + s] += (4 * g[i, n_occ + u, n_occ + s, n_occ + v] + 4 * g[i, n_occ + s, n_occ + u, n_occ + v] ) * K[0, (i*n_virt + u) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, (i*n_virt + t) * n_ex + i*n_virt + v+ 2*n_ex]

											elif ((k == i) and (j == i) and (n != i) and (n != j) and (n != k) and (n != m) and (m == i)):

												if ((u == s) and (t == s) and (w == s) and (v == s)):

													L3[i*n_virt + s] += (-4 * g[i, i, n, n_occ + s] + 4 * g[n, n_occ + s, n_occ + s, n_occ + s] + -4 * g[i, n, i, n_occ + s] ) * K[0, (i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] * K[1, (n*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex]

												elif ((u == s) and (t == s) and (w != s) and (w != t) and (w != u) and (w != v) and (v == s)):

													L3[i*n_virt + s] += (4 * g[i, n, i, n_occ + w] + -8 * g[i, i, n, n_occ + w] + -4 * g[n, n_occ + s, n_occ + s, n_occ + w] + 8 * g[n, n_occ + w, n_occ + s, n_occ + s] ) * K[0, (i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] * K[1, (n*n_virt + w) * n_ex + i*n_virt + s+ 2*n_ex]

												elif ((u != s) and (u != t) and (t == s) and (w == s) and (v == u)):

													L3[i*n_virt + s] += (-4 * g[i, i, n, n_occ + s] + 4 * g[n, n_occ + s, n_occ + s, n_occ + s] + -4 * g[i, n, i, n_occ + s] ) * K[0, (i*n_virt + u) * n_ex + i*n_virt + s+ 2*n_ex] * K[1, (n*n_virt + s) * n_ex + i*n_virt + u+ 2*n_ex]

												elif ((u != s) and (u != t) and (t == s) and (w == u) and (v == u)):

													L3[i*n_virt + s] += (4 * g[i, n, i, n_occ + u] + -8 * g[i, i, n, n_occ + u] + -4 * g[n, n_occ + s, n_occ + s, n_occ + u] + 8 * g[n, n_occ + u, n_occ + s, n_occ + s] ) * K[0, (i*n_virt + u) * n_ex + i*n_virt + s+ 2*n_ex] * K[1, (n*n_virt + u) * n_ex + i*n_virt + u+ 2*n_ex]

												elif ((u != s) and (u != t) and (t == s) and (w != s) and (w != t) and (w != u) and (w != v) and (v == u)):

													L3[i*n_virt + s] += (4 * g[i, n, i, n_occ + w] + -8 * g[i, i, n, n_occ + w] + -4 * g[n, n_occ + s, n_occ + s, n_occ + w] + 8 * g[n, n_occ + w, n_occ + s, n_occ + s] ) * K[0, (i*n_virt + u) * n_ex + i*n_virt + s+ 2*n_ex] * K[1, (n*n_virt + w) * n_ex + i*n_virt + u+ 2*n_ex]

												elif ((u == s) and (t != s) and (w == s) and (v == s)):

													L3[i*n_virt + s] += (4 * g[n, n_occ + s, n_occ + s, n_occ + t] ) * K[0, (i*n_virt + s) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, (n*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex]

												elif ((u == s) and (t != s) and (w == t) and (v == s)):

													L3[i*n_virt + s] += (-8 * g[i, n, i, n_occ + s] + 4 * g[i, i, n, n_occ + s] + 8 * g[n, n_occ + t, n_occ + s, n_occ + t] + -4 * g[n, n_occ + s, n_occ + t, n_occ + t] ) * K[0, (i*n_virt + s) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, (n*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex]

												elif ((u == s) and (t != s) and (w != s) and (w != t) and (w != u) and (w != v) and (v == s)):

													L3[i*n_virt + s] += (-4 * g[n, n_occ + s, n_occ + t, n_occ + w] + 8 * g[n, n_occ + w, n_occ + s, n_occ + t] ) * K[0, (i*n_virt + s) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, (n*n_virt + w) * n_ex + i*n_virt + s+ 2*n_ex]

												elif ((u == t) and (t != s) and (w == s) and (v == t)):

													L3[i*n_virt + s] += (4 * g[n, n_occ + s, n_occ + s, n_occ + t] ) * K[0, (i*n_virt + t) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, (n*n_virt + s) * n_ex + i*n_virt + t+ 2*n_ex]

												elif ((u == t) and (t != s) and (w == t) and (v == t)):

													L3[i*n_virt + s] += (-8 * g[i, n, i, n_occ + s] + 4 * g[i, i, n, n_occ + s] + 8 * g[n, n_occ + t, n_occ + s, n_occ + t] + -4 * g[n, n_occ + s, n_occ + t, n_occ + t] ) * K[0, (i*n_virt + t) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, (n*n_virt + t) * n_ex + i*n_virt + t+ 2*n_ex]

												elif ((u == t) and (t != s) and (w != s) and (w != t) and (w != u) and (w != v) and (v == t)):

													L3[i*n_virt + s] += (-4 * g[n, n_occ + s, n_occ + t, n_occ + w] + 8 * g[n, n_occ + w, n_occ + s, n_occ + t] ) * K[0, (i*n_virt + t) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, (n*n_virt + w) * n_ex + i*n_virt + t+ 2*n_ex]

												elif ((u != s) and (u != t) and (t != s) and (w == s) and (v == u)):

													L3[i*n_virt + s] += (4 * g[n, n_occ + s, n_occ + s, n_occ + t] ) * K[0, (i*n_virt + u) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, (n*n_virt + s) * n_ex + i*n_virt + u+ 2*n_ex]

												elif ((u != s) and (u != t) and (t != s) and (w == t) and (v == u)):

													L3[i*n_virt + s] += (-8 * g[i, n, i, n_occ + s] + 4 * g[i, i, n, n_occ + s] + 8 * g[n, n_occ + t, n_occ + s, n_occ + t] + -4 * g[n, n_occ + s, n_occ + t, n_occ + t] ) * K[0, (i*n_virt + u) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, (n*n_virt + t) * n_ex + i*n_virt + u+ 2*n_ex]

												elif ((u != s) and (u != t) and (t != s) and (w == u) and (v == u)):

													L3[i*n_virt + s] += (-4 * g[n, n_occ + s, n_occ + t, n_occ + u] + 8 * g[n, n_occ + u, n_occ + s, n_occ + t] ) * K[0, (i*n_virt + u) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, (n*n_virt + u) * n_ex + i*n_virt + u+ 2*n_ex]

												elif ((u != s) and (u != t) and (t != s) and (w != s) and (w != t) and (w != u) and (w != v) and (v == u)):

													L3[i*n_virt + s] += (-4 * g[n, n_occ + s, n_occ + t, n_occ + w] + 8 * g[n, n_occ + w, n_occ + s, n_occ + t] ) * K[0, (i*n_virt + u) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, (n*n_virt + w) * n_ex + i*n_virt + u+ 2*n_ex]

											elif ((k == i) and (j == i) and (n == i) and (m != i) and (m != j) and (m != k)):

												if ((u == s) and (t == s) and (w == s) and (v == s)):

													L3[i*n_virt + s] += (-8 * g[i, m, i, n_occ + s] ) * K[0, (i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] * K[1, (i*n_virt + s) * n_ex + m*n_virt + s+ 2*n_ex]

												elif ((u != s) and (u != t) and (t == s) and (w == s) and (v == s)):

													L3[i*n_virt + s] += (-4 * g[i, m, i, n_occ + u] ) * K[0, (i*n_virt + u) * n_ex + i*n_virt + s+ 2*n_ex] * K[1, (i*n_virt + s) * n_ex + m*n_virt + s+ 2*n_ex]

												elif ((u != s) and (u != t) and (t == s) and (w == s) and (v == u)):

													L3[i*n_virt + s] += (-4 * g[i, m, i, n_occ + s] ) * K[0, (i*n_virt + u) * n_ex + i*n_virt + s+ 2*n_ex] * K[1, (i*n_virt + s) * n_ex + m*n_virt + u+ 2*n_ex]

												elif ((u == s) and (t != s) and (w == t) and (v == s)):

													L3[i*n_virt + s] += (-8 * g[i, m, i, n_occ + s] ) * K[0, (i*n_virt + s) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, (i*n_virt + t) * n_ex + m*n_virt + s+ 2*n_ex]

												elif ((u == t) and (t != s) and (w == t) and (v == s)):

													L3[i*n_virt + s] += (-4 * g[i, m, i, n_occ + t] ) * K[0, (i*n_virt + t) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, (i*n_virt + t) * n_ex + m*n_virt + s+ 2*n_ex]

												elif ((u == t) and (t != s) and (w == t) and (v == t)):

													L3[i*n_virt + s] += (-4 * g[i, m, i, n_occ + s] ) * K[0, (i*n_virt + t) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, (i*n_virt + t) * n_ex + m*n_virt + t+ 2*n_ex]

												elif ((u != s) and (u != t) and (t != s) and (w == t) and (v == s)):

													L3[i*n_virt + s] += (-4 * g[i, m, i, n_occ + u] ) * K[0, (i*n_virt + u) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, (i*n_virt + t) * n_ex + m*n_virt + s+ 2*n_ex]

												elif ((u != s) and (u != t) and (t != s) and (w == t) and (v == u)):

													L3[i*n_virt + s] += (-4 * g[i, m, i, n_occ + s] ) * K[0, (i*n_virt + u) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, (i*n_virt + t) * n_ex + m*n_virt + u+ 2*n_ex]

											elif ((k != i) and (k != j) and (j == i) and (n == i) and (m == i)):

												if ((u == s) and (t == s) and (w == s) and (v == s)):

													L3[i*n_virt + s] += (4 * F[k, n_occ + s] + -4 * g[i, k, i, n_occ + s] + 4 * g[k, n_occ + s, n_occ + s, n_occ + s] + -4 * g[i, i, k, n_occ + s] ) * K[0, (k*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] * K[1, (i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex]

												elif ((u == s) and (t == s) and (w == s) and (v != s) and (v != t) and (v != u)):

													L3[i*n_virt + s] += (4 * g[k, n_occ + s, n_occ + s, n_occ + v] ) * K[0, (k*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] * K[1, (i*n_virt + s) * n_ex + i*n_virt + v+ 2*n_ex]

												elif ((u != s) and (u != t) and (t == s) and (w == s) and (v == s)):

													L3[i*n_virt + s] += (8 * F[k, n_occ + u] + -4 * g[k, n_occ + s, n_occ + s, n_occ + u] + 8 * g[k, n_occ + u, n_occ + s, n_occ + s] + -8 * g[i, i, k, n_occ + u] + 4 * g[i, k, i, n_occ + u] ) * K[0, (k*n_virt + u) * n_ex + i*n_virt + s+ 2*n_ex] * K[1, (i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex]

												elif ((u != s) and (u != t) and (t == s) and (w == s) and (v == u)):

													L3[i*n_virt + s] += (-4 * F[k, n_occ + s] + 8 * g[k, n_occ + u, n_occ + s, n_occ + u] + -4 * g[k, n_occ + s, n_occ + u, n_occ + u] + 4 * g[i, i, k, n_occ + s] + -8 * g[i, k, i, n_occ + s] ) * K[0, (k*n_virt + u) * n_ex + i*n_virt + s+ 2*n_ex] * K[1, (i*n_virt + s) * n_ex + i*n_virt + u+ 2*n_ex]

												elif ((u != s) and (u != t) and (t == s) and (w == s) and (v != s) and (v != t) and (v != u)):

													L3[i*n_virt + s] += (-4 * g[k, n_occ + s, n_occ + u, n_occ + v] + 8 * g[k, n_occ + u, n_occ + s, n_occ + v] ) * K[0, (k*n_virt + u) * n_ex + i*n_virt + s+ 2*n_ex] * K[1, (i*n_virt + s) * n_ex + i*n_virt + v+ 2*n_ex]

												elif ((u == s) and (t != s) and (w == t) and (v == s)):

													L3[i*n_virt + s] += (4 * F[k, n_occ + s] + -4 * g[i, k, i, n_occ + s] + 4 * g[k, n_occ + s, n_occ + s, n_occ + s] + -4 * g[i, i, k, n_occ + s] ) * K[0, (k*n_virt + s) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, (i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex]

												elif ((u == s) and (t != s) and (w == t) and (v == t)):

													L3[i*n_virt + s] += (4 * g[k, n_occ + s, n_occ + s, n_occ + t] ) * K[0, (k*n_virt + s) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, (i*n_virt + t) * n_ex + i*n_virt + t+ 2*n_ex]

												elif ((u == s) and (t != s) and (w == t) and (v != s) and (v != t) and (v != u)):

													L3[i*n_virt + s] += (4 * g[k, n_occ + s, n_occ + s, n_occ + v] ) * K[0, (k*n_virt + s) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, (i*n_virt + t) * n_ex + i*n_virt + v+ 2*n_ex]

												elif ((u == t) and (t != s) and (w == t) and (v == s)):

													L3[i*n_virt + s] += (8 * F[k, n_occ + t] + -4 * g[k, n_occ + s, n_occ + s, n_occ + t] + 8 * g[k, n_occ + t, n_occ + s, n_occ + s] + -8 * g[i, i, k, n_occ + t] + 4 * g[i, k, i, n_occ + t] ) * K[0, (k*n_virt + t) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, (i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex]

												elif ((u == t) and (t != s) and (w == t) and (v == t)):

													L3[i*n_virt + s] += (-4 * F[k, n_occ + s] + 8 * g[k, n_occ + t, n_occ + s, n_occ + t] + -4 * g[k, n_occ + s, n_occ + t, n_occ + t] + 4 * g[i, i, k, n_occ + s] + -8 * g[i, k, i, n_occ + s] ) * K[0, (k*n_virt + t) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, (i*n_virt + t) * n_ex + i*n_virt + t+ 2*n_ex]

												elif ((u == t) and (t != s) and (w == t) and (v != s) and (v != t) and (v != u)):

													L3[i*n_virt + s] += (-4 * g[k, n_occ + s, n_occ + t, n_occ + v] + 8 * g[k, n_occ + t, n_occ + s, n_occ + v] ) * K[0, (k*n_virt + t) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, (i*n_virt + t) * n_ex + i*n_virt + v+ 2*n_ex]

												elif ((u != s) and (u != t) and (t != s) and (w == t) and (v == s)):

													L3[i*n_virt + s] += (8 * F[k, n_occ + u] + -4 * g[k, n_occ + s, n_occ + s, n_occ + u] + 8 * g[k, n_occ + u, n_occ + s, n_occ + s] + -8 * g[i, i, k, n_occ + u] + 4 * g[i, k, i, n_occ + u] ) * K[0, (k*n_virt + u) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, (i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex]

												elif ((u != s) and (u != t) and (t != s) and (w == t) and (v == t)):

													L3[i*n_virt + s] += (-4 * g[k, n_occ + s, n_occ + t, n_occ + u] + 8 * g[k, n_occ + u, n_occ + s, n_occ + t] ) * K[0, (k*n_virt + u) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, (i*n_virt + t) * n_ex + i*n_virt + t+ 2*n_ex]

												elif ((u != s) and (u != t) and (t != s) and (w == t) and (v == u)):

													L3[i*n_virt + s] += (-4 * F[k, n_occ + s] + 8 * g[k, n_occ + u, n_occ + s, n_occ + u] + -4 * g[k, n_occ + s, n_occ + u, n_occ + u] + 4 * g[i, i, k, n_occ + s] + -8 * g[i, k, i, n_occ + s] ) * K[0, (k*n_virt + u) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, (i*n_virt + t) * n_ex + i*n_virt + u+ 2*n_ex]

												elif ((u != s) and (u != t) and (t != s) and (w == t) and (v != s) and (v != t) and (v != u)):

													L3[i*n_virt + s] += (-4 * g[k, n_occ + s, n_occ + u, n_occ + v] + 8 * g[k, n_occ + u, n_occ + s, n_occ + v] ) * K[0, (k*n_virt + u) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, (i*n_virt + t) * n_ex + i*n_virt + v+ 2*n_ex]

											elif ((k != i) and (k != j) and (j == i) and (n == i) and (m == k)):

												if ((u == s) and (t == s) and (w == s) and (v == s)):

													L3[i*n_virt + s] += (-4 * F[i, n_occ + s] + -8 * g[i, i, i, n_occ + s] + 12 * g[i, n_occ + s, n_occ + s, n_occ + s] + -4 * g[i, n_occ + s, k, k] + -4 * g[i, k, k, n_occ + s] ) * K[0, (k*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] * K[1, (i*n_virt + s) * n_ex + k*n_virt + s+ 2*n_ex]

												elif ((u == s) and (t == s) and (w != s) and (w != t) and (w != u) and (w != v) and (v == s)):

													L3[i*n_virt + s] += (-4 * g[i, i, i, n_occ + w] + 4 * g[i, n_occ + w, n_occ + s, n_occ + s] + 4 * g[i, n_occ + s, n_occ + s, n_occ + w] ) * K[0, (k*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] * K[1, (i*n_virt + w) * n_ex + k*n_virt + s+ 2*n_ex]

												elif ((u == s) and (t == s) and (w == s) and (v != s) and (v != t) and (v != u)):

													L3[i*n_virt + s] += (4 * g[i, n_occ + s, n_occ + s, n_occ + v] ) * K[0, (k*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] * K[1, (i*n_virt + s) * n_ex + k*n_virt + v+ 2*n_ex]

												elif ((u != s) and (u != t) and (t == s) and (w == s) and (v == s)):

													L3[i*n_virt + s] += (-4 * F[i, n_occ + u] + 8 * g[i, n_occ + s, n_occ + s, n_occ + u] + -4 * g[i, n_occ + u, n_occ + s, n_occ + s] + 4 * g[i, n_occ + u, k, k] + -8 * g[i, k, k, n_occ + u] ) * K[0, (k*n_virt + u) * n_ex + i*n_virt + s+ 2*n_ex] * K[1, (i*n_virt + s) * n_ex + k*n_virt + s+ 2*n_ex]

												elif ((u != s) and (u != t) and (t == s) and (w == s) and (v == u)):

													L3[i*n_virt + s] += (-4 * g[i, n_occ + u, n_occ + s, n_occ + u] + 8 * g[i, n_occ + s, n_occ + u, n_occ + u] + 8 * g[i, n_occ + s, n_occ + s, n_occ + s] + -8 * g[i, i, i, n_occ + s] + 4 * g[i, k, k, n_occ + s] + -8 * g[i, n_occ + s, k, k] ) * K[0, (k*n_virt + u) * n_ex + i*n_virt + s+ 2*n_ex] * K[1, (i*n_virt + s) * n_ex + k*n_virt + u+ 2*n_ex]

												elif ((u != s) and (u != t) and (t == s) and (w == u) and (v == u)):

													L3[i*n_virt + s] += (-4 * g[i, i, i, n_occ + u] + 4 * g[i, n_occ + u, n_occ + s, n_occ + s] + 4 * g[i, n_occ + s, n_occ + s, n_occ + u] ) * K[0, (k*n_virt + u) * n_ex + i*n_virt + s+ 2*n_ex] * K[1, (i*n_virt + u) * n_ex + k*n_virt + u+ 2*n_ex]

												elif ((u != s) and (u != t) and (t == s) and (w != s) and (w != t) and (w != u) and (w != v) and (v == u)):

													L3[i*n_virt + s] += (-4 * g[i, i, i, n_occ + w] + 4 * g[i, n_occ + w, n_occ + s, n_occ + s] + 4 * g[i, n_occ + s, n_occ + s, n_occ + w] ) * K[0, (k*n_virt + u) * n_ex + i*n_virt + s+ 2*n_ex] * K[1, (i*n_virt + w) * n_ex + k*n_virt + u+ 2*n_ex]

												elif ((u != s) and (u != t) and (t == s) and (w == s) and (v != s) and (v != t) and (v != u)):

													L3[i*n_virt + s] += (8 * g[i, n_occ + s, n_occ + u, n_occ + v] + -4 * g[i, n_occ + u, n_occ + s, n_occ + v] ) * K[0, (k*n_virt + u) * n_ex + i*n_virt + s+ 2*n_ex] * K[1, (i*n_virt + s) * n_ex + k*n_virt + v+ 2*n_ex]

												elif ((u == s) and (t != s) and (w == s) and (v == s)):

													L3[i*n_virt + s] += (8 * g[i, n_occ + s, n_occ + s, n_occ + t] ) * K[0, (k*n_virt + s) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, (i*n_virt + s) * n_ex + k*n_virt + s+ 2*n_ex]

												elif ((u == s) and (t != s) and (w == t) and (v == s)):

													L3[i*n_virt + s] += (-4 * F[i, n_occ + s] + 4 * g[i, n_occ + s, n_occ + s, n_occ + s] + 4 * g[i, n_occ + t, n_occ + s, n_occ + t] + 4 * g[i, n_occ + s, n_occ + t, n_occ + t] + -4 * g[i, n_occ + s, k, k] + -4 * g[i, i, i, n_occ + s] + -4 * g[i, k, k, n_occ + s] ) * K[0, (k*n_virt + s) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, (i*n_virt + t) * n_ex + k*n_virt + s+ 2*n_ex]

												elif ((u == s) and (t != s) and (w != s) and (w != t) and (w != u) and (w != v) and (v == s)):

													L3[i*n_virt + s] += (4 * g[i, n_occ + w, n_occ + s, n_occ + t] + 4 * g[i, n_occ + s, n_occ + t, n_occ + w] ) * K[0, (k*n_virt + s) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, (i*n_virt + w) * n_ex + k*n_virt + s+ 2*n_ex]

												elif ((u == s) and (t != s) and (w == t) and (v == t)):

													L3[i*n_virt + s] += (4 * g[i, n_occ + s, n_occ + s, n_occ + t] ) * K[0, (k*n_virt + s) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, (i*n_virt + t) * n_ex + k*n_virt + t+ 2*n_ex]

												elif ((u == s) and (t != s) and (w == t) and (v != s) and (v != t) and (v != u)):

													L3[i*n_virt + s] += (4 * g[i, n_occ + s, n_occ + s, n_occ + v] ) * K[0, (k*n_virt + s) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, (i*n_virt + t) * n_ex + k*n_virt + v+ 2*n_ex]

												elif ((u == t) and (t != s) and (w == t) and (v == s)):

													L3[i*n_virt + s] += (-4 * F[i, n_occ + t] + 8 * g[i, n_occ + s, n_occ + s, n_occ + t] + -4 * g[i, n_occ + t, n_occ + s, n_occ + s] + 4 * g[i, n_occ + t, k, k] + -8 * g[i, k, k, n_occ + t] ) * K[0, (k*n_virt + t) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, (i*n_virt + t) * n_ex + k*n_virt + s+ 2*n_ex]

												elif ((u == t) and (t != s) and (w == s) and (v == t)):

													L3[i*n_virt + s] += (8 * g[i, n_occ + s, n_occ + s, n_occ + t] ) * K[0, (k*n_virt + t) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, (i*n_virt + s) * n_ex + k*n_virt + t+ 2*n_ex]

												elif ((u == t) and (t != s) and (w == t) and (v == t)):

													L3[i*n_virt + s] += (12 * g[i, n_occ + s, n_occ + t, n_occ + t] + 4 * g[i, k, k, n_occ + s] + -8 * g[i, n_occ + s, k, k] + -4 * g[i, i, i, n_occ + s] ) * K[0, (k*n_virt + t) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, (i*n_virt + t) * n_ex + k*n_virt + t+ 2*n_ex]

												elif ((u == t) and (t != s) and (w != s) and (w != t) and (w != u) and (w != v) and (v == t)):

													L3[i*n_virt + s] += (4 * g[i, n_occ + w, n_occ + s, n_occ + t] + 4 * g[i, n_occ + s, n_occ + t, n_occ + w] ) * K[0, (k*n_virt + t) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, (i*n_virt + w) * n_ex + k*n_virt + t+ 2*n_ex]

												elif ((u == t) and (t != s) and (w == t) and (v != s) and (v != t) and (v != u)):

													L3[i*n_virt + s] += (8 * g[i, n_occ + s, n_occ + t, n_occ + v] + -4 * g[i, n_occ + t, n_occ + s, n_occ + v] ) * K[0, (k*n_virt + t) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, (i*n_virt + t) * n_ex + k*n_virt + v+ 2*n_ex]

												elif ((u != s) and (u != t) and (t != s) and (w == t) and (v == s)):

													L3[i*n_virt + s] += (-4 * F[i, n_occ + u] + 8 * g[i, n_occ + s, n_occ + s, n_occ + u] + -4 * g[i, n_occ + u, n_occ + s, n_occ + s] + 4 * g[i, n_occ + u, k, k] + -8 * g[i, k, k, n_occ + u] ) * K[0, (k*n_virt + u) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, (i*n_virt + t) * n_ex + k*n_virt + s+ 2*n_ex]

												elif ((u != s) and (u != t) and (t != s) and (w == t) and (v == t)):

													L3[i*n_virt + s] += (8 * g[i, n_occ + s, n_occ + t, n_occ + u] + -4 * g[i, n_occ + u, n_occ + s, n_occ + t] ) * K[0, (k*n_virt + u) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, (i*n_virt + t) * n_ex + k*n_virt + t+ 2*n_ex]

												elif ((u != s) and (u != t) and (t != s) and (w == s) and (v == u)):

													L3[i*n_virt + s] += (8 * g[i, n_occ + s, n_occ + s, n_occ + t] ) * K[0, (k*n_virt + u) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, (i*n_virt + s) * n_ex + k*n_virt + u+ 2*n_ex]

												elif ((u != s) and (u != t) and (t != s) and (w == t) and (v == u)):

													L3[i*n_virt + s] += (-4 * g[i, n_occ + u, n_occ + s, n_occ + u] + 8 * g[i, n_occ + s, n_occ + u, n_occ + u] + 4 * g[i, n_occ + t, n_occ + s, n_occ + t] + 4 * g[i, n_occ + s, n_occ + t, n_occ + t] + 4 * g[i, k, k, n_occ + s] + -8 * g[i, n_occ + s, k, k] + -4 * g[i, i, i, n_occ + s] ) * K[0, (k*n_virt + u) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, (i*n_virt + t) * n_ex + k*n_virt + u+ 2*n_ex]

												elif ((u != s) and (u != t) and (t != s) and (w == u) and (v == u)):

													L3[i*n_virt + s] += (4 * g[i, n_occ + u, n_occ + s, n_occ + t] + 4 * g[i, n_occ + s, n_occ + t, n_occ + u] ) * K[0, (k*n_virt + u) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, (i*n_virt + u) * n_ex + k*n_virt + u+ 2*n_ex]

												elif ((u != s) and (u != t) and (t != s) and (w != s) and (w != t) and (w != u) and (w != v) and (v == u)):

													L3[i*n_virt + s] += (4 * g[i, n_occ + w, n_occ + s, n_occ + t] + 4 * g[i, n_occ + s, n_occ + t, n_occ + w] ) * K[0, (k*n_virt + u) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, (i*n_virt + w) * n_ex + k*n_virt + u+ 2*n_ex]

												elif ((u != s) and (u != t) and (t != s) and (w == t) and (v != s) and (v != t) and (v != u)):

													L3[i*n_virt + s] += (8 * g[i, n_occ + s, n_occ + u, n_occ + v] + -4 * g[i, n_occ + u, n_occ + s, n_occ + v] ) * K[0, (k*n_virt + u) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, (i*n_virt + t) * n_ex + k*n_virt + v+ 2*n_ex]

											elif ((k != i) and (k != j) and (j == i) and (n == k) and (m == k)):

												if ((u == s) and (t == s) and (w == s) and (v == s)):

													L3[i*n_virt + s] += (-4 * g[i, i, k, n_occ + s] + 4 * g[k, n_occ + s, n_occ + s, n_occ + s] + -4 * g[i, k, i, n_occ + s] ) * K[0, (k*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] * K[1, (k*n_virt + s) * n_ex + k*n_virt + s+ 2*n_ex]

												elif ((u == s) and (t == s) and (w != s) and (w != t) and (w != u) and (w != v) and (v == s)):

													L3[i*n_virt + s] += (4 * g[i, k, i, n_occ + w] + -8 * g[i, i, k, n_occ + w] + -4 * g[k, n_occ + s, n_occ + s, n_occ + w] + 8 * g[k, n_occ + w, n_occ + s, n_occ + s] ) * K[0, (k*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] * K[1, (k*n_virt + w) * n_ex + k*n_virt + s+ 2*n_ex]

												elif ((u != s) and (u != t) and (t == s) and (w == s) and (v == u)):

													L3[i*n_virt + s] += (-4 * g[i, i, k, n_occ + s] + 4 * g[k, n_occ + s, n_occ + s, n_occ + s] + -4 * g[i, k, i, n_occ + s] ) * K[0, (k*n_virt + u) * n_ex + i*n_virt + s+ 2*n_ex] * K[1, (k*n_virt + s) * n_ex + k*n_virt + u+ 2*n_ex]

												elif ((u != s) and (u != t) and (t == s) and (w == u) and (v == u)):

													L3[i*n_virt + s] += (4 * g[i, k, i, n_occ + u] + -8 * g[i, i, k, n_occ + u] + -4 * g[k, n_occ + s, n_occ + s, n_occ + u] + 8 * g[k, n_occ + u, n_occ + s, n_occ + s] ) * K[0, (k*n_virt + u) * n_ex + i*n_virt + s+ 2*n_ex] * K[1, (k*n_virt + u) * n_ex + k*n_virt + u+ 2*n_ex]

												elif ((u != s) and (u != t) and (t == s) and (w != s) and (w != t) and (w != u) and (w != v) and (v == u)):

													L3[i*n_virt + s] += (4 * g[i, k, i, n_occ + w] + -8 * g[i, i, k, n_occ + w] + -4 * g[k, n_occ + s, n_occ + s, n_occ + w] + 8 * g[k, n_occ + w, n_occ + s, n_occ + s] ) * K[0, (k*n_virt + u) * n_ex + i*n_virt + s+ 2*n_ex] * K[1, (k*n_virt + w) * n_ex + k*n_virt + u+ 2*n_ex]

												elif ((u == s) and (t != s) and (w == s) and (v == s)):

													L3[i*n_virt + s] += (4 * g[k, n_occ + s, n_occ + s, n_occ + t] ) * K[0, (k*n_virt + s) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, (k*n_virt + s) * n_ex + k*n_virt + s+ 2*n_ex]

												elif ((u == s) and (t != s) and (w == t) and (v == s)):

													L3[i*n_virt + s] += (-8 * g[i, k, i, n_occ + s] + 4 * g[i, i, k, n_occ + s] + 8 * g[k, n_occ + t, n_occ + s, n_occ + t] + -4 * g[k, n_occ + s, n_occ + t, n_occ + t] ) * K[0, (k*n_virt + s) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, (k*n_virt + t) * n_ex + k*n_virt + s+ 2*n_ex]

												elif ((u == s) and (t != s) and (w != s) and (w != t) and (w != u) and (w != v) and (v == s)):

													L3[i*n_virt + s] += (-4 * g[k, n_occ + s, n_occ + t, n_occ + w] + 8 * g[k, n_occ + w, n_occ + s, n_occ + t] ) * K[0, (k*n_virt + s) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, (k*n_virt + w) * n_ex + k*n_virt + s+ 2*n_ex]

												elif ((u == t) and (t != s) and (w == s) and (v == t)):

													L3[i*n_virt + s] += (4 * g[k, n_occ + s, n_occ + s, n_occ + t] ) * K[0, (k*n_virt + t) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, (k*n_virt + s) * n_ex + k*n_virt + t+ 2*n_ex]

												elif ((u == t) and (t != s) and (w == t) and (v == t)):

													L3[i*n_virt + s] += (-8 * g[i, k, i, n_occ + s] + 4 * g[i, i, k, n_occ + s] + 8 * g[k, n_occ + t, n_occ + s, n_occ + t] + -4 * g[k, n_occ + s, n_occ + t, n_occ + t] ) * K[0, (k*n_virt + t) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, (k*n_virt + t) * n_ex + k*n_virt + t+ 2*n_ex]

												elif ((u == t) and (t != s) and (w != s) and (w != t) and (w != u) and (w != v) and (v == t)):

													L3[i*n_virt + s] += (-4 * g[k, n_occ + s, n_occ + t, n_occ + w] + 8 * g[k, n_occ + w, n_occ + s, n_occ + t] ) * K[0, (k*n_virt + t) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, (k*n_virt + w) * n_ex + k*n_virt + t+ 2*n_ex]

												elif ((u != s) and (u != t) and (t != s) and (w == s) and (v == u)):

													L3[i*n_virt + s] += (4 * g[k, n_occ + s, n_occ + s, n_occ + t] ) * K[0, (k*n_virt + u) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, (k*n_virt + s) * n_ex + k*n_virt + u+ 2*n_ex]

												elif ((u != s) and (u != t) and (t != s) and (w == t) and (v == u)):

													L3[i*n_virt + s] += (-8 * g[i, k, i, n_occ + s] + 4 * g[i, i, k, n_occ + s] + 8 * g[k, n_occ + t, n_occ + s, n_occ + t] + -4 * g[k, n_occ + s, n_occ + t, n_occ + t] ) * K[0, (k*n_virt + u) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, (k*n_virt + t) * n_ex + k*n_virt + u+ 2*n_ex]

												elif ((u != s) and (u != t) and (t != s) and (w == u) and (v == u)):

													L3[i*n_virt + s] += (-4 * g[k, n_occ + s, n_occ + t, n_occ + u] + 8 * g[k, n_occ + u, n_occ + s, n_occ + t] ) * K[0, (k*n_virt + u) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, (k*n_virt + u) * n_ex + k*n_virt + u+ 2*n_ex]

												elif ((u != s) and (u != t) and (t != s) and (w != s) and (w != t) and (w != u) and (w != v) and (v == u)):

													L3[i*n_virt + s] += (-4 * g[k, n_occ + s, n_occ + t, n_occ + w] + 8 * g[k, n_occ + w, n_occ + s, n_occ + t] ) * K[0, (k*n_virt + u) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, (k*n_virt + w) * n_ex + k*n_virt + u+ 2*n_ex]

											elif ((k != i) and (k != j) and (j == i) and (n != i) and (n != j) and (n != k) and (n != m) and (m == k)):

												if ((u == s) and (t == s) and (w == s) and (v == s)):

													L3[i*n_virt + s] += (-4 * g[i, i, n, n_occ + s] + 4 * g[n, n_occ + s, n_occ + s, n_occ + s] + -4 * g[i, n, i, n_occ + s] ) * K[0, (k*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] * K[1, (n*n_virt + s) * n_ex + k*n_virt + s+ 2*n_ex]

												elif ((u == s) and (t == s) and (w != s) and (w != t) and (w != u) and (w != v) and (v == s)):

													L3[i*n_virt + s] += (4 * g[i, n, i, n_occ + w] + -8 * g[i, i, n, n_occ + w] + -4 * g[n, n_occ + s, n_occ + s, n_occ + w] + 8 * g[n, n_occ + w, n_occ + s, n_occ + s] ) * K[0, (k*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] * K[1, (n*n_virt + w) * n_ex + k*n_virt + s+ 2*n_ex]

												elif ((u != s) and (u != t) and (t == s) and (w == s) and (v == u)):

													L3[i*n_virt + s] += (-4 * g[i, i, n, n_occ + s] + 4 * g[n, n_occ + s, n_occ + s, n_occ + s] + -4 * g[i, n, i, n_occ + s] ) * K[0, (k*n_virt + u) * n_ex + i*n_virt + s+ 2*n_ex] * K[1, (n*n_virt + s) * n_ex + k*n_virt + u+ 2*n_ex]

												elif ((u != s) and (u != t) and (t == s) and (w == u) and (v == u)):

													L3[i*n_virt + s] += (4 * g[i, n, i, n_occ + u] + -8 * g[i, i, n, n_occ + u] + -4 * g[n, n_occ + s, n_occ + s, n_occ + u] + 8 * g[n, n_occ + u, n_occ + s, n_occ + s] ) * K[0, (k*n_virt + u) * n_ex + i*n_virt + s+ 2*n_ex] * K[1, (n*n_virt + u) * n_ex + k*n_virt + u+ 2*n_ex]

												elif ((u != s) and (u != t) and (t == s) and (w != s) and (w != t) and (w != u) and (w != v) and (v == u)):

													L3[i*n_virt + s] += (4 * g[i, n, i, n_occ + w] + -8 * g[i, i, n, n_occ + w] + -4 * g[n, n_occ + s, n_occ + s, n_occ + w] + 8 * g[n, n_occ + w, n_occ + s, n_occ + s] ) * K[0, (k*n_virt + u) * n_ex + i*n_virt + s+ 2*n_ex] * K[1, (n*n_virt + w) * n_ex + k*n_virt + u+ 2*n_ex]

												elif ((u == s) and (t != s) and (w == s) and (v == s)):

													L3[i*n_virt + s] += (4 * g[n, n_occ + s, n_occ + s, n_occ + t] ) * K[0, (k*n_virt + s) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, (n*n_virt + s) * n_ex + k*n_virt + s+ 2*n_ex]

												elif ((u == s) and (t != s) and (w == t) and (v == s)):

													L3[i*n_virt + s] += (-8 * g[i, n, i, n_occ + s] + 4 * g[i, i, n, n_occ + s] + 8 * g[n, n_occ + t, n_occ + s, n_occ + t] + -4 * g[n, n_occ + s, n_occ + t, n_occ + t] ) * K[0, (k*n_virt + s) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, (n*n_virt + t) * n_ex + k*n_virt + s+ 2*n_ex]

												elif ((u == s) and (t != s) and (w != s) and (w != t) and (w != u) and (w != v) and (v == s)):

													L3[i*n_virt + s] += (-4 * g[n, n_occ + s, n_occ + t, n_occ + w] + 8 * g[n, n_occ + w, n_occ + s, n_occ + t] ) * K[0, (k*n_virt + s) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, (n*n_virt + w) * n_ex + k*n_virt + s+ 2*n_ex]

												elif ((u == t) and (t != s) and (w == s) and (v == t)):

													L3[i*n_virt + s] += (4 * g[n, n_occ + s, n_occ + s, n_occ + t] ) * K[0, (k*n_virt + t) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, (n*n_virt + s) * n_ex + k*n_virt + t+ 2*n_ex]

												elif ((u == t) and (t != s) and (w == t) and (v == t)):

													L3[i*n_virt + s] += (-8 * g[i, n, i, n_occ + s] + 4 * g[i, i, n, n_occ + s] + 8 * g[n, n_occ + t, n_occ + s, n_occ + t] + -4 * g[n, n_occ + s, n_occ + t, n_occ + t] ) * K[0, (k*n_virt + t) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, (n*n_virt + t) * n_ex + k*n_virt + t+ 2*n_ex]

												elif ((u == t) and (t != s) and (w != s) and (w != t) and (w != u) and (w != v) and (v == t)):

													L3[i*n_virt + s] += (-4 * g[n, n_occ + s, n_occ + t, n_occ + w] + 8 * g[n, n_occ + w, n_occ + s, n_occ + t] ) * K[0, (k*n_virt + t) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, (n*n_virt + w) * n_ex + k*n_virt + t+ 2*n_ex]

												elif ((u != s) and (u != t) and (t != s) and (w == s) and (v == u)):

													L3[i*n_virt + s] += (4 * g[n, n_occ + s, n_occ + s, n_occ + t] ) * K[0, (k*n_virt + u) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, (n*n_virt + s) * n_ex + k*n_virt + u+ 2*n_ex]

												elif ((u != s) and (u != t) and (t != s) and (w == t) and (v == u)):

													L3[i*n_virt + s] += (-8 * g[i, n, i, n_occ + s] + 4 * g[i, i, n, n_occ + s] + 8 * g[n, n_occ + t, n_occ + s, n_occ + t] + -4 * g[n, n_occ + s, n_occ + t, n_occ + t] ) * K[0, (k*n_virt + u) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, (n*n_virt + t) * n_ex + k*n_virt + u+ 2*n_ex]

												elif ((u != s) and (u != t) and (t != s) and (w == u) and (v == u)):

													L3[i*n_virt + s] += (-4 * g[n, n_occ + s, n_occ + t, n_occ + u] + 8 * g[n, n_occ + u, n_occ + s, n_occ + t] ) * K[0, (k*n_virt + u) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, (n*n_virt + u) * n_ex + k*n_virt + u+ 2*n_ex]

												elif ((u != s) and (u != t) and (t != s) and (w != s) and (w != t) and (w != u) and (w != v) and (v == u)):

													L3[i*n_virt + s] += (-4 * g[n, n_occ + s, n_occ + t, n_occ + w] + 8 * g[n, n_occ + w, n_occ + s, n_occ + t] ) * K[0, (k*n_virt + u) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, (n*n_virt + w) * n_ex + k*n_virt + u+ 2*n_ex]

											elif ((k != i) and (k != j) and (j == i) and (n == i) and (m != i) and (m != j) and (m != k)):

												if ((u == s) and (t == s) and (w == s) and (v == s)):

													L3[i*n_virt + s] += (-4 * g[i, m, k, n_occ + s] + -4 * g[i, n_occ + s, k, m] ) * K[0, (k*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] * K[1, (i*n_virt + s) * n_ex + m*n_virt + s+ 2*n_ex]

												elif ((u != s) and (u != t) and (t == s) and (w == s) and (v == s)):

													L3[i*n_virt + s] += (-8 * g[i, m, k, n_occ + u] + 4 * g[i, n_occ + u, k, m] ) * K[0, (k*n_virt + u) * n_ex + i*n_virt + s+ 2*n_ex] * K[1, (i*n_virt + s) * n_ex + m*n_virt + s+ 2*n_ex]

												elif ((u != s) and (u != t) and (t == s) and (w == s) and (v == u)):

													L3[i*n_virt + s] += (4 * g[i, m, k, n_occ + s] + -8 * g[i, n_occ + s, k, m] ) * K[0, (k*n_virt + u) * n_ex + i*n_virt + s+ 2*n_ex] * K[1, (i*n_virt + s) * n_ex + m*n_virt + u+ 2*n_ex]

												elif ((u == s) and (t != s) and (w == t) and (v == s)):

													L3[i*n_virt + s] += (-4 * g[i, m, k, n_occ + s] + -4 * g[i, n_occ + s, k, m] ) * K[0, (k*n_virt + s) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, (i*n_virt + t) * n_ex + m*n_virt + s+ 2*n_ex]

												elif ((u == t) and (t != s) and (w == t) and (v == s)):

													L3[i*n_virt + s] += (-8 * g[i, m, k, n_occ + t] + 4 * g[i, n_occ + t, k, m] ) * K[0, (k*n_virt + t) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, (i*n_virt + t) * n_ex + m*n_virt + s+ 2*n_ex]

												elif ((u == t) and (t != s) and (w == t) and (v == t)):

													L3[i*n_virt + s] += (4 * g[i, m, k, n_occ + s] + -8 * g[i, n_occ + s, k, m] ) * K[0, (k*n_virt + t) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, (i*n_virt + t) * n_ex + m*n_virt + t+ 2*n_ex]

												elif ((u != s) and (u != t) and (t != s) and (w == t) and (v == s)):

													L3[i*n_virt + s] += (-8 * g[i, m, k, n_occ + u] + 4 * g[i, n_occ + u, k, m] ) * K[0, (k*n_virt + u) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, (i*n_virt + t) * n_ex + m*n_virt + s+ 2*n_ex]

												elif ((u != s) and (u != t) and (t != s) and (w == t) and (v == u)):

													L3[i*n_virt + s] += (4 * g[i, m, k, n_occ + s] + -8 * g[i, n_occ + s, k, m] ) * K[0, (k*n_virt + u) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, (i*n_virt + t) * n_ex + m*n_virt + u+ 2*n_ex]

											elif ((k == i) and (j != i) and (n == i) and (m == i)):

												if ((u == s) and (t == s) and (w == s) and (v == s)):

													L3[i*n_virt + s] += (-8 * g[i, j, i, n_occ + s] ) * K[0, (i*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, (i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex]

												elif ((u == s) and (t == s) and (w != s) and (w != t) and (w != u) and (w != v) and (v == s)):

													L3[i*n_virt + s] += (-4 * g[i, j, i, n_occ + w] ) * K[0, (i*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, (i*n_virt + w) * n_ex + i*n_virt + s+ 2*n_ex]

												elif ((u != s) and (u != t) and (t == s) and (w == s) and (v == u)):

													L3[i*n_virt + s] += (-8 * g[i, j, i, n_occ + s] ) * K[0, (i*n_virt + u) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, (i*n_virt + s) * n_ex + i*n_virt + u+ 2*n_ex]

												elif ((u != s) and (u != t) and (t == s) and (w == u) and (v == u)):

													L3[i*n_virt + s] += (-4 * g[i, j, i, n_occ + u] ) * K[0, (i*n_virt + u) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, (i*n_virt + u) * n_ex + i*n_virt + u+ 2*n_ex]

												elif ((u != s) and (u != t) and (t == s) and (w != s) and (w != t) and (w != u) and (w != v) and (v == u)):

													L3[i*n_virt + s] += (-4 * g[i, j, i, n_occ + w] ) * K[0, (i*n_virt + u) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, (i*n_virt + w) * n_ex + i*n_virt + u+ 2*n_ex]

												elif ((u == s) and (t != s) and (w == t) and (v == s)):

													L3[i*n_virt + s] += (-4 * g[i, j, i, n_occ + s] ) * K[0, (i*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex]

												elif ((u == t) and (t != s) and (w == t) and (v == t)):

													L3[i*n_virt + s] += (-4 * g[i, j, i, n_occ + s] ) * K[0, (i*n_virt + t) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (i*n_virt + t) * n_ex + i*n_virt + t+ 2*n_ex]

												elif ((u != s) and (u != t) and (t != s) and (w == t) and (v == u)):

													L3[i*n_virt + s] += (-4 * g[i, j, i, n_occ + s] ) * K[0, (i*n_virt + u) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (i*n_virt + t) * n_ex + i*n_virt + u+ 2*n_ex]

											elif ((k == i) and (j != i) and (n == j) and (m == i)):

												if ((u == s) and (t == s) and (w == s) and (v == s)):

													L3[i*n_virt + s] += (12 * g[i, n_occ + s, n_occ + s, n_occ + s] + -4 * g[i, j, j, n_occ + s] + -8 * g[i, i, i, n_occ + s] + -4 * g[i, n_occ + s, j, j] ) * K[0, (i*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, (j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex]

												elif ((u == s) and (t == s) and (w != s) and (w != t) and (w != u) and (w != v) and (v == s)):

													L3[i*n_virt + s] += (-8 * g[i, j, j, n_occ + w] + 4 * g[i, n_occ + w, j, j] + 8 * g[i, n_occ + s, n_occ + s, n_occ + w] + -4 * g[i, n_occ + w, n_occ + s, n_occ + s] ) * K[0, (i*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, (j*n_virt + w) * n_ex + i*n_virt + s+ 2*n_ex]

												elif ((u == s) and (t == s) and (w == s) and (v != s) and (v != t) and (v != u)):

													L3[i*n_virt + s] += (8 * g[i, n_occ + s, n_occ + s, n_occ + v] ) * K[0, (i*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, (j*n_virt + s) * n_ex + i*n_virt + v+ 2*n_ex]

												elif ((u != s) and (u != t) and (t == s) and (w == s) and (v == s)):

													L3[i*n_virt + s] += (4 * F[i, n_occ + u] + 4 * g[i, n_occ + u, n_occ + s, n_occ + s] + 4 * g[i, n_occ + s, n_occ + s, n_occ + u] + -4 * g[i, i, i, n_occ + u] ) * K[0, (i*n_virt + u) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, (j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex]

												elif ((u != s) and (u != t) and (t == s) and (w == s) and (v == u)):

													L3[i*n_virt + s] += (-4 * F[i, n_occ + s] + 4 * g[i, n_occ + u, n_occ + s, n_occ + u] + 4 * g[i, n_occ + s, n_occ + u, n_occ + u] + 4 * g[i, n_occ + s, n_occ + s, n_occ + s] + -4 * g[i, n_occ + s, j, j] + -4 * g[i, i, i, n_occ + s] + -4 * g[i, j, j, n_occ + s] ) * K[0, (i*n_virt + u) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, (j*n_virt + s) * n_ex + i*n_virt + u+ 2*n_ex]

												elif ((u != s) and (u != t) and (t == s) and (w == u) and (v == u)):

													L3[i*n_virt + s] += (-8 * g[i, j, j, n_occ + u] + 4 * g[i, n_occ + u, j, j] + 8 * g[i, n_occ + s, n_occ + s, n_occ + u] + -4 * g[i, n_occ + u, n_occ + s, n_occ + s] ) * K[0, (i*n_virt + u) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, (j*n_virt + u) * n_ex + i*n_virt + u+ 2*n_ex]

												elif ((u != s) and (u != t) and (t == s) and (w != s) and (w != t) and (w != u) and (w != v) and (v == u)):

													L3[i*n_virt + s] += (-8 * g[i, j, j, n_occ + w] + 4 * g[i, n_occ + w, j, j] + 8 * g[i, n_occ + s, n_occ + s, n_occ + w] + -4 * g[i, n_occ + w, n_occ + s, n_occ + s] ) * K[0, (i*n_virt + u) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, (j*n_virt + w) * n_ex + i*n_virt + u+ 2*n_ex]

												elif ((u != s) and (u != t) and (t == s) and (w == s) and (v != s) and (v != t) and (v != u)):

													L3[i*n_virt + s] += (4 * g[i, n_occ + u, n_occ + s, n_occ + v] + 4 * g[i, n_occ + s, n_occ + u, n_occ + v] ) * K[0, (i*n_virt + u) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, (j*n_virt + s) * n_ex + i*n_virt + v+ 2*n_ex]

												elif ((u == s) and (t != s) and (w == s) and (v == s)):

													L3[i*n_virt + s] += (4 * g[i, n_occ + s, n_occ + s, n_occ + t] ) * K[0, (i*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex]

												elif ((u == s) and (t != s) and (w == t) and (v == s)):

													L3[i*n_virt + s] += (8 * g[i, n_occ + s, n_occ + s, n_occ + s] + -4 * g[i, n_occ + t, n_occ + s, n_occ + t] + 8 * g[i, n_occ + s, n_occ + t, n_occ + t] + -8 * g[i, i, i, n_occ + s] + 4 * g[i, j, j, n_occ + s] + -8 * g[i, n_occ + s, j, j] ) * K[0, (i*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex]

												elif ((u == s) and (t != s) and (w != s) and (w != t) and (w != u) and (w != v) and (v == s)):

													L3[i*n_virt + s] += (8 * g[i, n_occ + s, n_occ + t, n_occ + w] + -4 * g[i, n_occ + w, n_occ + s, n_occ + t] ) * K[0, (i*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (j*n_virt + w) * n_ex + i*n_virt + s+ 2*n_ex]

												elif ((u == s) and (t != s) and (w == t) and (v == t)):

													L3[i*n_virt + s] += (8 * g[i, n_occ + s, n_occ + s, n_occ + t] ) * K[0, (i*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (j*n_virt + t) * n_ex + i*n_virt + t+ 2*n_ex]

												elif ((u == s) and (t != s) and (w == t) and (v != s) and (v != t) and (v != u)):

													L3[i*n_virt + s] += (8 * g[i, n_occ + s, n_occ + s, n_occ + v] ) * K[0, (i*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (j*n_virt + t) * n_ex + i*n_virt + v+ 2*n_ex]

												elif ((u == t) and (t != s) and (w == t) and (v == s)):

													L3[i*n_virt + s] += (4 * F[i, n_occ + t] + 4 * g[i, n_occ + t, n_occ + s, n_occ + s] + 4 * g[i, n_occ + s, n_occ + s, n_occ + t] + -4 * g[i, i, i, n_occ + t] ) * K[0, (i*n_virt + t) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex]

												elif ((u == t) and (t != s) and (w == s) and (v == t)):

													L3[i*n_virt + s] += (4 * g[i, n_occ + s, n_occ + s, n_occ + t] ) * K[0, (i*n_virt + t) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (j*n_virt + s) * n_ex + i*n_virt + t+ 2*n_ex]

												elif ((u == t) and (t != s) and (w == t) and (v == t)):

													L3[i*n_virt + s] += (-4 * F[i, n_occ + s] + 12 * g[i, n_occ + s, n_occ + t, n_occ + t] + 4 * g[i, j, j, n_occ + s] + -8 * g[i, n_occ + s, j, j] + -4 * g[i, i, i, n_occ + s] ) * K[0, (i*n_virt + t) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (j*n_virt + t) * n_ex + i*n_virt + t+ 2*n_ex]

												elif ((u == t) and (t != s) and (w != s) and (w != t) and (w != u) and (w != v) and (v == t)):

													L3[i*n_virt + s] += (8 * g[i, n_occ + s, n_occ + t, n_occ + w] + -4 * g[i, n_occ + w, n_occ + s, n_occ + t] ) * K[0, (i*n_virt + t) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (j*n_virt + w) * n_ex + i*n_virt + t+ 2*n_ex]

												elif ((u == t) and (t != s) and (w == t) and (v != s) and (v != t) and (v != u)):

													L3[i*n_virt + s] += (4 * g[i, n_occ + t, n_occ + s, n_occ + v] + 4 * g[i, n_occ + s, n_occ + t, n_occ + v] ) * K[0, (i*n_virt + t) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (j*n_virt + t) * n_ex + i*n_virt + v+ 2*n_ex]

												elif ((u != s) and (u != t) and (t != s) and (w == t) and (v == s)):

													L3[i*n_virt + s] += (4 * F[i, n_occ + u] + 4 * g[i, n_occ + u, n_occ + s, n_occ + s] + 4 * g[i, n_occ + s, n_occ + s, n_occ + u] + -4 * g[i, i, i, n_occ + u] ) * K[0, (i*n_virt + u) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex]

												elif ((u != s) and (u != t) and (t != s) and (w == t) and (v == t)):

													L3[i*n_virt + s] += (4 * g[i, n_occ + u, n_occ + s, n_occ + t] + 4 * g[i, n_occ + s, n_occ + t, n_occ + u] ) * K[0, (i*n_virt + u) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (j*n_virt + t) * n_ex + i*n_virt + t+ 2*n_ex]

												elif ((u != s) and (u != t) and (t != s) and (w == s) and (v == u)):

													L3[i*n_virt + s] += (4 * g[i, n_occ + s, n_occ + s, n_occ + t] ) * K[0, (i*n_virt + u) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (j*n_virt + s) * n_ex + i*n_virt + u+ 2*n_ex]

												elif ((u != s) and (u != t) and (t != s) and (w == t) and (v == u)):

													L3[i*n_virt + s] += (-4 * F[i, n_occ + s] + 4 * g[i, n_occ + u, n_occ + s, n_occ + u] + 4 * g[i, n_occ + s, n_occ + u, n_occ + u] + -4 * g[i, n_occ + t, n_occ + s, n_occ + t] + 8 * g[i, n_occ + s, n_occ + t, n_occ + t] + 4 * g[i, j, j, n_occ + s] + -8 * g[i, n_occ + s, j, j] + -4 * g[i, i, i, n_occ + s] ) * K[0, (i*n_virt + u) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (j*n_virt + t) * n_ex + i*n_virt + u+ 2*n_ex]

												elif ((u != s) and (u != t) and (t != s) and (w == u) and (v == u)):

													L3[i*n_virt + s] += (8 * g[i, n_occ + s, n_occ + t, n_occ + u] + -4 * g[i, n_occ + u, n_occ + s, n_occ + t] ) * K[0, (i*n_virt + u) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (j*n_virt + u) * n_ex + i*n_virt + u+ 2*n_ex]

												elif ((u != s) and (u != t) and (t != s) and (w != s) and (w != t) and (w != u) and (w != v) and (v == u)):

													L3[i*n_virt + s] += (8 * g[i, n_occ + s, n_occ + t, n_occ + w] + -4 * g[i, n_occ + w, n_occ + s, n_occ + t] ) * K[0, (i*n_virt + u) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (j*n_virt + w) * n_ex + i*n_virt + u+ 2*n_ex]

												elif ((u != s) and (u != t) and (t != s) and (w == t) and (v != s) and (v != t) and (v != u)):

													L3[i*n_virt + s] += (4 * g[i, n_occ + u, n_occ + s, n_occ + v] + 4 * g[i, n_occ + s, n_occ + u, n_occ + v] ) * K[0, (i*n_virt + u) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (j*n_virt + t) * n_ex + i*n_virt + v+ 2*n_ex]

											elif ((k == i) and (j != i) and (n != i) and (n != j) and (n != k) and (n != m) and (m == i)):

												if ((u == s) and (t == s) and (w == s) and (v == s)):

													L3[i*n_virt + s] += (-4 * g[i, j, n, n_occ + s] + -4 * g[i, n_occ + s, j, n] ) * K[0, (i*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, (n*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex]

												elif ((u == s) and (t == s) and (w != s) and (w != t) and (w != u) and (w != v) and (v == s)):

													L3[i*n_virt + s] += (-8 * g[i, j, n, n_occ + w] + 4 * g[i, n_occ + w, j, n] ) * K[0, (i*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, (n*n_virt + w) * n_ex + i*n_virt + s+ 2*n_ex]

												elif ((u != s) and (u != t) and (t == s) and (w == s) and (v == u)):

													L3[i*n_virt + s] += (-4 * g[i, j, n, n_occ + s] + -4 * g[i, n_occ + s, j, n] ) * K[0, (i*n_virt + u) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, (n*n_virt + s) * n_ex + i*n_virt + u+ 2*n_ex]

												elif ((u != s) and (u != t) and (t == s) and (w == u) and (v == u)):

													L3[i*n_virt + s] += (-8 * g[i, j, n, n_occ + u] + 4 * g[i, n_occ + u, j, n] ) * K[0, (i*n_virt + u) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, (n*n_virt + u) * n_ex + i*n_virt + u+ 2*n_ex]

												elif ((u != s) and (u != t) and (t == s) and (w != s) and (w != t) and (w != u) and (w != v) and (v == u)):

													L3[i*n_virt + s] += (-8 * g[i, j, n, n_occ + w] + 4 * g[i, n_occ + w, j, n] ) * K[0, (i*n_virt + u) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, (n*n_virt + w) * n_ex + i*n_virt + u+ 2*n_ex]

												elif ((u == s) and (t != s) and (w == t) and (v == s)):

													L3[i*n_virt + s] += (4 * g[i, j, n, n_occ + s] + -8 * g[i, n_occ + s, j, n] ) * K[0, (i*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (n*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex]

												elif ((u == t) and (t != s) and (w == t) and (v == t)):

													L3[i*n_virt + s] += (4 * g[i, j, n, n_occ + s] + -8 * g[i, n_occ + s, j, n] ) * K[0, (i*n_virt + t) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (n*n_virt + t) * n_ex + i*n_virt + t+ 2*n_ex]

												elif ((u != s) and (u != t) and (t != s) and (w == t) and (v == u)):

													L3[i*n_virt + s] += (4 * g[i, j, n, n_occ + s] + -8 * g[i, n_occ + s, j, n] ) * K[0, (i*n_virt + u) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (n*n_virt + t) * n_ex + i*n_virt + u+ 2*n_ex]

											elif ((k == i) and (j != i) and (n == j) and (m == j)):

												if ((u == s) and (t == s) and (w == s) and (v == s)):

													L3[i*n_virt + s] += (-8 * g[i, j, i, n_occ + s] ) * K[0, (i*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, (j*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex]

												elif ((u != s) and (u != t) and (t == s) and (w == s) and (v == s)):

													L3[i*n_virt + s] += (-4 * g[i, j, i, n_occ + u] ) * K[0, (i*n_virt + u) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, (j*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex]

												elif ((u != s) and (u != t) and (t == s) and (w == s) and (v == u)):

													L3[i*n_virt + s] += (-4 * g[i, j, i, n_occ + s] ) * K[0, (i*n_virt + u) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, (j*n_virt + s) * n_ex + j*n_virt + u+ 2*n_ex]

												elif ((u == s) and (t != s) and (w == t) and (v == s)):

													L3[i*n_virt + s] += (-8 * g[i, j, i, n_occ + s] ) * K[0, (i*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (j*n_virt + t) * n_ex + j*n_virt + s+ 2*n_ex]

												elif ((u == t) and (t != s) and (w == t) and (v == s)):

													L3[i*n_virt + s] += (-4 * g[i, j, i, n_occ + t] ) * K[0, (i*n_virt + t) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (j*n_virt + t) * n_ex + j*n_virt + s+ 2*n_ex]

												elif ((u == t) and (t != s) and (w == t) and (v == t)):

													L3[i*n_virt + s] += (-4 * g[i, j, i, n_occ + s] ) * K[0, (i*n_virt + t) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (j*n_virt + t) * n_ex + j*n_virt + t+ 2*n_ex]

												elif ((u != s) and (u != t) and (t != s) and (w == t) and (v == s)):

													L3[i*n_virt + s] += (-4 * g[i, j, i, n_occ + u] ) * K[0, (i*n_virt + u) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (j*n_virt + t) * n_ex + j*n_virt + s+ 2*n_ex]

												elif ((u != s) and (u != t) and (t != s) and (w == t) and (v == u)):

													L3[i*n_virt + s] += (-4 * g[i, j, i, n_occ + s] ) * K[0, (i*n_virt + u) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (j*n_virt + t) * n_ex + j*n_virt + u+ 2*n_ex]

											elif ((k == i) and (j != i) and (n == j) and (m != i) and (m != j) and (m != k)):

												if ((u == s) and (t == s) and (w == s) and (v == s)):

													L3[i*n_virt + s] += (-8 * g[i, m, i, n_occ + s] ) * K[0, (i*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, (j*n_virt + s) * n_ex + m*n_virt + s+ 2*n_ex]

												elif ((u != s) and (u != t) and (t == s) and (w == s) and (v == s)):

													L3[i*n_virt + s] += (-4 * g[i, m, i, n_occ + u] ) * K[0, (i*n_virt + u) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, (j*n_virt + s) * n_ex + m*n_virt + s+ 2*n_ex]

												elif ((u != s) and (u != t) and (t == s) and (w == s) and (v == u)):

													L3[i*n_virt + s] += (-4 * g[i, m, i, n_occ + s] ) * K[0, (i*n_virt + u) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, (j*n_virt + s) * n_ex + m*n_virt + u+ 2*n_ex]

												elif ((u == s) and (t != s) and (w == t) and (v == s)):

													L3[i*n_virt + s] += (-8 * g[i, m, i, n_occ + s] ) * K[0, (i*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (j*n_virt + t) * n_ex + m*n_virt + s+ 2*n_ex]

												elif ((u == t) and (t != s) and (w == t) and (v == s)):

													L3[i*n_virt + s] += (-4 * g[i, m, i, n_occ + t] ) * K[0, (i*n_virt + t) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (j*n_virt + t) * n_ex + m*n_virt + s+ 2*n_ex]

												elif ((u == t) and (t != s) and (w == t) and (v == t)):

													L3[i*n_virt + s] += (-4 * g[i, m, i, n_occ + s] ) * K[0, (i*n_virt + t) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (j*n_virt + t) * n_ex + m*n_virt + t+ 2*n_ex]

												elif ((u != s) and (u != t) and (t != s) and (w == t) and (v == s)):

													L3[i*n_virt + s] += (-4 * g[i, m, i, n_occ + u] ) * K[0, (i*n_virt + u) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (j*n_virt + t) * n_ex + m*n_virt + s+ 2*n_ex]

												elif ((u != s) and (u != t) and (t != s) and (w == t) and (v == u)):

													L3[i*n_virt + s] += (-4 * g[i, m, i, n_occ + s] ) * K[0, (i*n_virt + u) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (j*n_virt + t) * n_ex + m*n_virt + u+ 2*n_ex]

											elif ((k == j) and (j != i) and (n == j) and (m == i)):

												if ((u == s) and (t == s) and (w == s) and (v == s)):

													L3[i*n_virt + s] += (4 * F[j, n_occ + s] + -4 * g[i, j, i, n_occ + s] + 4 * g[j, n_occ + s, n_occ + s, n_occ + s] + -4 * g[i, i, j, n_occ + s] ) * K[0, (j*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, (j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex]

												elif ((u == s) and (t == s) and (w == s) and (v != s) and (v != t) and (v != u)):

													L3[i*n_virt + s] += (4 * g[j, n_occ + s, n_occ + s, n_occ + v] ) * K[0, (j*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, (j*n_virt + s) * n_ex + i*n_virt + v+ 2*n_ex]

												elif ((u != s) and (u != t) and (t == s) and (w == s) and (v == s)):

													L3[i*n_virt + s] += (8 * F[j, n_occ + u] + -4 * g[j, n_occ + s, n_occ + s, n_occ + u] + 8 * g[j, n_occ + u, n_occ + s, n_occ + s] + -8 * g[i, i, j, n_occ + u] + 4 * g[i, j, i, n_occ + u] ) * K[0, (j*n_virt + u) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, (j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex]

												elif ((u != s) and (u != t) and (t == s) and (w == s) and (v == u)):

													L3[i*n_virt + s] += (-4 * F[j, n_occ + s] + 8 * g[j, n_occ + u, n_occ + s, n_occ + u] + -4 * g[j, n_occ + s, n_occ + u, n_occ + u] + 4 * g[i, i, j, n_occ + s] + -8 * g[i, j, i, n_occ + s] ) * K[0, (j*n_virt + u) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, (j*n_virt + s) * n_ex + i*n_virt + u+ 2*n_ex]

												elif ((u != s) and (u != t) and (t == s) and (w == s) and (v != s) and (v != t) and (v != u)):

													L3[i*n_virt + s] += (-4 * g[j, n_occ + s, n_occ + u, n_occ + v] + 8 * g[j, n_occ + u, n_occ + s, n_occ + v] ) * K[0, (j*n_virt + u) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, (j*n_virt + s) * n_ex + i*n_virt + v+ 2*n_ex]

												elif ((u == s) and (t != s) and (w == t) and (v == s)):

													L3[i*n_virt + s] += (4 * F[j, n_occ + s] + -4 * g[i, j, i, n_occ + s] + 4 * g[j, n_occ + s, n_occ + s, n_occ + s] + -4 * g[i, i, j, n_occ + s] ) * K[0, (j*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex]

												elif ((u == s) and (t != s) and (w == t) and (v == t)):

													L3[i*n_virt + s] += (4 * g[j, n_occ + s, n_occ + s, n_occ + t] ) * K[0, (j*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (j*n_virt + t) * n_ex + i*n_virt + t+ 2*n_ex]

												elif ((u == s) and (t != s) and (w == t) and (v != s) and (v != t) and (v != u)):

													L3[i*n_virt + s] += (4 * g[j, n_occ + s, n_occ + s, n_occ + v] ) * K[0, (j*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (j*n_virt + t) * n_ex + i*n_virt + v+ 2*n_ex]

												elif ((u == t) and (t != s) and (w == t) and (v == s)):

													L3[i*n_virt + s] += (8 * F[j, n_occ + t] + -4 * g[j, n_occ + s, n_occ + s, n_occ + t] + 8 * g[j, n_occ + t, n_occ + s, n_occ + s] + -8 * g[i, i, j, n_occ + t] + 4 * g[i, j, i, n_occ + t] ) * K[0, (j*n_virt + t) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex]

												elif ((u == t) and (t != s) and (w == t) and (v == t)):

													L3[i*n_virt + s] += (-4 * F[j, n_occ + s] + 8 * g[j, n_occ + t, n_occ + s, n_occ + t] + -4 * g[j, n_occ + s, n_occ + t, n_occ + t] + 4 * g[i, i, j, n_occ + s] + -8 * g[i, j, i, n_occ + s] ) * K[0, (j*n_virt + t) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (j*n_virt + t) * n_ex + i*n_virt + t+ 2*n_ex]

												elif ((u == t) and (t != s) and (w == t) and (v != s) and (v != t) and (v != u)):

													L3[i*n_virt + s] += (-4 * g[j, n_occ + s, n_occ + t, n_occ + v] + 8 * g[j, n_occ + t, n_occ + s, n_occ + v] ) * K[0, (j*n_virt + t) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (j*n_virt + t) * n_ex + i*n_virt + v+ 2*n_ex]

												elif ((u != s) and (u != t) and (t != s) and (w == t) and (v == s)):

													L3[i*n_virt + s] += (8 * F[j, n_occ + u] + -4 * g[j, n_occ + s, n_occ + s, n_occ + u] + 8 * g[j, n_occ + u, n_occ + s, n_occ + s] + -8 * g[i, i, j, n_occ + u] + 4 * g[i, j, i, n_occ + u] ) * K[0, (j*n_virt + u) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex]

												elif ((u != s) and (u != t) and (t != s) and (w == t) and (v == t)):

													L3[i*n_virt + s] += (-4 * g[j, n_occ + s, n_occ + t, n_occ + u] + 8 * g[j, n_occ + u, n_occ + s, n_occ + t] ) * K[0, (j*n_virt + u) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (j*n_virt + t) * n_ex + i*n_virt + t+ 2*n_ex]

												elif ((u != s) and (u != t) and (t != s) and (w == t) and (v == u)):

													L3[i*n_virt + s] += (-4 * F[j, n_occ + s] + 8 * g[j, n_occ + u, n_occ + s, n_occ + u] + -4 * g[j, n_occ + s, n_occ + u, n_occ + u] + 4 * g[i, i, j, n_occ + s] + -8 * g[i, j, i, n_occ + s] ) * K[0, (j*n_virt + u) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (j*n_virt + t) * n_ex + i*n_virt + u+ 2*n_ex]

												elif ((u != s) and (u != t) and (t != s) and (w == t) and (v != s) and (v != t) and (v != u)):

													L3[i*n_virt + s] += (-4 * g[j, n_occ + s, n_occ + u, n_occ + v] + 8 * g[j, n_occ + u, n_occ + s, n_occ + v] ) * K[0, (j*n_virt + u) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (j*n_virt + t) * n_ex + i*n_virt + v+ 2*n_ex]

											elif ((k == j) and (j != i) and (n == i) and (m == j)):

												if ((u == s) and (t == s) and (w == s) and (v == s)):

													L3[i*n_virt + s] += (-8 * g[i, j, i, n_occ + s] ) * K[0, (j*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, (i*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex]

												elif ((u == s) and (t == s) and (w != s) and (w != t) and (w != u) and (w != v) and (v == s)):

													L3[i*n_virt + s] += (-4 * g[i, j, i, n_occ + w] ) * K[0, (j*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, (i*n_virt + w) * n_ex + j*n_virt + s+ 2*n_ex]

												elif ((u != s) and (u != t) and (t == s) and (w == s) and (v == u)):

													L3[i*n_virt + s] += (-8 * g[i, j, i, n_occ + s] ) * K[0, (j*n_virt + u) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, (i*n_virt + s) * n_ex + j*n_virt + u+ 2*n_ex]

												elif ((u != s) and (u != t) and (t == s) and (w == u) and (v == u)):

													L3[i*n_virt + s] += (-4 * g[i, j, i, n_occ + u] ) * K[0, (j*n_virt + u) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, (i*n_virt + u) * n_ex + j*n_virt + u+ 2*n_ex]

												elif ((u != s) and (u != t) and (t == s) and (w != s) and (w != t) and (w != u) and (w != v) and (v == u)):

													L3[i*n_virt + s] += (-4 * g[i, j, i, n_occ + w] ) * K[0, (j*n_virt + u) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, (i*n_virt + w) * n_ex + j*n_virt + u+ 2*n_ex]

												elif ((u == s) and (t != s) and (w == t) and (v == s)):

													L3[i*n_virt + s] += (-4 * g[i, j, i, n_occ + s] ) * K[0, (j*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (i*n_virt + t) * n_ex + j*n_virt + s+ 2*n_ex]

												elif ((u == t) and (t != s) and (w == t) and (v == t)):

													L3[i*n_virt + s] += (-4 * g[i, j, i, n_occ + s] ) * K[0, (j*n_virt + t) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (i*n_virt + t) * n_ex + j*n_virt + t+ 2*n_ex]

												elif ((u != s) and (u != t) and (t != s) and (w == t) and (v == u)):

													L3[i*n_virt + s] += (-4 * g[i, j, i, n_occ + s] ) * K[0, (j*n_virt + u) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (i*n_virt + t) * n_ex + j*n_virt + u+ 2*n_ex]

											elif ((k == j) and (j != i) and (n == j) and (m == j)):

												if ((u == s) and (t == s) and (w == s) and (v == s)):

													L3[i*n_virt + s] += (-4 * F[i, n_occ + s] + 8 * g[i, n_occ + s, n_occ + s, n_occ + s] + -8 * g[i, j, j, n_occ + s] + -8 * g[i, n_occ + s, j, j] ) * K[0, (j*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, (j*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex]

												elif ((u == s) and (t == s) and (w != s) and (w != t) and (w != u) and (w != v) and (v == s)):

													L3[i*n_virt + s] += (-8 * g[i, j, j, n_occ + w] + 4 * g[i, n_occ + w, j, j] + 8 * g[i, n_occ + s, n_occ + s, n_occ + w] + -4 * g[i, n_occ + w, n_occ + s, n_occ + s] ) * K[0, (j*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, (j*n_virt + w) * n_ex + j*n_virt + s+ 2*n_ex]

												elif ((u == s) and (t == s) and (w == s) and (v != s) and (v != t) and (v != u)):

													L3[i*n_virt + s] += (4 * g[i, n_occ + s, n_occ + s, n_occ + v] ) * K[0, (j*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, (j*n_virt + s) * n_ex + j*n_virt + v+ 2*n_ex]

												elif ((u != s) and (u != t) and (t == s) and (w == s) and (v == s)):

													L3[i*n_virt + s] += (-4 * F[i, n_occ + u] + 8 * g[i, n_occ + s, n_occ + s, n_occ + u] + -4 * g[i, n_occ + u, n_occ + s, n_occ + s] + 4 * g[i, n_occ + u, j, j] + -8 * g[i, j, j, n_occ + u] ) * K[0, (j*n_virt + u) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, (j*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex]

												elif ((u != s) and (u != t) and (t == s) and (w == s) and (v == u)):

													L3[i*n_virt + s] += (-4 * g[i, n_occ + u, n_occ + s, n_occ + u] + 8 * g[i, n_occ + s, n_occ + u, n_occ + u] + 4 * g[i, n_occ + s, n_occ + s, n_occ + s] + -12 * g[i, n_occ + s, j, j] ) * K[0, (j*n_virt + u) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, (j*n_virt + s) * n_ex + j*n_virt + u+ 2*n_ex]

												elif ((u != s) and (u != t) and (t == s) and (w == u) and (v == u)):

													L3[i*n_virt + s] += (-8 * g[i, j, j, n_occ + u] + 4 * g[i, n_occ + u, j, j] + 8 * g[i, n_occ + s, n_occ + s, n_occ + u] + -4 * g[i, n_occ + u, n_occ + s, n_occ + s] ) * K[0, (j*n_virt + u) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, (j*n_virt + u) * n_ex + j*n_virt + u+ 2*n_ex]

												elif ((u != s) and (u != t) and (t == s) and (w != s) and (w != t) and (w != u) and (w != v) and (v == u)):

													L3[i*n_virt + s] += (-8 * g[i, j, j, n_occ + w] + 4 * g[i, n_occ + w, j, j] + 8 * g[i, n_occ + s, n_occ + s, n_occ + w] + -4 * g[i, n_occ + w, n_occ + s, n_occ + s] ) * K[0, (j*n_virt + u) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, (j*n_virt + w) * n_ex + j*n_virt + u+ 2*n_ex]

												elif ((u != s) and (u != t) and (t == s) and (w == s) and (v != s) and (v != t) and (v != u)):

													L3[i*n_virt + s] += (8 * g[i, n_occ + s, n_occ + u, n_occ + v] + -4 * g[i, n_occ + u, n_occ + s, n_occ + v] ) * K[0, (j*n_virt + u) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, (j*n_virt + s) * n_ex + j*n_virt + v+ 2*n_ex]

												elif ((u == s) and (t != s) and (w == s) and (v == s)):

													L3[i*n_virt + s] += (4 * g[i, n_occ + s, n_occ + s, n_occ + t] ) * K[0, (j*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (j*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex]

												elif ((u == s) and (t != s) and (w == t) and (v == s)):

													L3[i*n_virt + s] += (-4 * F[i, n_occ + s] + -12 * g[i, n_occ + s, j, j] + 4 * g[i, n_occ + s, n_occ + s, n_occ + s] + -4 * g[i, n_occ + t, n_occ + s, n_occ + t] + 8 * g[i, n_occ + s, n_occ + t, n_occ + t] ) * K[0, (j*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (j*n_virt + t) * n_ex + j*n_virt + s+ 2*n_ex]

												elif ((u == s) and (t != s) and (w != s) and (w != t) and (w != u) and (w != v) and (v == s)):

													L3[i*n_virt + s] += (8 * g[i, n_occ + s, n_occ + t, n_occ + w] + -4 * g[i, n_occ + w, n_occ + s, n_occ + t] ) * K[0, (j*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (j*n_virt + w) * n_ex + j*n_virt + s+ 2*n_ex]

												elif ((u == s) and (t != s) and (w == t) and (v == t)):

													L3[i*n_virt + s] += (4 * g[i, n_occ + s, n_occ + s, n_occ + t] ) * K[0, (j*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (j*n_virt + t) * n_ex + j*n_virt + t+ 2*n_ex]

												elif ((u == s) and (t != s) and (w == t) and (v != s) and (v != t) and (v != u)):

													L3[i*n_virt + s] += (4 * g[i, n_occ + s, n_occ + s, n_occ + v] ) * K[0, (j*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (j*n_virt + t) * n_ex + j*n_virt + v+ 2*n_ex]

												elif ((u == t) and (t != s) and (w == t) and (v == s)):

													L3[i*n_virt + s] += (-4 * F[i, n_occ + t] + 8 * g[i, n_occ + s, n_occ + s, n_occ + t] + -4 * g[i, n_occ + t, n_occ + s, n_occ + s] + 4 * g[i, n_occ + t, j, j] + -8 * g[i, j, j, n_occ + t] ) * K[0, (j*n_virt + t) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (j*n_virt + t) * n_ex + j*n_virt + s+ 2*n_ex]

												elif ((u == t) and (t != s) and (w == s) and (v == t)):

													L3[i*n_virt + s] += (4 * g[i, n_occ + s, n_occ + s, n_occ + t] ) * K[0, (j*n_virt + t) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (j*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex]

												elif ((u == t) and (t != s) and (w == t) and (v == t)):

													L3[i*n_virt + s] += (-8 * g[i, n_occ + t, n_occ + s, n_occ + t] + 16 * g[i, n_occ + s, n_occ + t, n_occ + t] + 8 * g[i, j, j, n_occ + s] + -16 * g[i, n_occ + s, j, j] ) * K[0, (j*n_virt + t) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (j*n_virt + t) * n_ex + j*n_virt + t+ 2*n_ex]

												elif ((u == t) and (t != s) and (w != s) and (w != t) and (w != u) and (w != v) and (v == t)):

													L3[i*n_virt + s] += (8 * g[i, n_occ + s, n_occ + t, n_occ + w] + -4 * g[i, n_occ + w, n_occ + s, n_occ + t] ) * K[0, (j*n_virt + t) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (j*n_virt + w) * n_ex + j*n_virt + t+ 2*n_ex]

												elif ((u == t) and (t != s) and (w == t) and (v != s) and (v != t) and (v != u)):

													L3[i*n_virt + s] += (8 * g[i, n_occ + s, n_occ + t, n_occ + v] + -4 * g[i, n_occ + t, n_occ + s, n_occ + v] ) * K[0, (j*n_virt + t) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (j*n_virt + t) * n_ex + j*n_virt + v+ 2*n_ex]

												elif ((u != s) and (u != t) and (t != s) and (w == t) and (v == s)):

													L3[i*n_virt + s] += (-4 * F[i, n_occ + u] + 8 * g[i, n_occ + s, n_occ + s, n_occ + u] + -4 * g[i, n_occ + u, n_occ + s, n_occ + s] + 4 * g[i, n_occ + u, j, j] + -8 * g[i, j, j, n_occ + u] ) * K[0, (j*n_virt + u) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (j*n_virt + t) * n_ex + j*n_virt + s+ 2*n_ex]

												elif ((u != s) and (u != t) and (t != s) and (w == t) and (v == t)):

													L3[i*n_virt + s] += (8 * g[i, n_occ + s, n_occ + t, n_occ + u] + -4 * g[i, n_occ + u, n_occ + s, n_occ + t] ) * K[0, (j*n_virt + u) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (j*n_virt + t) * n_ex + j*n_virt + t+ 2*n_ex]

												elif ((u != s) and (u != t) and (t != s) and (w == s) and (v == u)):

													L3[i*n_virt + s] += (4 * g[i, n_occ + s, n_occ + s, n_occ + t] ) * K[0, (j*n_virt + u) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (j*n_virt + s) * n_ex + j*n_virt + u+ 2*n_ex]

												elif ((u != s) and (u != t) and (t != s) and (w == t) and (v == u)):

													L3[i*n_virt + s] += (-4 * g[i, n_occ + u, n_occ + s, n_occ + u] + 8 * g[i, n_occ + s, n_occ + u, n_occ + u] + -4 * g[i, n_occ + t, n_occ + s, n_occ + t] + 8 * g[i, n_occ + s, n_occ + t, n_occ + t] + 8 * g[i, j, j, n_occ + s] + -16 * g[i, n_occ + s, j, j] ) * K[0, (j*n_virt + u) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (j*n_virt + t) * n_ex + j*n_virt + u+ 2*n_ex]

												elif ((u != s) and (u != t) and (t != s) and (w == u) and (v == u)):

													L3[i*n_virt + s] += (8 * g[i, n_occ + s, n_occ + t, n_occ + u] + -4 * g[i, n_occ + u, n_occ + s, n_occ + t] ) * K[0, (j*n_virt + u) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (j*n_virt + u) * n_ex + j*n_virt + u+ 2*n_ex]

												elif ((u != s) and (u != t) and (t != s) and (w != s) and (w != t) and (w != u) and (w != v) and (v == u)):

													L3[i*n_virt + s] += (8 * g[i, n_occ + s, n_occ + t, n_occ + w] + -4 * g[i, n_occ + w, n_occ + s, n_occ + t] ) * K[0, (j*n_virt + u) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (j*n_virt + w) * n_ex + j*n_virt + u+ 2*n_ex]

												elif ((u != s) and (u != t) and (t != s) and (w == t) and (v != s) and (v != t) and (v != u)):

													L3[i*n_virt + s] += (8 * g[i, n_occ + s, n_occ + u, n_occ + v] + -4 * g[i, n_occ + u, n_occ + s, n_occ + v] ) * K[0, (j*n_virt + u) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (j*n_virt + t) * n_ex + j*n_virt + v+ 2*n_ex]

											elif ((k == j) and (j != i) and (n != i) and (n != j) and (n != k) and (n != m) and (m == j)):

												if ((u == s) and (t == s) and (w == s) and (v == s)):

													L3[i*n_virt + s] += (-4 * g[i, j, n, n_occ + s] + -4 * g[i, n_occ + s, j, n] ) * K[0, (j*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, (n*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex]

												elif ((u == s) and (t == s) and (w != s) and (w != t) and (w != u) and (w != v) and (v == s)):

													L3[i*n_virt + s] += (-8 * g[i, j, n, n_occ + w] + 4 * g[i, n_occ + w, j, n] ) * K[0, (j*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, (n*n_virt + w) * n_ex + j*n_virt + s+ 2*n_ex]

												elif ((u != s) and (u != t) and (t == s) and (w == s) and (v == u)):

													L3[i*n_virt + s] += (-4 * g[i, j, n, n_occ + s] + -4 * g[i, n_occ + s, j, n] ) * K[0, (j*n_virt + u) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, (n*n_virt + s) * n_ex + j*n_virt + u+ 2*n_ex]

												elif ((u != s) and (u != t) and (t == s) and (w == u) and (v == u)):

													L3[i*n_virt + s] += (-8 * g[i, j, n, n_occ + u] + 4 * g[i, n_occ + u, j, n] ) * K[0, (j*n_virt + u) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, (n*n_virt + u) * n_ex + j*n_virt + u+ 2*n_ex]

												elif ((u != s) and (u != t) and (t == s) and (w != s) and (w != t) and (w != u) and (w != v) and (v == u)):

													L3[i*n_virt + s] += (-8 * g[i, j, n, n_occ + w] + 4 * g[i, n_occ + w, j, n] ) * K[0, (j*n_virt + u) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, (n*n_virt + w) * n_ex + j*n_virt + u+ 2*n_ex]

												elif ((u == s) and (t != s) and (w == t) and (v == s)):

													L3[i*n_virt + s] += (4 * g[i, j, n, n_occ + s] + -8 * g[i, n_occ + s, j, n] ) * K[0, (j*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (n*n_virt + t) * n_ex + j*n_virt + s+ 2*n_ex]

												elif ((u == t) and (t != s) and (w == t) and (v == t)):

													L3[i*n_virt + s] += (4 * g[i, j, n, n_occ + s] + -8 * g[i, n_occ + s, j, n] ) * K[0, (j*n_virt + t) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (n*n_virt + t) * n_ex + j*n_virt + t+ 2*n_ex]

												elif ((u != s) and (u != t) and (t != s) and (w == t) and (v == u)):

													L3[i*n_virt + s] += (4 * g[i, j, n, n_occ + s] + -8 * g[i, n_occ + s, j, n] ) * K[0, (j*n_virt + u) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (n*n_virt + t) * n_ex + j*n_virt + u+ 2*n_ex]

											elif ((k == j) and (j != i) and (n == j) and (m != i) and (m != j) and (m != k)):

												if ((u == s) and (t == s) and (w == s) and (v == s)):

													L3[i*n_virt + s] += (-4 * g[i, m, j, n_occ + s] + -4 * g[i, n_occ + s, j, m] ) * K[0, (j*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, (j*n_virt + s) * n_ex + m*n_virt + s+ 2*n_ex]

												elif ((u != s) and (u != t) and (t == s) and (w == s) and (v == s)):

													L3[i*n_virt + s] += (-8 * g[i, m, j, n_occ + u] + 4 * g[i, n_occ + u, j, m] ) * K[0, (j*n_virt + u) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, (j*n_virt + s) * n_ex + m*n_virt + s+ 2*n_ex]

												elif ((u != s) and (u != t) and (t == s) and (w == s) and (v == u)):

													L3[i*n_virt + s] += (4 * g[i, m, j, n_occ + s] + -8 * g[i, n_occ + s, j, m] ) * K[0, (j*n_virt + u) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, (j*n_virt + s) * n_ex + m*n_virt + u+ 2*n_ex]

												elif ((u == s) and (t != s) and (w == t) and (v == s)):

													L3[i*n_virt + s] += (-4 * g[i, m, j, n_occ + s] + -4 * g[i, n_occ + s, j, m] ) * K[0, (j*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (j*n_virt + t) * n_ex + m*n_virt + s+ 2*n_ex]

												elif ((u == t) and (t != s) and (w == t) and (v == s)):

													L3[i*n_virt + s] += (-8 * g[i, m, j, n_occ + t] + 4 * g[i, n_occ + t, j, m] ) * K[0, (j*n_virt + t) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (j*n_virt + t) * n_ex + m*n_virt + s+ 2*n_ex]

												elif ((u == t) and (t != s) and (w == t) and (v == t)):

													L3[i*n_virt + s] += (4 * g[i, m, j, n_occ + s] + -8 * g[i, n_occ + s, j, m] ) * K[0, (j*n_virt + t) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (j*n_virt + t) * n_ex + m*n_virt + t+ 2*n_ex]

												elif ((u != s) and (u != t) and (t != s) and (w == t) and (v == s)):

													L3[i*n_virt + s] += (-8 * g[i, m, j, n_occ + u] + 4 * g[i, n_occ + u, j, m] ) * K[0, (j*n_virt + u) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (j*n_virt + t) * n_ex + m*n_virt + s+ 2*n_ex]

												elif ((u != s) and (u != t) and (t != s) and (w == t) and (v == u)):

													L3[i*n_virt + s] += (4 * g[i, m, j, n_occ + s] + -8 * g[i, n_occ + s, j, m] ) * K[0, (j*n_virt + u) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (j*n_virt + t) * n_ex + m*n_virt + u+ 2*n_ex]

											elif ((k != i) and (k != j) and (j != i) and (n == j) and (m == i)):

												if ((u == s) and (t == s) and (w == s) and (v == s)):

													L3[i*n_virt + s] += (4 * F[k, n_occ + s] + -4 * g[i, k, i, n_occ + s] + 4 * g[k, n_occ + s, n_occ + s, n_occ + s] + -4 * g[i, i, k, n_occ + s] ) * K[0, (k*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, (j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex]

												elif ((u == s) and (t == s) and (w == s) and (v != s) and (v != t) and (v != u)):

													L3[i*n_virt + s] += (4 * g[k, n_occ + s, n_occ + s, n_occ + v] ) * K[0, (k*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, (j*n_virt + s) * n_ex + i*n_virt + v+ 2*n_ex]

												elif ((u != s) and (u != t) and (t == s) and (w == s) and (v == s)):

													L3[i*n_virt + s] += (8 * F[k, n_occ + u] + -4 * g[k, n_occ + s, n_occ + s, n_occ + u] + 8 * g[k, n_occ + u, n_occ + s, n_occ + s] + -8 * g[i, i, k, n_occ + u] + 4 * g[i, k, i, n_occ + u] ) * K[0, (k*n_virt + u) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, (j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex]

												elif ((u != s) and (u != t) and (t == s) and (w == s) and (v == u)):

													L3[i*n_virt + s] += (-4 * F[k, n_occ + s] + 8 * g[k, n_occ + u, n_occ + s, n_occ + u] + -4 * g[k, n_occ + s, n_occ + u, n_occ + u] + 4 * g[i, i, k, n_occ + s] + -8 * g[i, k, i, n_occ + s] ) * K[0, (k*n_virt + u) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, (j*n_virt + s) * n_ex + i*n_virt + u+ 2*n_ex]

												elif ((u != s) and (u != t) and (t == s) and (w == s) and (v != s) and (v != t) and (v != u)):

													L3[i*n_virt + s] += (-4 * g[k, n_occ + s, n_occ + u, n_occ + v] + 8 * g[k, n_occ + u, n_occ + s, n_occ + v] ) * K[0, (k*n_virt + u) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, (j*n_virt + s) * n_ex + i*n_virt + v+ 2*n_ex]

												elif ((u == s) and (t != s) and (w == t) and (v == s)):

													L3[i*n_virt + s] += (4 * F[k, n_occ + s] + -4 * g[i, k, i, n_occ + s] + 4 * g[k, n_occ + s, n_occ + s, n_occ + s] + -4 * g[i, i, k, n_occ + s] ) * K[0, (k*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex]

												elif ((u == s) and (t != s) and (w == t) and (v == t)):

													L3[i*n_virt + s] += (4 * g[k, n_occ + s, n_occ + s, n_occ + t] ) * K[0, (k*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (j*n_virt + t) * n_ex + i*n_virt + t+ 2*n_ex]

												elif ((u == s) and (t != s) and (w == t) and (v != s) and (v != t) and (v != u)):

													L3[i*n_virt + s] += (4 * g[k, n_occ + s, n_occ + s, n_occ + v] ) * K[0, (k*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (j*n_virt + t) * n_ex + i*n_virt + v+ 2*n_ex]

												elif ((u == t) and (t != s) and (w == t) and (v == s)):

													L3[i*n_virt + s] += (8 * F[k, n_occ + t] + -4 * g[k, n_occ + s, n_occ + s, n_occ + t] + 8 * g[k, n_occ + t, n_occ + s, n_occ + s] + -8 * g[i, i, k, n_occ + t] + 4 * g[i, k, i, n_occ + t] ) * K[0, (k*n_virt + t) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex]

												elif ((u == t) and (t != s) and (w == t) and (v == t)):

													L3[i*n_virt + s] += (-4 * F[k, n_occ + s] + 8 * g[k, n_occ + t, n_occ + s, n_occ + t] + -4 * g[k, n_occ + s, n_occ + t, n_occ + t] + 4 * g[i, i, k, n_occ + s] + -8 * g[i, k, i, n_occ + s] ) * K[0, (k*n_virt + t) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (j*n_virt + t) * n_ex + i*n_virt + t+ 2*n_ex]

												elif ((u == t) and (t != s) and (w == t) and (v != s) and (v != t) and (v != u)):

													L3[i*n_virt + s] += (-4 * g[k, n_occ + s, n_occ + t, n_occ + v] + 8 * g[k, n_occ + t, n_occ + s, n_occ + v] ) * K[0, (k*n_virt + t) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (j*n_virt + t) * n_ex + i*n_virt + v+ 2*n_ex]

												elif ((u != s) and (u != t) and (t != s) and (w == t) and (v == s)):

													L3[i*n_virt + s] += (8 * F[k, n_occ + u] + -4 * g[k, n_occ + s, n_occ + s, n_occ + u] + 8 * g[k, n_occ + u, n_occ + s, n_occ + s] + -8 * g[i, i, k, n_occ + u] + 4 * g[i, k, i, n_occ + u] ) * K[0, (k*n_virt + u) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex]

												elif ((u != s) and (u != t) and (t != s) and (w == t) and (v == t)):

													L3[i*n_virt + s] += (-4 * g[k, n_occ + s, n_occ + t, n_occ + u] + 8 * g[k, n_occ + u, n_occ + s, n_occ + t] ) * K[0, (k*n_virt + u) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (j*n_virt + t) * n_ex + i*n_virt + t+ 2*n_ex]

												elif ((u != s) and (u != t) and (t != s) and (w == t) and (v == u)):

													L3[i*n_virt + s] += (-4 * F[k, n_occ + s] + 8 * g[k, n_occ + u, n_occ + s, n_occ + u] + -4 * g[k, n_occ + s, n_occ + u, n_occ + u] + 4 * g[i, i, k, n_occ + s] + -8 * g[i, k, i, n_occ + s] ) * K[0, (k*n_virt + u) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (j*n_virt + t) * n_ex + i*n_virt + u+ 2*n_ex]

												elif ((u != s) and (u != t) and (t != s) and (w == t) and (v != s) and (v != t) and (v != u)):

													L3[i*n_virt + s] += (-4 * g[k, n_occ + s, n_occ + u, n_occ + v] + 8 * g[k, n_occ + u, n_occ + s, n_occ + v] ) * K[0, (k*n_virt + u) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (j*n_virt + t) * n_ex + i*n_virt + v+ 2*n_ex]

											elif ((k != i) and (k != j) and (j != i) and (n == j) and (m == j)):

												if ((u == s) and (t == s) and (w == s) and (v == s)):

													L3[i*n_virt + s] += (-4 * g[i, j, k, n_occ + s] + -4 * g[i, n_occ + s, j, k] ) * K[0, (k*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, (j*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex]

												elif ((u != s) and (u != t) and (t == s) and (w == s) and (v == s)):

													L3[i*n_virt + s] += (-8 * g[i, j, k, n_occ + u] + 4 * g[i, n_occ + u, j, k] ) * K[0, (k*n_virt + u) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, (j*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex]

												elif ((u != s) and (u != t) and (t == s) and (w == s) and (v == u)):

													L3[i*n_virt + s] += (4 * g[i, j, k, n_occ + s] + -8 * g[i, n_occ + s, j, k] ) * K[0, (k*n_virt + u) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, (j*n_virt + s) * n_ex + j*n_virt + u+ 2*n_ex]

												elif ((u == s) and (t != s) and (w == t) and (v == s)):

													L3[i*n_virt + s] += (-4 * g[i, j, k, n_occ + s] + -4 * g[i, n_occ + s, j, k] ) * K[0, (k*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (j*n_virt + t) * n_ex + j*n_virt + s+ 2*n_ex]

												elif ((u == t) and (t != s) and (w == t) and (v == s)):

													L3[i*n_virt + s] += (-8 * g[i, j, k, n_occ + t] + 4 * g[i, n_occ + t, j, k] ) * K[0, (k*n_virt + t) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (j*n_virt + t) * n_ex + j*n_virt + s+ 2*n_ex]

												elif ((u == t) and (t != s) and (w == t) and (v == t)):

													L3[i*n_virt + s] += (4 * g[i, j, k, n_occ + s] + -8 * g[i, n_occ + s, j, k] ) * K[0, (k*n_virt + t) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (j*n_virt + t) * n_ex + j*n_virt + t+ 2*n_ex]

												elif ((u != s) and (u != t) and (t != s) and (w == t) and (v == s)):

													L3[i*n_virt + s] += (-8 * g[i, j, k, n_occ + u] + 4 * g[i, n_occ + u, j, k] ) * K[0, (k*n_virt + u) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (j*n_virt + t) * n_ex + j*n_virt + s+ 2*n_ex]

												elif ((u != s) and (u != t) and (t != s) and (w == t) and (v == u)):

													L3[i*n_virt + s] += (4 * g[i, j, k, n_occ + s] + -8 * g[i, n_occ + s, j, k] ) * K[0, (k*n_virt + u) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (j*n_virt + t) * n_ex + j*n_virt + u+ 2*n_ex]

											elif ((k != i) and (k != j) and (j != i) and (n == i) and (m == k)):

												if ((u == s) and (t == s) and (w == s) and (v == s)):

													L3[i*n_virt + s] += (-8 * g[i, j, i, n_occ + s] ) * K[0, (k*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, (i*n_virt + s) * n_ex + k*n_virt + s+ 2*n_ex]

												elif ((u == s) and (t == s) and (w != s) and (w != t) and (w != u) and (w != v) and (v == s)):

													L3[i*n_virt + s] += (-4 * g[i, j, i, n_occ + w] ) * K[0, (k*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, (i*n_virt + w) * n_ex + k*n_virt + s+ 2*n_ex]

												elif ((u != s) and (u != t) and (t == s) and (w == s) and (v == u)):

													L3[i*n_virt + s] += (-8 * g[i, j, i, n_occ + s] ) * K[0, (k*n_virt + u) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, (i*n_virt + s) * n_ex + k*n_virt + u+ 2*n_ex]

												elif ((u != s) and (u != t) and (t == s) and (w == u) and (v == u)):

													L3[i*n_virt + s] += (-4 * g[i, j, i, n_occ + u] ) * K[0, (k*n_virt + u) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, (i*n_virt + u) * n_ex + k*n_virt + u+ 2*n_ex]

												elif ((u != s) and (u != t) and (t == s) and (w != s) and (w != t) and (w != u) and (w != v) and (v == u)):

													L3[i*n_virt + s] += (-4 * g[i, j, i, n_occ + w] ) * K[0, (k*n_virt + u) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, (i*n_virt + w) * n_ex + k*n_virt + u+ 2*n_ex]

												elif ((u == s) and (t != s) and (w == t) and (v == s)):

													L3[i*n_virt + s] += (-4 * g[i, j, i, n_occ + s] ) * K[0, (k*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (i*n_virt + t) * n_ex + k*n_virt + s+ 2*n_ex]

												elif ((u == t) and (t != s) and (w == t) and (v == t)):

													L3[i*n_virt + s] += (-4 * g[i, j, i, n_occ + s] ) * K[0, (k*n_virt + t) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (i*n_virt + t) * n_ex + k*n_virt + t+ 2*n_ex]

												elif ((u != s) and (u != t) and (t != s) and (w == t) and (v == u)):

													L3[i*n_virt + s] += (-4 * g[i, j, i, n_occ + s] ) * K[0, (k*n_virt + u) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (i*n_virt + t) * n_ex + k*n_virt + u+ 2*n_ex]

											elif ((k != i) and (k != j) and (j != i) and (n == j) and (m == k)):

												if ((u == s) and (t == s) and (w == s) and (v == s)):

													L3[i*n_virt + s] += (-4 * F[i, n_occ + s] + 8 * g[i, n_occ + s, n_occ + s, n_occ + s] + -4 * g[i, n_occ + s, j, j] + -4 * g[i, n_occ + s, k, k] + -4 * g[i, j, j, n_occ + s] + -4 * g[i, k, k, n_occ + s] ) * K[0, (k*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, (j*n_virt + s) * n_ex + k*n_virt + s+ 2*n_ex]

												elif ((u == s) and (t == s) and (w != s) and (w != t) and (w != u) and (w != v) and (v == s)):

													L3[i*n_virt + s] += (-8 * g[i, j, j, n_occ + w] + 4 * g[i, n_occ + w, j, j] + 8 * g[i, n_occ + s, n_occ + s, n_occ + w] + -4 * g[i, n_occ + w, n_occ + s, n_occ + s] ) * K[0, (k*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, (j*n_virt + w) * n_ex + k*n_virt + s+ 2*n_ex]

												elif ((u == s) and (t == s) and (w == s) and (v != s) and (v != t) and (v != u)):

													L3[i*n_virt + s] += (4 * g[i, n_occ + s, n_occ + s, n_occ + v] ) * K[0, (k*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, (j*n_virt + s) * n_ex + k*n_virt + v+ 2*n_ex]

												elif ((u != s) and (u != t) and (t == s) and (w == s) and (v == s)):

													L3[i*n_virt + s] += (-4 * F[i, n_occ + u] + 8 * g[i, n_occ + s, n_occ + s, n_occ + u] + -4 * g[i, n_occ + u, n_occ + s, n_occ + s] + 4 * g[i, n_occ + u, k, k] + -8 * g[i, k, k, n_occ + u] ) * K[0, (k*n_virt + u) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, (j*n_virt + s) * n_ex + k*n_virt + s+ 2*n_ex]

												elif ((u != s) and (u != t) and (t == s) and (w == s) and (v == u)):

													L3[i*n_virt + s] += (-4 * g[i, n_occ + u, n_occ + s, n_occ + u] + 8 * g[i, n_occ + s, n_occ + u, n_occ + u] + -4 * g[i, j, j, n_occ + s] + 4 * g[i, n_occ + s, n_occ + s, n_occ + s] + 4 * g[i, k, k, n_occ + s] + -8 * g[i, n_occ + s, k, k] + -4 * g[i, n_occ + s, j, j] ) * K[0, (k*n_virt + u) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, (j*n_virt + s) * n_ex + k*n_virt + u+ 2*n_ex]

												elif ((u != s) and (u != t) and (t == s) and (w == u) and (v == u)):

													L3[i*n_virt + s] += (-8 * g[i, j, j, n_occ + u] + 4 * g[i, n_occ + u, j, j] + 8 * g[i, n_occ + s, n_occ + s, n_occ + u] + -4 * g[i, n_occ + u, n_occ + s, n_occ + s] ) * K[0, (k*n_virt + u) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, (j*n_virt + u) * n_ex + k*n_virt + u+ 2*n_ex]

												elif ((u != s) and (u != t) and (t == s) and (w != s) and (w != t) and (w != u) and (w != v) and (v == u)):

													L3[i*n_virt + s] += (-8 * g[i, j, j, n_occ + w] + 4 * g[i, n_occ + w, j, j] + 8 * g[i, n_occ + s, n_occ + s, n_occ + w] + -4 * g[i, n_occ + w, n_occ + s, n_occ + s] ) * K[0, (k*n_virt + u) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, (j*n_virt + w) * n_ex + k*n_virt + u+ 2*n_ex]

												elif ((u != s) and (u != t) and (t == s) and (w == s) and (v != s) and (v != t) and (v != u)):

													L3[i*n_virt + s] += (8 * g[i, n_occ + s, n_occ + u, n_occ + v] + -4 * g[i, n_occ + u, n_occ + s, n_occ + v] ) * K[0, (k*n_virt + u) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, (j*n_virt + s) * n_ex + k*n_virt + v+ 2*n_ex]

												elif ((u == s) and (t != s) and (w == s) and (v == s)):

													L3[i*n_virt + s] += (4 * g[i, n_occ + s, n_occ + s, n_occ + t] ) * K[0, (k*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (j*n_virt + s) * n_ex + k*n_virt + s+ 2*n_ex]

												elif ((u == s) and (t != s) and (w == t) and (v == s)):

													L3[i*n_virt + s] += (-4 * F[i, n_occ + s] + 4 * g[i, n_occ + s, n_occ + s, n_occ + s] + -4 * g[i, n_occ + t, n_occ + s, n_occ + t] + 8 * g[i, n_occ + s, n_occ + t, n_occ + t] + 4 * g[i, j, j, n_occ + s] + -8 * g[i, n_occ + s, j, j] + -4 * g[i, n_occ + s, k, k] + -4 * g[i, k, k, n_occ + s] ) * K[0, (k*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (j*n_virt + t) * n_ex + k*n_virt + s+ 2*n_ex]

												elif ((u == s) and (t != s) and (w != s) and (w != t) and (w != u) and (w != v) and (v == s)):

													L3[i*n_virt + s] += (8 * g[i, n_occ + s, n_occ + t, n_occ + w] + -4 * g[i, n_occ + w, n_occ + s, n_occ + t] ) * K[0, (k*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (j*n_virt + w) * n_ex + k*n_virt + s+ 2*n_ex]

												elif ((u == s) and (t != s) and (w == t) and (v == t)):

													L3[i*n_virt + s] += (4 * g[i, n_occ + s, n_occ + s, n_occ + t] ) * K[0, (k*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (j*n_virt + t) * n_ex + k*n_virt + t+ 2*n_ex]

												elif ((u == s) and (t != s) and (w == t) and (v != s) and (v != t) and (v != u)):

													L3[i*n_virt + s] += (4 * g[i, n_occ + s, n_occ + s, n_occ + v] ) * K[0, (k*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (j*n_virt + t) * n_ex + k*n_virt + v+ 2*n_ex]

												elif ((u == t) and (t != s) and (w == t) and (v == s)):

													L3[i*n_virt + s] += (-4 * F[i, n_occ + t] + 8 * g[i, n_occ + s, n_occ + s, n_occ + t] + -4 * g[i, n_occ + t, n_occ + s, n_occ + s] + 4 * g[i, n_occ + t, k, k] + -8 * g[i, k, k, n_occ + t] ) * K[0, (k*n_virt + t) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (j*n_virt + t) * n_ex + k*n_virt + s+ 2*n_ex]

												elif ((u == t) and (t != s) and (w == s) and (v == t)):

													L3[i*n_virt + s] += (4 * g[i, n_occ + s, n_occ + s, n_occ + t] ) * K[0, (k*n_virt + t) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (j*n_virt + s) * n_ex + k*n_virt + t+ 2*n_ex]

												elif ((u == t) and (t != s) and (w == t) and (v == t)):

													L3[i*n_virt + s] += (-8 * g[i, n_occ + t, n_occ + s, n_occ + t] + 16 * g[i, n_occ + s, n_occ + t, n_occ + t] + 4 * g[i, j, j, n_occ + s] + 4 * g[i, k, k, n_occ + s] + -8 * g[i, n_occ + s, j, j] + -8 * g[i, n_occ + s, k, k] ) * K[0, (k*n_virt + t) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (j*n_virt + t) * n_ex + k*n_virt + t+ 2*n_ex]

												elif ((u == t) and (t != s) and (w != s) and (w != t) and (w != u) and (w != v) and (v == t)):

													L3[i*n_virt + s] += (8 * g[i, n_occ + s, n_occ + t, n_occ + w] + -4 * g[i, n_occ + w, n_occ + s, n_occ + t] ) * K[0, (k*n_virt + t) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (j*n_virt + w) * n_ex + k*n_virt + t+ 2*n_ex]

												elif ((u == t) and (t != s) and (w == t) and (v != s) and (v != t) and (v != u)):

													L3[i*n_virt + s] += (8 * g[i, n_occ + s, n_occ + t, n_occ + v] + -4 * g[i, n_occ + t, n_occ + s, n_occ + v] ) * K[0, (k*n_virt + t) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (j*n_virt + t) * n_ex + k*n_virt + v+ 2*n_ex]

												elif ((u != s) and (u != t) and (t != s) and (w == t) and (v == s)):

													L3[i*n_virt + s] += (-4 * F[i, n_occ + u] + 8 * g[i, n_occ + s, n_occ + s, n_occ + u] + -4 * g[i, n_occ + u, n_occ + s, n_occ + s] + 4 * g[i, n_occ + u, k, k] + -8 * g[i, k, k, n_occ + u] ) * K[0, (k*n_virt + u) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (j*n_virt + t) * n_ex + k*n_virt + s+ 2*n_ex]

												elif ((u != s) and (u != t) and (t != s) and (w == t) and (v == t)):

													L3[i*n_virt + s] += (8 * g[i, n_occ + s, n_occ + t, n_occ + u] + -4 * g[i, n_occ + u, n_occ + s, n_occ + t] ) * K[0, (k*n_virt + u) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (j*n_virt + t) * n_ex + k*n_virt + t+ 2*n_ex]

												elif ((u != s) and (u != t) and (t != s) and (w == s) and (v == u)):

													L3[i*n_virt + s] += (4 * g[i, n_occ + s, n_occ + s, n_occ + t] ) * K[0, (k*n_virt + u) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (j*n_virt + s) * n_ex + k*n_virt + u+ 2*n_ex]

												elif ((u != s) and (u != t) and (t != s) and (w == t) and (v == u)):

													L3[i*n_virt + s] += (-4 * g[i, n_occ + u, n_occ + s, n_occ + u] + 8 * g[i, n_occ + s, n_occ + u, n_occ + u] + -4 * g[i, n_occ + t, n_occ + s, n_occ + t] + 8 * g[i, n_occ + s, n_occ + t, n_occ + t] + 4 * g[i, j, j, n_occ + s] + 4 * g[i, k, k, n_occ + s] + -8 * g[i, n_occ + s, j, j] + -8 * g[i, n_occ + s, k, k] ) * K[0, (k*n_virt + u) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (j*n_virt + t) * n_ex + k*n_virt + u+ 2*n_ex]

												elif ((u != s) and (u != t) and (t != s) and (w == u) and (v == u)):

													L3[i*n_virt + s] += (8 * g[i, n_occ + s, n_occ + t, n_occ + u] + -4 * g[i, n_occ + u, n_occ + s, n_occ + t] ) * K[0, (k*n_virt + u) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (j*n_virt + u) * n_ex + k*n_virt + u+ 2*n_ex]

												elif ((u != s) and (u != t) and (t != s) and (w != s) and (w != t) and (w != u) and (w != v) and (v == u)):

													L3[i*n_virt + s] += (8 * g[i, n_occ + s, n_occ + t, n_occ + w] + -4 * g[i, n_occ + w, n_occ + s, n_occ + t] ) * K[0, (k*n_virt + u) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (j*n_virt + w) * n_ex + k*n_virt + u+ 2*n_ex]

												elif ((u != s) and (u != t) and (t != s) and (w == t) and (v != s) and (v != t) and (v != u)):

													L3[i*n_virt + s] += (8 * g[i, n_occ + s, n_occ + u, n_occ + v] + -4 * g[i, n_occ + u, n_occ + s, n_occ + v] ) * K[0, (k*n_virt + u) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (j*n_virt + t) * n_ex + k*n_virt + v+ 2*n_ex]

											elif ((k != i) and (k != j) and (j != i) and (n == k) and (m == k)):

												if ((u == s) and (t == s) and (w == s) and (v == s)):

													L3[i*n_virt + s] += (-4 * g[i, j, k, n_occ + s] + -4 * g[i, n_occ + s, j, k] ) * K[0, (k*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, (k*n_virt + s) * n_ex + k*n_virt + s+ 2*n_ex]

												elif ((u == s) and (t == s) and (w != s) and (w != t) and (w != u) and (w != v) and (v == s)):

													L3[i*n_virt + s] += (-8 * g[i, j, k, n_occ + w] + 4 * g[i, n_occ + w, j, k] ) * K[0, (k*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, (k*n_virt + w) * n_ex + k*n_virt + s+ 2*n_ex]

												elif ((u != s) and (u != t) and (t == s) and (w == s) and (v == u)):

													L3[i*n_virt + s] += (-4 * g[i, j, k, n_occ + s] + -4 * g[i, n_occ + s, j, k] ) * K[0, (k*n_virt + u) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, (k*n_virt + s) * n_ex + k*n_virt + u+ 2*n_ex]

												elif ((u != s) and (u != t) and (t == s) and (w == u) and (v == u)):

													L3[i*n_virt + s] += (-8 * g[i, j, k, n_occ + u] + 4 * g[i, n_occ + u, j, k] ) * K[0, (k*n_virt + u) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, (k*n_virt + u) * n_ex + k*n_virt + u+ 2*n_ex]

												elif ((u != s) and (u != t) and (t == s) and (w != s) and (w != t) and (w != u) and (w != v) and (v == u)):

													L3[i*n_virt + s] += (-8 * g[i, j, k, n_occ + w] + 4 * g[i, n_occ + w, j, k] ) * K[0, (k*n_virt + u) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, (k*n_virt + w) * n_ex + k*n_virt + u+ 2*n_ex]

												elif ((u == s) and (t != s) and (w == t) and (v == s)):

													L3[i*n_virt + s] += (4 * g[i, j, k, n_occ + s] + -8 * g[i, n_occ + s, j, k] ) * K[0, (k*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (k*n_virt + t) * n_ex + k*n_virt + s+ 2*n_ex]

												elif ((u == t) and (t != s) and (w == t) and (v == t)):

													L3[i*n_virt + s] += (4 * g[i, j, k, n_occ + s] + -8 * g[i, n_occ + s, j, k] ) * K[0, (k*n_virt + t) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (k*n_virt + t) * n_ex + k*n_virt + t+ 2*n_ex]

												elif ((u != s) and (u != t) and (t != s) and (w == t) and (v == u)):

													L3[i*n_virt + s] += (4 * g[i, j, k, n_occ + s] + -8 * g[i, n_occ + s, j, k] ) * K[0, (k*n_virt + u) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (k*n_virt + t) * n_ex + k*n_virt + u+ 2*n_ex]

											elif ((k != i) and (k != j) and (j != i) and (n != i) and (n != j) and (n != k) and (n != m) and (m == k)):

												if ((u == s) and (t == s) and (w == s) and (v == s)):

													L3[i*n_virt + s] += (-4 * g[i, j, n, n_occ + s] + -4 * g[i, n_occ + s, j, n] ) * K[0, (k*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, (n*n_virt + s) * n_ex + k*n_virt + s+ 2*n_ex]

												elif ((u == s) and (t == s) and (w != s) and (w != t) and (w != u) and (w != v) and (v == s)):

													L3[i*n_virt + s] += (-8 * g[i, j, n, n_occ + w] + 4 * g[i, n_occ + w, j, n] ) * K[0, (k*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, (n*n_virt + w) * n_ex + k*n_virt + s+ 2*n_ex]

												elif ((u != s) and (u != t) and (t == s) and (w == s) and (v == u)):

													L3[i*n_virt + s] += (-4 * g[i, j, n, n_occ + s] + -4 * g[i, n_occ + s, j, n] ) * K[0, (k*n_virt + u) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, (n*n_virt + s) * n_ex + k*n_virt + u+ 2*n_ex]

												elif ((u != s) and (u != t) and (t == s) and (w == u) and (v == u)):

													L3[i*n_virt + s] += (-8 * g[i, j, n, n_occ + u] + 4 * g[i, n_occ + u, j, n] ) * K[0, (k*n_virt + u) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, (n*n_virt + u) * n_ex + k*n_virt + u+ 2*n_ex]

												elif ((u != s) and (u != t) and (t == s) and (w != s) and (w != t) and (w != u) and (w != v) and (v == u)):

													L3[i*n_virt + s] += (-8 * g[i, j, n, n_occ + w] + 4 * g[i, n_occ + w, j, n] ) * K[0, (k*n_virt + u) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, (n*n_virt + w) * n_ex + k*n_virt + u+ 2*n_ex]

												elif ((u == s) and (t != s) and (w == t) and (v == s)):

													L3[i*n_virt + s] += (4 * g[i, j, n, n_occ + s] + -8 * g[i, n_occ + s, j, n] ) * K[0, (k*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (n*n_virt + t) * n_ex + k*n_virt + s+ 2*n_ex]

												elif ((u == t) and (t != s) and (w == t) and (v == t)):

													L3[i*n_virt + s] += (4 * g[i, j, n, n_occ + s] + -8 * g[i, n_occ + s, j, n] ) * K[0, (k*n_virt + t) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (n*n_virt + t) * n_ex + k*n_virt + t+ 2*n_ex]

												elif ((u != s) and (u != t) and (t != s) and (w == t) and (v == u)):

													L3[i*n_virt + s] += (4 * g[i, j, n, n_occ + s] + -8 * g[i, n_occ + s, j, n] ) * K[0, (k*n_virt + u) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (n*n_virt + t) * n_ex + k*n_virt + u+ 2*n_ex]

											elif ((k != i) and (k != j) and (j != i) and (n == j) and (m != i) and (m != j) and (m != k)):

												if ((u == s) and (t == s) and (w == s) and (v == s)):

													L3[i*n_virt + s] += (-4 * g[i, m, k, n_occ + s] + -4 * g[i, n_occ + s, k, m] ) * K[0, (k*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, (j*n_virt + s) * n_ex + m*n_virt + s+ 2*n_ex]

												elif ((u != s) and (u != t) and (t == s) and (w == s) and (v == s)):

													L3[i*n_virt + s] += (-8 * g[i, m, k, n_occ + u] + 4 * g[i, n_occ + u, k, m] ) * K[0, (k*n_virt + u) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, (j*n_virt + s) * n_ex + m*n_virt + s+ 2*n_ex]

												elif ((u != s) and (u != t) and (t == s) and (w == s) and (v == u)):

													L3[i*n_virt + s] += (4 * g[i, m, k, n_occ + s] + -8 * g[i, n_occ + s, k, m] ) * K[0, (k*n_virt + u) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, (j*n_virt + s) * n_ex + m*n_virt + u+ 2*n_ex]

												elif ((u == s) and (t != s) and (w == t) and (v == s)):

													L3[i*n_virt + s] += (-4 * g[i, m, k, n_occ + s] + -4 * g[i, n_occ + s, k, m] ) * K[0, (k*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (j*n_virt + t) * n_ex + m*n_virt + s+ 2*n_ex]

												elif ((u == t) and (t != s) and (w == t) and (v == s)):

													L3[i*n_virt + s] += (-8 * g[i, m, k, n_occ + t] + 4 * g[i, n_occ + t, k, m] ) * K[0, (k*n_virt + t) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (j*n_virt + t) * n_ex + m*n_virt + s+ 2*n_ex]

												elif ((u == t) and (t != s) and (w == t) and (v == t)):

													L3[i*n_virt + s] += (4 * g[i, m, k, n_occ + s] + -8 * g[i, n_occ + s, k, m] ) * K[0, (k*n_virt + t) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (j*n_virt + t) * n_ex + m*n_virt + t+ 2*n_ex]

												elif ((u != s) and (u != t) and (t != s) and (w == t) and (v == s)):

													L3[i*n_virt + s] += (-8 * g[i, m, k, n_occ + u] + 4 * g[i, n_occ + u, k, m] ) * K[0, (k*n_virt + u) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (j*n_virt + t) * n_ex + m*n_virt + s+ 2*n_ex]

												elif ((u != s) and (u != t) and (t != s) and (w == t) and (v == u)):

													L3[i*n_virt + s] += (4 * g[i, m, k, n_occ + s] + -8 * g[i, n_occ + s, k, m] ) * K[0, (k*n_virt + u) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (j*n_virt + t) * n_ex + m*n_virt + u+ 2*n_ex]

	# This operator combination: {'a': 3, 'b': 3, 'c': 2}
	for i in range(n_occ):
		for k in range(n_occ):
			for j in range(n_occ):
				for n in range(n_occ):
					for m in range(n_occ):
						for s in range(n_virt):
							for u in range(n_virt):
								for t in range(n_virt):
									for w in range(n_virt):
										for v in range(n_virt):

											if ((k == i) and (j == i) and (n == i) and (m == i)):

												if ((u == s) and (t == s) and (w == s) and (v == s)):

													L3[i*n_virt + s + n_ex] += (16 * g[i, i, i, n_occ + s] + -16 * g[i, n_occ + s, n_occ + s, n_occ + s] ) * K[0, (i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] * K[1, (i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex]

												elif ((u == s) and (t == s) and (w != s) and (w != t) and (w != u) and (w != v) and (v == s)):

													L3[i*n_virt + s + n_ex] += (-8 * g[i, n_occ + s, n_occ + s, n_occ + w] ) * K[0, (i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] * K[1, (i*n_virt + w) * n_ex + i*n_virt + s+ 2*n_ex]

												elif ((u == s) and (t == s) and (w == s) and (v != s) and (v != t) and (v != u)):

													L3[i*n_virt + s + n_ex] += (4 * g[i, i, i, n_occ + v] + -4 * g[i, n_occ + v, n_occ + s, n_occ + s] + -4 * g[i, n_occ + s, n_occ + s, n_occ + v] ) * K[0, (i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] * K[1, (i*n_virt + s) * n_ex + i*n_virt + v+ 2*n_ex]

												elif ((u != s) and (u != t) and (t == s) and (w == s) and (v == s)):

													L3[i*n_virt + s + n_ex] += (-8 * g[i, n_occ + s, n_occ + s, n_occ + u] ) * K[0, (i*n_virt + u) * n_ex + i*n_virt + s+ 2*n_ex] * K[1, (i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex]

												elif ((u != s) and (u != t) and (t == s) and (w == s) and (v == u)):

													L3[i*n_virt + s + n_ex] += (12 * g[i, i, i, n_occ + s] + -8 * g[i, n_occ + s, n_occ + s, n_occ + s] + -4 * g[i, n_occ + u, n_occ + s, n_occ + u] + -4 * g[i, n_occ + s, n_occ + u, n_occ + u] ) * K[0, (i*n_virt + u) * n_ex + i*n_virt + s+ 2*n_ex] * K[1, (i*n_virt + s) * n_ex + i*n_virt + u+ 2*n_ex]

												elif ((u != s) and (u != t) and (t == s) and (w == u) and (v == u)):

													L3[i*n_virt + s + n_ex] += (-8 * g[i, n_occ + s, n_occ + s, n_occ + u] ) * K[0, (i*n_virt + u) * n_ex + i*n_virt + s+ 2*n_ex] * K[1, (i*n_virt + u) * n_ex + i*n_virt + u+ 2*n_ex]

												elif ((u != s) and (u != t) and (t == s) and (w != s) and (w != t) and (w != u) and (w != v) and (v == u)):

													L3[i*n_virt + s + n_ex] += (-8 * g[i, n_occ + s, n_occ + s, n_occ + w] ) * K[0, (i*n_virt + u) * n_ex + i*n_virt + s+ 2*n_ex] * K[1, (i*n_virt + w) * n_ex + i*n_virt + u+ 2*n_ex]

												elif ((u != s) and (u != t) and (t == s) and (w == s) and (v != s) and (v != t) and (v != u)):

													L3[i*n_virt + s + n_ex] += (-4 * g[i, n_occ + v, n_occ + s, n_occ + u] + -4 * g[i, n_occ + s, n_occ + u, n_occ + v] ) * K[0, (i*n_virt + u) * n_ex + i*n_virt + s+ 2*n_ex] * K[1, (i*n_virt + s) * n_ex + i*n_virt + v+ 2*n_ex]

												elif ((u == s) and (t != s) and (w == s) and (v == s)):

													L3[i*n_virt + s + n_ex] += (-4 * F[i, n_occ + t] + -4 * g[i, n_occ + t, n_occ + s, n_occ + s] + -4 * g[i, n_occ + s, n_occ + s, n_occ + t] + 4 * g[i, i, i, n_occ + t] ) * K[0, (i*n_virt + s) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, (i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex]

												elif ((u == s) and (t != s) and (w == t) and (v == s)):

													L3[i*n_virt + s + n_ex] += (4 * F[i, n_occ + s] + 12 * g[i, i, i, n_occ + s] + -4 * g[i, n_occ + t, n_occ + s, n_occ + t] + -4 * g[i, n_occ + s, n_occ + t, n_occ + t] + -8 * g[i, n_occ + s, n_occ + s, n_occ + s] ) * K[0, (i*n_virt + s) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, (i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex]

												elif ((u == s) and (t != s) and (w != s) and (w != t) and (w != u) and (w != v) and (v == s)):

													L3[i*n_virt + s + n_ex] += (-4 * g[i, n_occ + t, n_occ + s, n_occ + w] + -4 * g[i, n_occ + s, n_occ + t, n_occ + w] ) * K[0, (i*n_virt + s) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, (i*n_virt + w) * n_ex + i*n_virt + s+ 2*n_ex]

												elif ((u == s) and (t != s) and (w == t) and (v == t)):

													L3[i*n_virt + s + n_ex] += (4 * g[i, i, i, n_occ + t] + -4 * g[i, n_occ + t, n_occ + s, n_occ + s] + -4 * g[i, n_occ + s, n_occ + s, n_occ + t] ) * K[0, (i*n_virt + s) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, (i*n_virt + t) * n_ex + i*n_virt + t+ 2*n_ex]

												elif ((u == s) and (t != s) and (w == t) and (v != s) and (v != t) and (v != u)):

													L3[i*n_virt + s + n_ex] += (4 * g[i, i, i, n_occ + v] + -4 * g[i, n_occ + v, n_occ + s, n_occ + s] + -4 * g[i, n_occ + s, n_occ + s, n_occ + v] ) * K[0, (i*n_virt + s) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, (i*n_virt + t) * n_ex + i*n_virt + v+ 2*n_ex]

												elif ((u == t) and (t != s) and (w == t) and (v == s)):

													L3[i*n_virt + s + n_ex] += (-8 * g[i, n_occ + s, n_occ + s, n_occ + t] ) * K[0, (i*n_virt + t) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, (i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex]

												elif ((u == t) and (t != s) and (w == s) and (v == t)):

													L3[i*n_virt + s + n_ex] += (-4 * F[i, n_occ + t] + -4 * g[i, n_occ + t, n_occ + s, n_occ + s] + -4 * g[i, n_occ + s, n_occ + s, n_occ + t] + 4 * g[i, i, i, n_occ + t] ) * K[0, (i*n_virt + t) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, (i*n_virt + s) * n_ex + i*n_virt + t+ 2*n_ex]

												elif ((u == t) and (t != s) and (w == t) and (v == t)):

													L3[i*n_virt + s + n_ex] += (4 * F[i, n_occ + s] + 8 * g[i, i, i, n_occ + s] + -8 * g[i, n_occ + t, n_occ + s, n_occ + t] + -8 * g[i, n_occ + s, n_occ + t, n_occ + t] ) * K[0, (i*n_virt + t) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, (i*n_virt + t) * n_ex + i*n_virt + t+ 2*n_ex]

												elif ((u == t) and (t != s) and (w != s) and (w != t) and (w != u) and (w != v) and (v == t)):

													L3[i*n_virt + s + n_ex] += (-4 * g[i, n_occ + t, n_occ + s, n_occ + w] + -4 * g[i, n_occ + s, n_occ + t, n_occ + w] ) * K[0, (i*n_virt + t) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, (i*n_virt + w) * n_ex + i*n_virt + t+ 2*n_ex]

												elif ((u == t) and (t != s) and (w == t) and (v != s) and (v != t) and (v != u)):

													L3[i*n_virt + s + n_ex] += (-4 * g[i, n_occ + v, n_occ + s, n_occ + t] + -4 * g[i, n_occ + s, n_occ + t, n_occ + v] ) * K[0, (i*n_virt + t) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, (i*n_virt + t) * n_ex + i*n_virt + v+ 2*n_ex]

												elif ((u != s) and (u != t) and (t != s) and (w == t) and (v == s)):

													L3[i*n_virt + s + n_ex] += (-8 * g[i, n_occ + s, n_occ + s, n_occ + u] ) * K[0, (i*n_virt + u) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, (i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex]

												elif ((u != s) and (u != t) and (t != s) and (w == t) and (v == t)):

													L3[i*n_virt + s + n_ex] += (-4 * g[i, n_occ + t, n_occ + s, n_occ + u] + -4 * g[i, n_occ + s, n_occ + t, n_occ + u] ) * K[0, (i*n_virt + u) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, (i*n_virt + t) * n_ex + i*n_virt + t+ 2*n_ex]

												elif ((u != s) and (u != t) and (t != s) and (w == s) and (v == u)):

													L3[i*n_virt + s + n_ex] += (-4 * F[i, n_occ + t] + -4 * g[i, n_occ + t, n_occ + s, n_occ + s] + -4 * g[i, n_occ + s, n_occ + s, n_occ + t] + 4 * g[i, i, i, n_occ + t] ) * K[0, (i*n_virt + u) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, (i*n_virt + s) * n_ex + i*n_virt + u+ 2*n_ex]

												elif ((u != s) and (u != t) and (t != s) and (w == t) and (v == u)):

													L3[i*n_virt + s + n_ex] += (4 * F[i, n_occ + s] + 8 * g[i, i, i, n_occ + s] + -4 * g[i, n_occ + t, n_occ + s, n_occ + t] + -4 * g[i, n_occ + s, n_occ + t, n_occ + t] + -4 * g[i, n_occ + u, n_occ + s, n_occ + u] + -4 * g[i, n_occ + s, n_occ + u, n_occ + u] ) * K[0, (i*n_virt + u) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, (i*n_virt + t) * n_ex + i*n_virt + u+ 2*n_ex]

												elif ((u != s) and (u != t) and (t != s) and (w == u) and (v == u)):

													L3[i*n_virt + s + n_ex] += (-4 * g[i, n_occ + t, n_occ + s, n_occ + u] + -4 * g[i, n_occ + s, n_occ + t, n_occ + u] ) * K[0, (i*n_virt + u) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, (i*n_virt + u) * n_ex + i*n_virt + u+ 2*n_ex]

												elif ((u != s) and (u != t) and (t != s) and (w != s) and (w != t) and (w != u) and (w != v) and (v == u)):

													L3[i*n_virt + s + n_ex] += (-4 * g[i, n_occ + t, n_occ + s, n_occ + w] + -4 * g[i, n_occ + s, n_occ + t, n_occ + w] ) * K[0, (i*n_virt + u) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, (i*n_virt + w) * n_ex + i*n_virt + u+ 2*n_ex]

												elif ((u != s) and (u != t) and (t != s) and (w == t) and (v != s) and (v != t) and (v != u)):

													L3[i*n_virt + s + n_ex] += (-4 * g[i, n_occ + v, n_occ + s, n_occ + u] + -4 * g[i, n_occ + s, n_occ + u, n_occ + v] ) * K[0, (i*n_virt + u) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, (i*n_virt + t) * n_ex + i*n_virt + v+ 2*n_ex]

											elif ((k == i) and (j == i) and (n != i) and (n != j) and (n != k) and (n != m) and (m == i)):

												if ((u == s) and (t == s) and (w == s) and (v == s)):

													L3[i*n_virt + s + n_ex] += (8 * g[i, n, i, n_occ + s] ) * K[0, (i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] * K[1, (n*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex]

												elif ((u != s) and (u != t) and (t == s) and (w == s) and (v == u)):

													L3[i*n_virt + s + n_ex] += (8 * g[i, n, i, n_occ + s] ) * K[0, (i*n_virt + u) * n_ex + i*n_virt + s+ 2*n_ex] * K[1, (n*n_virt + s) * n_ex + i*n_virt + u+ 2*n_ex]

												elif ((u == s) and (t != s) and (w == s) and (v == s)):

													L3[i*n_virt + s + n_ex] += (4 * g[i, n, i, n_occ + t] ) * K[0, (i*n_virt + s) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, (n*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex]

												elif ((u == s) and (t != s) and (w == t) and (v == s)):

													L3[i*n_virt + s + n_ex] += (4 * g[i, n, i, n_occ + s] ) * K[0, (i*n_virt + s) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, (n*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex]

												elif ((u == t) and (t != s) and (w == s) and (v == t)):

													L3[i*n_virt + s + n_ex] += (4 * g[i, n, i, n_occ + t] ) * K[0, (i*n_virt + t) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, (n*n_virt + s) * n_ex + i*n_virt + t+ 2*n_ex]

												elif ((u == t) and (t != s) and (w == t) and (v == t)):

													L3[i*n_virt + s + n_ex] += (4 * g[i, n, i, n_occ + s] ) * K[0, (i*n_virt + t) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, (n*n_virt + t) * n_ex + i*n_virt + t+ 2*n_ex]

												elif ((u != s) and (u != t) and (t != s) and (w == s) and (v == u)):

													L3[i*n_virt + s + n_ex] += (4 * g[i, n, i, n_occ + t] ) * K[0, (i*n_virt + u) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, (n*n_virt + s) * n_ex + i*n_virt + u+ 2*n_ex]

												elif ((u != s) and (u != t) and (t != s) and (w == t) and (v == u)):

													L3[i*n_virt + s + n_ex] += (4 * g[i, n, i, n_occ + s] ) * K[0, (i*n_virt + u) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, (n*n_virt + t) * n_ex + i*n_virt + u+ 2*n_ex]

											elif ((k == i) and (j == i) and (n == i) and (m != i) and (m != j) and (m != k)):

												if ((u == s) and (t == s) and (w == s) and (v == s)):

													L3[i*n_virt + s + n_ex] += (4 * g[i, i, m, n_occ + s] + -4 * g[m, n_occ + s, n_occ + s, n_occ + s] + 4 * g[i, m, i, n_occ + s] ) * K[0, (i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] * K[1, (i*n_virt + s) * n_ex + m*n_virt + s+ 2*n_ex]

												elif ((u == s) and (t == s) and (w == s) and (v != s) and (v != t) and (v != u)):

													L3[i*n_virt + s + n_ex] += (-4 * g[i, m, i, n_occ + v] + 8 * g[i, i, m, n_occ + v] + 4 * g[m, n_occ + s, n_occ + s, n_occ + v] + -8 * g[m, n_occ + v, n_occ + s, n_occ + s] ) * K[0, (i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] * K[1, (i*n_virt + s) * n_ex + m*n_virt + v+ 2*n_ex]

												elif ((u != s) and (u != t) and (t == s) and (w == s) and (v == s)):

													L3[i*n_virt + s + n_ex] += (-4 * g[m, n_occ + s, n_occ + s, n_occ + u] ) * K[0, (i*n_virt + u) * n_ex + i*n_virt + s+ 2*n_ex] * K[1, (i*n_virt + s) * n_ex + m*n_virt + s+ 2*n_ex]

												elif ((u != s) and (u != t) and (t == s) and (w == s) and (v == u)):

													L3[i*n_virt + s + n_ex] += (8 * g[i, m, i, n_occ + s] + -4 * g[i, i, m, n_occ + s] + -8 * g[m, n_occ + u, n_occ + s, n_occ + u] + 4 * g[m, n_occ + s, n_occ + u, n_occ + u] ) * K[0, (i*n_virt + u) * n_ex + i*n_virt + s+ 2*n_ex] * K[1, (i*n_virt + s) * n_ex + m*n_virt + u+ 2*n_ex]

												elif ((u != s) and (u != t) and (t == s) and (w == s) and (v != s) and (v != t) and (v != u)):

													L3[i*n_virt + s + n_ex] += (4 * g[m, n_occ + s, n_occ + u, n_occ + v] + -8 * g[m, n_occ + v, n_occ + s, n_occ + u] ) * K[0, (i*n_virt + u) * n_ex + i*n_virt + s+ 2*n_ex] * K[1, (i*n_virt + s) * n_ex + m*n_virt + v+ 2*n_ex]

												elif ((u == s) and (t != s) and (w == t) and (v == s)):

													L3[i*n_virt + s + n_ex] += (4 * g[i, i, m, n_occ + s] + -4 * g[m, n_occ + s, n_occ + s, n_occ + s] + 4 * g[i, m, i, n_occ + s] ) * K[0, (i*n_virt + s) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, (i*n_virt + t) * n_ex + m*n_virt + s+ 2*n_ex]

												elif ((u == s) and (t != s) and (w == t) and (v == t)):

													L3[i*n_virt + s + n_ex] += (-4 * g[i, m, i, n_occ + t] + 8 * g[i, i, m, n_occ + t] + 4 * g[m, n_occ + s, n_occ + s, n_occ + t] + -8 * g[m, n_occ + t, n_occ + s, n_occ + s] ) * K[0, (i*n_virt + s) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, (i*n_virt + t) * n_ex + m*n_virt + t+ 2*n_ex]

												elif ((u == s) and (t != s) and (w == t) and (v != s) and (v != t) and (v != u)):

													L3[i*n_virt + s + n_ex] += (-4 * g[i, m, i, n_occ + v] + 8 * g[i, i, m, n_occ + v] + 4 * g[m, n_occ + s, n_occ + s, n_occ + v] + -8 * g[m, n_occ + v, n_occ + s, n_occ + s] ) * K[0, (i*n_virt + s) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, (i*n_virt + t) * n_ex + m*n_virt + v+ 2*n_ex]

												elif ((u == t) and (t != s) and (w == t) and (v == s)):

													L3[i*n_virt + s + n_ex] += (-4 * g[m, n_occ + s, n_occ + s, n_occ + t] ) * K[0, (i*n_virt + t) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, (i*n_virt + t) * n_ex + m*n_virt + s+ 2*n_ex]

												elif ((u == t) and (t != s) and (w == t) and (v == t)):

													L3[i*n_virt + s + n_ex] += (8 * g[i, m, i, n_occ + s] + -4 * g[i, i, m, n_occ + s] + -8 * g[m, n_occ + t, n_occ + s, n_occ + t] + 4 * g[m, n_occ + s, n_occ + t, n_occ + t] ) * K[0, (i*n_virt + t) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, (i*n_virt + t) * n_ex + m*n_virt + t+ 2*n_ex]

												elif ((u == t) and (t != s) and (w == t) and (v != s) and (v != t) and (v != u)):

													L3[i*n_virt + s + n_ex] += (4 * g[m, n_occ + s, n_occ + t, n_occ + v] + -8 * g[m, n_occ + v, n_occ + s, n_occ + t] ) * K[0, (i*n_virt + t) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, (i*n_virt + t) * n_ex + m*n_virt + v+ 2*n_ex]

												elif ((u != s) and (u != t) and (t != s) and (w == t) and (v == s)):

													L3[i*n_virt + s + n_ex] += (-4 * g[m, n_occ + s, n_occ + s, n_occ + u] ) * K[0, (i*n_virt + u) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, (i*n_virt + t) * n_ex + m*n_virt + s+ 2*n_ex]

												elif ((u != s) and (u != t) and (t != s) and (w == t) and (v == t)):

													L3[i*n_virt + s + n_ex] += (4 * g[m, n_occ + s, n_occ + t, n_occ + u] + -8 * g[m, n_occ + t, n_occ + s, n_occ + u] ) * K[0, (i*n_virt + u) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, (i*n_virt + t) * n_ex + m*n_virt + t+ 2*n_ex]

												elif ((u != s) and (u != t) and (t != s) and (w == t) and (v == u)):

													L3[i*n_virt + s + n_ex] += (8 * g[i, m, i, n_occ + s] + -4 * g[i, i, m, n_occ + s] + -8 * g[m, n_occ + u, n_occ + s, n_occ + u] + 4 * g[m, n_occ + s, n_occ + u, n_occ + u] ) * K[0, (i*n_virt + u) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, (i*n_virt + t) * n_ex + m*n_virt + u+ 2*n_ex]

												elif ((u != s) and (u != t) and (t != s) and (w == t) and (v != s) and (v != t) and (v != u)):

													L3[i*n_virt + s + n_ex] += (4 * g[m, n_occ + s, n_occ + u, n_occ + v] + -8 * g[m, n_occ + v, n_occ + s, n_occ + u] ) * K[0, (i*n_virt + u) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, (i*n_virt + t) * n_ex + m*n_virt + v+ 2*n_ex]

											elif ((k != i) and (k != j) and (j == i) and (n == i) and (m == i)):

												if ((u == s) and (t == s) and (w == s) and (v == s)):

													L3[i*n_virt + s + n_ex] += (8 * g[i, k, i, n_occ + s] ) * K[0, (k*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] * K[1, (i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex]

												elif ((u == s) and (t == s) and (w == s) and (v != s) and (v != t) and (v != u)):

													L3[i*n_virt + s + n_ex] += (4 * g[i, k, i, n_occ + v] ) * K[0, (k*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] * K[1, (i*n_virt + s) * n_ex + i*n_virt + v+ 2*n_ex]

												elif ((u != s) and (u != t) and (t == s) and (w == s) and (v == u)):

													L3[i*n_virt + s + n_ex] += (4 * g[i, k, i, n_occ + s] ) * K[0, (k*n_virt + u) * n_ex + i*n_virt + s+ 2*n_ex] * K[1, (i*n_virt + s) * n_ex + i*n_virt + u+ 2*n_ex]

												elif ((u == s) and (t != s) and (w == t) and (v == s)):

													L3[i*n_virt + s + n_ex] += (8 * g[i, k, i, n_occ + s] ) * K[0, (k*n_virt + s) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, (i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex]

												elif ((u == s) and (t != s) and (w == t) and (v == t)):

													L3[i*n_virt + s + n_ex] += (4 * g[i, k, i, n_occ + t] ) * K[0, (k*n_virt + s) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, (i*n_virt + t) * n_ex + i*n_virt + t+ 2*n_ex]

												elif ((u == s) and (t != s) and (w == t) and (v != s) and (v != t) and (v != u)):

													L3[i*n_virt + s + n_ex] += (4 * g[i, k, i, n_occ + v] ) * K[0, (k*n_virt + s) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, (i*n_virt + t) * n_ex + i*n_virt + v+ 2*n_ex]

												elif ((u == t) and (t != s) and (w == t) and (v == t)):

													L3[i*n_virt + s + n_ex] += (4 * g[i, k, i, n_occ + s] ) * K[0, (k*n_virt + t) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, (i*n_virt + t) * n_ex + i*n_virt + t+ 2*n_ex]

												elif ((u != s) and (u != t) and (t != s) and (w == t) and (v == u)):

													L3[i*n_virt + s + n_ex] += (4 * g[i, k, i, n_occ + s] ) * K[0, (k*n_virt + u) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, (i*n_virt + t) * n_ex + i*n_virt + u+ 2*n_ex]

											elif ((k != i) and (k != j) and (j == i) and (n == i) and (m == k)):

												if ((u == s) and (t == s) and (w == s) and (v == s)):

													L3[i*n_virt + s + n_ex] += (-12 * g[i, n_occ + s, n_occ + s, n_occ + s] + 4 * g[i, k, k, n_occ + s] + 8 * g[i, i, i, n_occ + s] + 4 * g[i, n_occ + s, k, k] ) * K[0, (k*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] * K[1, (i*n_virt + s) * n_ex + k*n_virt + s+ 2*n_ex]

												elif ((u == s) and (t == s) and (w != s) and (w != t) and (w != u) and (w != v) and (v == s)):

													L3[i*n_virt + s + n_ex] += (-8 * g[i, n_occ + s, n_occ + s, n_occ + w] ) * K[0, (k*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] * K[1, (i*n_virt + w) * n_ex + k*n_virt + s+ 2*n_ex]

												elif ((u == s) and (t == s) and (w == s) and (v != s) and (v != t) and (v != u)):

													L3[i*n_virt + s + n_ex] += (8 * g[i, k, k, n_occ + v] + -4 * g[i, n_occ + v, k, k] + -8 * g[i, n_occ + s, n_occ + s, n_occ + v] + 4 * g[i, n_occ + v, n_occ + s, n_occ + s] ) * K[0, (k*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] * K[1, (i*n_virt + s) * n_ex + k*n_virt + v+ 2*n_ex]

												elif ((u != s) and (u != t) and (t == s) and (w == s) and (v == s)):

													L3[i*n_virt + s + n_ex] += (-4 * g[i, n_occ + s, n_occ + s, n_occ + u] ) * K[0, (k*n_virt + u) * n_ex + i*n_virt + s+ 2*n_ex] * K[1, (i*n_virt + s) * n_ex + k*n_virt + s+ 2*n_ex]

												elif ((u != s) and (u != t) and (t == s) and (w == s) and (v == u)):

													L3[i*n_virt + s + n_ex] += (-8 * g[i, n_occ + s, n_occ + s, n_occ + s] + 4 * g[i, n_occ + u, n_occ + s, n_occ + u] + -8 * g[i, n_occ + s, n_occ + u, n_occ + u] + 8 * g[i, i, i, n_occ + s] + -4 * g[i, k, k, n_occ + s] + 8 * g[i, n_occ + s, k, k] ) * K[0, (k*n_virt + u) * n_ex + i*n_virt + s+ 2*n_ex] * K[1, (i*n_virt + s) * n_ex + k*n_virt + u+ 2*n_ex]

												elif ((u != s) and (u != t) and (t == s) and (w == u) and (v == u)):

													L3[i*n_virt + s + n_ex] += (-8 * g[i, n_occ + s, n_occ + s, n_occ + u] ) * K[0, (k*n_virt + u) * n_ex + i*n_virt + s+ 2*n_ex] * K[1, (i*n_virt + u) * n_ex + k*n_virt + u+ 2*n_ex]

												elif ((u != s) and (u != t) and (t == s) and (w != s) and (w != t) and (w != u) and (w != v) and (v == u)):

													L3[i*n_virt + s + n_ex] += (-8 * g[i, n_occ + s, n_occ + s, n_occ + w] ) * K[0, (k*n_virt + u) * n_ex + i*n_virt + s+ 2*n_ex] * K[1, (i*n_virt + w) * n_ex + k*n_virt + u+ 2*n_ex]

												elif ((u != s) and (u != t) and (t == s) and (w == s) and (v != s) and (v != t) and (v != u)):

													L3[i*n_virt + s + n_ex] += (-8 * g[i, n_occ + s, n_occ + u, n_occ + v] + 4 * g[i, n_occ + v, n_occ + s, n_occ + u] ) * K[0, (k*n_virt + u) * n_ex + i*n_virt + s+ 2*n_ex] * K[1, (i*n_virt + s) * n_ex + k*n_virt + v+ 2*n_ex]

												elif ((u == s) and (t != s) and (w == s) and (v == s)):

													L3[i*n_virt + s + n_ex] += (-4 * F[i, n_occ + t] + -4 * g[i, n_occ + t, n_occ + s, n_occ + s] + -4 * g[i, n_occ + s, n_occ + s, n_occ + t] + 4 * g[i, i, i, n_occ + t] ) * K[0, (k*n_virt + s) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, (i*n_virt + s) * n_ex + k*n_virt + s+ 2*n_ex]

												elif ((u == s) and (t != s) and (w == t) and (v == s)):

													L3[i*n_virt + s + n_ex] += (4 * F[i, n_occ + s] + -4 * g[i, n_occ + t, n_occ + s, n_occ + t] + -4 * g[i, n_occ + s, n_occ + t, n_occ + t] + -4 * g[i, n_occ + s, n_occ + s, n_occ + s] + 4 * g[i, n_occ + s, k, k] + 4 * g[i, i, i, n_occ + s] + 4 * g[i, k, k, n_occ + s] ) * K[0, (k*n_virt + s) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, (i*n_virt + t) * n_ex + k*n_virt + s+ 2*n_ex]

												elif ((u == s) and (t != s) and (w != s) and (w != t) and (w != u) and (w != v) and (v == s)):

													L3[i*n_virt + s + n_ex] += (-4 * g[i, n_occ + t, n_occ + s, n_occ + w] + -4 * g[i, n_occ + s, n_occ + t, n_occ + w] ) * K[0, (k*n_virt + s) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, (i*n_virt + w) * n_ex + k*n_virt + s+ 2*n_ex]

												elif ((u == s) and (t != s) and (w == t) and (v == t)):

													L3[i*n_virt + s + n_ex] += (8 * g[i, k, k, n_occ + t] + -4 * g[i, n_occ + t, k, k] + -8 * g[i, n_occ + s, n_occ + s, n_occ + t] + 4 * g[i, n_occ + t, n_occ + s, n_occ + s] ) * K[0, (k*n_virt + s) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, (i*n_virt + t) * n_ex + k*n_virt + t+ 2*n_ex]

												elif ((u == s) and (t != s) and (w == t) and (v != s) and (v != t) and (v != u)):

													L3[i*n_virt + s + n_ex] += (8 * g[i, k, k, n_occ + v] + -4 * g[i, n_occ + v, k, k] + -8 * g[i, n_occ + s, n_occ + s, n_occ + v] + 4 * g[i, n_occ + v, n_occ + s, n_occ + s] ) * K[0, (k*n_virt + s) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, (i*n_virt + t) * n_ex + k*n_virt + v+ 2*n_ex]

												elif ((u == t) and (t != s) and (w == t) and (v == s)):

													L3[i*n_virt + s + n_ex] += (-4 * g[i, n_occ + s, n_occ + s, n_occ + t] ) * K[0, (k*n_virt + t) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, (i*n_virt + t) * n_ex + k*n_virt + s+ 2*n_ex]

												elif ((u == t) and (t != s) and (w == s) and (v == t)):

													L3[i*n_virt + s + n_ex] += (-4 * F[i, n_occ + t] + -4 * g[i, n_occ + t, n_occ + s, n_occ + s] + -4 * g[i, n_occ + s, n_occ + s, n_occ + t] + 4 * g[i, i, i, n_occ + t] ) * K[0, (k*n_virt + t) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, (i*n_virt + s) * n_ex + k*n_virt + t+ 2*n_ex]

												elif ((u == t) and (t != s) and (w == t) and (v == t)):

													L3[i*n_virt + s + n_ex] += (4 * F[i, n_occ + s] + -12 * g[i, n_occ + s, n_occ + t, n_occ + t] + -4 * g[i, k, k, n_occ + s] + 8 * g[i, n_occ + s, k, k] + 4 * g[i, i, i, n_occ + s] ) * K[0, (k*n_virt + t) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, (i*n_virt + t) * n_ex + k*n_virt + t+ 2*n_ex]

												elif ((u == t) and (t != s) and (w != s) and (w != t) and (w != u) and (w != v) and (v == t)):

													L3[i*n_virt + s + n_ex] += (-4 * g[i, n_occ + t, n_occ + s, n_occ + w] + -4 * g[i, n_occ + s, n_occ + t, n_occ + w] ) * K[0, (k*n_virt + t) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, (i*n_virt + w) * n_ex + k*n_virt + t+ 2*n_ex]

												elif ((u == t) and (t != s) and (w == t) and (v != s) and (v != t) and (v != u)):

													L3[i*n_virt + s + n_ex] += (-8 * g[i, n_occ + s, n_occ + t, n_occ + v] + 4 * g[i, n_occ + v, n_occ + s, n_occ + t] ) * K[0, (k*n_virt + t) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, (i*n_virt + t) * n_ex + k*n_virt + v+ 2*n_ex]

												elif ((u != s) and (u != t) and (t != s) and (w == t) and (v == s)):

													L3[i*n_virt + s + n_ex] += (-4 * g[i, n_occ + s, n_occ + s, n_occ + u] ) * K[0, (k*n_virt + u) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, (i*n_virt + t) * n_ex + k*n_virt + s+ 2*n_ex]

												elif ((u != s) and (u != t) and (t != s) and (w == t) and (v == t)):

													L3[i*n_virt + s + n_ex] += (-8 * g[i, n_occ + s, n_occ + t, n_occ + u] + 4 * g[i, n_occ + t, n_occ + s, n_occ + u] ) * K[0, (k*n_virt + u) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, (i*n_virt + t) * n_ex + k*n_virt + t+ 2*n_ex]

												elif ((u != s) and (u != t) and (t != s) and (w == s) and (v == u)):

													L3[i*n_virt + s + n_ex] += (-4 * F[i, n_occ + t] + -4 * g[i, n_occ + t, n_occ + s, n_occ + s] + -4 * g[i, n_occ + s, n_occ + s, n_occ + t] + 4 * g[i, i, i, n_occ + t] ) * K[0, (k*n_virt + u) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, (i*n_virt + s) * n_ex + k*n_virt + u+ 2*n_ex]

												elif ((u != s) and (u != t) and (t != s) and (w == t) and (v == u)):

													L3[i*n_virt + s + n_ex] += (4 * F[i, n_occ + s] + -4 * g[i, n_occ + t, n_occ + s, n_occ + t] + -4 * g[i, n_occ + s, n_occ + t, n_occ + t] + 4 * g[i, n_occ + u, n_occ + s, n_occ + u] + -8 * g[i, n_occ + s, n_occ + u, n_occ + u] + -4 * g[i, k, k, n_occ + s] + 8 * g[i, n_occ + s, k, k] + 4 * g[i, i, i, n_occ + s] ) * K[0, (k*n_virt + u) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, (i*n_virt + t) * n_ex + k*n_virt + u+ 2*n_ex]

												elif ((u != s) and (u != t) and (t != s) and (w == u) and (v == u)):

													L3[i*n_virt + s + n_ex] += (-4 * g[i, n_occ + t, n_occ + s, n_occ + u] + -4 * g[i, n_occ + s, n_occ + t, n_occ + u] ) * K[0, (k*n_virt + u) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, (i*n_virt + u) * n_ex + k*n_virt + u+ 2*n_ex]

												elif ((u != s) and (u != t) and (t != s) and (w != s) and (w != t) and (w != u) and (w != v) and (v == u)):

													L3[i*n_virt + s + n_ex] += (-4 * g[i, n_occ + t, n_occ + s, n_occ + w] + -4 * g[i, n_occ + s, n_occ + t, n_occ + w] ) * K[0, (k*n_virt + u) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, (i*n_virt + w) * n_ex + k*n_virt + u+ 2*n_ex]

												elif ((u != s) and (u != t) and (t != s) and (w == t) and (v != s) and (v != t) and (v != u)):

													L3[i*n_virt + s + n_ex] += (-8 * g[i, n_occ + s, n_occ + u, n_occ + v] + 4 * g[i, n_occ + v, n_occ + s, n_occ + u] ) * K[0, (k*n_virt + u) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, (i*n_virt + t) * n_ex + k*n_virt + v+ 2*n_ex]

											elif ((k != i) and (k != j) and (j == i) and (n == k) and (m == k)):

												if ((u == s) and (t == s) and (w == s) and (v == s)):

													L3[i*n_virt + s + n_ex] += (8 * g[i, k, i, n_occ + s] ) * K[0, (k*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] * K[1, (k*n_virt + s) * n_ex + k*n_virt + s+ 2*n_ex]

												elif ((u != s) and (u != t) and (t == s) and (w == s) and (v == u)):

													L3[i*n_virt + s + n_ex] += (8 * g[i, k, i, n_occ + s] ) * K[0, (k*n_virt + u) * n_ex + i*n_virt + s+ 2*n_ex] * K[1, (k*n_virt + s) * n_ex + k*n_virt + u+ 2*n_ex]

												elif ((u == s) and (t != s) and (w == s) and (v == s)):

													L3[i*n_virt + s + n_ex] += (4 * g[i, k, i, n_occ + t] ) * K[0, (k*n_virt + s) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, (k*n_virt + s) * n_ex + k*n_virt + s+ 2*n_ex]

												elif ((u == s) and (t != s) and (w == t) and (v == s)):

													L3[i*n_virt + s + n_ex] += (4 * g[i, k, i, n_occ + s] ) * K[0, (k*n_virt + s) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, (k*n_virt + t) * n_ex + k*n_virt + s+ 2*n_ex]

												elif ((u == t) and (t != s) and (w == s) and (v == t)):

													L3[i*n_virt + s + n_ex] += (4 * g[i, k, i, n_occ + t] ) * K[0, (k*n_virt + t) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, (k*n_virt + s) * n_ex + k*n_virt + t+ 2*n_ex]

												elif ((u == t) and (t != s) and (w == t) and (v == t)):

													L3[i*n_virt + s + n_ex] += (4 * g[i, k, i, n_occ + s] ) * K[0, (k*n_virt + t) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, (k*n_virt + t) * n_ex + k*n_virt + t+ 2*n_ex]

												elif ((u != s) and (u != t) and (t != s) and (w == s) and (v == u)):

													L3[i*n_virt + s + n_ex] += (4 * g[i, k, i, n_occ + t] ) * K[0, (k*n_virt + u) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, (k*n_virt + s) * n_ex + k*n_virt + u+ 2*n_ex]

												elif ((u != s) and (u != t) and (t != s) and (w == t) and (v == u)):

													L3[i*n_virt + s + n_ex] += (4 * g[i, k, i, n_occ + s] ) * K[0, (k*n_virt + u) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, (k*n_virt + t) * n_ex + k*n_virt + u+ 2*n_ex]

											elif ((k != i) and (k != j) and (j == i) and (n != i) and (n != j) and (n != k) and (n != m) and (m == k)):

												if ((u == s) and (t == s) and (w == s) and (v == s)):

													L3[i*n_virt + s + n_ex] += (8 * g[i, n, i, n_occ + s] ) * K[0, (k*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] * K[1, (n*n_virt + s) * n_ex + k*n_virt + s+ 2*n_ex]

												elif ((u != s) and (u != t) and (t == s) and (w == s) and (v == u)):

													L3[i*n_virt + s + n_ex] += (8 * g[i, n, i, n_occ + s] ) * K[0, (k*n_virt + u) * n_ex + i*n_virt + s+ 2*n_ex] * K[1, (n*n_virt + s) * n_ex + k*n_virt + u+ 2*n_ex]

												elif ((u == s) and (t != s) and (w == s) and (v == s)):

													L3[i*n_virt + s + n_ex] += (4 * g[i, n, i, n_occ + t] ) * K[0, (k*n_virt + s) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, (n*n_virt + s) * n_ex + k*n_virt + s+ 2*n_ex]

												elif ((u == s) and (t != s) and (w == t) and (v == s)):

													L3[i*n_virt + s + n_ex] += (4 * g[i, n, i, n_occ + s] ) * K[0, (k*n_virt + s) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, (n*n_virt + t) * n_ex + k*n_virt + s+ 2*n_ex]

												elif ((u == t) and (t != s) and (w == s) and (v == t)):

													L3[i*n_virt + s + n_ex] += (4 * g[i, n, i, n_occ + t] ) * K[0, (k*n_virt + t) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, (n*n_virt + s) * n_ex + k*n_virt + t+ 2*n_ex]

												elif ((u == t) and (t != s) and (w == t) and (v == t)):

													L3[i*n_virt + s + n_ex] += (4 * g[i, n, i, n_occ + s] ) * K[0, (k*n_virt + t) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, (n*n_virt + t) * n_ex + k*n_virt + t+ 2*n_ex]

												elif ((u != s) and (u != t) and (t != s) and (w == s) and (v == u)):

													L3[i*n_virt + s + n_ex] += (4 * g[i, n, i, n_occ + t] ) * K[0, (k*n_virt + u) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, (n*n_virt + s) * n_ex + k*n_virt + u+ 2*n_ex]

												elif ((u != s) and (u != t) and (t != s) and (w == t) and (v == u)):

													L3[i*n_virt + s + n_ex] += (4 * g[i, n, i, n_occ + s] ) * K[0, (k*n_virt + u) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, (n*n_virt + t) * n_ex + k*n_virt + u+ 2*n_ex]

											elif ((k != i) and (k != j) and (j == i) and (n == i) and (m != i) and (m != j) and (m != k)):

												if ((u == s) and (t == s) and (w == s) and (v == s)):

													L3[i*n_virt + s + n_ex] += (4 * g[i, k, m, n_occ + s] + 4 * g[i, n_occ + s, k, m] ) * K[0, (k*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] * K[1, (i*n_virt + s) * n_ex + m*n_virt + s+ 2*n_ex]

												elif ((u == s) and (t == s) and (w == s) and (v != s) and (v != t) and (v != u)):

													L3[i*n_virt + s + n_ex] += (8 * g[i, k, m, n_occ + v] + -4 * g[i, n_occ + v, k, m] ) * K[0, (k*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] * K[1, (i*n_virt + s) * n_ex + m*n_virt + v+ 2*n_ex]

												elif ((u != s) and (u != t) and (t == s) and (w == s) and (v == u)):

													L3[i*n_virt + s + n_ex] += (-4 * g[i, k, m, n_occ + s] + 8 * g[i, n_occ + s, k, m] ) * K[0, (k*n_virt + u) * n_ex + i*n_virt + s+ 2*n_ex] * K[1, (i*n_virt + s) * n_ex + m*n_virt + u+ 2*n_ex]

												elif ((u == s) and (t != s) and (w == t) and (v == s)):

													L3[i*n_virt + s + n_ex] += (4 * g[i, k, m, n_occ + s] + 4 * g[i, n_occ + s, k, m] ) * K[0, (k*n_virt + s) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, (i*n_virt + t) * n_ex + m*n_virt + s+ 2*n_ex]

												elif ((u == s) and (t != s) and (w == t) and (v == t)):

													L3[i*n_virt + s + n_ex] += (8 * g[i, k, m, n_occ + t] + -4 * g[i, n_occ + t, k, m] ) * K[0, (k*n_virt + s) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, (i*n_virt + t) * n_ex + m*n_virt + t+ 2*n_ex]

												elif ((u == s) and (t != s) and (w == t) and (v != s) and (v != t) and (v != u)):

													L3[i*n_virt + s + n_ex] += (8 * g[i, k, m, n_occ + v] + -4 * g[i, n_occ + v, k, m] ) * K[0, (k*n_virt + s) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, (i*n_virt + t) * n_ex + m*n_virt + v+ 2*n_ex]

												elif ((u == t) and (t != s) and (w == t) and (v == t)):

													L3[i*n_virt + s + n_ex] += (-4 * g[i, k, m, n_occ + s] + 8 * g[i, n_occ + s, k, m] ) * K[0, (k*n_virt + t) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, (i*n_virt + t) * n_ex + m*n_virt + t+ 2*n_ex]

												elif ((u != s) and (u != t) and (t != s) and (w == t) and (v == u)):

													L3[i*n_virt + s + n_ex] += (-4 * g[i, k, m, n_occ + s] + 8 * g[i, n_occ + s, k, m] ) * K[0, (k*n_virt + u) * n_ex + i*n_virt + t+ 2*n_ex] * K[1, (i*n_virt + t) * n_ex + m*n_virt + u+ 2*n_ex]

											elif ((k == i) and (j != i) and (n == i) and (m == i)):

												if ((u == s) and (t == s) and (w == s) and (v == s)):

													L3[i*n_virt + s + n_ex] += (-4 * F[j, n_occ + s] + 4 * g[i, j, i, n_occ + s] + -4 * g[j, n_occ + s, n_occ + s, n_occ + s] + 4 * g[i, i, j, n_occ + s] ) * K[0, (i*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, (i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex]

												elif ((u == s) and (t == s) and (w != s) and (w != t) and (w != u) and (w != v) and (v == s)):

													L3[i*n_virt + s + n_ex] += (-4 * g[j, n_occ + s, n_occ + s, n_occ + w] ) * K[0, (i*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, (i*n_virt + w) * n_ex + i*n_virt + s+ 2*n_ex]

												elif ((u != s) and (u != t) and (t == s) and (w == s) and (v == u)):

													L3[i*n_virt + s + n_ex] += (-4 * F[j, n_occ + s] + 4 * g[i, j, i, n_occ + s] + -4 * g[j, n_occ + s, n_occ + s, n_occ + s] + 4 * g[i, i, j, n_occ + s] ) * K[0, (i*n_virt + u) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, (i*n_virt + s) * n_ex + i*n_virt + u+ 2*n_ex]

												elif ((u != s) and (u != t) and (t == s) and (w == u) and (v == u)):

													L3[i*n_virt + s + n_ex] += (-4 * g[j, n_occ + s, n_occ + s, n_occ + u] ) * K[0, (i*n_virt + u) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, (i*n_virt + u) * n_ex + i*n_virt + u+ 2*n_ex]

												elif ((u != s) and (u != t) and (t == s) and (w != s) and (w != t) and (w != u) and (w != v) and (v == u)):

													L3[i*n_virt + s + n_ex] += (-4 * g[j, n_occ + s, n_occ + s, n_occ + w] ) * K[0, (i*n_virt + u) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, (i*n_virt + w) * n_ex + i*n_virt + u+ 2*n_ex]

												elif ((u == s) and (t != s) and (w == s) and (v == s)):

													L3[i*n_virt + s + n_ex] += (-8 * F[j, n_occ + t] + 4 * g[j, n_occ + s, n_occ + s, n_occ + t] + -8 * g[j, n_occ + t, n_occ + s, n_occ + s] + 8 * g[i, i, j, n_occ + t] + -4 * g[i, j, i, n_occ + t] ) * K[0, (i*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex]

												elif ((u == s) and (t != s) and (w == t) and (v == s)):

													L3[i*n_virt + s + n_ex] += (4 * F[j, n_occ + s] + -8 * g[j, n_occ + t, n_occ + s, n_occ + t] + 4 * g[j, n_occ + s, n_occ + t, n_occ + t] + -4 * g[i, i, j, n_occ + s] + 8 * g[i, j, i, n_occ + s] ) * K[0, (i*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex]

												elif ((u == s) and (t != s) and (w != s) and (w != t) and (w != u) and (w != v) and (v == s)):

													L3[i*n_virt + s + n_ex] += (4 * g[j, n_occ + s, n_occ + t, n_occ + w] + -8 * g[j, n_occ + t, n_occ + s, n_occ + w] ) * K[0, (i*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (i*n_virt + w) * n_ex + i*n_virt + s+ 2*n_ex]

												elif ((u == t) and (t != s) and (w == s) and (v == t)):

													L3[i*n_virt + s + n_ex] += (-8 * F[j, n_occ + t] + 4 * g[j, n_occ + s, n_occ + s, n_occ + t] + -8 * g[j, n_occ + t, n_occ + s, n_occ + s] + 8 * g[i, i, j, n_occ + t] + -4 * g[i, j, i, n_occ + t] ) * K[0, (i*n_virt + t) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (i*n_virt + s) * n_ex + i*n_virt + t+ 2*n_ex]

												elif ((u == t) and (t != s) and (w == t) and (v == t)):

													L3[i*n_virt + s + n_ex] += (4 * F[j, n_occ + s] + -8 * g[j, n_occ + t, n_occ + s, n_occ + t] + 4 * g[j, n_occ + s, n_occ + t, n_occ + t] + -4 * g[i, i, j, n_occ + s] + 8 * g[i, j, i, n_occ + s] ) * K[0, (i*n_virt + t) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (i*n_virt + t) * n_ex + i*n_virt + t+ 2*n_ex]

												elif ((u == t) and (t != s) and (w != s) and (w != t) and (w != u) and (w != v) and (v == t)):

													L3[i*n_virt + s + n_ex] += (4 * g[j, n_occ + s, n_occ + t, n_occ + w] + -8 * g[j, n_occ + t, n_occ + s, n_occ + w] ) * K[0, (i*n_virt + t) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (i*n_virt + w) * n_ex + i*n_virt + t+ 2*n_ex]

												elif ((u != s) and (u != t) and (t != s) and (w == s) and (v == u)):

													L3[i*n_virt + s + n_ex] += (-8 * F[j, n_occ + t] + 4 * g[j, n_occ + s, n_occ + s, n_occ + t] + -8 * g[j, n_occ + t, n_occ + s, n_occ + s] + 8 * g[i, i, j, n_occ + t] + -4 * g[i, j, i, n_occ + t] ) * K[0, (i*n_virt + u) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (i*n_virt + s) * n_ex + i*n_virt + u+ 2*n_ex]

												elif ((u != s) and (u != t) and (t != s) and (w == t) and (v == u)):

													L3[i*n_virt + s + n_ex] += (4 * F[j, n_occ + s] + -8 * g[j, n_occ + t, n_occ + s, n_occ + t] + 4 * g[j, n_occ + s, n_occ + t, n_occ + t] + -4 * g[i, i, j, n_occ + s] + 8 * g[i, j, i, n_occ + s] ) * K[0, (i*n_virt + u) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (i*n_virt + t) * n_ex + i*n_virt + u+ 2*n_ex]

												elif ((u != s) and (u != t) and (t != s) and (w == u) and (v == u)):

													L3[i*n_virt + s + n_ex] += (4 * g[j, n_occ + s, n_occ + t, n_occ + u] + -8 * g[j, n_occ + t, n_occ + s, n_occ + u] ) * K[0, (i*n_virt + u) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (i*n_virt + u) * n_ex + i*n_virt + u+ 2*n_ex]

												elif ((u != s) and (u != t) and (t != s) and (w != s) and (w != t) and (w != u) and (w != v) and (v == u)):

													L3[i*n_virt + s + n_ex] += (4 * g[j, n_occ + s, n_occ + t, n_occ + w] + -8 * g[j, n_occ + t, n_occ + s, n_occ + w] ) * K[0, (i*n_virt + u) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (i*n_virt + w) * n_ex + i*n_virt + u+ 2*n_ex]

											elif ((k == i) and (j != i) and (n == j) and (m == i)):

												if ((u == s) and (t == s) and (w == s) and (v == s)):

													L3[i*n_virt + s + n_ex] += (4 * F[i, n_occ + s] + 8 * g[i, i, i, n_occ + s] + -12 * g[i, n_occ + s, n_occ + s, n_occ + s] + 4 * g[i, n_occ + s, j, j] + 4 * g[i, j, j, n_occ + s] ) * K[0, (i*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, (j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex]

												elif ((u == s) and (t == s) and (w != s) and (w != t) and (w != u) and (w != v) and (v == s)):

													L3[i*n_virt + s + n_ex] += (-4 * g[i, n_occ + s, n_occ + s, n_occ + w] ) * K[0, (i*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, (j*n_virt + w) * n_ex + i*n_virt + s+ 2*n_ex]

												elif ((u == s) and (t == s) and (w == s) and (v != s) and (v != t) and (v != u)):

													L3[i*n_virt + s + n_ex] += (4 * g[i, i, i, n_occ + v] + -4 * g[i, n_occ + v, n_occ + s, n_occ + s] + -4 * g[i, n_occ + s, n_occ + s, n_occ + v] ) * K[0, (i*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, (j*n_virt + s) * n_ex + i*n_virt + v+ 2*n_ex]

												elif ((u != s) and (u != t) and (t == s) and (w == s) and (v == s)):

													L3[i*n_virt + s + n_ex] += (-8 * g[i, n_occ + s, n_occ + s, n_occ + u] ) * K[0, (i*n_virt + u) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, (j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex]

												elif ((u != s) and (u != t) and (t == s) and (w == s) and (v == u)):

													L3[i*n_virt + s + n_ex] += (4 * F[i, n_occ + s] + -4 * g[i, n_occ + s, n_occ + s, n_occ + s] + -4 * g[i, n_occ + u, n_occ + s, n_occ + u] + -4 * g[i, n_occ + s, n_occ + u, n_occ + u] + 4 * g[i, n_occ + s, j, j] + 4 * g[i, i, i, n_occ + s] + 4 * g[i, j, j, n_occ + s] ) * K[0, (i*n_virt + u) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, (j*n_virt + s) * n_ex + i*n_virt + u+ 2*n_ex]

												elif ((u != s) and (u != t) and (t == s) and (w == u) and (v == u)):

													L3[i*n_virt + s + n_ex] += (-4 * g[i, n_occ + s, n_occ + s, n_occ + u] ) * K[0, (i*n_virt + u) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, (j*n_virt + u) * n_ex + i*n_virt + u+ 2*n_ex]

												elif ((u != s) and (u != t) and (t == s) and (w != s) and (w != t) and (w != u) and (w != v) and (v == u)):

													L3[i*n_virt + s + n_ex] += (-4 * g[i, n_occ + s, n_occ + s, n_occ + w] ) * K[0, (i*n_virt + u) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, (j*n_virt + w) * n_ex + i*n_virt + u+ 2*n_ex]

												elif ((u != s) and (u != t) and (t == s) and (w == s) and (v != s) and (v != t) and (v != u)):

													L3[i*n_virt + s + n_ex] += (-4 * g[i, n_occ + v, n_occ + s, n_occ + u] + -4 * g[i, n_occ + s, n_occ + u, n_occ + v] ) * K[0, (i*n_virt + u) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, (j*n_virt + s) * n_ex + i*n_virt + v+ 2*n_ex]

												elif ((u == s) and (t != s) and (w == s) and (v == s)):

													L3[i*n_virt + s + n_ex] += (4 * F[i, n_occ + t] + -8 * g[i, n_occ + s, n_occ + s, n_occ + t] + 4 * g[i, n_occ + t, n_occ + s, n_occ + s] + -4 * g[i, n_occ + t, j, j] + 8 * g[i, j, j, n_occ + t] ) * K[0, (i*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex]

												elif ((u == s) and (t != s) and (w == t) and (v == s)):

													L3[i*n_virt + s + n_ex] += (4 * g[i, n_occ + t, n_occ + s, n_occ + t] + -8 * g[i, n_occ + s, n_occ + t, n_occ + t] + -8 * g[i, n_occ + s, n_occ + s, n_occ + s] + 8 * g[i, i, i, n_occ + s] + -4 * g[i, j, j, n_occ + s] + 8 * g[i, n_occ + s, j, j] ) * K[0, (i*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex]

												elif ((u == s) and (t != s) and (w != s) and (w != t) and (w != u) and (w != v) and (v == s)):

													L3[i*n_virt + s + n_ex] += (-8 * g[i, n_occ + s, n_occ + t, n_occ + w] + 4 * g[i, n_occ + t, n_occ + s, n_occ + w] ) * K[0, (i*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (j*n_virt + w) * n_ex + i*n_virt + s+ 2*n_ex]

												elif ((u == s) and (t != s) and (w == t) and (v == t)):

													L3[i*n_virt + s + n_ex] += (4 * g[i, i, i, n_occ + t] + -4 * g[i, n_occ + t, n_occ + s, n_occ + s] + -4 * g[i, n_occ + s, n_occ + s, n_occ + t] ) * K[0, (i*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (j*n_virt + t) * n_ex + i*n_virt + t+ 2*n_ex]

												elif ((u == s) and (t != s) and (w == t) and (v != s) and (v != t) and (v != u)):

													L3[i*n_virt + s + n_ex] += (4 * g[i, i, i, n_occ + v] + -4 * g[i, n_occ + v, n_occ + s, n_occ + s] + -4 * g[i, n_occ + s, n_occ + s, n_occ + v] ) * K[0, (i*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (j*n_virt + t) * n_ex + i*n_virt + v+ 2*n_ex]

												elif ((u == t) and (t != s) and (w == t) and (v == s)):

													L3[i*n_virt + s + n_ex] += (-8 * g[i, n_occ + s, n_occ + s, n_occ + t] ) * K[0, (i*n_virt + t) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex]

												elif ((u == t) and (t != s) and (w == s) and (v == t)):

													L3[i*n_virt + s + n_ex] += (4 * F[i, n_occ + t] + -8 * g[i, n_occ + s, n_occ + s, n_occ + t] + 4 * g[i, n_occ + t, n_occ + s, n_occ + s] + -4 * g[i, n_occ + t, j, j] + 8 * g[i, j, j, n_occ + t] ) * K[0, (i*n_virt + t) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (j*n_virt + s) * n_ex + i*n_virt + t+ 2*n_ex]

												elif ((u == t) and (t != s) and (w == t) and (v == t)):

													L3[i*n_virt + s + n_ex] += (-12 * g[i, n_occ + s, n_occ + t, n_occ + t] + -4 * g[i, j, j, n_occ + s] + 8 * g[i, n_occ + s, j, j] + 4 * g[i, i, i, n_occ + s] ) * K[0, (i*n_virt + t) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (j*n_virt + t) * n_ex + i*n_virt + t+ 2*n_ex]

												elif ((u == t) and (t != s) and (w != s) and (w != t) and (w != u) and (w != v) and (v == t)):

													L3[i*n_virt + s + n_ex] += (-8 * g[i, n_occ + s, n_occ + t, n_occ + w] + 4 * g[i, n_occ + t, n_occ + s, n_occ + w] ) * K[0, (i*n_virt + t) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (j*n_virt + w) * n_ex + i*n_virt + t+ 2*n_ex]

												elif ((u == t) and (t != s) and (w == t) and (v != s) and (v != t) and (v != u)):

													L3[i*n_virt + s + n_ex] += (-4 * g[i, n_occ + v, n_occ + s, n_occ + t] + -4 * g[i, n_occ + s, n_occ + t, n_occ + v] ) * K[0, (i*n_virt + t) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (j*n_virt + t) * n_ex + i*n_virt + v+ 2*n_ex]

												elif ((u != s) and (u != t) and (t != s) and (w == t) and (v == s)):

													L3[i*n_virt + s + n_ex] += (-8 * g[i, n_occ + s, n_occ + s, n_occ + u] ) * K[0, (i*n_virt + u) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex]

												elif ((u != s) and (u != t) and (t != s) and (w == t) and (v == t)):

													L3[i*n_virt + s + n_ex] += (-4 * g[i, n_occ + t, n_occ + s, n_occ + u] + -4 * g[i, n_occ + s, n_occ + t, n_occ + u] ) * K[0, (i*n_virt + u) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (j*n_virt + t) * n_ex + i*n_virt + t+ 2*n_ex]

												elif ((u != s) and (u != t) and (t != s) and (w == s) and (v == u)):

													L3[i*n_virt + s + n_ex] += (4 * F[i, n_occ + t] + -8 * g[i, n_occ + s, n_occ + s, n_occ + t] + 4 * g[i, n_occ + t, n_occ + s, n_occ + s] + -4 * g[i, n_occ + t, j, j] + 8 * g[i, j, j, n_occ + t] ) * K[0, (i*n_virt + u) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (j*n_virt + s) * n_ex + i*n_virt + u+ 2*n_ex]

												elif ((u != s) and (u != t) and (t != s) and (w == t) and (v == u)):

													L3[i*n_virt + s + n_ex] += (4 * g[i, n_occ + t, n_occ + s, n_occ + t] + -8 * g[i, n_occ + s, n_occ + t, n_occ + t] + -4 * g[i, n_occ + u, n_occ + s, n_occ + u] + -4 * g[i, n_occ + s, n_occ + u, n_occ + u] + -4 * g[i, j, j, n_occ + s] + 8 * g[i, n_occ + s, j, j] + 4 * g[i, i, i, n_occ + s] ) * K[0, (i*n_virt + u) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (j*n_virt + t) * n_ex + i*n_virt + u+ 2*n_ex]

												elif ((u != s) and (u != t) and (t != s) and (w == u) and (v == u)):

													L3[i*n_virt + s + n_ex] += (-8 * g[i, n_occ + s, n_occ + t, n_occ + u] + 4 * g[i, n_occ + t, n_occ + s, n_occ + u] ) * K[0, (i*n_virt + u) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (j*n_virt + u) * n_ex + i*n_virt + u+ 2*n_ex]

												elif ((u != s) and (u != t) and (t != s) and (w != s) and (w != t) and (w != u) and (w != v) and (v == u)):

													L3[i*n_virt + s + n_ex] += (-8 * g[i, n_occ + s, n_occ + t, n_occ + w] + 4 * g[i, n_occ + t, n_occ + s, n_occ + w] ) * K[0, (i*n_virt + u) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (j*n_virt + w) * n_ex + i*n_virt + u+ 2*n_ex]

												elif ((u != s) and (u != t) and (t != s) and (w == t) and (v != s) and (v != t) and (v != u)):

													L3[i*n_virt + s + n_ex] += (-4 * g[i, n_occ + v, n_occ + s, n_occ + u] + -4 * g[i, n_occ + s, n_occ + u, n_occ + v] ) * K[0, (i*n_virt + u) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (j*n_virt + t) * n_ex + i*n_virt + v+ 2*n_ex]

											elif ((k == i) and (j != i) and (n != i) and (n != j) and (n != k) and (n != m) and (m == i)):

												if ((u == s) and (t == s) and (w == s) and (v == s)):

													L3[i*n_virt + s + n_ex] += (4 * g[i, n, j, n_occ + s] + 4 * g[i, n_occ + s, j, n] ) * K[0, (i*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, (n*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex]

												elif ((u != s) and (u != t) and (t == s) and (w == s) and (v == u)):

													L3[i*n_virt + s + n_ex] += (4 * g[i, n, j, n_occ + s] + 4 * g[i, n_occ + s, j, n] ) * K[0, (i*n_virt + u) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, (n*n_virt + s) * n_ex + i*n_virt + u+ 2*n_ex]

												elif ((u == s) and (t != s) and (w == s) and (v == s)):

													L3[i*n_virt + s + n_ex] += (8 * g[i, n, j, n_occ + t] + -4 * g[i, n_occ + t, j, n] ) * K[0, (i*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (n*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex]

												elif ((u == s) and (t != s) and (w == t) and (v == s)):

													L3[i*n_virt + s + n_ex] += (-4 * g[i, n, j, n_occ + s] + 8 * g[i, n_occ + s, j, n] ) * K[0, (i*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (n*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex]

												elif ((u == t) and (t != s) and (w == s) and (v == t)):

													L3[i*n_virt + s + n_ex] += (8 * g[i, n, j, n_occ + t] + -4 * g[i, n_occ + t, j, n] ) * K[0, (i*n_virt + t) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (n*n_virt + s) * n_ex + i*n_virt + t+ 2*n_ex]

												elif ((u == t) and (t != s) and (w == t) and (v == t)):

													L3[i*n_virt + s + n_ex] += (-4 * g[i, n, j, n_occ + s] + 8 * g[i, n_occ + s, j, n] ) * K[0, (i*n_virt + t) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (n*n_virt + t) * n_ex + i*n_virt + t+ 2*n_ex]

												elif ((u != s) and (u != t) and (t != s) and (w == s) and (v == u)):

													L3[i*n_virt + s + n_ex] += (8 * g[i, n, j, n_occ + t] + -4 * g[i, n_occ + t, j, n] ) * K[0, (i*n_virt + u) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (n*n_virt + s) * n_ex + i*n_virt + u+ 2*n_ex]

												elif ((u != s) and (u != t) and (t != s) and (w == t) and (v == u)):

													L3[i*n_virt + s + n_ex] += (-4 * g[i, n, j, n_occ + s] + 8 * g[i, n_occ + s, j, n] ) * K[0, (i*n_virt + u) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (n*n_virt + t) * n_ex + i*n_virt + u+ 2*n_ex]

											elif ((k == i) and (j != i) and (n == j) and (m == j)):

												if ((u == s) and (t == s) and (w == s) and (v == s)):

													L3[i*n_virt + s + n_ex] += (4 * g[i, i, j, n_occ + s] + -4 * g[j, n_occ + s, n_occ + s, n_occ + s] + 4 * g[i, j, i, n_occ + s] ) * K[0, (i*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, (j*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex]

												elif ((u == s) and (t == s) and (w == s) and (v != s) and (v != t) and (v != u)):

													L3[i*n_virt + s + n_ex] += (-4 * g[i, j, i, n_occ + v] + 8 * g[i, i, j, n_occ + v] + 4 * g[j, n_occ + s, n_occ + s, n_occ + v] + -8 * g[j, n_occ + v, n_occ + s, n_occ + s] ) * K[0, (i*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, (j*n_virt + s) * n_ex + j*n_virt + v+ 2*n_ex]

												elif ((u != s) and (u != t) and (t == s) and (w == s) and (v == s)):

													L3[i*n_virt + s + n_ex] += (-4 * g[j, n_occ + s, n_occ + s, n_occ + u] ) * K[0, (i*n_virt + u) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, (j*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex]

												elif ((u != s) and (u != t) and (t == s) and (w == s) and (v == u)):

													L3[i*n_virt + s + n_ex] += (8 * g[i, j, i, n_occ + s] + -4 * g[i, i, j, n_occ + s] + -8 * g[j, n_occ + u, n_occ + s, n_occ + u] + 4 * g[j, n_occ + s, n_occ + u, n_occ + u] ) * K[0, (i*n_virt + u) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, (j*n_virt + s) * n_ex + j*n_virt + u+ 2*n_ex]

												elif ((u != s) and (u != t) and (t == s) and (w == s) and (v != s) and (v != t) and (v != u)):

													L3[i*n_virt + s + n_ex] += (4 * g[j, n_occ + s, n_occ + u, n_occ + v] + -8 * g[j, n_occ + v, n_occ + s, n_occ + u] ) * K[0, (i*n_virt + u) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, (j*n_virt + s) * n_ex + j*n_virt + v+ 2*n_ex]

												elif ((u == s) and (t != s) and (w == t) and (v == s)):

													L3[i*n_virt + s + n_ex] += (4 * g[i, i, j, n_occ + s] + -4 * g[j, n_occ + s, n_occ + s, n_occ + s] + 4 * g[i, j, i, n_occ + s] ) * K[0, (i*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (j*n_virt + t) * n_ex + j*n_virt + s+ 2*n_ex]

												elif ((u == s) and (t != s) and (w == t) and (v == t)):

													L3[i*n_virt + s + n_ex] += (-4 * g[i, j, i, n_occ + t] + 8 * g[i, i, j, n_occ + t] + 4 * g[j, n_occ + s, n_occ + s, n_occ + t] + -8 * g[j, n_occ + t, n_occ + s, n_occ + s] ) * K[0, (i*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (j*n_virt + t) * n_ex + j*n_virt + t+ 2*n_ex]

												elif ((u == s) and (t != s) and (w == t) and (v != s) and (v != t) and (v != u)):

													L3[i*n_virt + s + n_ex] += (-4 * g[i, j, i, n_occ + v] + 8 * g[i, i, j, n_occ + v] + 4 * g[j, n_occ + s, n_occ + s, n_occ + v] + -8 * g[j, n_occ + v, n_occ + s, n_occ + s] ) * K[0, (i*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (j*n_virt + t) * n_ex + j*n_virt + v+ 2*n_ex]

												elif ((u == t) and (t != s) and (w == t) and (v == s)):

													L3[i*n_virt + s + n_ex] += (-4 * g[j, n_occ + s, n_occ + s, n_occ + t] ) * K[0, (i*n_virt + t) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (j*n_virt + t) * n_ex + j*n_virt + s+ 2*n_ex]

												elif ((u == t) and (t != s) and (w == t) and (v == t)):

													L3[i*n_virt + s + n_ex] += (8 * g[i, j, i, n_occ + s] + -4 * g[i, i, j, n_occ + s] + -8 * g[j, n_occ + t, n_occ + s, n_occ + t] + 4 * g[j, n_occ + s, n_occ + t, n_occ + t] ) * K[0, (i*n_virt + t) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (j*n_virt + t) * n_ex + j*n_virt + t+ 2*n_ex]

												elif ((u == t) and (t != s) and (w == t) and (v != s) and (v != t) and (v != u)):

													L3[i*n_virt + s + n_ex] += (4 * g[j, n_occ + s, n_occ + t, n_occ + v] + -8 * g[j, n_occ + v, n_occ + s, n_occ + t] ) * K[0, (i*n_virt + t) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (j*n_virt + t) * n_ex + j*n_virt + v+ 2*n_ex]

												elif ((u != s) and (u != t) and (t != s) and (w == t) and (v == s)):

													L3[i*n_virt + s + n_ex] += (-4 * g[j, n_occ + s, n_occ + s, n_occ + u] ) * K[0, (i*n_virt + u) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (j*n_virt + t) * n_ex + j*n_virt + s+ 2*n_ex]

												elif ((u != s) and (u != t) and (t != s) and (w == t) and (v == t)):

													L3[i*n_virt + s + n_ex] += (4 * g[j, n_occ + s, n_occ + t, n_occ + u] + -8 * g[j, n_occ + t, n_occ + s, n_occ + u] ) * K[0, (i*n_virt + u) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (j*n_virt + t) * n_ex + j*n_virt + t+ 2*n_ex]

												elif ((u != s) and (u != t) and (t != s) and (w == t) and (v == u)):

													L3[i*n_virt + s + n_ex] += (8 * g[i, j, i, n_occ + s] + -4 * g[i, i, j, n_occ + s] + -8 * g[j, n_occ + u, n_occ + s, n_occ + u] + 4 * g[j, n_occ + s, n_occ + u, n_occ + u] ) * K[0, (i*n_virt + u) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (j*n_virt + t) * n_ex + j*n_virt + u+ 2*n_ex]

												elif ((u != s) and (u != t) and (t != s) and (w == t) and (v != s) and (v != t) and (v != u)):

													L3[i*n_virt + s + n_ex] += (4 * g[j, n_occ + s, n_occ + u, n_occ + v] + -8 * g[j, n_occ + v, n_occ + s, n_occ + u] ) * K[0, (i*n_virt + u) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (j*n_virt + t) * n_ex + j*n_virt + v+ 2*n_ex]

											elif ((k == i) and (j != i) and (n == j) and (m != i) and (m != j) and (m != k)):

												if ((u == s) and (t == s) and (w == s) and (v == s)):

													L3[i*n_virt + s + n_ex] += (4 * g[i, i, m, n_occ + s] + -4 * g[m, n_occ + s, n_occ + s, n_occ + s] + 4 * g[i, m, i, n_occ + s] ) * K[0, (i*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, (j*n_virt + s) * n_ex + m*n_virt + s+ 2*n_ex]

												elif ((u == s) and (t == s) and (w == s) and (v != s) and (v != t) and (v != u)):

													L3[i*n_virt + s + n_ex] += (-4 * g[i, m, i, n_occ + v] + 8 * g[i, i, m, n_occ + v] + 4 * g[m, n_occ + s, n_occ + s, n_occ + v] + -8 * g[m, n_occ + v, n_occ + s, n_occ + s] ) * K[0, (i*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, (j*n_virt + s) * n_ex + m*n_virt + v+ 2*n_ex]

												elif ((u != s) and (u != t) and (t == s) and (w == s) and (v == s)):

													L3[i*n_virt + s + n_ex] += (-4 * g[m, n_occ + s, n_occ + s, n_occ + u] ) * K[0, (i*n_virt + u) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, (j*n_virt + s) * n_ex + m*n_virt + s+ 2*n_ex]

												elif ((u != s) and (u != t) and (t == s) and (w == s) and (v == u)):

													L3[i*n_virt + s + n_ex] += (8 * g[i, m, i, n_occ + s] + -4 * g[i, i, m, n_occ + s] + -8 * g[m, n_occ + u, n_occ + s, n_occ + u] + 4 * g[m, n_occ + s, n_occ + u, n_occ + u] ) * K[0, (i*n_virt + u) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, (j*n_virt + s) * n_ex + m*n_virt + u+ 2*n_ex]

												elif ((u != s) and (u != t) and (t == s) and (w == s) and (v != s) and (v != t) and (v != u)):

													L3[i*n_virt + s + n_ex] += (4 * g[m, n_occ + s, n_occ + u, n_occ + v] + -8 * g[m, n_occ + v, n_occ + s, n_occ + u] ) * K[0, (i*n_virt + u) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, (j*n_virt + s) * n_ex + m*n_virt + v+ 2*n_ex]

												elif ((u == s) and (t != s) and (w == t) and (v == s)):

													L3[i*n_virt + s + n_ex] += (4 * g[i, i, m, n_occ + s] + -4 * g[m, n_occ + s, n_occ + s, n_occ + s] + 4 * g[i, m, i, n_occ + s] ) * K[0, (i*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (j*n_virt + t) * n_ex + m*n_virt + s+ 2*n_ex]

												elif ((u == s) and (t != s) and (w == t) and (v == t)):

													L3[i*n_virt + s + n_ex] += (-4 * g[i, m, i, n_occ + t] + 8 * g[i, i, m, n_occ + t] + 4 * g[m, n_occ + s, n_occ + s, n_occ + t] + -8 * g[m, n_occ + t, n_occ + s, n_occ + s] ) * K[0, (i*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (j*n_virt + t) * n_ex + m*n_virt + t+ 2*n_ex]

												elif ((u == s) and (t != s) and (w == t) and (v != s) and (v != t) and (v != u)):

													L3[i*n_virt + s + n_ex] += (-4 * g[i, m, i, n_occ + v] + 8 * g[i, i, m, n_occ + v] + 4 * g[m, n_occ + s, n_occ + s, n_occ + v] + -8 * g[m, n_occ + v, n_occ + s, n_occ + s] ) * K[0, (i*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (j*n_virt + t) * n_ex + m*n_virt + v+ 2*n_ex]

												elif ((u == t) and (t != s) and (w == t) and (v == s)):

													L3[i*n_virt + s + n_ex] += (-4 * g[m, n_occ + s, n_occ + s, n_occ + t] ) * K[0, (i*n_virt + t) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (j*n_virt + t) * n_ex + m*n_virt + s+ 2*n_ex]

												elif ((u == t) and (t != s) and (w == t) and (v == t)):

													L3[i*n_virt + s + n_ex] += (8 * g[i, m, i, n_occ + s] + -4 * g[i, i, m, n_occ + s] + -8 * g[m, n_occ + t, n_occ + s, n_occ + t] + 4 * g[m, n_occ + s, n_occ + t, n_occ + t] ) * K[0, (i*n_virt + t) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (j*n_virt + t) * n_ex + m*n_virt + t+ 2*n_ex]

												elif ((u == t) and (t != s) and (w == t) and (v != s) and (v != t) and (v != u)):

													L3[i*n_virt + s + n_ex] += (4 * g[m, n_occ + s, n_occ + t, n_occ + v] + -8 * g[m, n_occ + v, n_occ + s, n_occ + t] ) * K[0, (i*n_virt + t) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (j*n_virt + t) * n_ex + m*n_virt + v+ 2*n_ex]

												elif ((u != s) and (u != t) and (t != s) and (w == t) and (v == s)):

													L3[i*n_virt + s + n_ex] += (-4 * g[m, n_occ + s, n_occ + s, n_occ + u] ) * K[0, (i*n_virt + u) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (j*n_virt + t) * n_ex + m*n_virt + s+ 2*n_ex]

												elif ((u != s) and (u != t) and (t != s) and (w == t) and (v == t)):

													L3[i*n_virt + s + n_ex] += (4 * g[m, n_occ + s, n_occ + t, n_occ + u] + -8 * g[m, n_occ + t, n_occ + s, n_occ + u] ) * K[0, (i*n_virt + u) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (j*n_virt + t) * n_ex + m*n_virt + t+ 2*n_ex]

												elif ((u != s) and (u != t) and (t != s) and (w == t) and (v == u)):

													L3[i*n_virt + s + n_ex] += (8 * g[i, m, i, n_occ + s] + -4 * g[i, i, m, n_occ + s] + -8 * g[m, n_occ + u, n_occ + s, n_occ + u] + 4 * g[m, n_occ + s, n_occ + u, n_occ + u] ) * K[0, (i*n_virt + u) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (j*n_virt + t) * n_ex + m*n_virt + u+ 2*n_ex]

												elif ((u != s) and (u != t) and (t != s) and (w == t) and (v != s) and (v != t) and (v != u)):

													L3[i*n_virt + s + n_ex] += (4 * g[m, n_occ + s, n_occ + u, n_occ + v] + -8 * g[m, n_occ + v, n_occ + s, n_occ + u] ) * K[0, (i*n_virt + u) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (j*n_virt + t) * n_ex + m*n_virt + v+ 2*n_ex]

											elif ((k == j) and (j != i) and (n == j) and (m == i)):

												if ((u == s) and (t == s) and (w == s) and (v == s)):

													L3[i*n_virt + s + n_ex] += (8 * g[i, j, i, n_occ + s] ) * K[0, (j*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, (j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex]

												elif ((u == s) and (t == s) and (w == s) and (v != s) and (v != t) and (v != u)):

													L3[i*n_virt + s + n_ex] += (4 * g[i, j, i, n_occ + v] ) * K[0, (j*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, (j*n_virt + s) * n_ex + i*n_virt + v+ 2*n_ex]

												elif ((u != s) and (u != t) and (t == s) and (w == s) and (v == u)):

													L3[i*n_virt + s + n_ex] += (4 * g[i, j, i, n_occ + s] ) * K[0, (j*n_virt + u) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, (j*n_virt + s) * n_ex + i*n_virt + u+ 2*n_ex]

												elif ((u == s) and (t != s) and (w == t) and (v == s)):

													L3[i*n_virt + s + n_ex] += (8 * g[i, j, i, n_occ + s] ) * K[0, (j*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex]

												elif ((u == s) and (t != s) and (w == t) and (v == t)):

													L3[i*n_virt + s + n_ex] += (4 * g[i, j, i, n_occ + t] ) * K[0, (j*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (j*n_virt + t) * n_ex + i*n_virt + t+ 2*n_ex]

												elif ((u == s) and (t != s) and (w == t) and (v != s) and (v != t) and (v != u)):

													L3[i*n_virt + s + n_ex] += (4 * g[i, j, i, n_occ + v] ) * K[0, (j*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (j*n_virt + t) * n_ex + i*n_virt + v+ 2*n_ex]

												elif ((u == t) and (t != s) and (w == t) and (v == t)):

													L3[i*n_virt + s + n_ex] += (4 * g[i, j, i, n_occ + s] ) * K[0, (j*n_virt + t) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (j*n_virt + t) * n_ex + i*n_virt + t+ 2*n_ex]

												elif ((u != s) and (u != t) and (t != s) and (w == t) and (v == u)):

													L3[i*n_virt + s + n_ex] += (4 * g[i, j, i, n_occ + s] ) * K[0, (j*n_virt + u) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (j*n_virt + t) * n_ex + i*n_virt + u+ 2*n_ex]

											elif ((k == j) and (j != i) and (n == i) and (m == j)):

												if ((u == s) and (t == s) and (w == s) and (v == s)):

													L3[i*n_virt + s + n_ex] += (-4 * F[j, n_occ + s] + 4 * g[i, j, i, n_occ + s] + -4 * g[j, n_occ + s, n_occ + s, n_occ + s] + 4 * g[i, i, j, n_occ + s] ) * K[0, (j*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, (i*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex]

												elif ((u == s) and (t == s) and (w != s) and (w != t) and (w != u) and (w != v) and (v == s)):

													L3[i*n_virt + s + n_ex] += (-4 * g[j, n_occ + s, n_occ + s, n_occ + w] ) * K[0, (j*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, (i*n_virt + w) * n_ex + j*n_virt + s+ 2*n_ex]

												elif ((u != s) and (u != t) and (t == s) and (w == s) and (v == u)):

													L3[i*n_virt + s + n_ex] += (-4 * F[j, n_occ + s] + 4 * g[i, j, i, n_occ + s] + -4 * g[j, n_occ + s, n_occ + s, n_occ + s] + 4 * g[i, i, j, n_occ + s] ) * K[0, (j*n_virt + u) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, (i*n_virt + s) * n_ex + j*n_virt + u+ 2*n_ex]

												elif ((u != s) and (u != t) and (t == s) and (w == u) and (v == u)):

													L3[i*n_virt + s + n_ex] += (-4 * g[j, n_occ + s, n_occ + s, n_occ + u] ) * K[0, (j*n_virt + u) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, (i*n_virt + u) * n_ex + j*n_virt + u+ 2*n_ex]

												elif ((u != s) and (u != t) and (t == s) and (w != s) and (w != t) and (w != u) and (w != v) and (v == u)):

													L3[i*n_virt + s + n_ex] += (-4 * g[j, n_occ + s, n_occ + s, n_occ + w] ) * K[0, (j*n_virt + u) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, (i*n_virt + w) * n_ex + j*n_virt + u+ 2*n_ex]

												elif ((u == s) and (t != s) and (w == s) and (v == s)):

													L3[i*n_virt + s + n_ex] += (-8 * F[j, n_occ + t] + 4 * g[j, n_occ + s, n_occ + s, n_occ + t] + -8 * g[j, n_occ + t, n_occ + s, n_occ + s] + 8 * g[i, i, j, n_occ + t] + -4 * g[i, j, i, n_occ + t] ) * K[0, (j*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (i*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex]

												elif ((u == s) and (t != s) and (w == t) and (v == s)):

													L3[i*n_virt + s + n_ex] += (4 * F[j, n_occ + s] + -8 * g[j, n_occ + t, n_occ + s, n_occ + t] + 4 * g[j, n_occ + s, n_occ + t, n_occ + t] + -4 * g[i, i, j, n_occ + s] + 8 * g[i, j, i, n_occ + s] ) * K[0, (j*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (i*n_virt + t) * n_ex + j*n_virt + s+ 2*n_ex]

												elif ((u == s) and (t != s) and (w != s) and (w != t) and (w != u) and (w != v) and (v == s)):

													L3[i*n_virt + s + n_ex] += (4 * g[j, n_occ + s, n_occ + t, n_occ + w] + -8 * g[j, n_occ + t, n_occ + s, n_occ + w] ) * K[0, (j*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (i*n_virt + w) * n_ex + j*n_virt + s+ 2*n_ex]

												elif ((u == t) and (t != s) and (w == s) and (v == t)):

													L3[i*n_virt + s + n_ex] += (-8 * F[j, n_occ + t] + 4 * g[j, n_occ + s, n_occ + s, n_occ + t] + -8 * g[j, n_occ + t, n_occ + s, n_occ + s] + 8 * g[i, i, j, n_occ + t] + -4 * g[i, j, i, n_occ + t] ) * K[0, (j*n_virt + t) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (i*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex]

												elif ((u == t) and (t != s) and (w == t) and (v == t)):

													L3[i*n_virt + s + n_ex] += (4 * F[j, n_occ + s] + -8 * g[j, n_occ + t, n_occ + s, n_occ + t] + 4 * g[j, n_occ + s, n_occ + t, n_occ + t] + -4 * g[i, i, j, n_occ + s] + 8 * g[i, j, i, n_occ + s] ) * K[0, (j*n_virt + t) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (i*n_virt + t) * n_ex + j*n_virt + t+ 2*n_ex]

												elif ((u == t) and (t != s) and (w != s) and (w != t) and (w != u) and (w != v) and (v == t)):

													L3[i*n_virt + s + n_ex] += (4 * g[j, n_occ + s, n_occ + t, n_occ + w] + -8 * g[j, n_occ + t, n_occ + s, n_occ + w] ) * K[0, (j*n_virt + t) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (i*n_virt + w) * n_ex + j*n_virt + t+ 2*n_ex]

												elif ((u != s) and (u != t) and (t != s) and (w == s) and (v == u)):

													L3[i*n_virt + s + n_ex] += (-8 * F[j, n_occ + t] + 4 * g[j, n_occ + s, n_occ + s, n_occ + t] + -8 * g[j, n_occ + t, n_occ + s, n_occ + s] + 8 * g[i, i, j, n_occ + t] + -4 * g[i, j, i, n_occ + t] ) * K[0, (j*n_virt + u) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (i*n_virt + s) * n_ex + j*n_virt + u+ 2*n_ex]

												elif ((u != s) and (u != t) and (t != s) and (w == t) and (v == u)):

													L3[i*n_virt + s + n_ex] += (4 * F[j, n_occ + s] + -8 * g[j, n_occ + t, n_occ + s, n_occ + t] + 4 * g[j, n_occ + s, n_occ + t, n_occ + t] + -4 * g[i, i, j, n_occ + s] + 8 * g[i, j, i, n_occ + s] ) * K[0, (j*n_virt + u) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (i*n_virt + t) * n_ex + j*n_virt + u+ 2*n_ex]

												elif ((u != s) and (u != t) and (t != s) and (w == u) and (v == u)):

													L3[i*n_virt + s + n_ex] += (4 * g[j, n_occ + s, n_occ + t, n_occ + u] + -8 * g[j, n_occ + t, n_occ + s, n_occ + u] ) * K[0, (j*n_virt + u) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (i*n_virt + u) * n_ex + j*n_virt + u+ 2*n_ex]

												elif ((u != s) and (u != t) and (t != s) and (w != s) and (w != t) and (w != u) and (w != v) and (v == u)):

													L3[i*n_virt + s + n_ex] += (4 * g[j, n_occ + s, n_occ + t, n_occ + w] + -8 * g[j, n_occ + t, n_occ + s, n_occ + w] ) * K[0, (j*n_virt + u) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (i*n_virt + w) * n_ex + j*n_virt + u+ 2*n_ex]

											elif ((k == j) and (j != i) and (n == j) and (m == j)):

												if ((u == s) and (t == s) and (w == s) and (v == s)):

													L3[i*n_virt + s + n_ex] += (4 * F[i, n_occ + s] + -8 * g[i, n_occ + s, n_occ + s, n_occ + s] + 8 * g[i, j, j, n_occ + s] + 8 * g[i, n_occ + s, j, j] ) * K[0, (j*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, (j*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex]

												elif ((u == s) and (t == s) and (w != s) and (w != t) and (w != u) and (w != v) and (v == s)):

													L3[i*n_virt + s + n_ex] += (-4 * g[i, n_occ + s, n_occ + s, n_occ + w] ) * K[0, (j*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, (j*n_virt + w) * n_ex + j*n_virt + s+ 2*n_ex]

												elif ((u == s) and (t == s) and (w == s) and (v != s) and (v != t) and (v != u)):

													L3[i*n_virt + s + n_ex] += (8 * g[i, j, j, n_occ + v] + -4 * g[i, n_occ + v, j, j] + -8 * g[i, n_occ + s, n_occ + s, n_occ + v] + 4 * g[i, n_occ + v, n_occ + s, n_occ + s] ) * K[0, (j*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, (j*n_virt + s) * n_ex + j*n_virt + v+ 2*n_ex]

												elif ((u != s) and (u != t) and (t == s) and (w == s) and (v == s)):

													L3[i*n_virt + s + n_ex] += (-4 * g[i, n_occ + s, n_occ + s, n_occ + u] ) * K[0, (j*n_virt + u) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, (j*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex]

												elif ((u != s) and (u != t) and (t == s) and (w == s) and (v == u)):

													L3[i*n_virt + s + n_ex] += (4 * F[i, n_occ + s] + 12 * g[i, n_occ + s, j, j] + -4 * g[i, n_occ + s, n_occ + s, n_occ + s] + 4 * g[i, n_occ + u, n_occ + s, n_occ + u] + -8 * g[i, n_occ + s, n_occ + u, n_occ + u] ) * K[0, (j*n_virt + u) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, (j*n_virt + s) * n_ex + j*n_virt + u+ 2*n_ex]

												elif ((u != s) and (u != t) and (t == s) and (w == u) and (v == u)):

													L3[i*n_virt + s + n_ex] += (-4 * g[i, n_occ + s, n_occ + s, n_occ + u] ) * K[0, (j*n_virt + u) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, (j*n_virt + u) * n_ex + j*n_virt + u+ 2*n_ex]

												elif ((u != s) and (u != t) and (t == s) and (w != s) and (w != t) and (w != u) and (w != v) and (v == u)):

													L3[i*n_virt + s + n_ex] += (-4 * g[i, n_occ + s, n_occ + s, n_occ + w] ) * K[0, (j*n_virt + u) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, (j*n_virt + w) * n_ex + j*n_virt + u+ 2*n_ex]

												elif ((u != s) and (u != t) and (t == s) and (w == s) and (v != s) and (v != t) and (v != u)):

													L3[i*n_virt + s + n_ex] += (-8 * g[i, n_occ + s, n_occ + u, n_occ + v] + 4 * g[i, n_occ + v, n_occ + s, n_occ + u] ) * K[0, (j*n_virt + u) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, (j*n_virt + s) * n_ex + j*n_virt + v+ 2*n_ex]

												elif ((u == s) and (t != s) and (w == s) and (v == s)):

													L3[i*n_virt + s + n_ex] += (4 * F[i, n_occ + t] + -8 * g[i, n_occ + s, n_occ + s, n_occ + t] + 4 * g[i, n_occ + t, n_occ + s, n_occ + s] + -4 * g[i, n_occ + t, j, j] + 8 * g[i, j, j, n_occ + t] ) * K[0, (j*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (j*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex]

												elif ((u == s) and (t != s) and (w == t) and (v == s)):

													L3[i*n_virt + s + n_ex] += (4 * g[i, n_occ + t, n_occ + s, n_occ + t] + -8 * g[i, n_occ + s, n_occ + t, n_occ + t] + -4 * g[i, n_occ + s, n_occ + s, n_occ + s] + 12 * g[i, n_occ + s, j, j] ) * K[0, (j*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (j*n_virt + t) * n_ex + j*n_virt + s+ 2*n_ex]

												elif ((u == s) and (t != s) and (w != s) and (w != t) and (w != u) and (w != v) and (v == s)):

													L3[i*n_virt + s + n_ex] += (-8 * g[i, n_occ + s, n_occ + t, n_occ + w] + 4 * g[i, n_occ + t, n_occ + s, n_occ + w] ) * K[0, (j*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (j*n_virt + w) * n_ex + j*n_virt + s+ 2*n_ex]

												elif ((u == s) and (t != s) and (w == t) and (v == t)):

													L3[i*n_virt + s + n_ex] += (8 * g[i, j, j, n_occ + t] + -4 * g[i, n_occ + t, j, j] + -8 * g[i, n_occ + s, n_occ + s, n_occ + t] + 4 * g[i, n_occ + t, n_occ + s, n_occ + s] ) * K[0, (j*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (j*n_virt + t) * n_ex + j*n_virt + t+ 2*n_ex]

												elif ((u == s) and (t != s) and (w == t) and (v != s) and (v != t) and (v != u)):

													L3[i*n_virt + s + n_ex] += (8 * g[i, j, j, n_occ + v] + -4 * g[i, n_occ + v, j, j] + -8 * g[i, n_occ + s, n_occ + s, n_occ + v] + 4 * g[i, n_occ + v, n_occ + s, n_occ + s] ) * K[0, (j*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (j*n_virt + t) * n_ex + j*n_virt + v+ 2*n_ex]

												elif ((u == t) and (t != s) and (w == t) and (v == s)):

													L3[i*n_virt + s + n_ex] += (-4 * g[i, n_occ + s, n_occ + s, n_occ + t] ) * K[0, (j*n_virt + t) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (j*n_virt + t) * n_ex + j*n_virt + s+ 2*n_ex]

												elif ((u == t) and (t != s) and (w == s) and (v == t)):

													L3[i*n_virt + s + n_ex] += (4 * F[i, n_occ + t] + -8 * g[i, n_occ + s, n_occ + s, n_occ + t] + 4 * g[i, n_occ + t, n_occ + s, n_occ + s] + -4 * g[i, n_occ + t, j, j] + 8 * g[i, j, j, n_occ + t] ) * K[0, (j*n_virt + t) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (j*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex]

												elif ((u == t) and (t != s) and (w == t) and (v == t)):

													L3[i*n_virt + s + n_ex] += (8 * g[i, n_occ + t, n_occ + s, n_occ + t] + -16 * g[i, n_occ + s, n_occ + t, n_occ + t] + -8 * g[i, j, j, n_occ + s] + 16 * g[i, n_occ + s, j, j] ) * K[0, (j*n_virt + t) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (j*n_virt + t) * n_ex + j*n_virt + t+ 2*n_ex]

												elif ((u == t) and (t != s) and (w != s) and (w != t) and (w != u) and (w != v) and (v == t)):

													L3[i*n_virt + s + n_ex] += (-8 * g[i, n_occ + s, n_occ + t, n_occ + w] + 4 * g[i, n_occ + t, n_occ + s, n_occ + w] ) * K[0, (j*n_virt + t) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (j*n_virt + w) * n_ex + j*n_virt + t+ 2*n_ex]

												elif ((u == t) and (t != s) and (w == t) and (v != s) and (v != t) and (v != u)):

													L3[i*n_virt + s + n_ex] += (-8 * g[i, n_occ + s, n_occ + t, n_occ + v] + 4 * g[i, n_occ + v, n_occ + s, n_occ + t] ) * K[0, (j*n_virt + t) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (j*n_virt + t) * n_ex + j*n_virt + v+ 2*n_ex]

												elif ((u != s) and (u != t) and (t != s) and (w == t) and (v == s)):

													L3[i*n_virt + s + n_ex] += (-4 * g[i, n_occ + s, n_occ + s, n_occ + u] ) * K[0, (j*n_virt + u) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (j*n_virt + t) * n_ex + j*n_virt + s+ 2*n_ex]

												elif ((u != s) and (u != t) and (t != s) and (w == t) and (v == t)):

													L3[i*n_virt + s + n_ex] += (-8 * g[i, n_occ + s, n_occ + t, n_occ + u] + 4 * g[i, n_occ + t, n_occ + s, n_occ + u] ) * K[0, (j*n_virt + u) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (j*n_virt + t) * n_ex + j*n_virt + t+ 2*n_ex]

												elif ((u != s) and (u != t) and (t != s) and (w == s) and (v == u)):

													L3[i*n_virt + s + n_ex] += (4 * F[i, n_occ + t] + -8 * g[i, n_occ + s, n_occ + s, n_occ + t] + 4 * g[i, n_occ + t, n_occ + s, n_occ + s] + -4 * g[i, n_occ + t, j, j] + 8 * g[i, j, j, n_occ + t] ) * K[0, (j*n_virt + u) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (j*n_virt + s) * n_ex + j*n_virt + u+ 2*n_ex]

												elif ((u != s) and (u != t) and (t != s) and (w == t) and (v == u)):

													L3[i*n_virt + s + n_ex] += (4 * g[i, n_occ + t, n_occ + s, n_occ + t] + -8 * g[i, n_occ + s, n_occ + t, n_occ + t] + 4 * g[i, n_occ + u, n_occ + s, n_occ + u] + -8 * g[i, n_occ + s, n_occ + u, n_occ + u] + -8 * g[i, j, j, n_occ + s] + 16 * g[i, n_occ + s, j, j] ) * K[0, (j*n_virt + u) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (j*n_virt + t) * n_ex + j*n_virt + u+ 2*n_ex]

												elif ((u != s) and (u != t) and (t != s) and (w == u) and (v == u)):

													L3[i*n_virt + s + n_ex] += (-8 * g[i, n_occ + s, n_occ + t, n_occ + u] + 4 * g[i, n_occ + t, n_occ + s, n_occ + u] ) * K[0, (j*n_virt + u) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (j*n_virt + u) * n_ex + j*n_virt + u+ 2*n_ex]

												elif ((u != s) and (u != t) and (t != s) and (w != s) and (w != t) and (w != u) and (w != v) and (v == u)):

													L3[i*n_virt + s + n_ex] += (-8 * g[i, n_occ + s, n_occ + t, n_occ + w] + 4 * g[i, n_occ + t, n_occ + s, n_occ + w] ) * K[0, (j*n_virt + u) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (j*n_virt + w) * n_ex + j*n_virt + u+ 2*n_ex]

												elif ((u != s) and (u != t) and (t != s) and (w == t) and (v != s) and (v != t) and (v != u)):

													L3[i*n_virt + s + n_ex] += (-8 * g[i, n_occ + s, n_occ + u, n_occ + v] + 4 * g[i, n_occ + v, n_occ + s, n_occ + u] ) * K[0, (j*n_virt + u) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (j*n_virt + t) * n_ex + j*n_virt + v+ 2*n_ex]

											elif ((k == j) and (j != i) and (n != i) and (n != j) and (n != k) and (n != m) and (m == j)):

												if ((u == s) and (t == s) and (w == s) and (v == s)):

													L3[i*n_virt + s + n_ex] += (4 * g[i, n, j, n_occ + s] + 4 * g[i, n_occ + s, j, n] ) * K[0, (j*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, (n*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex]

												elif ((u != s) and (u != t) and (t == s) and (w == s) and (v == u)):

													L3[i*n_virt + s + n_ex] += (4 * g[i, n, j, n_occ + s] + 4 * g[i, n_occ + s, j, n] ) * K[0, (j*n_virt + u) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, (n*n_virt + s) * n_ex + j*n_virt + u+ 2*n_ex]

												elif ((u == s) and (t != s) and (w == s) and (v == s)):

													L3[i*n_virt + s + n_ex] += (8 * g[i, n, j, n_occ + t] + -4 * g[i, n_occ + t, j, n] ) * K[0, (j*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (n*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex]

												elif ((u == s) and (t != s) and (w == t) and (v == s)):

													L3[i*n_virt + s + n_ex] += (-4 * g[i, n, j, n_occ + s] + 8 * g[i, n_occ + s, j, n] ) * K[0, (j*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (n*n_virt + t) * n_ex + j*n_virt + s+ 2*n_ex]

												elif ((u == t) and (t != s) and (w == s) and (v == t)):

													L3[i*n_virt + s + n_ex] += (8 * g[i, n, j, n_occ + t] + -4 * g[i, n_occ + t, j, n] ) * K[0, (j*n_virt + t) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (n*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex]

												elif ((u == t) and (t != s) and (w == t) and (v == t)):

													L3[i*n_virt + s + n_ex] += (-4 * g[i, n, j, n_occ + s] + 8 * g[i, n_occ + s, j, n] ) * K[0, (j*n_virt + t) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (n*n_virt + t) * n_ex + j*n_virt + t+ 2*n_ex]

												elif ((u != s) and (u != t) and (t != s) and (w == s) and (v == u)):

													L3[i*n_virt + s + n_ex] += (8 * g[i, n, j, n_occ + t] + -4 * g[i, n_occ + t, j, n] ) * K[0, (j*n_virt + u) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (n*n_virt + s) * n_ex + j*n_virt + u+ 2*n_ex]

												elif ((u != s) and (u != t) and (t != s) and (w == t) and (v == u)):

													L3[i*n_virt + s + n_ex] += (-4 * g[i, n, j, n_occ + s] + 8 * g[i, n_occ + s, j, n] ) * K[0, (j*n_virt + u) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (n*n_virt + t) * n_ex + j*n_virt + u+ 2*n_ex]

											elif ((k == j) and (j != i) and (n == j) and (m != i) and (m != j) and (m != k)):

												if ((u == s) and (t == s) and (w == s) and (v == s)):

													L3[i*n_virt + s + n_ex] += (4 * g[i, j, m, n_occ + s] + 4 * g[i, n_occ + s, j, m] ) * K[0, (j*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, (j*n_virt + s) * n_ex + m*n_virt + s+ 2*n_ex]

												elif ((u == s) and (t == s) and (w == s) and (v != s) and (v != t) and (v != u)):

													L3[i*n_virt + s + n_ex] += (8 * g[i, j, m, n_occ + v] + -4 * g[i, n_occ + v, j, m] ) * K[0, (j*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, (j*n_virt + s) * n_ex + m*n_virt + v+ 2*n_ex]

												elif ((u != s) and (u != t) and (t == s) and (w == s) and (v == u)):

													L3[i*n_virt + s + n_ex] += (-4 * g[i, j, m, n_occ + s] + 8 * g[i, n_occ + s, j, m] ) * K[0, (j*n_virt + u) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, (j*n_virt + s) * n_ex + m*n_virt + u+ 2*n_ex]

												elif ((u == s) and (t != s) and (w == t) and (v == s)):

													L3[i*n_virt + s + n_ex] += (4 * g[i, j, m, n_occ + s] + 4 * g[i, n_occ + s, j, m] ) * K[0, (j*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (j*n_virt + t) * n_ex + m*n_virt + s+ 2*n_ex]

												elif ((u == s) and (t != s) and (w == t) and (v == t)):

													L3[i*n_virt + s + n_ex] += (8 * g[i, j, m, n_occ + t] + -4 * g[i, n_occ + t, j, m] ) * K[0, (j*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (j*n_virt + t) * n_ex + m*n_virt + t+ 2*n_ex]

												elif ((u == s) and (t != s) and (w == t) and (v != s) and (v != t) and (v != u)):

													L3[i*n_virt + s + n_ex] += (8 * g[i, j, m, n_occ + v] + -4 * g[i, n_occ + v, j, m] ) * K[0, (j*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (j*n_virt + t) * n_ex + m*n_virt + v+ 2*n_ex]

												elif ((u == t) and (t != s) and (w == t) and (v == t)):

													L3[i*n_virt + s + n_ex] += (-4 * g[i, j, m, n_occ + s] + 8 * g[i, n_occ + s, j, m] ) * K[0, (j*n_virt + t) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (j*n_virt + t) * n_ex + m*n_virt + t+ 2*n_ex]

												elif ((u != s) and (u != t) and (t != s) and (w == t) and (v == u)):

													L3[i*n_virt + s + n_ex] += (-4 * g[i, j, m, n_occ + s] + 8 * g[i, n_occ + s, j, m] ) * K[0, (j*n_virt + u) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (j*n_virt + t) * n_ex + m*n_virt + u+ 2*n_ex]

											elif ((k != i) and (k != j) and (j != i) and (n == j) and (m == i)):

												if ((u == s) and (t == s) and (w == s) and (v == s)):

													L3[i*n_virt + s + n_ex] += (8 * g[i, k, i, n_occ + s] ) * K[0, (k*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, (j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex]

												elif ((u == s) and (t == s) and (w == s) and (v != s) and (v != t) and (v != u)):

													L3[i*n_virt + s + n_ex] += (4 * g[i, k, i, n_occ + v] ) * K[0, (k*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, (j*n_virt + s) * n_ex + i*n_virt + v+ 2*n_ex]

												elif ((u != s) and (u != t) and (t == s) and (w == s) and (v == u)):

													L3[i*n_virt + s + n_ex] += (4 * g[i, k, i, n_occ + s] ) * K[0, (k*n_virt + u) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, (j*n_virt + s) * n_ex + i*n_virt + u+ 2*n_ex]

												elif ((u == s) and (t != s) and (w == t) and (v == s)):

													L3[i*n_virt + s + n_ex] += (8 * g[i, k, i, n_occ + s] ) * K[0, (k*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex]

												elif ((u == s) and (t != s) and (w == t) and (v == t)):

													L3[i*n_virt + s + n_ex] += (4 * g[i, k, i, n_occ + t] ) * K[0, (k*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (j*n_virt + t) * n_ex + i*n_virt + t+ 2*n_ex]

												elif ((u == s) and (t != s) and (w == t) and (v != s) and (v != t) and (v != u)):

													L3[i*n_virt + s + n_ex] += (4 * g[i, k, i, n_occ + v] ) * K[0, (k*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (j*n_virt + t) * n_ex + i*n_virt + v+ 2*n_ex]

												elif ((u == t) and (t != s) and (w == t) and (v == t)):

													L3[i*n_virt + s + n_ex] += (4 * g[i, k, i, n_occ + s] ) * K[0, (k*n_virt + t) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (j*n_virt + t) * n_ex + i*n_virt + t+ 2*n_ex]

												elif ((u != s) and (u != t) and (t != s) and (w == t) and (v == u)):

													L3[i*n_virt + s + n_ex] += (4 * g[i, k, i, n_occ + s] ) * K[0, (k*n_virt + u) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (j*n_virt + t) * n_ex + i*n_virt + u+ 2*n_ex]

											elif ((k != i) and (k != j) and (j != i) and (n == j) and (m == j)):

												if ((u == s) and (t == s) and (w == s) and (v == s)):

													L3[i*n_virt + s + n_ex] += (4 * g[i, k, j, n_occ + s] + 4 * g[i, n_occ + s, j, k] ) * K[0, (k*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, (j*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex]

												elif ((u == s) and (t == s) and (w == s) and (v != s) and (v != t) and (v != u)):

													L3[i*n_virt + s + n_ex] += (8 * g[i, k, j, n_occ + v] + -4 * g[i, n_occ + v, j, k] ) * K[0, (k*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, (j*n_virt + s) * n_ex + j*n_virt + v+ 2*n_ex]

												elif ((u != s) and (u != t) and (t == s) and (w == s) and (v == u)):

													L3[i*n_virt + s + n_ex] += (-4 * g[i, k, j, n_occ + s] + 8 * g[i, n_occ + s, j, k] ) * K[0, (k*n_virt + u) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, (j*n_virt + s) * n_ex + j*n_virt + u+ 2*n_ex]

												elif ((u == s) and (t != s) and (w == t) and (v == s)):

													L3[i*n_virt + s + n_ex] += (4 * g[i, k, j, n_occ + s] + 4 * g[i, n_occ + s, j, k] ) * K[0, (k*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (j*n_virt + t) * n_ex + j*n_virt + s+ 2*n_ex]

												elif ((u == s) and (t != s) and (w == t) and (v == t)):

													L3[i*n_virt + s + n_ex] += (8 * g[i, k, j, n_occ + t] + -4 * g[i, n_occ + t, j, k] ) * K[0, (k*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (j*n_virt + t) * n_ex + j*n_virt + t+ 2*n_ex]

												elif ((u == s) and (t != s) and (w == t) and (v != s) and (v != t) and (v != u)):

													L3[i*n_virt + s + n_ex] += (8 * g[i, k, j, n_occ + v] + -4 * g[i, n_occ + v, j, k] ) * K[0, (k*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (j*n_virt + t) * n_ex + j*n_virt + v+ 2*n_ex]

												elif ((u == t) and (t != s) and (w == t) and (v == t)):

													L3[i*n_virt + s + n_ex] += (-4 * g[i, k, j, n_occ + s] + 8 * g[i, n_occ + s, j, k] ) * K[0, (k*n_virt + t) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (j*n_virt + t) * n_ex + j*n_virt + t+ 2*n_ex]

												elif ((u != s) and (u != t) and (t != s) and (w == t) and (v == u)):

													L3[i*n_virt + s + n_ex] += (-4 * g[i, k, j, n_occ + s] + 8 * g[i, n_occ + s, j, k] ) * K[0, (k*n_virt + u) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (j*n_virt + t) * n_ex + j*n_virt + u+ 2*n_ex]

											elif ((k != i) and (k != j) and (j != i) and (n == i) and (m == k)):

												if ((u == s) and (t == s) and (w == s) and (v == s)):

													L3[i*n_virt + s + n_ex] += (-4 * F[j, n_occ + s] + 4 * g[i, j, i, n_occ + s] + -4 * g[j, n_occ + s, n_occ + s, n_occ + s] + 4 * g[i, i, j, n_occ + s] ) * K[0, (k*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, (i*n_virt + s) * n_ex + k*n_virt + s+ 2*n_ex]

												elif ((u == s) and (t == s) and (w != s) and (w != t) and (w != u) and (w != v) and (v == s)):

													L3[i*n_virt + s + n_ex] += (-4 * g[j, n_occ + s, n_occ + s, n_occ + w] ) * K[0, (k*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, (i*n_virt + w) * n_ex + k*n_virt + s+ 2*n_ex]

												elif ((u != s) and (u != t) and (t == s) and (w == s) and (v == u)):

													L3[i*n_virt + s + n_ex] += (-4 * F[j, n_occ + s] + 4 * g[i, j, i, n_occ + s] + -4 * g[j, n_occ + s, n_occ + s, n_occ + s] + 4 * g[i, i, j, n_occ + s] ) * K[0, (k*n_virt + u) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, (i*n_virt + s) * n_ex + k*n_virt + u+ 2*n_ex]

												elif ((u != s) and (u != t) and (t == s) and (w == u) and (v == u)):

													L3[i*n_virt + s + n_ex] += (-4 * g[j, n_occ + s, n_occ + s, n_occ + u] ) * K[0, (k*n_virt + u) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, (i*n_virt + u) * n_ex + k*n_virt + u+ 2*n_ex]

												elif ((u != s) and (u != t) and (t == s) and (w != s) and (w != t) and (w != u) and (w != v) and (v == u)):

													L3[i*n_virt + s + n_ex] += (-4 * g[j, n_occ + s, n_occ + s, n_occ + w] ) * K[0, (k*n_virt + u) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, (i*n_virt + w) * n_ex + k*n_virt + u+ 2*n_ex]

												elif ((u == s) and (t != s) and (w == s) and (v == s)):

													L3[i*n_virt + s + n_ex] += (-8 * F[j, n_occ + t] + 4 * g[j, n_occ + s, n_occ + s, n_occ + t] + -8 * g[j, n_occ + t, n_occ + s, n_occ + s] + 8 * g[i, i, j, n_occ + t] + -4 * g[i, j, i, n_occ + t] ) * K[0, (k*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (i*n_virt + s) * n_ex + k*n_virt + s+ 2*n_ex]

												elif ((u == s) and (t != s) and (w == t) and (v == s)):

													L3[i*n_virt + s + n_ex] += (4 * F[j, n_occ + s] + -8 * g[j, n_occ + t, n_occ + s, n_occ + t] + 4 * g[j, n_occ + s, n_occ + t, n_occ + t] + -4 * g[i, i, j, n_occ + s] + 8 * g[i, j, i, n_occ + s] ) * K[0, (k*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (i*n_virt + t) * n_ex + k*n_virt + s+ 2*n_ex]

												elif ((u == s) and (t != s) and (w != s) and (w != t) and (w != u) and (w != v) and (v == s)):

													L3[i*n_virt + s + n_ex] += (4 * g[j, n_occ + s, n_occ + t, n_occ + w] + -8 * g[j, n_occ + t, n_occ + s, n_occ + w] ) * K[0, (k*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (i*n_virt + w) * n_ex + k*n_virt + s+ 2*n_ex]

												elif ((u == t) and (t != s) and (w == s) and (v == t)):

													L3[i*n_virt + s + n_ex] += (-8 * F[j, n_occ + t] + 4 * g[j, n_occ + s, n_occ + s, n_occ + t] + -8 * g[j, n_occ + t, n_occ + s, n_occ + s] + 8 * g[i, i, j, n_occ + t] + -4 * g[i, j, i, n_occ + t] ) * K[0, (k*n_virt + t) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (i*n_virt + s) * n_ex + k*n_virt + t+ 2*n_ex]

												elif ((u == t) and (t != s) and (w == t) and (v == t)):

													L3[i*n_virt + s + n_ex] += (4 * F[j, n_occ + s] + -8 * g[j, n_occ + t, n_occ + s, n_occ + t] + 4 * g[j, n_occ + s, n_occ + t, n_occ + t] + -4 * g[i, i, j, n_occ + s] + 8 * g[i, j, i, n_occ + s] ) * K[0, (k*n_virt + t) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (i*n_virt + t) * n_ex + k*n_virt + t+ 2*n_ex]

												elif ((u == t) and (t != s) and (w != s) and (w != t) and (w != u) and (w != v) and (v == t)):

													L3[i*n_virt + s + n_ex] += (4 * g[j, n_occ + s, n_occ + t, n_occ + w] + -8 * g[j, n_occ + t, n_occ + s, n_occ + w] ) * K[0, (k*n_virt + t) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (i*n_virt + w) * n_ex + k*n_virt + t+ 2*n_ex]

												elif ((u != s) and (u != t) and (t != s) and (w == s) and (v == u)):

													L3[i*n_virt + s + n_ex] += (-8 * F[j, n_occ + t] + 4 * g[j, n_occ + s, n_occ + s, n_occ + t] + -8 * g[j, n_occ + t, n_occ + s, n_occ + s] + 8 * g[i, i, j, n_occ + t] + -4 * g[i, j, i, n_occ + t] ) * K[0, (k*n_virt + u) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (i*n_virt + s) * n_ex + k*n_virt + u+ 2*n_ex]

												elif ((u != s) and (u != t) and (t != s) and (w == t) and (v == u)):

													L3[i*n_virt + s + n_ex] += (4 * F[j, n_occ + s] + -8 * g[j, n_occ + t, n_occ + s, n_occ + t] + 4 * g[j, n_occ + s, n_occ + t, n_occ + t] + -4 * g[i, i, j, n_occ + s] + 8 * g[i, j, i, n_occ + s] ) * K[0, (k*n_virt + u) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (i*n_virt + t) * n_ex + k*n_virt + u+ 2*n_ex]

												elif ((u != s) and (u != t) and (t != s) and (w == u) and (v == u)):

													L3[i*n_virt + s + n_ex] += (4 * g[j, n_occ + s, n_occ + t, n_occ + u] + -8 * g[j, n_occ + t, n_occ + s, n_occ + u] ) * K[0, (k*n_virt + u) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (i*n_virt + u) * n_ex + k*n_virt + u+ 2*n_ex]

												elif ((u != s) and (u != t) and (t != s) and (w != s) and (w != t) and (w != u) and (w != v) and (v == u)):

													L3[i*n_virt + s + n_ex] += (4 * g[j, n_occ + s, n_occ + t, n_occ + w] + -8 * g[j, n_occ + t, n_occ + s, n_occ + w] ) * K[0, (k*n_virt + u) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (i*n_virt + w) * n_ex + k*n_virt + u+ 2*n_ex]

											elif ((k != i) and (k != j) and (j != i) and (n == j) and (m == k)):

												if ((u == s) and (t == s) and (w == s) and (v == s)):

													L3[i*n_virt + s + n_ex] += (4 * F[i, n_occ + s] + -8 * g[i, n_occ + s, n_occ + s, n_occ + s] + 4 * g[i, n_occ + s, j, j] + 4 * g[i, n_occ + s, k, k] + 4 * g[i, j, j, n_occ + s] + 4 * g[i, k, k, n_occ + s] ) * K[0, (k*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, (j*n_virt + s) * n_ex + k*n_virt + s+ 2*n_ex]

												elif ((u == s) and (t == s) and (w != s) and (w != t) and (w != u) and (w != v) and (v == s)):

													L3[i*n_virt + s + n_ex] += (-4 * g[i, n_occ + s, n_occ + s, n_occ + w] ) * K[0, (k*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, (j*n_virt + w) * n_ex + k*n_virt + s+ 2*n_ex]

												elif ((u == s) and (t == s) and (w == s) and (v != s) and (v != t) and (v != u)):

													L3[i*n_virt + s + n_ex] += (8 * g[i, k, k, n_occ + v] + -4 * g[i, n_occ + v, k, k] + -8 * g[i, n_occ + s, n_occ + s, n_occ + v] + 4 * g[i, n_occ + v, n_occ + s, n_occ + s] ) * K[0, (k*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, (j*n_virt + s) * n_ex + k*n_virt + v+ 2*n_ex]

												elif ((u != s) and (u != t) and (t == s) and (w == s) and (v == s)):

													L3[i*n_virt + s + n_ex] += (-4 * g[i, n_occ + s, n_occ + s, n_occ + u] ) * K[0, (k*n_virt + u) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, (j*n_virt + s) * n_ex + k*n_virt + s+ 2*n_ex]

												elif ((u != s) and (u != t) and (t == s) and (w == s) and (v == u)):

													L3[i*n_virt + s + n_ex] += (4 * F[i, n_occ + s] + -4 * g[i, n_occ + s, n_occ + s, n_occ + s] + 4 * g[i, n_occ + u, n_occ + s, n_occ + u] + -8 * g[i, n_occ + s, n_occ + u, n_occ + u] + -4 * g[i, k, k, n_occ + s] + 8 * g[i, n_occ + s, k, k] + 4 * g[i, n_occ + s, j, j] + 4 * g[i, j, j, n_occ + s] ) * K[0, (k*n_virt + u) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, (j*n_virt + s) * n_ex + k*n_virt + u+ 2*n_ex]

												elif ((u != s) and (u != t) and (t == s) and (w == u) and (v == u)):

													L3[i*n_virt + s + n_ex] += (-4 * g[i, n_occ + s, n_occ + s, n_occ + u] ) * K[0, (k*n_virt + u) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, (j*n_virt + u) * n_ex + k*n_virt + u+ 2*n_ex]

												elif ((u != s) and (u != t) and (t == s) and (w != s) and (w != t) and (w != u) and (w != v) and (v == u)):

													L3[i*n_virt + s + n_ex] += (-4 * g[i, n_occ + s, n_occ + s, n_occ + w] ) * K[0, (k*n_virt + u) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, (j*n_virt + w) * n_ex + k*n_virt + u+ 2*n_ex]

												elif ((u != s) and (u != t) and (t == s) and (w == s) and (v != s) and (v != t) and (v != u)):

													L3[i*n_virt + s + n_ex] += (-8 * g[i, n_occ + s, n_occ + u, n_occ + v] + 4 * g[i, n_occ + v, n_occ + s, n_occ + u] ) * K[0, (k*n_virt + u) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, (j*n_virt + s) * n_ex + k*n_virt + v+ 2*n_ex]

												elif ((u == s) and (t != s) and (w == s) and (v == s)):

													L3[i*n_virt + s + n_ex] += (4 * F[i, n_occ + t] + -8 * g[i, n_occ + s, n_occ + s, n_occ + t] + 4 * g[i, n_occ + t, n_occ + s, n_occ + s] + -4 * g[i, n_occ + t, j, j] + 8 * g[i, j, j, n_occ + t] ) * K[0, (k*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (j*n_virt + s) * n_ex + k*n_virt + s+ 2*n_ex]

												elif ((u == s) and (t != s) and (w == t) and (v == s)):

													L3[i*n_virt + s + n_ex] += (4 * g[i, n_occ + t, n_occ + s, n_occ + t] + -8 * g[i, n_occ + s, n_occ + t, n_occ + t] + 4 * g[i, k, k, n_occ + s] + -4 * g[i, n_occ + s, n_occ + s, n_occ + s] + -4 * g[i, j, j, n_occ + s] + 8 * g[i, n_occ + s, j, j] + 4 * g[i, n_occ + s, k, k] ) * K[0, (k*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (j*n_virt + t) * n_ex + k*n_virt + s+ 2*n_ex]

												elif ((u == s) and (t != s) and (w != s) and (w != t) and (w != u) and (w != v) and (v == s)):

													L3[i*n_virt + s + n_ex] += (-8 * g[i, n_occ + s, n_occ + t, n_occ + w] + 4 * g[i, n_occ + t, n_occ + s, n_occ + w] ) * K[0, (k*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (j*n_virt + w) * n_ex + k*n_virt + s+ 2*n_ex]

												elif ((u == s) and (t != s) and (w == t) and (v == t)):

													L3[i*n_virt + s + n_ex] += (8 * g[i, k, k, n_occ + t] + -4 * g[i, n_occ + t, k, k] + -8 * g[i, n_occ + s, n_occ + s, n_occ + t] + 4 * g[i, n_occ + t, n_occ + s, n_occ + s] ) * K[0, (k*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (j*n_virt + t) * n_ex + k*n_virt + t+ 2*n_ex]

												elif ((u == s) and (t != s) and (w == t) and (v != s) and (v != t) and (v != u)):

													L3[i*n_virt + s + n_ex] += (8 * g[i, k, k, n_occ + v] + -4 * g[i, n_occ + v, k, k] + -8 * g[i, n_occ + s, n_occ + s, n_occ + v] + 4 * g[i, n_occ + v, n_occ + s, n_occ + s] ) * K[0, (k*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (j*n_virt + t) * n_ex + k*n_virt + v+ 2*n_ex]

												elif ((u == t) and (t != s) and (w == t) and (v == s)):

													L3[i*n_virt + s + n_ex] += (-4 * g[i, n_occ + s, n_occ + s, n_occ + t] ) * K[0, (k*n_virt + t) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (j*n_virt + t) * n_ex + k*n_virt + s+ 2*n_ex]

												elif ((u == t) and (t != s) and (w == s) and (v == t)):

													L3[i*n_virt + s + n_ex] += (4 * F[i, n_occ + t] + -8 * g[i, n_occ + s, n_occ + s, n_occ + t] + 4 * g[i, n_occ + t, n_occ + s, n_occ + s] + -4 * g[i, n_occ + t, j, j] + 8 * g[i, j, j, n_occ + t] ) * K[0, (k*n_virt + t) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (j*n_virt + s) * n_ex + k*n_virt + t+ 2*n_ex]

												elif ((u == t) and (t != s) and (w == t) and (v == t)):

													L3[i*n_virt + s + n_ex] += (8 * g[i, n_occ + t, n_occ + s, n_occ + t] + -16 * g[i, n_occ + s, n_occ + t, n_occ + t] + -4 * g[i, j, j, n_occ + s] + -4 * g[i, k, k, n_occ + s] + 8 * g[i, n_occ + s, j, j] + 8 * g[i, n_occ + s, k, k] ) * K[0, (k*n_virt + t) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (j*n_virt + t) * n_ex + k*n_virt + t+ 2*n_ex]

												elif ((u == t) and (t != s) and (w != s) and (w != t) and (w != u) and (w != v) and (v == t)):

													L3[i*n_virt + s + n_ex] += (-8 * g[i, n_occ + s, n_occ + t, n_occ + w] + 4 * g[i, n_occ + t, n_occ + s, n_occ + w] ) * K[0, (k*n_virt + t) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (j*n_virt + w) * n_ex + k*n_virt + t+ 2*n_ex]

												elif ((u == t) and (t != s) and (w == t) and (v != s) and (v != t) and (v != u)):

													L3[i*n_virt + s + n_ex] += (-8 * g[i, n_occ + s, n_occ + t, n_occ + v] + 4 * g[i, n_occ + v, n_occ + s, n_occ + t] ) * K[0, (k*n_virt + t) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (j*n_virt + t) * n_ex + k*n_virt + v+ 2*n_ex]

												elif ((u != s) and (u != t) and (t != s) and (w == t) and (v == s)):

													L3[i*n_virt + s + n_ex] += (-4 * g[i, n_occ + s, n_occ + s, n_occ + u] ) * K[0, (k*n_virt + u) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (j*n_virt + t) * n_ex + k*n_virt + s+ 2*n_ex]

												elif ((u != s) and (u != t) and (t != s) and (w == t) and (v == t)):

													L3[i*n_virt + s + n_ex] += (-8 * g[i, n_occ + s, n_occ + t, n_occ + u] + 4 * g[i, n_occ + t, n_occ + s, n_occ + u] ) * K[0, (k*n_virt + u) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (j*n_virt + t) * n_ex + k*n_virt + t+ 2*n_ex]

												elif ((u != s) and (u != t) and (t != s) and (w == s) and (v == u)):

													L3[i*n_virt + s + n_ex] += (4 * F[i, n_occ + t] + -8 * g[i, n_occ + s, n_occ + s, n_occ + t] + 4 * g[i, n_occ + t, n_occ + s, n_occ + s] + -4 * g[i, n_occ + t, j, j] + 8 * g[i, j, j, n_occ + t] ) * K[0, (k*n_virt + u) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (j*n_virt + s) * n_ex + k*n_virt + u+ 2*n_ex]

												elif ((u != s) and (u != t) and (t != s) and (w == t) and (v == u)):

													L3[i*n_virt + s + n_ex] += (4 * g[i, n_occ + t, n_occ + s, n_occ + t] + -8 * g[i, n_occ + s, n_occ + t, n_occ + t] + 4 * g[i, n_occ + u, n_occ + s, n_occ + u] + -8 * g[i, n_occ + s, n_occ + u, n_occ + u] + -4 * g[i, j, j, n_occ + s] + -4 * g[i, k, k, n_occ + s] + 8 * g[i, n_occ + s, j, j] + 8 * g[i, n_occ + s, k, k] ) * K[0, (k*n_virt + u) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (j*n_virt + t) * n_ex + k*n_virt + u+ 2*n_ex]

												elif ((u != s) and (u != t) and (t != s) and (w == u) and (v == u)):

													L3[i*n_virt + s + n_ex] += (-8 * g[i, n_occ + s, n_occ + t, n_occ + u] + 4 * g[i, n_occ + t, n_occ + s, n_occ + u] ) * K[0, (k*n_virt + u) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (j*n_virt + u) * n_ex + k*n_virt + u+ 2*n_ex]

												elif ((u != s) and (u != t) and (t != s) and (w != s) and (w != t) and (w != u) and (w != v) and (v == u)):

													L3[i*n_virt + s + n_ex] += (-8 * g[i, n_occ + s, n_occ + t, n_occ + w] + 4 * g[i, n_occ + t, n_occ + s, n_occ + w] ) * K[0, (k*n_virt + u) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (j*n_virt + w) * n_ex + k*n_virt + u+ 2*n_ex]

												elif ((u != s) and (u != t) and (t != s) and (w == t) and (v != s) and (v != t) and (v != u)):

													L3[i*n_virt + s + n_ex] += (-8 * g[i, n_occ + s, n_occ + u, n_occ + v] + 4 * g[i, n_occ + v, n_occ + s, n_occ + u] ) * K[0, (k*n_virt + u) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (j*n_virt + t) * n_ex + k*n_virt + v+ 2*n_ex]

											elif ((k != i) and (k != j) and (j != i) and (n == k) and (m == k)):

												if ((u == s) and (t == s) and (w == s) and (v == s)):

													L3[i*n_virt + s + n_ex] += (4 * g[i, k, j, n_occ + s] + 4 * g[i, n_occ + s, j, k] ) * K[0, (k*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, (k*n_virt + s) * n_ex + k*n_virt + s+ 2*n_ex]

												elif ((u != s) and (u != t) and (t == s) and (w == s) and (v == u)):

													L3[i*n_virt + s + n_ex] += (4 * g[i, k, j, n_occ + s] + 4 * g[i, n_occ + s, j, k] ) * K[0, (k*n_virt + u) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, (k*n_virt + s) * n_ex + k*n_virt + u+ 2*n_ex]

												elif ((u == s) and (t != s) and (w == s) and (v == s)):

													L3[i*n_virt + s + n_ex] += (8 * g[i, k, j, n_occ + t] + -4 * g[i, n_occ + t, j, k] ) * K[0, (k*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (k*n_virt + s) * n_ex + k*n_virt + s+ 2*n_ex]

												elif ((u == s) and (t != s) and (w == t) and (v == s)):

													L3[i*n_virt + s + n_ex] += (-4 * g[i, k, j, n_occ + s] + 8 * g[i, n_occ + s, j, k] ) * K[0, (k*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (k*n_virt + t) * n_ex + k*n_virt + s+ 2*n_ex]

												elif ((u == t) and (t != s) and (w == s) and (v == t)):

													L3[i*n_virt + s + n_ex] += (8 * g[i, k, j, n_occ + t] + -4 * g[i, n_occ + t, j, k] ) * K[0, (k*n_virt + t) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (k*n_virt + s) * n_ex + k*n_virt + t+ 2*n_ex]

												elif ((u == t) and (t != s) and (w == t) and (v == t)):

													L3[i*n_virt + s + n_ex] += (-4 * g[i, k, j, n_occ + s] + 8 * g[i, n_occ + s, j, k] ) * K[0, (k*n_virt + t) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (k*n_virt + t) * n_ex + k*n_virt + t+ 2*n_ex]

												elif ((u != s) and (u != t) and (t != s) and (w == s) and (v == u)):

													L3[i*n_virt + s + n_ex] += (8 * g[i, k, j, n_occ + t] + -4 * g[i, n_occ + t, j, k] ) * K[0, (k*n_virt + u) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (k*n_virt + s) * n_ex + k*n_virt + u+ 2*n_ex]

												elif ((u != s) and (u != t) and (t != s) and (w == t) and (v == u)):

													L3[i*n_virt + s + n_ex] += (-4 * g[i, k, j, n_occ + s] + 8 * g[i, n_occ + s, j, k] ) * K[0, (k*n_virt + u) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (k*n_virt + t) * n_ex + k*n_virt + u+ 2*n_ex]

											elif ((k != i) and (k != j) and (j != i) and (n != i) and (n != j) and (n != k) and (n != m) and (m == k)):

												if ((u == s) and (t == s) and (w == s) and (v == s)):

													L3[i*n_virt + s + n_ex] += (4 * g[i, n, j, n_occ + s] + 4 * g[i, n_occ + s, j, n] ) * K[0, (k*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, (n*n_virt + s) * n_ex + k*n_virt + s+ 2*n_ex]

												elif ((u != s) and (u != t) and (t == s) and (w == s) and (v == u)):

													L3[i*n_virt + s + n_ex] += (4 * g[i, n, j, n_occ + s] + 4 * g[i, n_occ + s, j, n] ) * K[0, (k*n_virt + u) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, (n*n_virt + s) * n_ex + k*n_virt + u+ 2*n_ex]

												elif ((u == s) and (t != s) and (w == s) and (v == s)):

													L3[i*n_virt + s + n_ex] += (8 * g[i, n, j, n_occ + t] + -4 * g[i, n_occ + t, j, n] ) * K[0, (k*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (n*n_virt + s) * n_ex + k*n_virt + s+ 2*n_ex]

												elif ((u == s) and (t != s) and (w == t) and (v == s)):

													L3[i*n_virt + s + n_ex] += (-4 * g[i, n, j, n_occ + s] + 8 * g[i, n_occ + s, j, n] ) * K[0, (k*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (n*n_virt + t) * n_ex + k*n_virt + s+ 2*n_ex]

												elif ((u == t) and (t != s) and (w == s) and (v == t)):

													L3[i*n_virt + s + n_ex] += (8 * g[i, n, j, n_occ + t] + -4 * g[i, n_occ + t, j, n] ) * K[0, (k*n_virt + t) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (n*n_virt + s) * n_ex + k*n_virt + t+ 2*n_ex]

												elif ((u == t) and (t != s) and (w == t) and (v == t)):

													L3[i*n_virt + s + n_ex] += (-4 * g[i, n, j, n_occ + s] + 8 * g[i, n_occ + s, j, n] ) * K[0, (k*n_virt + t) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (n*n_virt + t) * n_ex + k*n_virt + t+ 2*n_ex]

												elif ((u != s) and (u != t) and (t != s) and (w == s) and (v == u)):

													L3[i*n_virt + s + n_ex] += (8 * g[i, n, j, n_occ + t] + -4 * g[i, n_occ + t, j, n] ) * K[0, (k*n_virt + u) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (n*n_virt + s) * n_ex + k*n_virt + u+ 2*n_ex]

												elif ((u != s) and (u != t) and (t != s) and (w == t) and (v == u)):

													L3[i*n_virt + s + n_ex] += (-4 * g[i, n, j, n_occ + s] + 8 * g[i, n_occ + s, j, n] ) * K[0, (k*n_virt + u) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (n*n_virt + t) * n_ex + k*n_virt + u+ 2*n_ex]

											elif ((k != i) and (k != j) and (j != i) and (n == j) and (m != i) and (m != j) and (m != k)):

												if ((u == s) and (t == s) and (w == s) and (v == s)):

													L3[i*n_virt + s + n_ex] += (4 * g[i, k, m, n_occ + s] + 4 * g[i, n_occ + s, k, m] ) * K[0, (k*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, (j*n_virt + s) * n_ex + m*n_virt + s+ 2*n_ex]

												elif ((u == s) and (t == s) and (w == s) and (v != s) and (v != t) and (v != u)):

													L3[i*n_virt + s + n_ex] += (8 * g[i, k, m, n_occ + v] + -4 * g[i, n_occ + v, k, m] ) * K[0, (k*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, (j*n_virt + s) * n_ex + m*n_virt + v+ 2*n_ex]

												elif ((u != s) and (u != t) and (t == s) and (w == s) and (v == u)):

													L3[i*n_virt + s + n_ex] += (-4 * g[i, k, m, n_occ + s] + 8 * g[i, n_occ + s, k, m] ) * K[0, (k*n_virt + u) * n_ex + j*n_virt + s+ 2*n_ex] * K[1, (j*n_virt + s) * n_ex + m*n_virt + u+ 2*n_ex]

												elif ((u == s) and (t != s) and (w == t) and (v == s)):

													L3[i*n_virt + s + n_ex] += (4 * g[i, k, m, n_occ + s] + 4 * g[i, n_occ + s, k, m] ) * K[0, (k*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (j*n_virt + t) * n_ex + m*n_virt + s+ 2*n_ex]

												elif ((u == s) and (t != s) and (w == t) and (v == t)):

													L3[i*n_virt + s + n_ex] += (8 * g[i, k, m, n_occ + t] + -4 * g[i, n_occ + t, k, m] ) * K[0, (k*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (j*n_virt + t) * n_ex + m*n_virt + t+ 2*n_ex]

												elif ((u == s) and (t != s) and (w == t) and (v != s) and (v != t) and (v != u)):

													L3[i*n_virt + s + n_ex] += (8 * g[i, k, m, n_occ + v] + -4 * g[i, n_occ + v, k, m] ) * K[0, (k*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (j*n_virt + t) * n_ex + m*n_virt + v+ 2*n_ex]

												elif ((u == t) and (t != s) and (w == t) and (v == t)):

													L3[i*n_virt + s + n_ex] += (-4 * g[i, k, m, n_occ + s] + 8 * g[i, n_occ + s, k, m] ) * K[0, (k*n_virt + t) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (j*n_virt + t) * n_ex + m*n_virt + t+ 2*n_ex]

												elif ((u != s) and (u != t) and (t != s) and (w == t) and (v == u)):

													L3[i*n_virt + s + n_ex] += (-4 * g[i, k, m, n_occ + s] + 8 * g[i, n_occ + s, k, m] ) * K[0, (k*n_virt + u) * n_ex + j*n_virt + t+ 2*n_ex] * K[1, (j*n_virt + t) * n_ex + m*n_virt + u+ 2*n_ex]

	# This operator combination: {'a': 3, 'b': 3, 'c': 3}
	# All terms vanished for this combination
	return L3

