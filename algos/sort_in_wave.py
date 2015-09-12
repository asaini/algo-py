def sort_in_wave(array):
	"""
	Given an unsorted array of integers, sort the array 
	into a wave like array. 
	An array arr[0..n-1] is sorted in wave form 
	if arr[0] >= arr[1] <= arr[2] >= arr[3] <= arr[4] >= 
	"""
	n = len(array)
	for i in range(n - 1):
		if i % 2 == 0 and array[i] < array[i+1]:
			array[i], array[i+1] = array[i+1], array[i]
	return array


if __name__=='__main__':
	array = [10, 90, 49, 2, 1, 5, 23]
	print sort_in_wave(array)

	array = [0, 1, 2, 3]
	print sort_in_wave(array)