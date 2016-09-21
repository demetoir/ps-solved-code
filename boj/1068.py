N=int(input())
p=list(map(int,input().split()))
d=int(input())
check=[1]*N
T=[[]for i in range(N)]

def dfs(n):
    if T[n]==[]:return 1
    ret=0
    for i in T[n]:ret+=dfs(i)
    return ret
#find root
for i in range(N):
    if p[i]==-1:root=i
#make TREE
for i in range(N):
    if p[i]>-1 and i!=d:T[p[i]]+=[i]

if d==root:print(0)
else:print(dfs(root))
