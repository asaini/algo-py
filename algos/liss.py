class Node:
	def __init__(self, data, left=None, right=None,
				 liss=None):
		self.data = data
		self.left = left
		self.right = right
		self.liss = liss

	def __str__(self):
		if self.data:
			return str(self.data)
		return ''

def liss(root):
	"""
	largest independent set in a given binary tree
	"""		
	if root is None:
		return 0

	if root.liss:
		return root.liss

	if root.left is None and root.right is None:
		root.liss = 1
		return root.liss

	# Size excluding current node
	size_excluding = liss(root.left) + liss(root.right)

	# Size including current node
	size_including = 1 
	if root.left:
		size_including += liss(root.left.left) + liss(root.left.right)

	if root.right:
		size_including += liss(root.right.left) + liss(root.right.right)

	root.liss = max(size_excluding, size_including)

	return root.liss



if __name__ == '__main__':
    
    root = Node(20)
    root.left = Node(8)
    root.left.left = Node(4)
    root.left.right = Node(12)
    root.left.right.left = Node(10)
    root.left.right.right = Node(14)
    root.right = Node(22)
    root.right.right = Node(25)

    print liss(root)