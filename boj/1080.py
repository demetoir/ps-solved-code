N,M=map(int,input().split())
A=[]
B=[]
for i in range(N):A+=[[int(j) for j in input()]]
for i in range(N):B+=[[int(j) for j in input()]]

def togle(x,y):
    pre=[(0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)]
    for a,b in pre:A[x+a][y+b]=(A[x+a][y+b]+1)%2

ans=0
for i in range(N-2):
    for j in range(M-2):
        if A[i][j]!=B[i][j]:
            togle(i,j)
            ans+=1

for i in range(N):
    for j in range(M):
        if A[i][j]!=B[i][j]:ans= -1
print(ans)
