def swap(a, start, end):
	z = list(a)
	temp = z[end]
	z[end] = z[start]
	z[start] = temp
	return ''.join(z)

def permute(a, start, end):
	if start == end:
		print a

	else:
		for i in range(start, end + 1):
			s = swap(a, start, start + i)
			permute(s, start + 1, end)
			a = 


if __name__ == '__main__':
    x = 'abcdef'
    permute(x, 0, len(x) - 1)
