import sys
import thread
sys.setrecursionlimit(10300)
thread.stack_size(1024*80)
n=input()
l=[]
for i in range(n):
    l+=[list(map(int,raw_input().split()))]
check=[]
 
def isOK(x,y):
	global n
	if x<0 or x>=n:return False
	if y<0 or y>=n:return False
	return True
 
def dfs(x,y):
	global check,l,level

	if check[y][x]>0:return
	check[y][x]=1
	delta=[(1,0),(0,1),(0,-1),(-1,0)]
 
	for a,b in delta:
		if isOK(a+x,b+y) and l[b+y][a+x]>level:
			dfs(a+x,b+y)
 
	return
ans=0
for level in range(101):
	check=[[0]*n for i in range(n)]
	cur=0
	for i in range(n):
		for j in range(n):
			if l[j][i]<=level or check[j][i]==1 :continue
			cur+=1
			dfs(i,j)
	ans=max(ans,cur)

print (ans)