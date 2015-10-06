class Graph:
	"""
	Class to represent a graph object
	"""

	def __init__(self, v, adj={}):
		"""
		@param v: number of vertices
		@param adj: Adjacency matrix, kindof
		"""
		self.v = v
		self.adj = adj

	def add_edge(self, i, j):
		"""
		Add an edge between vertices i
		and j
		"""
		if i in self.adj.keys():
			self.adj[i].add(j)
		else:
			self.adj[i] = set([j])

	def bfs(self, start):
		"""
		Bread first search, starting at the node 'start'
		"""
		visited, stack = set(), [start]
		while len(stack) > 0:
			vertex = stack.pop(0)
			if vertex not in visited:
				visited.add(vertex)
				print 'Visiting %s' % vertex
				stack.extend(self.adj[vertex] - visited)
		return visited

	def dfs(self, start):
		"""
		Depth first search, starting at node 'start'
		"""
		visited, stack = set(), [start]
		while len(stack) > 0:
			vertex = stack.pop()
			if vertex not in visited:
				visited.add(vertex)
				stack.extend(self.adj[vertex] - visited)
		return visited

	def dfs_paths(self, start, goal):
		"""
		Yield each possible path from start to goal
		"""
		stack = [(start, [start])]
		while stack:
			(vertex, path) = stack.pop()
			for next in self.adj[vertex] - set(path):
				if next == goal:
					yield path + [next]
				else:
					stack.append((next, path + [next]))


if __name__ == '__main__':
	g = Graph(4)
	g.add_edge(0, 1)
	g.add_edge(0, 2)
	g.add_edge(1, 2)
	g.add_edge(2, 0)
	g.add_edge(2, 3)
	g.add_edge(3, 3)

	print "Following is Breadth First Traversal (starting from vertex 2) \n"
	print g.bfs(2)

	print "\nList all paths from start node to goal node"
	for path in g.dfs_paths(0, 3):
		print path
