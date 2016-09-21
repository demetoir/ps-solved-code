m,n=map(int,input().split())

l=[input() for i in range(m)]
a=min(m,n)-1

for size in range(a,-1,-1):
    for i in range(size,m):
        for j in range(size,n):
            if l[i][j]==l[i-size][j-size] and l[i-size][j]==l[i][j-size] and l[i][j]==l[i][j-size]:
                print((size+1)**2)
                exit()
