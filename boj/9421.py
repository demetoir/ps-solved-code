N=int(input())
n=1000001
l=[-1]*n
def next(i):
    n=0
    while i>0:n+=(i%10)**2;i=i//10
    return n
s=[1]*n
sl=[]
for i in range(2,n):
    if s[i]==0:continue
    sl+=[i]
    for j in range(i+i,n,i):s[j]=0

for i in sl:
    cur = i
    path=dict()
    while 1:
        if l[cur]>-1:cur=l[cur];break
        if cur in path:break
        path[cur]=0
        cur=next(cur)
    for number in path:l[number]=cur
    if N<i:break
    if cur==1:print(i)