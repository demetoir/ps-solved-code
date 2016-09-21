memo=[]
for test in range(int(input())):
    input()
    coins=list(map(int,input().split()))
    m=int(input())
    memo=[1]+[0]*m
    for coin in coins:
        for i in range(coin,m+1):
            if i>=coin:
                memo[i]+=memo[i-coin]
    print(memo[m])
