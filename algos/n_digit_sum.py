"""
Given two integers 'n' and 'sum', find count of all 
n digit numbers with sum of digits as 'sum'. 

Leading 0s are not counted as digits.
"""

lookup = None

def create_lookup_table(n, target_sum):
	"""
	Create a lookup table and assign 
	to the global variable
	"""
	global lookup
	lookup = [ [-1]*(target_sum + 1) for i in range(n + 1) ]


def helper(n, target_sum):
	print n, target_sum
	global lookup
	print lookup
	if n == 0:
		return 0

	if lookup[n][target_sum] != -1:
		return lookup[n][target_sum]

	if n == 1 and target_sum < 10:
		lookup[n][target_sum] = 1
		return 1

	result = 0

	for i in range(0, 10):
		if target_sum - i >= 0:
			result += helper(n - 1, target_sum - i)

	lookup[n][target_sum] = result

	return result

def digit_sum_count(n, target_sum):
	"""
	"""
	result = 0
	for i in range(1, 10):
		if target_sum - i >= 0:
			result += helper(n-1, target_sum - i)

	return result


if __name__ == '__main__':
	create_lookup_table(3, 5)
	print digit_sum_count(3, 5)
