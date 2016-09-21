m,n=map(int,raw_input().split())
tomato=[]
for i in range(n):
	tomato+=[list(map(int,raw_input().split()))]


def bfs():
	import Queue
	q=Queue.Queue()
	dx=[1,0,-1,0]
	dy=[0,1,0,-1]
	for j in range(n):
		for i in range(m):
			if tomato[j][i]==1:
				q.put((i,j))

	while not q.empty():
		x,y=q.get()
		#print x,y
		for i in range(4):
			a=x+dx[i]
			b=y+dy[i]
			if a<0 or m<=a:continue
			if b<0 or n<=b:continue
			if tomato[b][a]==-1:continue
			if tomato[b][a]==0 or tomato[b][a]>tomato[y][x]+1:
				tomato[b][a]=tomato[y][x]+1
				q.put((a,b))

	#print tomato
	ans=0
	for j in range(n):
		for i in range(m):
			if tomato[j][i]==0:
				return -1
			ans=max(ans,tomato[j][i])

	return ans-1

print bfs()