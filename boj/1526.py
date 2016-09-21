l=[]
def f (n,c):
    global l
    if c==0:return
    l+=[n*10+7,n*10+4]
    f(n*10+7,c-1)
    f(n*10+4,c-1)
f(0,6)
l.sort()
ans=0
n=int(input())
for i in l:
    if i>n:break
    ans=i
print(ans)