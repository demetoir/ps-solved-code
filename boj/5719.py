import Queue,sys

def dijkstra(start,end,G):
	q=Queue.Queue()
	distance=[9876543210]*n
	distance[start]=0
	q.put(start)
	path=[[]for i in range(n)]

	while 1:
		if q.empty():break
		cur=q.get()
		for post,w in G[cur]:
			if distance[post]>distance[cur]+w:
				distance[post]=distance[cur]+w
				q.put(post)
				path[post]=[cur]
			elif distance[post]==distance[cur]+w:
				path[post]+=[cur]

	if distance[end]==9876543210:distance[end]=-1
	return distance[end],path

def dfs(cur):
	for post in path[cur]:
		check[post][cur]=1
		dfs(post)
	return

while 1:
	n,m=map(int,raw_input().split())
	if (n,m)==(0,0):
		break

	G=[[] for i in range(n)]
	start,end=map(int,raw_input().split())
	for i in range(m):
		a,b,w=map(int,sys.stdin.readline().split())
		G[a]+=[(b,w)]

	cost,path=dijkstra(start,end,G)

	"""
	print "cost"
	print cost
	print "path"
	for i in range(n):
		print i,path[i]
	"""

	check=[[0]*n for i in range(n)]
	dfs(end)

	"""
	print "check"
	for i in range(n):
		print i,check[i]
	"""

	newG=[[] for i in range(n)]
	for a in range(n):
		for b,w in G[a]:
			if check[a][b]==0:
				newG[a]+=[(b,w)]
	"""
	print "newG"
	for i in range(n):
		print i,newG[i]
	"""

	ans,newpath=dijkstra(start,end,newG)

	"""
	print "ans"
	"""

	print ans