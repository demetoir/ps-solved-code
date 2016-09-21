import Queue
n,m,x=map(int,raw_input().split())
G1=[ [] for i in range(n+1) ]
G2=[ [] for i in range(n+1) ]

for i in range(m):
    a,b,c=map(int,raw_input().split())
    G1[a]+=[(b,c)]
    G2[b]+=[(a,c)]


q=Queue.Queue()
distance1=[-1]*(n+1)
distance2=[-1]*(n+1)
q.put(x)
distance1[x]=0
while not q.empty():
    cur=q.get()
    d=distance1[cur]

    for next,c in G1[cur]:
        if distance1[next]== -1 or distance1[next]>d+c:
            distance1[next]=d+c
            q.put(next)
q=Queue.Queue()
q.put(x)
distance2[x]=0
while not q.empty():
    cur=q.get()
    d=distance2[cur]

    for next,c in G2[cur]:
        if distance2[next] == -1 or distance2[next]>d+c:
            distance2[next] = d+c
            q.put(next)

#print distance1
#print distance2
ans = -1
for i in range(1,n+1):
    ans=max(ans,distance2[i]+distance1[i])
print ans



