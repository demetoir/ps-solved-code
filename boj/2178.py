n,m=map(int,raw_input().split())
ll=[]
for i in range(n):
	s=[int(a) for a in raw_input()]
	ll+=[s]



delta=[(0,1),(1,0),(-1,0),(0,-1)]
distance=[[987654321]*m for i in range(n)]

import Queue
q=Queue.deque()
q+=[(0,0)]
distance[0][0]=1
while len(q)>0:
	b,a=q.pop()

	for dx,dy in delta:
		if a+dx<0 or a+dx>m-1:continue
		if b+dy<0 or b+dy>n-1:continue
		if ll[b+dy][a+dx]==0:continue

		if distance[b][a]+1<distance[b+dy][a+dx]:
			distance[b+dy][a+dx] = distance[b][a] + 1
			q+=[(b+dy,a+dx)]

print distance[n-1][m-1]

