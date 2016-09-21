for T in range(input()):
    n=input()
    l=map(int,raw_input().split())
    m=input()
    memo=[0]*(m+1)
    memo[0]=1
    for a in l:
        for i in range(a,m+1):
            memo[i]+=memo[i-a]
    #print memo
    print memo[m]