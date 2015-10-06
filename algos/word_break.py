"""
Given an input string and a dictionary of words,
segment the input string into a space-separated
sequence of dictionary words if possible. For
example, if the input string is "applepie" and
dictionary contains a standard set of English words,
then we would return the string "apple pie" as output.

See : http://thenoisychannel.com/2011/08/08/retiring-a-great-interview-problem
"""

def segment_string_into_two(input_string, dictionary):
	"""
	Simple solution

	Assumes that a string can only be broken into 
	2 words
	"""
	n = len(input_string)
	for i in range(1, n):
		prefix = input_string[:i]
	
		if prefix in dictionary:
			suffix = input_string[i:]
			
			if suffix in dictionary:
				return prefix + " " + suffix

def segment_string_recursive(input_string, dictionary):
	"""
	Recursive solution

	Exponential complexity, eg. Consider a pathological dictionary 
	containing the words "a", "aa", "aaa", ...
	"""

	print "Input String = %s" % input_string
	if input_string in dictionary:
		return input_string

	n = len(input_string)

	for i in range(1, n):
		prefix = input_string[:i]

		if prefix in dictionary:
			suffix = input_string[i:]

			segmented_suffix = segment_string_recursive(suffix, dictionary)

			if segmented_suffix:
				return prefix + " " + segmented_suffix

	return None

def segment_string(input_string, dictionary, memo):

	print 'Input String = %s' % input_string

	if input_string in dictionary:
		return input_string

	if input_string in memo:
		return memo[input_string]

	n = len(input_string)

	for i in range(1, n):
		prefix = input_string[:i]

		if prefix in dictionary:
			suffix = input_string[i:]

			segmented_suffix = segment_string(suffix, dictionary, memo)

			#memo[suffix] = segmented_suffix
			print 'Memo = %s' % memo

			if segmented_suffix:
				return prefix + " " + segmented_suffix

	memo[input_string] = None
	return None
				
def segment_string_memoized(input_string, dictionary):
	"""
	Dynamic programming solution with memoization.
	"""
	memo = {}

	out = segment_string(input_string, dictionary, memo)
	return out

if __name__ == '__main__':
	input_string = 'aaaaaab'

	# dictionary containing vocabulary
	dictionary = {
		'aaa': 1,
		'aaaa': 1,
		'aaaaa': 1,
		'aaaaa': 1,
		'ab': 1
	}

	print "Simple Segmentation into two = %s" % segment_string_into_two(input_string, dictionary)

	print "Recursive Segmentation = %s" % segment_string_recursive(input_string, dictionary)

	print "Memoized Segmentation = %s" % segment_string_memoized(input_string, dictionary)
