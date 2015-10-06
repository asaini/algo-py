def is_operand(item):
	if item >= 'a' and item <= 'z':
		return True
	return False

def precision(item):
	prec = {
		'+' : 1,
		'-' : 1,
		'*' : 2,
		'/' : 2,
		'^' : 3
	}
	out = -1
	try:
		out = prec[item]
	except KeyError:
		pass
	return out

def infix_to_postfix(expression):
	n = len(expression)

	stack = []
	out = []

	for item in expression:
		# If operand, add to output
		if is_operand(item):
			out.append(item)
		elif item == '(':
			stack.append(item)
		elif item == ')':
			while len(stack) > 0 and stack[-1] != '(':
				x = stack.pop()
				out.append(x)
			if len(stack) > 0 and stack[-1] != '(':
				return -1
			else:
				stack.pop()

		else:
			while len(stack) > 0 and precision(item) <= precision(stack[-1]):
				x = stack.pop()
				out.append(x)
			stack.append(item)

	while len(stack) > 0:
		x = stack.pop()
		out.append(x)

	return out

if __name__ == '__main__':
	exp = "a+b*(c^d-e)^(f+g*h)-i"
	print infix_to_postfix(exp)

