n=input()
l=list(map(int,raw_input().split()))
indexlist=[-1]*(n+1)

for i in range(n):
	indexlist[l[i]]=i

count=0
anslist=[0]
for i in range(1,n):
	if indexlist[i]>indexlist[i+1]:
		anslist+=[i]
anslist+=[n]
ans=0
for i in range(len(anslist)-1):
	ans=max(anslist[i+1]-anslist[i],ans)
print n-ans
