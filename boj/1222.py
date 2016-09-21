
n=input()
l=list(map(int,raw_input().split()))

memo=[0]*2000001
for a in l:
	for j in range(1,1416):
		if a<j*j:break
		if a%j==0:
			x=j
			y=a//j
			if x==y:memo[x]-=1
			memo[x]+=1
			memo[y]+=1
ans=0
for i in range(1,2000001):
	if memo[i]>1:
		ans=max(ans,memo[i]*i)

print ans