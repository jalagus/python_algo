def BWT(seq):
	def genRotationPermutations(seq):
		rotations = []
		for i in range(0, len(seq)):
			rotations += [seq[i:] + seq[:i]] 
		return rotations
	
	bwt = [x[-1] for x in sorted(genRotationPermutations(seq + "#"))]
	return bwt

def inverseBWT(seq):
	items = [list() for _ in seq]
	eof_i = 0
	for _ in seq:
		for i,c in enumerate(seq):
			items[i] = [c] + items[i]
			if c == '#':
				eof_i = i
		items = sorted(items)
	return items[eof_i][:-1]


print("".join(inverseBWT(BWT('ACGTGCGCGCGAAGGTGGGTTACGCGATCGCTAGAGAG'))))

