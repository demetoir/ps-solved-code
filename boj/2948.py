import sys
import Queue
data=Queue.deque()
for line in sys.stdin:
    data+=map(int,line.split())   
    
m=[31,28,31,30,31,30,31,31,30,31,30,31]
d=["Thursday","Friday","Saturday","Sunday","Monday","Tuesday","Wednesday"]
b,a=data.popleft(),data.popleft()
x=sum(m[:a-1])+b-1
print d[x%7]
