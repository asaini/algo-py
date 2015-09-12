class Node:
	def __init__(self, data, left=None, right=None):
		self.left = left
		self.right = right
		self.data = data


def is_identical(root1, root2):
	"""
	Determine if Two Trees are Identical
	"""

	# Both trees are empty
	if root1 is None and root2 is None:
		return True

	# Recursively compare them if both are non-empty
	if root1 != None and root2 != None:
		data_check = root1.data == root2.data
		left_check = is_identical(root1.left, root2.left)
		right_check = is_identical(root1.right, root2.right)

		if data_check and left_check and right_check:
			return True

	return False


if __name__ == '__main__':

	# Construct the trees
	root1 = Node(1)
	root2 = Node(1)

	root1.left = Node(2)
	root1.right = Node(3)
	root1.left.left = Node(4)
	root1.left.right = Node(5)

	root2.left = Node(2)
	root2.right = Node(3)
	root2.left.left = Node(4)
	root2.left.right = Node(5)	

	# Check for identical trees
	print is_identical(root1, root2)



	# Check for non-identical trees
	root1 = Node(1)
	root2 = Node(1)

	root1.left = Node(2)
	root1.right = Node(3)
	root1.left.left = Node(4)
	root1.left.right = Node(5)

	root2.left = Node(2)
	root2.right = Node(3)
	root2.left.left = Node(4)

	print is_identical(root1, root2)