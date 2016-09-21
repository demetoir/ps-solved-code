def f(n,p):
    if n==0:return 0
    return n+f(n//p,p)

seive=[1]*(10**5+1)
prime=[]
ans=1
for p in range(2,10**5+1):
    if seive[p]==0:continue
    prime+=[p]
    for j in range(2*p,10**5+1,p):seive[j]=0

while 1:
    try:n,k=map(int,input().split())
    except:exit()
    ans=1
    for p in prime:
        for i in range(1,f(n//p,p)+1):
            if k%(p**i)==0:
                ans*=p
            else:break
    print(ans)