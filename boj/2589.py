import Queue

n,m=map(int,raw_input().split())
l=[]
for i in range(n):
	p=[]
	for c in raw_input():
		p+=[c]
	l+=[p]

def bfs(start):
	q=Queue.deque()
	q.appendleft(start)
	a,b=start
	distance=[[-1]*(m+1) for i in range(n+1)]
	distance[b][a]=0
	delta=[(0,1),(0,-1),(1,0),(-1,0)]
	ret=-1
	while len(q)>0:
		x,y=q.pop()
		for a,b in delta:
			i=x+a
			j=y+b
			if i>=m or i<0:continue
			if j>=n or j<0:continue
			if l[j][i]=="L" and distance[j][i]==-1:
				distance[j][i]=distance[y][x]+1
				q.appendleft((i,j))
				ret=max(ret,distance[j][i])
	return ret
ans=-1
for i in range(m):
	for j in range(n):
		if l[j][i]=="L":
			ans=max(ans,bfs((i,j)))
print ans
