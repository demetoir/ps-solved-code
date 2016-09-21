
n=5
Aboard=[[0]*n for i in range(n)]
Bboard=[[0]*n for i in range(n)]
block=[(2,2)]
for i in range(n):
    for j in range(n):
        Aboard[j][i]= j*5+i
        Bboard[j][i] = j*5 + i
        
D=[(1,1),(-1,1),(1,-1),(-1,-1)]

for j in range(n):
    for i in range(n):        
        if (j,i) in block:
            Bboard[j][i]=-1
            continue
        val=Aboard[j][i]    
        for dx,dy in [(1,1),(-1,-1)]:
            for k in range(1,n+1):
                a=i +dx*k 
                b=j + dy*k
                if (a,b) in block:break 
                if a<0 or n<=a:break
                if b<0 or n<=b:break                
                Aboard[b][a]=val
                

for j in range(n):
    for i in range(n):        
        if (j,i) in block:
            Aboard[j][i]=-1
            continue
        val=Bboard[j][i]    
        for dx,dy in [(1,-1),(-1,1)]:
            for k in range(1,n+1):
                a=i +dx*k 
                b=j + dy*k
                if (a,b) in block:break 
                if a<0 or n<=a:break
                if b<0 or n<=b:break                
                Bboard[b][a]=val                

    
A=[[] for i in range(n*n)]
B=[[] for i in range(n*n)]

for j in range(n):
    for i in range(n):
        if (i,j) in block:continue
        A[Aboard[j][i]]+=[Bboard[j][i]]
        B[Bboard[j][i]]+=[Aboard[j][i]]
        
check=[False]*(n*n)
BtoA=[-1]*(n*n)

def dfs(cur):
    if check[cur]:return False
    check[cur]=True
    
    for next in A[cur]:
        if BtoA[next]==-1 or dfs(BtoA[next]):
            BtoA[next]=cur
            return True
    return False
#for i in range(n*n):print i,A[i]
count=0
for i in range(n*n):
    if len(A[i])==0:continue
    check=[False]*(n*n)
    if dfs(i):
        count +=1

print count             
                
                 
                 
                
                