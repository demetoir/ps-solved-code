l=[]
def f (n,c):
    global l
    if c==0:return
    l+=[n*10+7,n*10+4]
    f(n*10+7,c-1)
    f(n*10+4,c-1)
f(0,9)
l.sort()
ans=0
a,b=map(int,input().split())
for i in l:
    if i>=a and i<=b:ans+=1
print(ans)