a,b=map(int,input().split())
n=10001
s=[1]*n
sl=[]
for i in range(2,n):
    if s[i]==0:continue
    sl+=[i]
    for j in range(i+i,n,i):s[j]=0
P=[]
for i in range(1,n):s=str(i);P+=[int(s+s[::-1]),int(s[:-1]+s[::-1])]
P.sort()
ans=[]
for p in P:
    f=False
    for number in sl:
        if number**2>p:break
        if p%number==0:f=True;break
    if f==False and (p>=a and p<=b):print(p)
print(-1)

