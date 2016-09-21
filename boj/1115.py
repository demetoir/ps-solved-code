N=int(input())
l=list(map(int,input().split()))
check=[0]*N
ans=0
for i in range(N):
    if check[i]==1:continue
    cur=i
    while check[cur]==0:
        ans+=1
        check[cur]=1
        cur=l[cur]
    if i==0 and ans==N:break
    ans-=1
print(N-ans)