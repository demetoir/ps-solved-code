import fractions

n=input()
G=[[]for i in range(n)]

for i in range(n-1):
	a,b,x,y=map(int,raw_input().split())
	g=fractions.gcd(x,y)

	x=x//g
	y=y//g
	G[a]+=[(b,x)]
	G[b]+=[(a,y)]
check=[False]*n

def dfs(cur):
	check[cur]=True
	ret=1
	for next,mul in G[cur]:
		if check[next]==False:
			ret=ret*mul*dfs(next)
	return ret

l=[]
for i in range(n):
	check=[False]*n
	l+=[dfs(i)]
a=l[0]
for i in range(1,n):
	a=fractions.gcd(a,l[i])
ans=[]
for i in l:
	ans+=[str(i//a)]
print " ".join(ans)
