import Queue

def bfs(start,end):
	q=Queue.Queue()
	check=[-1]*10000
	check[start]=0
	q.put((start))
	while 1:
		if q.empty():break

		cur=q.get()
		if cur==end:break
		s=str(cur)
		for j in range(4):
			for i in range(10):

				post=s[:j]+str(i)+s[j+1:]

				if int(post)>999 and post!=s and prime[int(post)]==1 and check[int(post)]==-1:

					check[int(post)]=check[cur]+1
					q.put(int(post))
	return check[end]

prime=[0]*2+[1]*10000
for i in range(2,10000):
	if prime[i]==0:continue
	for j in range(i*i,10000,i):
		prime[j]=0


for T in range(input()):
	s,e=map(int,raw_input().split())
	ans=bfs(s,e)
	if ans==-1:print "Impossible"
	else:print ans