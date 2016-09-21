import sys
import Queue
 
 
n,k=map(int,raw_input().split())
l=[0]
old=int(raw_input())
 
 
pq=Queue.PriorityQueue()
for i in range(1,n):
    val=int(sys.stdin.readline())
    l+=[val-old]
    old=val
    pq.put((l[i],i))
 
 
check=[False]*(n+1)
L=[i-1 for i in range(n+1)] 
R=[i+1 for i in range(n+1)]
L[1]=0
R[n-1]=0
 
ans=0 
i=0
 
  
while i<k:
    #print pq.queue
    #print i
    val,index=pq.get()
    if check[index]==True:
        continue
     
     
    #print i,val,index
     
 
    left=L[index]
    right=R[index]
    p=0
    if left :
        check[left]=True
        p+=l[left]
         
    if right :
        check[right]=True    
        p+=l[right]
    ans+=val
     
    l[index]=p-l[index]
     
    if left and right :
        pq.put((l[index],index))
         
        L[index]=L[left]
        R[index]=R[right]
    else: 
        index=0
         
    if R[right] :    
        L[R[right]]=index
         
    if L[left] :
        R[L[left]]=index    
    i+=1
print ans
 