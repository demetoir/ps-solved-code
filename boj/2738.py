n,m=map(int,raw_input().split())

a=[]
for i in range(n):
    a+=[list(map(int,raw_input().split()))]
b=[]
for i in range(n):
    b+=[list(map(int,raw_input().split()))]
    
for i in range(n):
    for j in range(m):
        a[i][j]+=b[i][j]
for i in range(n):
    print " ".join(str(i) for i in a[i])