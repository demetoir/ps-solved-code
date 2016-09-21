def f(m,c):
    if memo[m][c]>-1:
        return memo[m][c]
    ret=0
    for i in range(m+1):
        a=f(m-i,c-1)+table[i][c]
        if ret<=a:
            ret=a
            path[m][c]=i

    memo[m][c]=ret
    return ret

m,c=map(int,input().split())
table=[[0]*(c+1) for i in range(m+1)]

for i in range(m):
    l=list(map(int,input().split()))
    for j in range(c):
        table[l[0]][j+1]=l[j+1]


memo=[[-1]*(c+1)for i in range(m+1)]
memo[0][1]=0
path=[[0]*(c+1)for i in range(m+1)]

for i in range(1,m+1):
    memo[i][1]=table[i][1]
    path[i][1]=i
print(f(i,c))

cur=m
l=[]
for i in range(c,0,-1):
    l=[str(path[cur][i])]+l
    cur-=path[cur][i]
print(" ".join(l))



