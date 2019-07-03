def merge(input, memory, start, mid, end):
	left_count = mid - start + 1
	right_count = end - mid

	left_arr = list(range(left_count))
	right_arr = list(range(right_count))
	memory_left_arr = list(range(left_count))
	memory_right_arr = list(range(left_count)) 

	for i in range(0 , left_count):
		left_arr[i] = input[start + i]
		memory_left_arr[i] = memory[start + i]

	for j in range(0 , right_count):
		right_arr[j] = input[mid + 1 + j]
		memory_right_arr[j] = memory[mid + 1 + j]

	i = 0	 
	j = 0	
	k = start

	while i < left_count and j < right_count :
		if left_arr[i] <= right_arr[j]:
			input[k] = left_arr[i]
			memory[k] = memory_left_arr[i] 
			i += 1
		else:
			input[k] = right_arr[j]
			memory[k] = memory_right_arr[j]
			j += 1
		k += 1

	while i < left_count:
		input[k] = left_arr[i]
		memory[k] = memory_left_arr[i] 
		i += 1
		k += 1

	while j < right_count:
		input[k] = right_arr[j]
		memory[k] = memory_right_arr[j] 
		j += 1
		k += 1

def mergeSort(input, memory, start, end):
	if start < end:

		mid = (start + end)/2

		mergeSort(input, memory, start, mid)
		mergeSort(input, memory, mid+1, end)
		merge(input, memory, start, mid, end)

def memory_sort(input):
	length = len(input)
	memory = [0] * length 
	for i in range(0 , length):
		memory[i] = i+1

	mergeSort(input, memory, 0, length-1)
	return [input, memory]

input = [4, 2, 1] 
print memory_sort(input)

'''
used link: https://github.com/cyandterry/Python-Study/blob/master/solutions.md
'''


