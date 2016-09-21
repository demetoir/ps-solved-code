n,k=map(int,raw_input().split())
l=map(int,raw_input().split())

cur=sum(l[:k])
ans=cur

for i in range(k,n):
    cur+=l[i]-l[i-k]
    ans=max(ans,cur)
print ans

