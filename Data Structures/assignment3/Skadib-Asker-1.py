#Algorithm : count number of 0's in a given binary array

def count(lst, start, end):
        totalZero = 0
        #base case if empty list
        if start == end:
                return 0
        
        #base case single element
        if start == end-1:
                if lst[start] == 0:
                        return 1
                else:   
                        return 0        
                        
                
        totalZero += count(lst, start, (start+end)/2)
        totalZero += count(lst, (start+end)/2, end)

        return totalZero

# All operation in the function take O(1) time. and the total Complexity is T(n) = 2T(n/2) + O(1)= O(n)



def count_zero(lst):
        return count(List, 0, len(List))
#Test example
List = [0, 0, 0, 1, 1, 1, 1]
print(count_zero(List))
