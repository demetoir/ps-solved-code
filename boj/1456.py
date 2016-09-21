n=10**7
l=[1]*(n+10)
pn=[]
a,b=map(int,input().split())
ans=0
print(ans)
for i in range(2,n):
    if l[i]==0:continue
    s=i*i
    while s<=b:
        if s>=a and s<=b:ans+=1
        s*=i
    for j in range(i*i,n,i):
        l[j]=0

print(ans)

