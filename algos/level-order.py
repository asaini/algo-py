"""
Level order traversal of a tree
"""

class Node:

	def __init__(self, data, left=None, right=None):
		self.data = data
		self.left = left
		self.right = right

def height(root):
	if root == None:
		return 0

	return 1 + max(height(root.left),
				   height(root.right))

def print_level(root, level):
	if root is None:
		return
	if level == 1:
		print root.data,
	elif level > 1:
		print_level(root.left, level - 1)
		print_level(root.right, level - 1)

def level_order_traversal(root):
	h = height(root)

	for i in range(1, h + 1):
		print_level(root, i)
		print ''

if __name__ == '__main__':

	root = Node(1)
	root.left = Node(2)
	root.right = Node(3)
	root.left.left = Node(4)
	root.left.right = Node(5)

	level_order_traversal(root)