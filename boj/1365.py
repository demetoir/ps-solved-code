import bisect

n=input()

data=list(map(int,raw_input().split()))


lis=[data[0]]
for i in range(1,n):
	last=len(lis)-1
	if lis[last]<data[i]:
		lis+=[data[i]]
	else:
		index=bisect.bisect_left(lis,data[i])

		lis[index]=data[i]

print n-len(lis)
