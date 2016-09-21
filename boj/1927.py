import queue
import  sys
pq=queue.PriorityQueue()
for i in range(int(input())):
    a=int(sys.stdin.readline())
    if a==0:
        if pq.empty():print(0)
        else:print(pq.get())
    else:
        pq.put(a)