class Graph:

	def __init__(self, V, adj = {}):
		self.V = V
		self.adj = adj
	
	def add_edge(self, i, j):
		if i in self.adj.keys():
			self.adj[i].add(j)
		else:
			self.adj[i] = set([j])	

	def is_cyclic(self, current, visited, parent):
		"""
		@param current: current node number
		@visited: list determining whether node x has been visited
		@parent: parent node of current
		"""

		visited[current] = True
		for i in self.adj[current]:
			if not visited[i] and self.is_cyclic(i, visited, current):
				return True
			elif visited[i] and i != parent:
				return True

		return False


	def is_tree(self):
		visited = [False]*self.V

		if self.is_cyclic(0, visited, -1):
			return False

		for i in range(self.V):
			if not visited[i]:
				return False

		return True


if __name__ == '__main__':

	g1 = Graph(5)
	g1.add_edge(1, 0)
	g1.add_edge(0, 2)
	g1.add_edge(0, 3)
	g1.add_edge(3, 4)
	print "Is g1 a tree --> %s" % g1.is_tree()
 
	g2 = Graph(5)
	g2.add_edge(1, 0);
	g2.add_edge(0, 2);
	g2.add_edge(2, 1);
	g2.add_edge(0, 3);
	g2.add_edge(3, 4);
	print "Is g2 a tree --> %s" % g2.is_tree()