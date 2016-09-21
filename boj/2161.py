n=input()
import Queue
q=Queue.deque()
l=[]
for i in range(1,n+1):
    q+=[i]
while len(q)>0:
    l+=[q.popleft()]
    if len(q)==0:break
    q+=[q.popleft()]
print " ".join(str(i) for i in l)