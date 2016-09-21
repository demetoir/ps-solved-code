seive=[0]*(10**6+1)
pl=[]
for p in range(2,10**6+1):
    if seive[p]>0:continue
    pl+=[p]
    for j in range(2*p,10**6+1,p):seive[j]=p

for T in range(int(input())):
    n=int(input())
    ans="YES"
    for i in pl:
        if n%i==0:ans="NO";break
    print(ans)