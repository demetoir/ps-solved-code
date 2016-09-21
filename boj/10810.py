n,m=map(int,raw_input().split())
l=[0]*(n+1)
for M in range(m):
    i,j,k=map(int,raw_input().split())
    for a in range(i,j+1):
        l[a]=k
print " ".join(map(str,l[1:]))