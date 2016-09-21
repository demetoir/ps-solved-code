import Queue
q=Queue.deque()
INF=987654321
n=input()
l=[0]+list(map(int,raw_input().split()))
a,b=map(int,raw_input().split())
d=[INF]*(n+1)
q+=[a]
d[a]=0

while len(q)>0:
	cur=q.popleft()
	jump=l[cur]
	for i in range(cur+jump,n+1,jump):
		if d[i]>d[cur]+1:
			d[i]=d[cur]+1
			q+=[i]
	for i in range(cur-jump,0,-jump):
		if d[i]>d[cur]+1:
			d[i]=d[cur]+1
			q+=[i]

if d[b]==INF:print -1
else:print d[b]