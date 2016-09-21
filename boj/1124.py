seive=[0]*(100000+1)
pl=[]
for p in range(2,100000+1):
    if seive[p]>0:continue
    pl+=[p]
    seive[p]=1
    for j in range(2*p,100000+1,p):seive[j]=p
a,b=map(int,input().split())
ans=0

for i in range(a,b+1):
    k=i
    count=1
    while seive[k]!=1:
        k=k//seive[k]
        count+=1
    if seive[count]==1:ans+=1
print(ans)
