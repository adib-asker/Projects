
"""
Algorithm:
	Sort the graph array by weight to respect the greedy way: always take the globally min weight
	Add each edge from sorted graph which doesn't form a cycle to the minimum spanning tree array.

	To find out if the edge makes a cycle, we check if both its nodes are in the list of nodes
	which are already in MST. 
	
	Used links 
		https://stackoverflow.com/questions/20099669/python-sort-multidimensional-array-based-on-2nd-element-of-subarray
		https://stackoverflow.com/questions/14434490/what-is-the-complexity-of-this-python-sort-method
		https://stackoverflow.com/questions/13884177/complexity-of-in-operator-in-python
"""

def MST(graph):
	MST = []      											#min spanning tree(MST)
	list_node = []											#list of nodes already in the MST
	sorted_graph = sorted(graph, key = lambda x: x[2])  	#returns a graph sorted by weight 
	
	for node in sorted_graph:								
		if(	(node[0] in list_node) and (node[1] in list_node)): #check if the node makes loop
			continue
		
		MST.append(node)
		list_node.append(node[0])							
		list_node.append(node[1])

	return(MST)

#example input
a = [[5,6,1],[1,2,2],[2,5,3],[1,3,4],[3,4,6],[1,4,7],[2,6,5],[2,4,9]]
#print("Initial graph", a)
print("MST", MST(a))

"""
The runtime of the algorithm consist of the running time of two main procedures in the code
1. standard library's function "list.sorted()" which is O(n log n)
2. "for node in sorted_graph:								
		if(	(node[0] in list_node) and (node[1] in list_node))"
	It's loop in the loop and we can consider it as O(n^2)
Since this two procedures are independent, it follows that the overall running time is
	
				# O(n log n) + O(n^2) = O(n^2) wrong
				It takes o(n) operation
	
"""
