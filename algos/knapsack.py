import sys

def knapsack(val, wt, W):
	"""
	Given weights and values of n items, put these items 
	in a knapsack of capacity W to get the maximum total 
	value in the knapsack
	"""
	n = len(val)

	table = [ [0]*(W + 1) for i in range(n + 1) ]

	for i in range(1, n + 1):
		for w in range(1, W + 1):

			if wt[i - 1] <= W:
				table[i][w] = max(table[i - 1][w], table[i - 1][w - wt[i-1]] + val[i-1])
			else:
				table[i][w] = table[i-1][w]

	return table[n][W]



if __name__ == '__main__':
	val = [60, 100, 120]
	wt = [10, 20, 30]
	W = 30

	print knapsack(val, wt, W)