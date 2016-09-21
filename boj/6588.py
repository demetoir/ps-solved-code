import sys

seive=[1]*(1000000+1)
prime=[]
ans=1
for p in range(2,1000000+1):
    if seive[p]==0:continue
    prime+=[p]
    for j in range(2*p,1000000,p):seive[j]=0

while 1:
    n=int(sys.stdin.readline())
    if n==0:break

    for p in prime:
        if p+p>n:break
        if seive[n-p]==1:
            sys.stdout.write(str(n)+" = "+str(p)+" + "+str(n-p)+"\n")
            break