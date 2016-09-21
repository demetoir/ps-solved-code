from fractions import gcd
x,y=map(int,input().split())
c=gcd(x,y)
print((x//c+y//c-1)*c)