import bisect

n=input()
l=[-1]*500001
d={}
for i in range(n):
	a,b=map(int,raw_input().split())
	l[b]=a


data=[]
path=[-1]*500001
for i in range(1,500001):
	if l[i]>0:
		data+=[l[i]]

lis=[data[0]]

for i in range(1,n):
	last=len(lis)-1
	if lis[last]<data[i]:
		lis+=[data[i]]
		path[data[i]]=lis[last]
	else:
		index=bisect.bisect_left(lis,data[i])
		if index>0:
			path[data[i]]=lis[index-1]
		lis[index]=data[i]



print n-len(lis)

last=len(lis)-1

cur = lis[last]
ans=[]
index=n-1

while cur>-1:
	while cur!=data[index]:
		index-=1
	data[index]=-1
	cur=path[cur]
	index-=1

ans.reverse()

for i in range(n):
	if data[i]>0:
		ans+=[data[i]]

ans.sort()

print "\n".join(str(i)for i in ans)