n,k=map(int,raw_input().split())
l=list(map(int,raw_input().split()))
s=""
for i in l:s+=str(i)

target="".join(str(i) for i in range(1,n+1))

import Queue
q=Queue.deque()
d={s:0}

def bfs(start):
	global n,k
	q=Queue.deque()
	q.appendleft(start)
	while len(q):
		cur=q.pop()

		for i in range(n-k+1):
			p=""

			for j in range(i)+range(i+k-1,i-1,-1)+range(i+k,n):
				p+=cur[j]

			if p not in d:
				d[p]=d[cur]+1
				q.appendleft(p)

			if p==target:return

	return

bfs(s)



if target in d:print(d[target])
else:print -1