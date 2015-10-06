def reverse_words(string):
	"""
	Reverse the words in a given string

	Eg. 
	  Input: i like this program very much
	  Output: much very program this like i
	"""
	rev_string = list(reversed(string))

	string_len, i, word_start_index = len(string), 0, 0

	while i < string_len - 1:
		i += 1

		if i == string_len - 1:
			rev_string = reverse_string(rev_string, word_start_index, i)
		elif rev_string[i] == ' ':
			rev_string = reverse_string(rev_string, word_start_index, i - 1)
			word_start_index = i + 1
	return rev_string


def reverse_string(iterable, start, end):
	while start < end:
		iterable[start], iterable[end] = iterable[end], iterable[start]
		start += 1
		end -= 1
	return iterable

if __name__ == '__main__':
	s = "i like this program very much"
	print ''.join(reverse_words(s))

