N,V,M=map(int,input().split())
l=list(map(int,input().split()))
memo=[[0]*1001 for i in range(2)]
memo[1][V]=1
for j in range(N):
    memo[j%2]=[0]*1001
    for i in range(M+1):
        t=memo[(j+1)%2][i]
        if i+l[j]<=M and 0<=l[j]+i:memo[j%2][i+l[j]]+=t
        if i-l[j]<=M and 0<=i-l[j]:memo[j%2][i-l[j]]+=t
ans=-1
for i in range(M,-1,-1):
    if memo[(N+1)%2][i]>0:ans=i;break
print(ans)