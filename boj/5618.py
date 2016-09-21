from fractions import gcd
n=int(input())

if n==3:a,b,c=map(int,input().split())
else:a,b=map(int,input().split());c=a*b

n=gcd(a,gcd(b,c))

l=[]
for i in range(1,int(n**0.5)+1):
    if n%i==0:
        if i!=n//i:l+=[n//i]
        l+=[i]
l.sort()

for i in l:print(i)