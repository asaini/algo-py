def number_of_triangles(array):
	"""
	Given an array find the number of triangular
	pairs in it
	"""
	array = sorted(array)
	n = len(array)

	count = 0

	for i in range(n-2):
		k = i+2
		for j in range(i+1, n):
			print count
			while k < n and array[i] + array[j] < array[k]:
				k += 1
			count += k - j - 1
	return count

if __name__ == '__main__':
	array =   [10, 21, 22, 100, 101, 200, 300]

	print "Number of triangles = %s" % number_of_triangles(array)