import collections

n=input()

memo=[(-1,-1)]*(n+1)
check=[0]*(n+1)

T=[[] for i in range(n+1)]
G=[[] for i in range(n+1)]

for i in range(n-1):
	a,b=map(int,raw_input().split())
	G[a]+=[b]
	G[b]+=[a]

def bfs():
	q=collections.deque()
	l=collections.deque()
	q.appendleft(1)
	while len(q)>0:
		cur=q.pop()
		check[cur]=1
		l+=[cur]
		for post in G[cur]:
			if check[post]==1:continue
			q.appendleft(post)
			T[cur]+=[post]
	return l

l=bfs()

for i in reversed(l):
	a,b=1,0
	for post in T[i]:
		x,y=memo[post]
		a+=min(x,y)
		b+=x
	memo[i]=(a,b)

print min(memo[1])
