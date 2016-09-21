import sys
import Queue
q=Queue.deque()

v,e=map(int,sys.stdin.readline().split())
INF=987654321
start=int(sys.stdin.readline())
g=[Queue.deque() for i in range(v+1)]
distance=[INF]*(v+1)
   
for i in range(e):
    u,v,w=map(int,sys.stdin.readline().split())
    g[u].appendleft((v,w))
   

distance[start]=0
q.appendleft(start)

while(len(q)>0):
    cur=q.pop()

    for n,w in g[cur]:
        if distance[n]>distance[cur]+w:
            distance[n]=distance[cur]+w
            q.appendleft(n)
   
   
for i in distance[1:]:
    if i==INF:
        print("INF")
    else:print(i)