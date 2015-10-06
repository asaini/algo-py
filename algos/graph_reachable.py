class Graph:

	def __init__(self, V, adj={}):
		self.V = V
		self.adj = adj

	def add_edge(self, i, j):
		if i in self.adj.keys():
			self.adj[i].add(j)
		else:
			self.adj[i] = set([j])

	def is_reachable(self, i, j):
		if i == j:
			return True

		visited = [False]*self.V

		stack = [i]

		while len(stack) > 0:
			s = stack.pop(0)
			if not visited[s]:
				visited[s] = True
				neighbours = list(self.adj[s])
				for n in neighbours:
					if n == j:
						return True
					if not visited[n]:
						stack.append(n)

		return False


if __name__ == '__main__':
	g = Graph(4)
	g.add_edge(0, 1)
	g.add_edge(0, 2)
	g.add_edge(1, 2)
	g.add_edge(2, 0)
	g.add_edge(2, 3)
	g.add_edge(3, 3)	

	print "is_reachable(1, 3) --> %s" % g.is_reachable(1, 3)
	print "is_reachable(3, 1) --> %s" % g.is_reachable(3, 1)