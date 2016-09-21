n,m=map(int,raw_input().split())
l=[]
for i in range(n):
    a,b=map(int,raw_input().split())
    l+=[(a,b)]
l.sort()
l+=[(0,0)]
ans=0
for i in range(1,len(l)):
    a,b=l[i-1]
    c,d=l[i]
    if b>d:
        ans+=b-d
print ans