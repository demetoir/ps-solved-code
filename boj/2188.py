def dfs(cur):
	global check,bi
	if check[cur]:return False
	check[cur]=True
	for post in G[cur]:
		if bi[post]==-1 or dfs(bi[post]):
			bi[post]=cur
			return True
	return False

def match():
	global check,bi,n
	bi=[-1]*250
	size=0
	for i in range(1,n+1):
		check=[False]*250
		if dfs(i):size+=1
	return size


n,m=map(int,raw_input().split())
G=[[]for i in range(250)]
check=[]
bi=[]
for i in range(n):
	l=list(map(int,raw_input().split()))
	si=l[0]
	for j in range(1,si+1):
		G[i+1]+=[l[j]]
#print G
print match()
