import Queue
import sys
import heapq
n,m,k=map(int,raw_input().split())
G=[[]for i in range(n+1)]
for i in range(m):
    a,b,c=map(int,raw_input().split())
    G[a]+=[(b,c)]
"""
data=Queue.deque()
for line in sys.stdin:
    data+=map(int,line.split())
r=lambda :data.popleft()

n,m,k=r(),r(),r()
G=[[]for i in range(n+1)]

for i in range(m):
    a,b,c=r(),r(),r()
    G[a]+=[(b,c)]
"""

qlist=[[] for i in range(n+1)]
qlist[1]+=[0]
#print G
q=Queue.PriorityQueue()

q.put((0,1))


while not q.empty():
    cost,cur=q.get()
    #print cur,cost

    for next,c in G[cur]:

        if len(qlist[next])< k:
            heapq.heappush(qlist[next],-(cost+c))
            q.put((cost+c,next))
        else:
            top = -qlist[next][0]
            if cost+c < top:
                heapq.heappop(qlist[next])
                heapq.heappush(qlist[next],-(cost+c))
                q.put((cost+c,next))



for i in range(1,n+1):
    if len(qlist[i]) < k:
        print -1
        continue


    print -qlist[i][0]
