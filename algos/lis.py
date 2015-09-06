def lis_len(sequence):
    """
    Return the lengh of the 
    L.I.S. (Longest Increasing Subsequence) present 
    in sequence

    Complexity of this Dynamic Programmig (DP) 
    solution is O(n^2)
    """
    
    n = len(sequence)
    lis = [1] * n

    for i in range(n):
    	for j in range(i):
    		if sequence[i] > sequence[j] and lis[i] < lis[j] + 1:
    			lis[i] = lis[j] + 1

    return max(lis)

if __name__ == '__main__':
	sequence = [1, 11, 2, 10, 4, 5, 2, 1]
	print lis_len(sequence)

	sequence = [10, 22, 9, 33, 21, 50, 41, 60]
	print lis_len(sequence)