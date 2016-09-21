from fractions import gcd
t=lambda:map(int,input().split())
a,b=t();c,d=t();a=a*d+b*c;b=b*d;g=gcd(a,b);print(a//g,b//g)