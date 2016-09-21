n,m=map(int,raw_input().split())
pack=98765432100
one=98765432100
ans=98765432100
for i in range(m):
    a,b=map(int,raw_input().split())
    pack=min(pack,a)
    one=min(one,b)

for i in range(10000):
    j=n-i*6
    if j<0:j=0
    ans=min(ans,i*pack+j*one)

print ans