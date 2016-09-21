N=1000
next_number=[[7],[2,4],[1,3,5],[2,6],[1,5,7],[2,4,6,8],[3,5,9],[4,8,0],[5,7,9],[6,8]]
memo=[[1]*10]+[[0]*10 for i in range(N+1)]
for n in range(1,N+1):
    for i in range(10):
        for number in next_number[i]:
            memo[n][i]+=memo[n-1][number]
for T in range(int(input())):
    a=int(input())
    print(sum(memo[a-1])%1234567)