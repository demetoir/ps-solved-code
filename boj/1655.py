import sys
import Queue
down = Queue.PriorityQueue()
up = Queue.PriorityQueue()
for i in range(1,input()+1):
    cur = int(sys.stdin.readline())
    down.put(-cur)
    if up.qsize()>0:
        b= up.queue[0]
        if cur >=b:
            down.get()
            down.put(-up.get())
            up.put(cur)
    if down.qsize()>i//2+i%2:
        up.put(-down.get())

    print -down.queue[0]


