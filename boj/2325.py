__author__ = 'SLAVE2'
n,m=map(int,raw_input().split())
G=[[]for i in range(n+1)]
for i in range(m):
    a,b,c=map(int,raw_input().split())
    G[a]+=[(b,c)]
    G[b]+=[(a,c)]

DAG=[[]for i in range(n+1)]
import Queue

def dijkstra2():
    distance=[987654321]*(n+1)
    distance[1]=0
    Q=Queue.Queue()
    Q.put(1)
    while not Q.empty():
        cur=Q.get()
        val=distance[cur]
        for next,cost in G[cur]:
            if distance[next]>val +cost:
                distance[next]=val+cost
                Q.put(next)
    return distance[n]

def dijkstra1():
    global DAG
    distance=[987654321]*(n+1)
    distance[1]=0
    #back=[[]for i in range(n+1)]
    Q=Queue.Queue()
    Q.put(1)
    while not Q.empty():
        cur=Q.get()
        val=distance[cur]
        for next,cost in G[cur]:
            if distance[next]==val+cost:
                DAG[next]+=[cur]
            if distance[next]>val +cost:
                distance[next]=val+cost
                DAG[next]=[cur]
                Q.put(next)

    return distance[n]

distance=dijkstra1()

candidate=[]

check=[[0]*(n+1)for i in range(n+1)]

def dfs(cur):
    #print cur
    global  candidate
    if cur == 1:
        return
    val=0
    for next in DAG[cur]:
        if check[next][cur]==0:
            check[next][cur]=1
            return dfs(next)
        else:
            val=next
    candidate+=[(val,cur)]
    check[val][cur]=2
    return dfs(val)

dfs(n)
#print "#"
dfs(n)
#print "#"
ans=0
for i,j in candidate:
    if check[i][j]==2:

        A=[]
        B=[]
        for next,cost in G[i]:
            if next == j :
                Acost=cost
                continue
            A+=[(next,cost)]

        for next,cost in G[j]:
            if next == i:
                Bcost=cost
                continue
            B+=[(next,cost)]
        G[i]=A
        G[j]=B
        val=dijkstra2()
        ans=max(val,ans)
        G[i]+=[(j,Acost)]
        G[j]+=[(i,Bcost)]

#print "ans:"
print ans


