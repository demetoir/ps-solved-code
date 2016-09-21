seive=[1]*(123456*3+1)
pl=[]
for p in range(2,123456*3+1):
    if seive[p]==0:continue
    pl+=[p]
    for j in range(2*p,123456*3+1,p):seive[j]=0
while 1:
    n=int(input())
    if n==0:break
    ans=0
    for i in pl:
        if i<=n+n and i>n:ans+=1
    print(ans)
