n=int(input())
l=[987654321]*(10**6+10)
l[n]=0
import queue
q=queue.deque()
q.append(n)

while len(q)>0:
    a=q.popleft()

    if a==1:break
    if a%3==0 and l[a//3]>l[a]+1:
        l[a//3]=l[a]+1
        q.append(a//3)
    if a%2==0  and l[a//2]>l[a]+1:
        l[a//2]=l[a]+1
        q.append(a//2)
    if  l[a-1]>l[a]+1:
        l[a-1]=l[a]+1
        q.append(a-1)
print(l[1])

