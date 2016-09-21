import Queue
import sys
INF=987654321000
check=0
G=0
memo=0
 
def f():
    global q
    q+=[(0,0,1)]
    ret=987654321000
    while len(q)>0:
        (cost,time,cur)=q.popleft()

        if cur==n:
            ret=min(time,ret)
            continue





        for c,d,next in G[cur]:
            if cost+c>m:continue

            if time+d<=ret :

                q+=[(cost+c,time+d,next)]
 
 
    return ret
 
 
 
 
for T in range(input()):
    n,m,k=map(int,sys.stdin.readline().split())
    G=[[]for i in range(n+1)]
    q=Queue.deque()
    memo=[INF]*(n+1)
    memo[1]=0
 
    for i in range(k):
        a,b,c,d=map(int,sys.stdin.readline().split())
        G[a]+=[(c,d,b)]
    ans=f()

 
    if ans >memo[n]:
        ans=memo[n]
 
    if ans==INF:
        print ("Poor KCM")
    else:
        print (ans)
        