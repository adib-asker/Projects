
"""
The idea of the algorithm is to check for every node (but not a leaf one)
if its left and right child is greater than the current node.
If this condition is true we call again this procedure for each child.

Running time:
	each time the recursion function calls itself
	we consider(2 times) only the half of the original array(by increasing the index)
	plus we do some comparing. So we can write the complexity as
	
		T(n) = 2T(n/2) + O(1)
		Using the Master theorem we obtain that the time complexity is O(n log n)
	
 
	Due to the problem requires the function with only one input argument,
	I created another function(isMinHeap) inside this one with neccesary arguments.
"""
def TraiteHeap(arr):
	n = len(arr)
	i = 0

	if(isMinHeap(arr, i, n)):
		return(True)
	else:
		return(False)

def isMinHeap(arr, index, size):
	
	#leaf node case. Leaf is a min heap
	if(index > (size - 2)//2 - 1):
		return(True)

	left_child = False
	right_child = False
	#if left child is a heap
	if( (arr[index] <= arr[2*index + 1]) and (isMinHeap(arr, 2*index + 1, size)) ):
		left_child = True

	#if right child is a heap
	if( (arr[index] <= arr[2*index + 2]) and (isMinHeap(arr, 2*index + 2, size)) ):
		right_child = True

	#if both left and right child are heap
	if (left_child and right_child):
		return(True)
	return(False)
	
#Test example
not_heap = [1,5,6,3,9,8]
heap = [1,3,6,5,9,8]


print("Array ", not_heap, "is minheap :", TraiteHeap(not_heap))
print("Array ", heap, "is minheap :", TraiteHeap(heap))	
