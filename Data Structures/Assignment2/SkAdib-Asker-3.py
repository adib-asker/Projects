
"""
Heap-Insert
The algorithm consist of 2 steps:
	1. Inserting the given value x to the leftmost position of the last leaf level of heap(to the end of the array)
	2. Move the inserted node up by comparing the inserted element with its parent node and swap them if 
			parent > new_node

The running Time is O(log n) because the loop which compares and swap the parent and new node
runs only through the parent nodes. In the worst case we loop till the root.
Hence we can consider the running time which takes to walk from root to the leaf visiting only one
node on each level of the tree, which is equal to the heigh of the tree h = O(log n base 2) 

"""
def HeapInsert(arr, x):

	#inserting x to the end of the heap
	arr.append(x)

	#move the new node on a proper place
	parent_pos = (len(arr) // 2) - 1     #parent position of node x
	x_pos = len(arr) - 1   	  			#x node position
	
	while(parent_pos >= 0):    			#until no parent for x
		if(arr[parent_pos] > arr[x_pos]):
		
			#wrong place for node x. Swap
			temp = arr[parent_pos]
			arr[parent_pos] = arr[x_pos]
			arr[x_pos] = temp
			
			x_pos = parent_pos          #new position of node x
			parent_pos = x_pos//2 - 1
		
		else:
			break						#x is on its place
	
	return(arr)

#example input
a = [1,3,6,5,9,8]
x = 2
print("Example 1:Initial heap", a)
print("Example 1: Inserted x = 2", HeapInsert(a,x))
b = [1,3,6,5,9,8]
x = -2
print("Example 2: Initial heap", b)
print("Example 2: Inserted x = -2", HeapInsert(b,x))
