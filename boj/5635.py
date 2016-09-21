l=[]
for i in range(int(input())):
    n,d,m,y=input().split()
    d=d.zfill(2)
    m=m.zfill(2)
    y=y.zfill(4)
    l+=[(y+m+d,n)]
l.sort(key=lambda a:a[0])
print(l[len(l)-1][1])
print(l[0][1])