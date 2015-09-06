def latest_no_overlap(jobs, n):
	"""
	Find the job before the nth job which does not
	overlap with the nth job

	Return -1 if no such job found
	"""
	for j in range(n - 1, -1, -1):
		if jobs[j][1] <= jobs[n][0]:
			return j;
	return -1;


def optimal_profit(jobs):
	"""
	Given a list of jobs return the maximum 
	profit from choosing a subset of the jobs
	such that no 2 jobs overlap
	"""

	# sort jobs according to finish time
	jobs = sorted(jobs, key = lambda x: x[1])

	n = len(jobs)
	table = [0] * n
	table[0] = jobs[0][2]
	
	# Include the latest job
	for i in range(1, n):
		profit = jobs[i][2]
		j = latest_no_overlap(jobs, i)
		
		if j != -1:
			profit += table[j]

		table[i] = max(profit, table[i-1])

	result = table[n - 1]
	return result


if __name__ == '__main__':
	
	# Every item in tuple is of the form
	# (start_time, finish_time, weight)
	jobs = [
		(3, 10, 20),
		(1, 2, 50), 
		(6, 19, 100), 
		(2, 100, 200)
	]

	print optimal_profit(jobs)
