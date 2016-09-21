n,m=map(int,raw_input().split())
l=[i for i in range(n+1)]
for i in range(m):
    a,b=map(int,raw_input().split())
    l=l[:a]+l[b:a-1:-1]+l[b+1:]
print " ".join(map(str,l[1:]))