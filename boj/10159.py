import sys
import Queue
data= Queue.deque()
for line in sys.stdin:
    data+=line.split()
 
n=int(data.popleft())
m=int(data.popleft())
  
G=[[]for i in range(n+10)]
matrix=[[0]*(n+1) for i in range(n+1)]
  
for i in range(m):
    a,b=int(data.popleft()),int(data.popleft())
    G[a]+=[b]
#print G
   
   
def bfs(start):
    global G
    check=[False]*(n+10)
  
    q=Queue.deque()
    q+=[start]
    check[start]=True
    
    while len(q)>0: 
        cur=q.pop()
        #print start,cur
        for post in G[cur]:
            if check[post]:continue
            q+=[post]
            check[post]=True
            
            matrix[start][post]=1
            matrix[post][start]=1

   
ans=0
 
for i in range(1,n+1):
    bfs(i)

      
for i in range(1,n+1):
    if sum(matrix[i]) == n-1:
        ans+=1  
    print n-1-sum(matrix[i])
