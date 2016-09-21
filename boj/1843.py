n=int(input())

s=[1]*(n+1)
pn=[]
for i in range(2,n+1):
    if s[i]==0:continue
    pn+=[i]
    for j in range(i+i,n+1,i):s[j]=0


dl=[]
l=[0]*(n+1)
for i in range(1,n+1):
    if n%i==0:
        dl+=[i]
        l[i]=i


A=0
for i in range(1,n+1):
    if i+i+1>n:break
    A+=n-2*i



B=0
for i in range(len(dl)):
    for j in range(i,len(dl)):
        x=dl[i]
        y=dl[j]
        z=x+y

        if z>n:continue
        if l[z]>0:
            B+=1

C=0

for i in range(len(pn)):
    x=2
    y=pn[i]
    z=x+y
    #print(x,y,z)
    if z>n:break
    if s[z]>0:
        C+=1

print(A)
print(B)
print(C)






