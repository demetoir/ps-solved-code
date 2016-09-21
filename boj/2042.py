import  sys
N,M,k,a,b,c=0,0,0,0,0,0
heap=[0]*4000000
l=[0]*1000000
ans=0
n=0

def sum(index,t):
    global heap
    x=index*t
    y=x+t-1
    if b<=x and y<=c:return heap[index]
    if y<b or c<x:return 0
    return sum(index*2,t//2)+sum(index*2+1,t//2)

def update(index,val):
    global heap
    heap[index]+=val
    if index==1:return
    return update(index//2,val)

def makeheap():
    global N,n,heap
    for i in range(n,n+N):heap[i]=l[i-n]
    for i in range(n-1,-1,-1):heap[i]=heap[i*2]+heap[i*2+1]


N,M,k=map(int,input().split())
n=1
for i in range(100):
    n*=2
    if n>=N:break

for i in range(N):l[i]=int(sys.stdin.readline())

makeheap()
for i in range(M+k):
    a,b,c=map(int,sys.stdin.readline().split())
    if a==1:
        update(b+n-1,c-l[b-1])
        l[b-1]=c
    else:
        b+=n-1
        c+=n-1
        print(sum(1,n))
