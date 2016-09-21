n,k=map(int,input().split())
a=(10**len(str(n)))%k
ans=-1
p=1
r=n%k
for i in range(1,k+10):
    if r==0:ans=i;break
    p=(p*a)%k;r=((n*p)+r)%k
print(ans)