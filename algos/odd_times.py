def odd_elements(array):
	"""
	"""
	odd = set()
	for item in array:
		if item in odd:
			odd.remove(item)
		else:
			odd.add(item)
	return odd

if __name__ == '__main__':
	array = [2, 3, 5, 4, 5, 2, 4, 3, 5, 2, 4, 4, 2]
	print odd_elements(array)