def lcs(x, y):
	"""
	Longest Common Subsequence 
	"""
	n = len(x) + 1
	m = len(y) + 1

	table = [ [0]*m for i in range(n) ]

	for i in range(n):
		for j in range(m):

			# If either string is empty, then lcs = 0
			if i == 0 or j == 0:
				table[i][j] = 0


			elif x[i - 1] == y[j - 1]:
				table[i][j] = 1 + table[i-1][j-1]

			else:
				table[i][j] = max(table[i-1][j], table[i][j-1])

	return table[len(x)][len(y)]

if __name__ == '__main__':
    x = "AGGTAB"
    y = "GXTXAYB"

    print lcs(x, y)
