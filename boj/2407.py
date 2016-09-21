"""
from math import factorial as f
n,r=map(int,input().split())
print(int(f(n)/f(r)/f(n-r)))
"""

m,n=map(int,input().split())
p=1
for i in range(m-min(n,m-n)+1,m+1):p*=i
for i in range(1,min(n,m-n)+1):p=p//i
print(p)