import sys
import Queue

n,e=map(int,sys.stdin.readline().split())
G=[[]for i in range(n+1)]
INF=987654321012345789

for i in range(e):
    a,b,c=map(int,sys.stdin.readline().split())
    G[a]+=[[b,c]]
    G[b]+=[[a,c]]
a,b=map(int,sys.stdin.readline().split())



def dijkstra (start,end):
    global INF,n

    distance=[INF]*(n+1)
    q=Queue.deque()

    q.append(start)
    distance[start]=0

    while len(q)>0:
        cur=q.popleft()
        for i,cost in G[cur]:
            if distance[i]> distance[cur]+cost:
                distance[i]=distance[cur]+cost
                q.append(i)

    return distance[end]


one=dijkstra(1,a)+dijkstra(b,n) +dijkstra(a,b)
two=dijkstra(1,b)+dijkstra(a,n) +dijkstra(a,b)
result=min(one,two)
if result >=INF:
    print(-1)
else:
    print(result)














