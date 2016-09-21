n,m=map(int,input().split())
l=[input() for i in range(n)]
c=["BW"*4 if i%2==1 else "WB"*4 for i in range(8)]
rc=list(reversed(c))
ans=64
for a in range(n-8+1):
    for b in range(m-8+1):
        x=0;y=0
        for i in range(8):
            for j in range(8):
                if c[i][j]!=l[i+a][j+b]:x+=1
                if rc[i][j]!=l[i+a][j+b]:y+=1
        ans=min(ans,x,y)
print(ans)






