n,M=map(int,raw_input().split())
ans=[i for i in range(n+1)]

for m in range(M):
    i,j,k=map(int,raw_input().split())
    ans=ans[:i]+ans[k:j+1]+ans[i:k]+ans[j+1:]
print " ".join(map(str,ans[1:]))