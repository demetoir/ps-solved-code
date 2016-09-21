def r(x,y):
    dx=[1,0,-1,0]
    dy=[0,1,0,-1]
    q=[(x,y)]
    f[y][x]=0
    while q!=[]:
        x,y=q.pop(0)
        for i in range(4):
            a,b=dx[i],dy[i]
            if check_range(a+x,b+y)==1 and f[y+b][a+x]==1:
                q+=[(x+a,y+b)]
                f[y+b][a+x]=0
    return 1

def check_range(a,b):
    if a<0 or a>=m:
        return 0
    if b<0 or b>=n:
        return 0
    return 1

def next_location():
    for i in range(m):
        for j in range(n):
            if f[j][i]==1:
                return(i,j)
    return -1

for testcase in range(int(input())):

    m,n,k=map(int,input().split())
    f=[[0]*m for i in range(n)]
    for i in range(k):
        a,b=map(int,input().split())
        f[b][a]=1

    count=0
    while 1:
        next_loc=next_location()
        if next_loc==-1:break
        p,q=next_loc;
        if r(p,q)==1:
            count+=1
    print(count)
