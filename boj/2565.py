import bisect

n=input()
l=[-1]*501
for i in range(n):
	a,b=map(int,raw_input().split())
	l[a]=b

data=[]
for i in range(1,501):
	if l[i]>0:
		data+=[l[i]]

lis=[data[0]]
for i in range(1,n):
	last=len(lis)-1
	if lis[last]<data[i]:
		lis+=[data[i]]
	else:
		index=bisect.bisect_left(lis,data[i])

		lis[index]=data[i]

print n-len(lis)
