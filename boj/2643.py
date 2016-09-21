memo=[[0]*1000 for i in range(1000)]
for i in range(int(input())):
    a,b=map(int,input().split())
    if b>a:a,b=b,a
    memo[a][b]=1
for y in range(1,1000):
    for x in range(1,1000):
        memo[y][x]+=max(memo[y-1][x],memo[y][x-1],memo[y-1][x-1])
print(memo[999][999])