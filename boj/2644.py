n=input()
a,b=map(int,raw_input().split())
m=input()
G=[[]for i in range(n+1)]

for i in range(m):
    x,y=map(int,raw_input().split())
    G[x]+=[y]
    G[y]+=[x]
ans=-1
check=[-1]*(n+1)

import Queue
Q=Queue.Queue()
Q.put(a)
check[a]=0
while not Q.empty() :
    cur=Q.get()
    if cur==b:break

    for next in G[cur]:
        if check[next]==-1:
            check[next]=check[cur]+1
            Q.put(next)




print check[b]