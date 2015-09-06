def check_subset_sum(items, target_sum):
	"""
	Given a set of non-negative integers, and a value sum, 
	determine if there is a subset of the given set with 
	sum equal to given sum.
	"""

	size = len(items)
	'''	
	subset[i][j] will be true if there is a 
	subset of set[0..j-1] whose sum is target_sum
	'''

	subset = [ [False]*(size + 1) for n in range(target_sum + 1) ]


	# If target_sum = 0, then there is a subset whose 
	# sum is 0, i.e. the empty set
	for i in range(size + 1):
		subset[0][i] = True


	for i in range(1, target_sum + 1):
		for j in range(1, size + 1):
			subset[i][j] = subset[i][j-1]

			k = items[j - 1]
			if i >= k:
				subset[i][j] = subset[i][j] or subset[i - k][j-1]

	return subset[target_sum][size]


if __name__ == '__main__':
	items = [3, 34, 4, 12, 5, 2]
	print check_subset_sum(items, 9)
