n=int(input())
memo=[0]*(n+1)
memo[0]=1
for t in range(n+1):
    a=2**t
    if a>n:break
    for i in range(a,n+1):
        memo[i]+=memo[i-a]
        memo[i]=memo[i]%1000000000
print(memo[n])


"""
    dp[0]=1;
    for(i=1;i<=n;i++){
        dp[i]=dp[i-1];
        if(i%2==0){
            dp[i]+=dp[i/2];
            dp[i]%=mod;
        }
    }
    printf("%d",dp[n]);
"""