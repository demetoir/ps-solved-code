import sys

n,k=map(int,sys.stdin.readline().split())
jewelry=[]
bag=[]
for i in range(n):
    m,v=map(int,sys.stdin.readline().split())
    jewelry+=[(m,v)]
jewelry.sort()

for i in range(k):    
    bag+=[int(sys.stdin.readline())]
bag.sort()
    
import Queue
pq=Queue.PriorityQueue()
#print bag
#print jewelry
j=0
ans=0
for b in bag:
    while j<n:
        m,v=jewelry[j]
        if b<m:break
        pq.put(-v)
        j+=1
    if pq.qsize()==0:
        continue
    ans-=pq.get()
print ans

    
    
    
    
    
    

    