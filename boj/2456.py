m=[0]*3
v=[[0]*4 for i in range(4)]
for _ in range(int(input())):
    a=list(map(int,input().split()))
    for i in range(3):
        m[i]+=a[i]
        v[a[i]][i+1]+=1


a,b,c=m
if a!=b and b!=c and c!=a:
    print(m.index(max(m))+1,max(m))

elif v[3].count(max(v[3]))==1:
    print(v[3].index(max(v[3])),max(m))
elif v[2].count(max(v[2]))==1:
    print(v[2].index(max(v[2])),max(m))
else:
    print(0,max(m))







