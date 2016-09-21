n,m=map(int,raw_input().split())
l=[i for i in range(n+1)]
for i in range(m):
    a,b=map(int,raw_input().split())
    l[a],l[b]=l[b],l[a]
print " ".join(map(str,l[1:]))