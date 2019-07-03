"""
Algorithm:
  1.Find all inverse indecies. Save all pairs of inverse indecies to some array B .
  2.In the array B of pair of the inverse indecies we take each pair and count the value A[i] - A[j] to find the max value among all pairs.

Complexity:
  In the function FindInversion(A) we have 2 loops + the complexity of the function MaxInversePair(A, inverse_index_arr) which contains 1 loop.
  So the complexity is O(n^2) + O(n) = O(n^2)
 
"""

def MaxInversePair(A, inverse_index_arr):
  
  if(len(inverse_index_arr) == 0):
    return("No inverions in the array", A)

  max_ = 0
  max_inverse_pos = []  #the resulting indecies
  i = 0                 #first index in the pair[i,j]
  j = 1                 #second index in the pair[i,j]
  for pair in inverse_index_arr:
    if(A[pair[i]] - A[pair[j]] > max_):
      max_inverse_pos = pair    
      max_ = A[pair[i]] - A[pair[j]]
  
  return(max_inverse_pos)

def FindInversion(A):
  n = len(A)
  inverse_pos = [] #array of index pairs corresponding  an inversion
  for i in range(0, n - 1):
    for j in range(i+1, n):
      if(A[i] >= A[j]):
        inverse_pos.append([i,j]) #append the inversion into new array
  return(MaxInversePair(A, inverse_pos))

#Examples case
A = [1,25,2,6,11,16,8]
B = [1,2,3]
print(FindInversion(A))
print(FindInversion(B))

