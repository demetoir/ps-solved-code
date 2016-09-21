N,K=map(int,raw_input().split())


l=[]
for i in range(N+1):
    a,b=map(int,raw_input().split())
    l+=[[a,b]]
#for i in l:print i

new=[[-1,-1,-1]for i in range(K+2)]
old=[[-1,-1,-1]for i in range(K+2)]
old[0][2]=l[0][0]+l[0][1]
old[1][0]=l[0][0]
old[1][1]=l[0][1]
ans=0
for n in range(1,N):
    new=[[-1,-1,-1]for i in range(K+2)]

    for k in range(K+1):
        if old[k][0]>-1:
            new[k+1][0]=max(new[k+1][2],old[k][0]+l[n][0])
            new[k][2]=max(new[k][2],old[k][0] +l[n][0]+l[n][1])
            #ans=max(new[k+1][0],new[k][2])
            
        if old[k][1]>-1:
            new[k+1][1]=max(new[k+1][1],old[k][1]+l[n][1])
            new[k][2]=max(new[k][2],old[k][1] +l[n][0]+l[n][1])
            #ans=max(new[k+1][1],new[k][2])
            
        if old[k][2]>-1:
            new[k+1][0]=max(new[k+1][0],old[k][2]+l[n][0])
            new[k+1][1]=max(new[k+1][1],old[k][2]+l[n][1])
            new[k][2]=max(new[k][2],old[k][2] +l[n][0]+l[n][1])
            #ans=max(new[k+1][0]+new[k+1][1],new[k][2])

    old=new[:]    
#print ans   
print max(new[K]) 
    
    
    
    
    
    
    
    
    
    
    
    
    
    
