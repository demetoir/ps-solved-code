l,r=map(int,raw_input().split())
a,b=str(l),str(r)
ans=123132
c=""
def f(x,n):

    global ans
    if n==len(x) :
        if int(x)<=r and l<=int(x):
            ret=0
            for i in x:
                if i=="8":ret+=1
            ans = min(ans,ret)
        return

    f(x,n+1)
    f(x[:n]+c+x[n+1:],n+1)

if len(a)<len(b):
    a="0"*(len(a)-len(b))+a
elif len(a)>len(b):
    b="0"*(len(b)-len(a))+b
c="9"
f(a,0)
c="7"
f(b,0)
print ans