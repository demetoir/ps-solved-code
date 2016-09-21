import itertools
b=[0]*10
n=[]
for i in range(int(input())):
    a=raw_input()
    n+=[ord(a[0])-65]
    for j in range(len(a)):
        b[ord(a[j])-65]+=10**(len(a)-j-1)

m=0
for p in itertools.permutations(range(10)):
    total=0
    for  i in range(10):
        total+=p[i]*b[i]
        if p[i]==0 and i in n:
            total=0
            break
    if m<total:m=total
print(m)
