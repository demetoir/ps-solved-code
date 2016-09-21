from fractions import gcd
for _ in range(int(input())):
    l=list(map(int,input().split()))
    n,l=l[0],l[1:]
    s=0
    for i in range(n):
        for j in range(i+1,n):
            s+=gcd(l[i],l[j])
    print(s)