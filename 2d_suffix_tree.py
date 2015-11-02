import numpy as np

def find_match(ST, pattern):
	T = ST
	for c in pattern:
		if c not in T:
			return False
		T = T[c]
	return True

def suffix_tree(text):
	def compact_suffix_tree(T):
		for k,e in list(T.items()):
			if len(e) == 1 and k in T:
				k_next = next(iter(e.keys()))
				T[k + k_next] = T[k][k_next]
				del T[k]
				compact_suffix_tree(T)
			else:
				compact_suffix_tree(e)
	T = {}
	suffixes = sorted([tuple(text[i:]) + (-1, ) for i,e in enumerate(text)])

	for x in suffixes:
		
		cT = T
		i = 0
		while i < len(x):
			if (x[i], ) in cT:
				cT = cT[(x[i], )]
			else:
				break
			i += 1
		while i < len(x):
			cT[(x[i], )] = {}
			cT = cT[(x[i], )]
			i += 1
	compact_suffix_tree(T)
	return T

def radix_sort(l, radix):
	def recur(l, pos):
		if len(l) == 0 or pos >= len(l[0][0]):
			return l
		buckets = [list() for _ in range(radix)]
		for item in l:
			buckets[item[0][pos]] += [item]
		final = []
		for item in buckets:
			if item:
				for x in recur(item, pos + 1):
					final += [x]
		return final
	return recur([(x, i) for i,x in enumerate(l)], 0)
		
def isuffix(A):
	def get_B(C):
		tuples = []
		for i in range(0,int(C.shape[0]), 2):
			for j in range(0, int(C.shape[1]), 2):
				tuples += [C[i:i+2,j:j+2].flatten()]
		slist = radix_sort(tuples, C.max() + 1)
		enc_m = np.zeros(int(C.shape[0] / 2) * int(C.shape[1] / 2), dtype=np.uint8)
		j = 0
		for x in slist:
			enc_m[x[1]] = j
			j += 1
		enc_m = enc_m.reshape((int(C.shape[0] / 2), int(C.shape[1] / 2)))
		return enc_m

	if (A.shape[0] == 1):
		return suffix_tree(A.tolist()[0])

	vd = np.zeros((A.shape[0], 1), dtype=np.uint8)
	hd = np.zeros((1, A.shape[1]), dtype=np.uint8)

	A1 = A
	A2 = np.append(A[1:,0:], hd, axis=0)
	A3 = np.append(A[0:,1:], vd, axis=1)
	A4 = np.append(np.append(A[1:,1:], hd[0:,0:-1], axis=0), vd, axis=1)

	A123 = np.concatenate((A1, A2, A3), axis=1)

	B123 = get_B(A123)
	print(B123)
	return isuffix(B123)

def decode():
	pass

in_m = np.random.random_integers(0, 9, (8, 8))
for k,x in isuffix(in_m).items():
	print(k,x)

