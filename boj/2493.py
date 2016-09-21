import sys
import Queue
 
  
stream=Queue.deque()
for line in sys.stdin:
    stream += map(int,line.split())

n=int(stream.popleft())
data=[0]
for i in range(n):
    data+=[int(stream.popleft())]
"""
n=int(input())
data=[0]+map(int,raw_input().split())
"""
 
l=[]
ans=[]
for i in range(1,n+1):
    number=data[i]
 
    while len(l)>0 :
        a=l.pop()
        if number<data[a]:
            l+=[a]
            break
 
 
    if len(l)==0:
        ans+=[0]
    else:
        a=l.pop()
        ans+=[a]
        l+=[a]
    l+=[i]
print " ".join(str(i) for i in ans)