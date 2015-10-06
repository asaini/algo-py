class TwoStacks:
	"""
	Two stacks in an array
	"""
	def __init__(self, n):
		self.size = n
		self.array = [None] * n
		self.top1 = -1
		self.top2 = self.size

	def push1(self, x):
		if self.top1 < self.top2 - 1:
			self.top1 += 1
			self.array[self.top1] = x
		else:
			raise IndexError("StackOverflow")

	def push2(self, x):
		if self.top1 < self.top2 - 1:
			self.top2 -= 1
			self.array[self.top2] = x
		else:
			raise IndexError("StackOverflow")

	def pop1(self):
		if self.top1 > 0:
			x = self.array[self.top1]
			self.top1 -= 1
			return x
		else:
			raise IndexError("StackUnderflow")

	def pop2(self):
		if self.top2 < self.size:
			x = self.array[self.top2]
			self.top2 += 1
			return x
		else:
			raise IndexError("StackUnderflow")

if __name__ == '__main__':
	ts = TwoStacks(6)
	ts.push1(5)
	ts.push2(10)
	ts.push2(15)
	ts.push1(11)
	print ts.array