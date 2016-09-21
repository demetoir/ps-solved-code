
n,k=map(int,raw_input().split())
l=list(map(int,raw_input().split()))



d={0:1}
s=[0]
a=0
for i in l:
	a+=i
	if a in d:d[a]+=1
	else:d[a]=1
	s+=[a]

ans=0
for i in range(1,n+1):
	t=s[i-1]+k
	d[s[i-1]]-=1

	if t in d:
		ans+=d[t]
		#print i,t,d[t],d


print ans