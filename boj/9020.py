seive=[1]*(10**4+1)
prime=[]
ans=1
for p in range(2,10**4+1):
    if seive[p]==0:continue
    prime+=[p]
    for j in range(2*p,10**4+1,p):seive[j]=0

for T in range(int(input())):
    n=int(input())
    a,b=0,0
    for p in prime:
        if p+p>n:break
        if seive[n-p]==1:
            a,b=p,n-p
    print(a,b)