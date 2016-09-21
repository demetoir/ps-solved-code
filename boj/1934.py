def gcd(m,n):
    while n != 0:
        t = m%n
        (m,n) = (n,t)
    return abs(m)
for i in range(int(input())):
    a,b=map(int,input().split())
    print(a*b//gcd(a,b))