from fractions import gcd
for t in range(int(input())):
    a,b=map(int,input().split())
    print(int(a*b/gcd(a,b)),gcd(a,b))