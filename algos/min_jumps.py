import sys
import math


def min_jumps(array, end):
	jumps = [0] * end 

	if end == 0 or array[0] == 0:
		return -1

	for i in range(1, end):
		jumps[i] = float("inf")

		for j in range(0, i):
			if i <= j + array[j] and not math.isinf(jumps[j]):
				jumps[i] = min(jumps[j] + 1, jumps[i])
				break

	return jumps[end - 1]


if __name__ == '__main__':
	array = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
	print min_jumps(array, len(array))