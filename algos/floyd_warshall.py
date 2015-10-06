import math


def floyd_warshall(graph):
	"""
	All Pairs Shortest Path problem. 
	The problem is to find shortest distances between every 
	pair of vertices in a given edge weighted directed Graph
	"""
	n = len(graph[0])

	dist = [ [0]*n for i in range(n) ]

	# Initialize the solution matrix same as input graph matrix
	for i in range(n):
		for j in range(n):
			dist[i][j] = graph[i][j]

	for k in range(n):
		for i in range(n):
			for j in range(n):
				if dist[i][k] + dist[k][j] < dist[i][j]:
					dist[i][j] = dist[i][k] + dist[k][j]

	return dist


def print_solution(dist):
	"""
	"""
	n = len(dist[0])

	for i in range(n):
		print dist[i]

	return


if __name__ == '__main__':
	INF = float('inf')
	graph =  [ 
		[0,   5,  INF, 10],
		[INF, 0,   3, INF],
		[INF, INF, 0,   1],
		[INF, INF, INF, 0]
	]

	dist = floyd_warshall(graph)

	print_solution(dist)

