import numpy as np


def L2(n_occ, n_virt, H00, F, g, K): 
 
	n_ex = n_occ * n_virt

	# This operator combination: {'a': 1, 'b': 1}
	for i in range(n_occ):
		for j in range(n_occ):
			for s in range(n_virt):
				for t in range(n_virt):

					if ((j == i)):

						if ((t == s)):

							L2[i*n_virt + s] += (-2 * g[i, n_occ + s, i, n_occ + s] ) * K[0, i*n_virt + s]

						elif ((t != s)):

							L2[i*n_virt + s] += (-2 * g[i, n_occ + s, i, n_occ + t] ) * K[0, i*n_virt + t]

					elif ((j != i)):

						if ((t == s)):

							L2[i*n_virt + s] += (-2 * g[i, n_occ + s, j, n_occ + s] ) * K[0, j*n_virt + s]

						elif ((t != s)):

							L2[i*n_virt + s] += (-4 * g[i, n_occ + s, j, n_occ + t] + 2 * g[i, n_occ + t, j, n_occ + s] ) * K[0, j*n_virt + t]

	# This operator combination: {'a': 1, 'b': 2}
	for i in range(n_occ):
		for j in range(n_occ):
			for s in range(n_virt):
				for t in range(n_virt):

					if ((j == i)):

						if ((t == s)):

							L2[i*n_virt + s + n_ex] += (-2 * F[i, i] + 2 * F[n_occ + s, n_occ + s] + -2 * g[i, i, n_occ + s, n_occ + s] + 4 * g[i, n_occ + s, i, n_occ + s] ) * K[0, i*n_virt + s]

						elif ((t != s)):

							L2[i*n_virt + s + n_ex] += (2 * F[n_occ + s, n_occ + t] + -2 * g[i, i, n_occ + s, n_occ + t] + 4 * g[i, n_occ + s, i, n_occ + t] ) * K[0, i*n_virt + t]

					elif ((j != i)):

						if ((t == s)):

							L2[i*n_virt + s + n_ex] += (-2 * F[i, j] + 4 * g[i, n_occ + s, j, n_occ + s] + -2 * g[i, j, n_occ + s, n_occ + s] ) * K[0, j*n_virt + s]

						elif ((t != s)):

							L2[i*n_virt + s + n_ex] += (-2 * g[i, j, n_occ + s, n_occ + t] + 4 * g[i, n_occ + s, j, n_occ + t] ) * K[0, j*n_virt + t]

	# This operator combination: {'a': 1, 'b': 3}
	# All terms vanished for this combination

	# This operator combination: {'a': 2, 'b': 1}
	for i in range(n_occ):
		for j in range(n_occ):
			for s in range(n_virt):
				for t in range(n_virt):

					if ((j == i)):

						if ((t == s)):

							L2[i*n_virt + s] += (-2 * F[n_occ + s, n_occ + s] + 2 * F[i, i] + 2 * g[i, i, n_occ + s, n_occ + s] + -4 * g[i, n_occ + s, i, n_occ + s] ) * K[0, i*n_virt + s + n_ex]

						elif ((t != s)):

							L2[i*n_virt + s] += (-2 * F[n_occ + s, n_occ + t] + 2 * g[i, i, n_occ + s, n_occ + t] + -4 * g[i, n_occ + s, i, n_occ + t] ) * K[0, i*n_virt + t + n_ex]

					elif ((j != i)):

						if ((t == s)):

							L2[i*n_virt + s] += (2 * F[i, j] + -4 * g[i, n_occ + s, j, n_occ + s] + 2 * g[i, j, n_occ + s, n_occ + s] ) * K[0, j*n_virt + s + n_ex]

						elif ((t != s)):

							L2[i*n_virt + s] += (2 * g[i, j, n_occ + s, n_occ + t] + -4 * g[i, n_occ + s, j, n_occ + t] ) * K[0, j*n_virt + t + n_ex]

	# This operator combination: {'a': 2, 'b': 2}
	for i in range(n_occ):
		for j in range(n_occ):
			for s in range(n_virt):
				for t in range(n_virt):

					if ((j == i)):

						if ((t == s)):

							L2[i*n_virt + s + n_ex] += (2 * g[i, n_occ + s, i, n_occ + s] ) * K[0, i*n_virt + s + n_ex]

						elif ((t != s)):

							L2[i*n_virt + s + n_ex] += (2 * g[i, n_occ + s, i, n_occ + t] ) * K[0, i*n_virt + t + n_ex]

					elif ((j != i)):

						if ((t == s)):

							L2[i*n_virt + s + n_ex] += (2 * g[i, n_occ + s, j, n_occ + s] ) * K[0, j*n_virt + s + n_ex]

						elif ((t != s)):

							L2[i*n_virt + s + n_ex] += (4 * g[i, n_occ + s, j, n_occ + t] + -2 * g[i, n_occ + t, j, n_occ + s] ) * K[0, j*n_virt + t + n_ex]

	# This operator combination: {'a': 2, 'b': 3}
	# All terms vanished for this combination

	# This operator combination: {'a': 3, 'b': 1}
	for i in range(n_occ):
		for k in range(n_occ):
			for j in range(n_occ):
				for s in range(n_virt):
					for u in range(n_virt):
						for t in range(n_virt):

							if ((k == i) and (j == i)):

								if ((u == s) and (t == s)):

									L2[i*n_virt + s] += (4 * F[i, n_occ + s] ) * K[0, (i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex]

								elif ((u != s) and (u != t) and (t == s)):

									L2[i*n_virt + s] += (4 * F[i, n_occ + u] ) * K[0, (i*n_virt + u) * n_ex + i*n_virt + s+ 2*n_ex]

							elif ((k != i) and (k != j) and (j == i)):

								if ((u == s) and (t == s)):

									L2[i*n_virt + s] += (4 * F[k, n_occ + s] ) * K[0, (k*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex]

								elif ((u != s) and (u != t) and (t == s)):

									L2[i*n_virt + s] += (4 * F[k, n_occ + u] ) * K[0, (k*n_virt + u) * n_ex + i*n_virt + s+ 2*n_ex]

	# This operator combination: {'a': 3, 'b': 2}
	for i in range(n_occ):
		for k in range(n_occ):
			for j in range(n_occ):
				for s in range(n_virt):
					for u in range(n_virt):
						for t in range(n_virt):

							if ((k == i) and (j == i)):

								if ((u == s) and (t == s)):

									L2[i*n_virt + s + n_ex] += (-4 * F[i, n_occ + s] ) * K[0, (i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex]

								elif ((u == s) and (t != s)):

									L2[i*n_virt + s + n_ex] += (-4 * F[i, n_occ + t] ) * K[0, (i*n_virt + s) * n_ex + i*n_virt + t+ 2*n_ex]

							elif ((k == i) and (j != i)):

								if ((u == s) and (t == s)):

									L2[i*n_virt + s + n_ex] += (-4 * F[j, n_occ + s] ) * K[0, (i*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex]

								elif ((u == s) and (t != s)):

									L2[i*n_virt + s + n_ex] += (-4 * F[j, n_occ + t] ) * K[0, (i*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex]

	# This operator combination: {'a': 3, 'b': 3}
	for j in range(n_occ):
		for i in range(n_occ):
			for m in range(n_occ):
				for k in range(n_occ):
					for t in range(n_virt):
						for s in range(n_virt):
							for v in range(n_virt):
								for u in range(n_virt):

									if ((j == i) and (m == i) and (k == i)):

										if ((t == s) and (v != s) and (v != t) and (v != u) and (u == s)):

											L2[(i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * F[n_occ + s, n_occ + v] + -4 * g[i, i, n_occ + s, n_occ + v] + 8 * g[i, n_occ + s, i, n_occ + v] ) * K[0, (i*n_virt + v) * n_ex + i*n_virt + s+ 2*n_ex]

										elif ((t == s) and (v == s) and (u != s) and (u != t)):

											L2[(i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * F[n_occ + s, n_occ + u] + 4 * g[i, i, n_occ + s, n_occ + u] + -8 * g[i, n_occ + s, i, n_occ + u] ) * K[0, (i*n_virt + s) * n_ex + i*n_virt + u+ 2*n_ex]

										elif ((t != s) and (v == s) and (u == s)):

											L2[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * F[n_occ + s, n_occ + t] + 4 * g[i, i, n_occ + s, n_occ + t] + -8 * g[i, n_occ + s, i, n_occ + t] ) * K[0, (i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex]

										elif ((t != s) and (v == s) and (u == t)):

											L2[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * F[n_occ + t, n_occ + t] + 4 * F[n_occ + s, n_occ + s] + -4 * g[i, i, n_occ + s, n_occ + s] + 4 * g[i, i, n_occ + t, n_occ + t] + 8 * g[i, n_occ + s, i, n_occ + s] + -8 * g[i, n_occ + t, i, n_occ + t] ) * K[0, (i*n_virt + s) * n_ex + i*n_virt + t+ 2*n_ex]

										elif ((t != s) and (v == t) and (u == t)):

											L2[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * F[n_occ + s, n_occ + t] + -4 * g[i, i, n_occ + s, n_occ + t] + 8 * g[i, n_occ + s, i, n_occ + t] ) * K[0, (i*n_virt + t) * n_ex + i*n_virt + t+ 2*n_ex]

										elif ((t != s) and (v != s) and (v != t) and (v != u) and (u == t)):

											L2[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * F[n_occ + s, n_occ + v] + -4 * g[i, i, n_occ + s, n_occ + v] + 8 * g[i, n_occ + s, i, n_occ + v] ) * K[0, (i*n_virt + v) * n_ex + i*n_virt + t+ 2*n_ex]

										elif ((t != s) and (v == s) and (u != s) and (u != t)):

											L2[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * F[n_occ + t, n_occ + u] + 4 * g[i, i, n_occ + t, n_occ + u] + -8 * g[i, n_occ + t, i, n_occ + u] ) * K[0, (i*n_virt + s) * n_ex + i*n_virt + u+ 2*n_ex]

									elif ((j == i) and (m != i) and (m != j) and (m != k) and (k == i)):

										if ((t == s) and (v == s) and (u == s)):

											L2[(i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * F[i, m] + 8 * g[i, n_occ + s, m, n_occ + s] + -4 * g[i, m, n_occ + s, n_occ + s] ) * K[0, (m*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex]

										elif ((t == s) and (v != s) and (v != t) and (v != u) and (u == s)):

											L2[(i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, m, n_occ + s, n_occ + v] + 8 * g[i, n_occ + s, m, n_occ + v] ) * K[0, (m*n_virt + v) * n_ex + i*n_virt + s+ 2*n_ex]

										elif ((t != s) and (v == s) and (u == t)):

											L2[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * F[i, m] + 8 * g[i, n_occ + s, m, n_occ + s] + -4 * g[i, m, n_occ + s, n_occ + s] ) * K[0, (m*n_virt + s) * n_ex + i*n_virt + t+ 2*n_ex]

										elif ((t != s) and (v == t) and (u == t)):

											L2[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, m, n_occ + s, n_occ + t] + 8 * g[i, n_occ + s, m, n_occ + t] ) * K[0, (m*n_virt + t) * n_ex + i*n_virt + t+ 2*n_ex]

										elif ((t != s) and (v != s) and (v != t) and (v != u) and (u == t)):

											L2[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, m, n_occ + s, n_occ + v] + 8 * g[i, n_occ + s, m, n_occ + v] ) * K[0, (m*n_virt + v) * n_ex + i*n_virt + t+ 2*n_ex]

									elif ((j == i) and (m == i) and (k != i) and (k != j)):

										if ((t == s) and (v == s) and (u == s)):

											L2[(i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * F[i, k] + -8 * g[i, n_occ + s, k, n_occ + s] + 4 * g[i, k, n_occ + s, n_occ + s] ) * K[0, (i*n_virt + s) * n_ex + k*n_virt + s+ 2*n_ex]

										elif ((t == s) and (v == s) and (u != s) and (u != t)):

											L2[(i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, k, n_occ + s, n_occ + u] + -8 * g[i, n_occ + s, k, n_occ + u] ) * K[0, (i*n_virt + s) * n_ex + k*n_virt + u+ 2*n_ex]

										elif ((t != s) and (v == s) and (u == s)):

											L2[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, k, n_occ + s, n_occ + t] + -8 * g[i, n_occ + t, k, n_occ + s] ) * K[0, (i*n_virt + s) * n_ex + k*n_virt + s+ 2*n_ex]

										elif ((t != s) and (v == s) and (u == t)):

											L2[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * F[i, k] + -8 * g[i, n_occ + t, k, n_occ + t] + 4 * g[i, k, n_occ + t, n_occ + t] ) * K[0, (i*n_virt + s) * n_ex + k*n_virt + t+ 2*n_ex]

										elif ((t != s) and (v == s) and (u != s) and (u != t)):

											L2[(i*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, k, n_occ + t, n_occ + u] + -8 * g[i, n_occ + t, k, n_occ + u] ) * K[0, (i*n_virt + s) * n_ex + k*n_virt + u+ 2*n_ex]

									elif ((j != i) and (m == i) and (k == i)):

										if ((t == s) and (v == s) and (u == s)):

											L2[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * F[i, j] + -8 * g[i, n_occ + s, j, n_occ + s] + 4 * g[i, j, n_occ + s, n_occ + s] ) * K[0, (i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex]

										elif ((t == s) and (v == s) and (u != s) and (u != t)):

											L2[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, j, n_occ + s, n_occ + u] + -8 * g[i, n_occ + u, j, n_occ + s] ) * K[0, (i*n_virt + s) * n_ex + i*n_virt + u+ 2*n_ex]

										elif ((t != s) and (v == s) and (u == s)):

											L2[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, j, n_occ + s, n_occ + t] + -8 * g[i, n_occ + s, j, n_occ + t] ) * K[0, (i*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex]

										elif ((t != s) and (v == s) and (u == t)):

											L2[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * F[i, j] + -8 * g[i, n_occ + t, j, n_occ + t] + 4 * g[i, j, n_occ + t, n_occ + t] ) * K[0, (i*n_virt + s) * n_ex + i*n_virt + t+ 2*n_ex]

										elif ((t != s) and (v == s) and (u != s) and (u != t)):

											L2[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[i, j, n_occ + t, n_occ + u] + -8 * g[i, n_occ + u, j, n_occ + t] ) * K[0, (i*n_virt + s) * n_ex + i*n_virt + u+ 2*n_ex]

									elif ((j != i) and (m == i) and (k == j)):

										if ((t == s) and (v == s) and (u == s)):

											L2[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * F[i, i] + 4 * F[j, j] + 4 * g[j, j, n_occ + s, n_occ + s] + 8 * g[i, n_occ + s, i, n_occ + s] + -8 * g[j, n_occ + s, j, n_occ + s] + -4 * g[i, i, n_occ + s, n_occ + s] ) * K[0, (i*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex]

										elif ((t == s) and (v != s) and (v != t) and (v != u) and (u == s)):

											L2[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * F[n_occ + s, n_occ + v] + -4 * g[i, i, n_occ + s, n_occ + v] + 8 * g[i, n_occ + s, i, n_occ + v] ) * K[0, (i*n_virt + v) * n_ex + j*n_virt + s+ 2*n_ex]

										elif ((t == s) and (v == s) and (u != s) and (u != t)):

											L2[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * F[n_occ + s, n_occ + u] + 4 * g[j, j, n_occ + s, n_occ + u] + -8 * g[j, n_occ + s, j, n_occ + u] ) * K[0, (i*n_virt + s) * n_ex + j*n_virt + u+ 2*n_ex]

										elif ((t != s) and (v == s) and (u == s)):

											L2[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * F[n_occ + s, n_occ + t] + 4 * g[j, j, n_occ + s, n_occ + t] + -8 * g[j, n_occ + s, j, n_occ + t] ) * K[0, (i*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex]

										elif ((t != s) and (v == s) and (u == t)):

											L2[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * F[i, i] + -4 * F[n_occ + t, n_occ + t] + 4 * F[n_occ + s, n_occ + s] + 4 * F[j, j] + -4 * g[i, i, n_occ + s, n_occ + s] + 4 * g[j, j, n_occ + t, n_occ + t] + 8 * g[i, n_occ + s, i, n_occ + s] + -8 * g[j, n_occ + t, j, n_occ + t] ) * K[0, (i*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex]

										elif ((t != s) and (v == t) and (u == t)):

											L2[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * F[n_occ + s, n_occ + t] + -4 * g[i, i, n_occ + s, n_occ + t] + 8 * g[i, n_occ + s, i, n_occ + t] ) * K[0, (i*n_virt + t) * n_ex + j*n_virt + t+ 2*n_ex]

										elif ((t != s) and (v != s) and (v != t) and (v != u) and (u == t)):

											L2[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * F[n_occ + s, n_occ + v] + -4 * g[i, i, n_occ + s, n_occ + v] + 8 * g[i, n_occ + s, i, n_occ + v] ) * K[0, (i*n_virt + v) * n_ex + j*n_virt + t+ 2*n_ex]

										elif ((t != s) and (v == s) and (u != s) and (u != t)):

											L2[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * F[n_occ + t, n_occ + u] + 4 * g[j, j, n_occ + t, n_occ + u] + -8 * g[j, n_occ + t, j, n_occ + u] ) * K[0, (i*n_virt + s) * n_ex + j*n_virt + u+ 2*n_ex]

									elif ((j != i) and (m == j) and (k == j)):

										if ((t == s) and (v == s) and (u == s)):

											L2[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * F[i, j] + 8 * g[i, n_occ + s, j, n_occ + s] + -4 * g[i, j, n_occ + s, n_occ + s] ) * K[0, (j*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex]

										elif ((t == s) and (v != s) and (v != t) and (v != u) and (u == s)):

											L2[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, j, n_occ + s, n_occ + v] + 8 * g[i, n_occ + s, j, n_occ + v] ) * K[0, (j*n_virt + v) * n_ex + j*n_virt + s+ 2*n_ex]

										elif ((t != s) and (v == s) and (u == t)):

											L2[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * F[i, j] + 8 * g[i, n_occ + s, j, n_occ + s] + -4 * g[i, j, n_occ + s, n_occ + s] ) * K[0, (j*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex]

										elif ((t != s) and (v == t) and (u == t)):

											L2[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, j, n_occ + s, n_occ + t] + 8 * g[i, n_occ + s, j, n_occ + t] ) * K[0, (j*n_virt + t) * n_ex + j*n_virt + t+ 2*n_ex]

										elif ((t != s) and (v != s) and (v != t) and (v != u) and (u == t)):

											L2[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, j, n_occ + s, n_occ + v] + 8 * g[i, n_occ + s, j, n_occ + v] ) * K[0, (j*n_virt + v) * n_ex + j*n_virt + t+ 2*n_ex]

									elif ((j != i) and (m != i) and (m != j) and (m != k) and (k == j)):

										if ((t == s) and (v == s) and (u == s)):

											L2[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * F[i, m] + 8 * g[i, n_occ + s, m, n_occ + s] + -4 * g[i, m, n_occ + s, n_occ + s] ) * K[0, (m*n_virt + s) * n_ex + j*n_virt + s+ 2*n_ex]

										elif ((t == s) and (v != s) and (v != t) and (v != u) and (u == s)):

											L2[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, m, n_occ + s, n_occ + v] + 8 * g[i, n_occ + s, m, n_occ + v] ) * K[0, (m*n_virt + v) * n_ex + j*n_virt + s+ 2*n_ex]

										elif ((t != s) and (v == s) and (u == t)):

											L2[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * F[i, m] + 8 * g[i, n_occ + s, m, n_occ + s] + -4 * g[i, m, n_occ + s, n_occ + s] ) * K[0, (m*n_virt + s) * n_ex + j*n_virt + t+ 2*n_ex]

										elif ((t != s) and (v == t) and (u == t)):

											L2[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, m, n_occ + s, n_occ + t] + 8 * g[i, n_occ + s, m, n_occ + t] ) * K[0, (m*n_virt + t) * n_ex + j*n_virt + t+ 2*n_ex]

										elif ((t != s) and (v != s) and (v != t) and (v != u) and (u == t)):

											L2[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (-4 * g[i, m, n_occ + s, n_occ + v] + 8 * g[i, n_occ + s, m, n_occ + v] ) * K[0, (m*n_virt + v) * n_ex + j*n_virt + t+ 2*n_ex]

									elif ((j != i) and (m == i) and (k != i) and (k != j)):

										if ((t == s) and (v == s) and (u == s)):

											L2[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * F[j, k] + -8 * g[j, n_occ + s, k, n_occ + s] + 4 * g[j, k, n_occ + s, n_occ + s] ) * K[0, (i*n_virt + s) * n_ex + k*n_virt + s+ 2*n_ex]

										elif ((t == s) and (v == s) and (u != s) and (u != t)):

											L2[(j*n_virt + s) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[j, k, n_occ + s, n_occ + u] + -8 * g[j, n_occ + s, k, n_occ + u] ) * K[0, (i*n_virt + s) * n_ex + k*n_virt + u+ 2*n_ex]

										elif ((t != s) and (v == s) and (u == s)):

											L2[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[j, k, n_occ + s, n_occ + t] + -8 * g[j, n_occ + t, k, n_occ + s] ) * K[0, (i*n_virt + s) * n_ex + k*n_virt + s+ 2*n_ex]

										elif ((t != s) and (v == s) and (u == t)):

											L2[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * F[j, k] + -8 * g[j, n_occ + t, k, n_occ + t] + 4 * g[j, k, n_occ + t, n_occ + t] ) * K[0, (i*n_virt + s) * n_ex + k*n_virt + t+ 2*n_ex]

										elif ((t != s) and (v == s) and (u != s) and (u != t)):

											L2[(j*n_virt + t) * n_ex + i*n_virt + s+ 2*n_ex] += (4 * g[j, k, n_occ + t, n_occ + u] + -8 * g[j, n_occ + t, k, n_occ + u] ) * K[0, (i*n_virt + s) * n_ex + k*n_virt + u+ 2*n_ex]

