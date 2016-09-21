N,K=map(int,input().split())
ans=0
for i in range(100):
    b=bin(N)[2:]
    p=len(b)-b.rindex("1")-1
    if bin(N).count("1")<=K:break
    N+=2**p
    ans+=2**p
print(ans)


