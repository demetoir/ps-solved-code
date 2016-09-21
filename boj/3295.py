import sys

def dfs(cur):
	if check[cur]:return False
	check[cur]=True

	for next in G[cur]:
		if toleft[next]==-1 or dfs(toleft[next]):
			toleft[next]=cur
			return True
	return False


def matching():
	global toleft,n,check
	toleft=[-1]*n
	count=0
	for i in range(n):
		check=[False]*n
		if dfs(i):
			count+=1
	return count

for T in range(input()):
	n,m=map(int,raw_input().split())
	G=[[]for i in range(n)]

	for i in range(m):
		a,b=map(int,sys.stdin.readline().split())
		G[a]+=[b]
	print matching()