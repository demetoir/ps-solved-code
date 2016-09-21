from fractions import gcd
n=input()
l=list(map(int,raw_input().split()))
a=l[0]
l=l[1:]
for i in range(n-1):
    g=gcd(a,l[i])
    print str(a//g)+"/"+str(l[i]//g) 