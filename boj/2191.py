import sys
import math
sys.setrecursionlimit(100000)
right=[]

def bi_matching():
	global check,right
	right=[-1]*(n+1)
	size=0
	for cur in range(1,n+1):
		check=[False]*(n+1)
		if dfs(cur):size+=1

	return size

def dfs(cur):

	if check[cur]:return False
	check[cur]=True
	for post in G[cur]:
		if right[post]==-1 or dfs(right[post]):
			right[post]=cur
			return True

	return False


n,m,s,v=map(int,sys.stdin.readline().split())
rat=[]
cave=[]

for i in range(n):
	x,y=list(map(float,sys.stdin.readline().split()))
	rat+=[[x,y]]

for i in range(m):
	x,y=list(map(float,sys.stdin.readline().split()))
	cave+=[[x,y]]


G=[[] for i in range(1000)]

##Graph

for i in range(n):
	for j in range(m):
		a,b=rat[i]
		x,y=cave[j]
		if math.hypot(a-x,b-y)<=v*s:
			G[i+1]+=[j+1]

#print rat
#print cave
#print G
check=[]
right=[]

ret=bi_matching()

#print ans
print (n-ret)

