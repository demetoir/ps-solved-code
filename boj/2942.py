from fractions import gcd
r,g=map(int,input().split())
d=gcd(r,g)
l=[]
f=int(d**0.5)
for i in range(1,f+1):
    if d%i==0:l+=[i,d//i]
l=set(l)
for i in l:print(i,r//i,g//i)
