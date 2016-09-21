d1,d2=map(int,input().split())
import fractions
G=fractions.gcd
l=[]
for down in range(d1,d2+1):
    for up in range(1,down+1):
        g=G(down,up)
        l+=[(down//g,up//g)]

print(len(set(l)))

###################################
d1,d2=map(int,input().split())
s={}
for d in range(d1,d2+1):
    for u in range(1,d+1):
        if u/d not in s:d[u/d]=0
print(len(s))
