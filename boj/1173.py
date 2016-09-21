N,m,M,T,R=map(int,input().split())
x=m
t=0
if m+T>M:
    print(-1)
    exit(0)
while 1:
    if N==0:break
    if x+T>M:
        t+=1
        x=max(x-R,m)
    else:
        t+=1
        x+=T
        N-=1
print(t)

