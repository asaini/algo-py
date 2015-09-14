def max_substr_palindrome(string):
	"""
	Given a string, find the longest substring which is palindrome. 
	eg, input  : forgeeksskeegfor, 
	    output : geeksskeeg
	"""
	n = len(string)

	# table[i][j] is the substring string[i:j]
	table = [ [0]*n for i in range(n) ]


	# Strings of length 1 
	for i in range(n):
		table[i][i] = True

	start, max_length = 0, 0
	for i in range(n-1):
		if string[i] == string[i+1]:
			start, max_length = i, 2

	for k in range(3, n+1):
		for i in range(n - k + 1):
			j = i + k - 1
			



if __name__=='__main__':
	string = "forgeeksskeegfor"
	print max_substr_palindrome(string)
