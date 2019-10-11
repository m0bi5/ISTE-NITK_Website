#Logic: This program prints the diffrence of cube
#of number having maximum abslute value and minimum absolute value.

def solve(a):
	minv=1000000000
	maxv=0
	for i in a:
		minv=min(minv,abs(i))
		maxv=max(maxv,abs(i))

	# print(maxv,minv)
	return (maxv*maxv*maxv-minv*minv*minv)


a = [1,2,-1,2,-1]
print(solve(a))
