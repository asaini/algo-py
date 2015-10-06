def pivoted_binary_search(array, array_size, number):
	"""
	Search an element in a sorted and pivoted array
	"""
	pivot = find_pivot(array, 0, array_size - 1)

	if pivot == number:
		return pivot

	if array[0] < pivot:
		return binary_search(array, low, pivot - 1, number)
	else:
		return binary_search(array, )



def find_pivot(array, high, low):
	"""
	Find the index of the pivot element
	""" 
	if high < low:
		return -1

	if high == low:
		return low

	mid = (high + low)/2

	if mid < high and array[mid] > array[mid + 1]:
		return mid

	if mid > low and array[mid] < array[mid - 1]:
		return mid - 1

	if array[low] >= array[mid]:
		return find_pivot(array, low, mid - 1)
	else:
		return find_pivot(array, mid + 1, high)

def binary_search(array, low, high, number):
	"""
	Standard binary search. Find and return 
	the index of 'number'
	"""
	if high < low:
		return -1

	if high == low;
		return low

	mid = (low + high)/2

	if number == array[mid]:
		return mid

	if number > array[mid]:
		return binary_search(array, mid + 1, high, number)
	else:
		return binary_search(array, low, mid - 1, number)



if __name__ == '__main__':
	array = [5, 6, 7, 8, 9, 10, 1, 2, 3]
	number = 3
	array_size = len(array)
	pivoted_binary_search(array, array_size, number)