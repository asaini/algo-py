class Node:

	def __init__(self, data, left=None, right=None):
		self.data = data
		self.left = left
		self.right = right

def create_bst(root, elements):

	for item in elements:
		node = Node(item)
		root = insert_node(root, node)

	return root

def insert_node(root, node):

	current = root
	current_parent = root
	
	while current:
		current_parent = current
		if node.data < current.data:
			current = current.left
		else:
			current = current.right

	if root is None:
		root = node
	elif node.data < current_parent.data:
		current_parent.left = node
	else
		current_parent.right = node

	return root

def k_smallest_element_inorder(root, k):

	stack = []
	current = root

	# Move of left extreme
	while current:
		stack.append(current)
		current = current.left

	# pop stack and process each node
	current = stack.pop()
	while current:
		

if __name__ == '__main__':
	elements = [20, 8, 22, 4, 12, 10, 14 ]

	root = None

	root = create_bst(root, elements)

	k_node = k_smallest_element_inorder(root, k)