import queue
import sys


def dfs(n):
    global dfs_squence,dfs_visted
    dfs_visted[n]=1
    dfs_squence+=[str(n)]
    for i in G[n]:
        if dfs_visted[i]==0:
            dfs(i)

def bfs(start):
    q=queue.deque()
    squence=[]
    visited=[0]*(n+1)
    visited[start]=1
    q.append(start)
    while len(q)>0:
        a=q.popleft()
        squence+=[str(a)]
        for i in G[a]:
            if visited[i]==0:
                visited[i]=1
                q.append(i)
    return squence

n,m,start=map(int,input().split())
dfs_squence=[]
dfs_visted=[0]*(n+1)

G=[[]for i in range(n+1)]

for i in range(m):
    a,b=map(int,sys.stdin.readline().split())
    G[a]+=[b]
    G[b]+=[a]
for i in G:
    i.sort()

dfs(start)
print(" ".join(dfs_squence))
sq=bfs(start)
print(" ".join(sq))