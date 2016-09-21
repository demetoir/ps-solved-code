n=input()
t=[0]*(n+1)
g=[[]for i in range(n+1)]
queue=[0]
pre=[0]*(n+1)
memo=[0]*(n+1)
for i in range(n):
	l=list(map(int,raw_input().split()))
	t[i+1]=l[0]
	if l[1]==0:continue
	pre[i+1]=l[2]
	g[i+1]=l[2:]

memo[1]=t[1]


def f(n):
	if memo[n]>0:
		return memo[n]
	ret=0
	for i in g[n]:
		ret=max(ret,f(i))
	memo[n]=ret+t[n]
	return  memo[n]
ans=0
for i in range(1,n+1):
	ans=max(ans,f(i))

print(ans)
