
"""
Algorithm:
	1.Sort the list of tasks by the deadline value t in ascending order.
	2.Loop through the list and compute the profit valued for the task t_i,
	if we have several tasks with the same deadline value t, we just take one,
	which has the max profit value p
		and it will be the last element in the slice of tasks with same deadline value because of sorted algorithm in step 1
	
	To sort the array of the arrays we use standard python sort function,
	by default it sorts the array of the arrays by first element, 
	if first elements of the initial array are equal it sorts by second element.
	Example:
	>>> a = [[7, 5], [1, 3], [4, 2], [1, 2]]
	>>> sorted(a)
	>>> [[1, 2], [1, 3], [4, 2], [7, 5]]

	Used links:
		https://stackoverflow.com/questions/6890170/how-to-find-the-last-occurrence-of-an-item-in-a-python-list
		https://stackoverflow.com/questions/14434490/what-is-the-complexity-of-this-python-sort-method
		https://stackoverflow.com/questions/5913671/complexity-of-list-indexx-in-python

	Running time for sorted() algorithm is O(n log n) plus
	the running time of
		while(i < n):
			j = n - first_index_arr[::-1].index(first_index_arr[i]) - 1
	The loop running time is O(n) and for list.index() standard function the runtime is also O(n).
	Since it's loop inside "loop" the total time for thi part of code is O(n^2)
	Hence, the overall running time of the function is
		
		O(n log n) + O(n^2) = O(n^2)
"""
def TaskProfit(arr):
	profit = 0					
	n = len(arr)						#the len of the array

	sorted_arr = sorted(arr);			#sort the input array by first coordinate
	first_index_arr = [x[0] for x in sorted_arr]     #array, containing only first elements of each array in the initial one(tasks' deadlines) 

	i = 0                               #task index
	while(i < n):
		j = n - first_index_arr[::-1].index(first_index_arr[i]) - 1  #last occurence of the task i
		if (i == j):
			#i == j means that the considered task is a unique and we just take its profit value
			profit += sorted_arr[i][1]
			i += 1						#go to the next task
		else:
			#if we have several tasks with the same deadline value, we take the last one, because it has the max profit value
			profit += sorted_arr[j][1]
			i = j + 1                  #go to the next unique task
	
	return(profit)
	
#example input
a = [[7, 5], [1, 3], [4, 2], [1, 2]]
b = [[1,10], [3,5],[2,4],[3,9]]
print("Input array", a, "\n Profit = ", TaskProfit(a) )
print("Input array", b, "\n Profit = ", TaskProfit(b) )
