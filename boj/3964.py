v=[1]*(10**6+1)
for i in range(2,10**3+1):
 if v[i]==1:
  for j in range(i*2,10**6,i):v[j]=0
p=[i for i in range(10**6) if v[i]==1]
p=p[2:]+[1000000]
r=lambda x,n:0 if n<x else r(x,n//x)+n//x
for i in range(int(input())):
 n,k=map(int,input().split());s={}
 while k>1:
  for i in p:
   if k%i==0:break
   if int(k**0.5)<i:i=k;break
  s[i]=1+s[i] if i in s else 1;k=k//i
 print(min([r(i,n)//s[i] for i in s]))