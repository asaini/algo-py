def max_sub_array(array):
	"""
	Returns the sum of contiguous subarray within a 
	one-dimensional array of numbers which has the largest sum
	"""
	max_so_far = current_max = array[0]
	n = len(array)

	for i in range(1, n):
		current_max = max(array[i], current_max + array[i])
		max_so_far = max(current_max, max_so_far)

	return max_so_far

if __name__ == '__main__':
	array = [-2, -3, 4, -1, -2, 1, 5, -3]
	print max_sub_array(array)

	# Negatives only
	array = [-2, -3, -1, -2, -3]
	print max_sub_array(array)
