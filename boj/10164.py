n,m,k=map(int,raw_input().split())

memo=[[0]*15 for i in range(15)]
memo[0]=[1]*15
for i in range(15):
    memo[i][0]=1
for i in range(1,15):
    for j in range(1,15):
        memo[i][j]=memo[i-1][j]+memo[i][j-1]
#for line in memo:print line

k-=1
a,b=k//m,k%m


if k==-1:
    print memo[n-1][m-1]
else:

    print memo[a][b]*memo[n-a-1][m-b-1]