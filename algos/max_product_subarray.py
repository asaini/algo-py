def maximum_product_subarray(array):
	"""
	Product of the maximum product subarray
	"""
	
	max_ending_here = 1
	min_ending_here = 1
	
	max_so_far = 1

	n = len(array)

	for i in range(n):
		print 'max = %s, min = %s' % (max_ending_here, min_ending_here)
	
		if array[i] > 0:
			max_ending_here = max_ending_here * array[i]
			min_ending_here = min(min_ending_here * array[i], 1)
		
		elif array[i] == 0:
			max_ending_here = 1
			min_ending_here = 1

		# Handle negative case		
		elif array[i] < 0:
			temp = max_ending_here
			max_ending_here = max(min_ending_here * array[i], 1)
			min_ending_here = temp * array[i]	
		
		max_so_far = max(max_ending_here, max_so_far)

	return max_so_far
						
	

if __name__ == '__main__':
	array = [1, -2, -3, 0, 7, -8, -2]
	print 'Maximum sub array product = %s' % maximum_product_subarray(array)
