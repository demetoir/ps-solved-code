N=1120;K=15
seive=[1]*(N+1)
pl=[]
for i in range(2,N+1):
    if seive[i]==0:continue
    pl+=[i]
    for j in range(2*i,N+1,i):seive[j]=0
memo=[[0 for j in range(N+1)]for j in range(K)]
memo[0][0]=1
for p in pl:
    for k in range(K-1,0,-1):
        for n in range(p,N+1):memo[k][n]+=memo[k-1][n-p]
for T in range(int(input())):
    n,k=map(int,input().split())
    print(memo[k][n])
