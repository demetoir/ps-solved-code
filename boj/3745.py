import bisect
import sys
while 1:
	try:n=int(sys.stdin.readline())
	except:break

	data=list(map(int,sys.stdin.readline().split()))

	lis=[data[0]]
	for i in range(1,n):
		last=len(lis)-1
		if lis[last]<data[i]:
			lis+=[data[i]]
		else:
			index=bisect.bisect_left(lis,data[i])
			lis[index]=data[i]

	print len(lis)
