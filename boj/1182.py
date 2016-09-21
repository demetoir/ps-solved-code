N,S=map(int,input().split())
l=list(map(int,input().split()))
c=0
if S==0:c=-1
def f(n,s):
    global c
    if n==N:
        if S==s:c+=1
        return
    f(n+1,s+l[n])
    f(n+1,s)
f(0,0)
print(c)

