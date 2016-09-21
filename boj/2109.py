import sys
import Queue
data = Queue.deque()

for line in sys.stdin:
    data += list(map(int, line.split()))


scan = data.popleft
Q = Queue.PriorityQueue()


n = scan()
day = [[] for i in range(12345)]
for i in range(n):
    p, d = scan(), scan()
    
    day[d] += [p]
ans = 0

for i in range(10000, 0, -1):
    for p in day[i]:
        Q.put(-p) 
    if Q.empty():continue
    pay = -Q.get()
   
    ans += pay
print ans
    
    
    
    
    
    
    
    
    
    
