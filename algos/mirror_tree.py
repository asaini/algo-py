class Node:

	def __init__(self, data, left=None, right=None):
		self.data = data
		self.left = left
		self.right = right

	@classmethod
	def mirror(cls, root):
		if root is None:
			return

		cls.mirror(root.left)
		cls.mirror(root.right)

		root.left, root.right = root.right, root.left

	@classmethod
	def in_order(cls, root):
		if root is None:
			return
		cls.in_order(root.left)
		print root.data
		cls.in_order(root.right)


if __name__ == '__main__':
	root = Node(1)
	root.left = Node(2)
	root.right = Node(3)
	root.left.left = Node(4)
	root.left.right = Node(5)

	Node.in_order(root)

	Node.mirror(root)

	Node.in_order(root)