a=[0]*1001
b=[0]*1001
for i in range(3):
    x,y=map(int,input().split())
    a[x]+=1
    b[y]+=1
print(a.index(1),b.index(1))