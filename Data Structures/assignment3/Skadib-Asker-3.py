#Approximate cubic root
def cubic(start, end, x, d):
	mid = (start+end)/2.0

	if(abs(mid*mid*mid - x) < d):
		return mid

	if(mid*mid*mid > x):
		return cubic(start, mid, x, d)
	else:
		return cubic(mid, end, x, d)


def cubic_root(x, err):
	if(err == 0):
		return "d must be greater than 0"
	return cubic(0, x, x, err)


#Example case
print cubic_root(10, 0.1)

#The time complexity of this function is: T(n) = T(n/2) + O(1)= O(log n)
