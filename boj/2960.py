n,k=map(int,input().split())
seive=[1]*(n+1)
for p in range(2,n+1):
    if seive[p]==0:continue
    for j in range(p,n+1,p):
        if seive[j]==1:k-=1
        if k==0:print(j);exit()
        seive[j]=0