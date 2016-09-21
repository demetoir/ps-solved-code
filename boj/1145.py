from itertools import combinations as c
from fractions import gcd as g
t=lambda m,n:m*n//g(m,n)
a=list(map(int,input().split()))
l=[]
for(x,y,z)in c(range(5),3):l+=[t(a[x],t(a[y],a[z]))]
print(min(l))