import Queue

n,m=map(int,raw_input().split())
G=[[]for i in range(n+1)]
for i in range(n-1):
	a,b,w=map(int,raw_input().split())
	G[a]+=[(b,w)]
	G[b]+=[(a,w)]

def bfs(start,end):
	q=Queue.Queue()
	q.put(start)
	distance=[-1]*(n+1)
	distance[start]=0
	while 1:
		if q.empty():break
		cur=q.get()
		for post,w in G[cur]:
			if distance[post]==-1:
				distance[post]=distance[cur]+w
				q.put(post)
			if post==end:break
	return distance[end]

for i in range(m):
	start,end=map(int,raw_input().split())
	print bfs(start,end)
