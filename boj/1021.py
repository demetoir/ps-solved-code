m,n=map(int,input().split())
a=list(map(int,input().split()))
q=list(range(1,m+1))
ans=0
for i in a:
    i=q.index(i)
    if len(q)-i>=i:ans+=i
    else:ans+=len(q)-i
    q=q[i+1:]+q[:i]
print(ans)
#print(q)