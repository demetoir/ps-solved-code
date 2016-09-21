import Queue
q=Queue.PriorityQueue()

n=input()
l=[]
first=9876543210
for i in range(n):
    a,b=map(int,raw_input().split())
    l+=[(b,a)]
    first=min(b,first)
    q.put((b,a))

ans=0
last=-9876543210    
while not q.empty():
    
    end,start=q.get()
    #print end,start,last
    if last<=start:
        ans+=1
        last=end
        #print ans,start,end,last
print ans
    
    
    
