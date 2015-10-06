def move_to_end(M, m):
	"""
	move m elements at the end of array
	"""
	i, j = 0, size - 1
	for i in range(size - 1, -1, -1):
		if M[i] != None:
			M[j] = M[i]
			j = j - 1
	return

def merge(M, N, m, n):
	"""
	"""
	# Index for input from larger array, which 
	# has been moved to the end
	i = n

	# Index for smaller array, N
	j = 0

	# Index for the start of the larger array
	k = 0

	while k < m+n:

		# Choose the smaller element
		if  (i < m+n and M[i] <= N[j]) or j == n:
			M[k] = M[i]
			k += 1
			i += 1
		else:
			M[k] = N[j]
			k += 1
			j += 1

	return

if __name__ == '__main__':

	# Bigger array of size m + n
	M = [2, 8, None, None, None , 13, None, 15, 20]
	m = len(M)

	# Smaller array of size n
	N = [5, 7, 9, 25]
	n = len(N)
	
	size = len(M)
	move_to_end(M, m)
	print M

	merge(M, N, m - n, n)
	print M
