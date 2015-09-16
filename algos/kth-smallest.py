def kth_smallest(array, start, end, k):
	"""
	"""
	print "kth_smallest ", array, start, end, k
	if k > 0 and k < end - start + 1:
		pos = partition(array, start, end)

		if pos - start == k - 1:
			return array[pos]

		if pos - start > k - 1:
			return kth_smallest(array, start, pos - 1, k)

		return kth_smallest(array, pos + 1, end, k - pos + start - 1)
	
	return -1



def partition(array, start, end):
	"""
	Standard partition process of QuickSort().  It considers the last
	element as pivot and moves all smaller element to left of it
	and greater elements to right
	"""
	print "partition ", array, start, end
	last = array[end]
	i = start
	for j in range(start, end):
		if array[j] <= last:
			# Swap elements at i and j
			array[i], array[j] = array[j], array[i]
			i = i + 1

	# Swap the last element to where it belongs
	array[i], array[end] = array[end], array[i]
	return i



if __name__ == '__main__':
	array = [12, 3, 5, 7, 4, 19, 26, 11]
	n = len(array)
	print kth_smallest(array, 0, n - 1, 3);