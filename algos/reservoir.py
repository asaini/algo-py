def select_k_items(stream, n, k):
	reservoir = []

	for i in range(k):
		reservoir.append(stream[i])

	

if __name__ == '__main__':
	stream = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
	n = len(stream)

	k = 5
	select_k_items(stream, n, k)