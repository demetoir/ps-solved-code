n=int(input())
L=[]

ans=0
for i in range(n):
    l,h=map(int,raw_input().split())
    L+=[(l,h)]
ans=0
L.sort()
l,r=[],[]
cur=0

#print L
for i in range(n):
    a,b=L[i]
    if b>cur:
        #print a,b
        cur=b
        l+=[(a,b)]
#print l
cur=0
for i in range(n-1,-1,-1):
    a,b=L[i]
    if b>cur:
        #print a,b
        cur=b
        r+=[(a,b)]
#print r

for i in range(1,len(l)):
    a,b=l[i-1]
    c,d=l[i]
    ans+=(c-a)*b
#print ans


for i in range(len(r)-1,0,-1):
    a,b=r[i]
    c,d=r[i-1]
    ans+=(c-a)*d


a,b=l[len(l)-1]
c,d=r[len(r)-1]

ans+= (c+1-a)*b
print ans