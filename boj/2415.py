n=int(raw_input())

from decimal import Decimal

l=[]
for i in range(n):
    x,y=map(int,raw_input().split())
    l+=[(x,y)]
l.sort()

A=[]
for x,y in l:
    for a,b in l:
        if x<=a and y<=b:              
            V=(x-a,y-b)
            VV=(b-y,x-a)
            dx=b-y
            dy=x-a
            T=y*dx-x*dy  
            A+=[(V,T,(x,y))]
        
A.sort()    
V,T,(x,y)=A[0]
old=(V,T)
ans=0

for i in range(1,len(A)):
    V,T,(a,b)=A[i]
    cur=(V,T)

    if cur==old :
        vx,vy=V
        val=(vx**2+vy**2)*((x-a)**2+(y-b)**2)
        ans=max(ans,val)
    else:
        x,y=a,b
        old=cur

ans=Decimal(ans)
ans=ans.sqrt()
print int(ans)
    
    