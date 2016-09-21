import queue
import sys
pq=queue.PriorityQueue()
n,m=map(int,sys.stdin.readline().split())
G=[[]for i in range(n+1)]
number=[0]*(n+1)
for i in range(m):
    a,b=map(int,sys.stdin.readline().split())
    G[a]+=[b]
    number[b]+=1
for i in range(1,n+1):
    if number[i]==0:pq.put(i)
s=[]
while pq.empty()==False:
    a=pq.get()
    s+=[str(a)]
    for i in G[a]:
        number[i]-=1
        if number[i]==0:pq.put(i)
print(" ".join(s))