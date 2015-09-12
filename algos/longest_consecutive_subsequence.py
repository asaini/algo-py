def longest_consecutive_subsequence(array):
	"""
	Given an array of integers, find the length of the 
	longest sub-sequence such that elements in the subsequence 
	are consecutive integers, the consecutive numbers can be in any order.
	"""

	n = len(array)
	result = 0

	# Insert all array elements into a hash
	d = {}
	for i in array:
		d[i] = 1

	for i in range(n):
		current = array[i]
		while current in d.keys():
			current = current + 1
		result = max(result, current - array[i])

	return result



if __name__ == '__main__':
	array = [1, 9, 3, 10, 4, 20, 2]
	print 'Sequence = %s' % array
	print 'Length of longest consecutive subsequence = %s\n' % longest_consecutive_subsequence(array)

	array = [36, 41, 56, 35, 44, 33, 34, 92, 43, 32, 42]
	print 'Sequence = %s' % array
	print 'Length of longest consecutive subsequence = %s\n' % longest_consecutive_subsequence(array)