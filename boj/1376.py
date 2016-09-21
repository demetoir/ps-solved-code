import sys
import Queue
    
n,m=map(int,sys.stdin.readline().split())

G=[{} for i in range(n+1)]
index=0
for i in range(m):    
    a,b=map(int,sys.stdin.readline().split())
    G[a][b]=1
    G[b][a]=1

pqlist=[Queue.PriorityQueue() for i in range(n+1)]
check=[False]*(n+1)
vn=[0]*(n+1)
downdeq=[Queue.deque() for i in range(n+1)]
updeq=[Queue.deque() for i in range(n+1)]
downn=[0]*(n+1)
upn=[0]*(n+1)
newG=[[]for i in range(n+1)]

for i in range(1,n+1):
    nextvertex = list(G[i])
    nextvertex.sort()
    for j in nextvertex:        
        newG[i]+=[j]
        vn[i]+=1
        pqlist[i].put(j)
G=newG

for i in range(1,n+1):   
    a=len(G[i])
    for j in range(a//2+ a%2):
        downdeq[i]+=[G[i][j]]
    for j in range(a//2 + a%2 ,a):
        updeq[i]+=[G[i][j]]
    downn[i]=a//2 + a%2
    upn[i]=a//2

def syn(number):
 
    while len(updeq[number])>0:
        val=updeq[number][0]
        if check[val]==False:break
        updeq[number].popleft()

    while len(downdeq[number]) >0:
        val=downdeq[number][len(downdeq[number])-1]
        if  check[val]==False:break
        downdeq[number].pop()
        

def f():
    ansL=[]
    stack=[1]
    while len(stack)>0:

        cur = stack[len(stack)-1]

        if check[cur]== False:
            check[cur]=True
            ansL+=[cur]

            for next in G[cur]:
                
                vn[next]-=1

                mid=downdeq[next][len(downdeq[next])-1]
                if cur<mid:
                    downn[next]-=1
                elif cur>mid:
                    upn[next]-=1
                else:
                    downdeq[next].pop()
                    downn[next]-=1
                syn(next)
                if downn[next] == upn[next] or downn[next] == upn[next]+1 :continue

                if downn[next] < upn[next]:
                    downdeq[next]+=[updeq[next].popleft()]
                    downn[next]+=1
                    upn[next]-=1
                elif downn[next] > upn[next]:
                    updeq[next].appendleft(downdeq[next].pop())
                    downn[next]-=1
                    upn[next]+=1
                syn(next)

        if vn[cur]==0:
            stack.pop()
        else:            
            if vn[cur]%2 == 0:
                next=0
                for next in downdeq[cur]: 
                    if check[next] == False:break
                stack+=[next]
            else:
                next=downdeq[cur][len(downdeq[cur])-1]
                stack+=[next]

    print " ".join(str(i) for i in ansL)

f()