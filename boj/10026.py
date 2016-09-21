n=int(input())
G=[]
from collections import deque


for i in range(n):
    G+=[[c for c  in input()]]
check=[[0]*n for i in range(n)]

def bfs(x,y):
    if check[y][x]==1:return 0
    delta=[(0,1),(1,0),(-1,0),(0,-1)]
    q=deque()
    q.extend([(x,y)])
    color=G[y][x]

    while len(q)>0:
        x,y=q.pop()
        check[y][x]=1
        for a,b in delta:
            if x+a<0 or x+a>=n:continue
            if y+b<0 or y+b>=n:continue
            if G[y+b][x+a]!=color:continue
            if check[y+b][x+a]==1:continue
            q.extend([(x+a,y+b)])

    return 1


ans1=0
ans2=0

check=[[0]*n for i in range(n)]
for x in range(n):
    for y in range(n):
      ans1+=bfs(x,y)


for x in range(n):
    for y in range(n):
        if G[y][x]=='G':G[y][x]="R"

check=[[0]*n for i in range(n)]
for x in range(n):
    for y in range(n):
      ans2+=bfs(x,y)


print(ans1,ans2)