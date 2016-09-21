n,k=map(int,raw_input().split())

d={}
d[n]=0

import Queue

q=Queue.Queue()
q.put(n)
while not q.empty():
    cur=q.get()
    if cur<0 or cur>100000:continue
    if cur==k:
        print d[cur]
        break
    if cur+1 not in d :
        q.put(cur+1)
        d[cur+1]=d[cur]+1
    if cur-1 not in d:
        q.put(cur-1)
        d[cur-1]=d[cur]+1
    if cur*2 not in d:
        q.put(cur*2)
        d[cur*2]=d[cur]+1
        