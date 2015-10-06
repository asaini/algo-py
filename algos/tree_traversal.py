class Node:

	def __init__(self, data, left=None, right=None):
		self.data = data
		self.left = left
		self.right = right

	def __str__(self):

		out = 'data = %s, left = %s, right = %s' % (
			self.data,
			self.left,
			self.right
		)
		return out



	@classmethod
	def post_order(cls, root):
		if root is None:
			return

		cls.post_order(root.left)
		cls.post_order(root.right)

		print root.data

	@classmethod
	def in_order(cls, root):
		if root is None:
			return

		cls.in_order(root.left)
		print root.data
		cls.in_order(root.right)

	@classmethod
	def pre_order(cls, root):
		if root is None:
			return

		print root.data
		cls.pre_order(root.left)
		cls.pre_order(root.right)

if __name__ == '__main__':
	root = Node(1)
	root.left = Node(2)
	root.right = Node(3)
	root.left.left = Node(4)
	root.left.right = Node(5)

	print root

	Node.pre_order(root)

	Node.in_order(root)

	Node.post_order(root)


