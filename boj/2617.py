
n,m=map(int,raw_input().split())

G=[[]for i in range(n+1)]
for i in range(m):
    a,b=map(int,raw_input().split())
    G[a]+=[b]

check=[False]*(n+1)
reach=[[0]*(n+1) for i in range(n+1)]
def dfs(cur):
    if check[cur]:return False
    check[cur]=True
    for next in G[cur]:
        if dfs(next):
            reach[start][next]=1
            reach[next][start]=-1
            #print start,next
    return True


start=0
for i in range(1,n+1):
    check=[False]*(n+1)
    start=i
    dfs(start)

ans=0

for i in range(1,n+1):

    if reach[i].count(-1)>= n//2+1 or reach[i].count(1)>=n//2+1:
        ans+=1
        #print i
    #print reach[i]
print ans





