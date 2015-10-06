class Node:

	def __init__(self, data, left=None, right=None):
		self.data = data
		self.left = left
		self.right = right

	@classmethod
	def construct_tree(cls, preorder):
		"""
		"""
		stack = []
		n = len(preorder)

		if n == 0:
			return None

		root = Node(preorder[0])

		stack.append(root)

		for i in range(1, n):
			item = preorder[i]
			temp = None

			while len(stack) > 0 and  item > stack[-1].data:
				temp = stack.pop()

			if temp:
				temp.right = Node(item)
				stack.append(temp.right)
			else:
				stack[-1].left = Node(item)
				stack.append(stack[-1].left)

		return root


def print_inorder(root):
	if root is None:
		return

	print_inorder(root.left)
	print root.data
	print_inorder(root.right)


if __name__ == '__main__':
	preorder = [10, 5, 1, 7, 40, 50]

	root = Node.construct_tree(preorder)

	print_inorder(root)