import sys
import Queue
q=Queue.deque()
m,n,h =map(int,sys.stdin.readline().split())
lll=[]

for j in range(h):
    ll =[]
    for i in range(n):
        ll+=[list(map(int,sys.stdin.readline().split()))]
    lll+=[ll]
  
ans=0        
def bfs():
    q=Queue.deque()
    for k in range(h):
        for j in range(n):
            for i in range(m):
                if lll[k][j][i]==1:    
                    q+=[(i,j,k)]
    delta=[(1,0,0,),(0,1,0),(0,0,1),(-1,0,0),(0,-1,0),(0,0,-1)]
    while len(q)>0:
        x,y,z=q.popleft()
        for dx,dy,dz in delta:
            nx,ny,nz=dx+x,dy+y,dz+z
            if nx<0 or nx>=m:continue
            if ny<0 or ny>=n:continue
            if nz<0 or nz>=h:continue
           
            if lll[nz][ny][nx]==0 or lll[nz][ny][nx]>lll[z][y][x]+1:
                q+=[(nx,ny,nz)]
                lll[nz][ny][nx]=lll[z][y][x]+1
                
ans=0            
bfs()

for k in range(h):
    for j in range(n):
        for i in range(m):
            if lll[k][j][i]==0:
                print -1
                exit()
            ans=max(lll[k][j][i],ans)
"""            
for ll in lll:
    for l in ll:
        print l
"""
if ans ==1:
    print 0
else:
    print ans-1
        
    
    
    
    
    
    
    

