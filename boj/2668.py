n=input()
l=[-1]
for i in range(n):
    l+=[input()]
check=[False]*(n+1)
visited=[False]*n
ansl=[]
def dfs(cur):
    global ansl
    #print cur
    if cur==val:return True
    if check[cur]:return False

    next=l[cur]
    if next>=n:return False
    check[cur]=True
    if dfs(next):
        ansl+=[cur]
        #print cur

        return True
    else:
        check[cur]=False
        return False

ansl=[]
for i in range(1,n+1):
    #print "#",i
    if check[i]:continue
    val=i
    check[i]=True
    if dfs(l[i]):
        ansl+=[i]
    #print "#",i
ansl.sort()
print len(ansl)
for i in ansl:
    print i
