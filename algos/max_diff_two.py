def maximum_diff(array):
	"""
	Given an array array of integers, 
	find out the difference between any two elements such that 
	larger element appears after the smaller number in array
	"""
	max_diff = array[1] - array[0]
	min_element = array[0]
	n = len(array)

	for i in range(1, n):
		if array[i] - min_element > max_diff:
			max_diff = array[i] - min_element
		if array[i] < min_element:
			min_element = array[i]

	return max_diff


if __name__ == '__main__':
	array = [1, 2, 6, 80, 100]
	print maximum_diff(array)