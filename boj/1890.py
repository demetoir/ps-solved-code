n=int(raw_input())
board=[]
memo=[[0]*n for i in range(n)]

for i in range(n):
    board+=[list(map(int,raw_input().split()))]
memo[0][0]=1

for i in range(n):
    for j in range(n):
        cur=board[i][j]
        if cur==0:continue        
        if cur+i <n:
            memo[cur+i][j]+=memo[i][j]
        if cur +j<n:
            memo[i][j+cur]+=memo[i][j]
            
print memo[n-1][n-1]
#for i in range(n):print memo[i]
    
    
    