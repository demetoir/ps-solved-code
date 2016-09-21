import sys
n,m=map(int,sys.stdin.readline().split())
X=[0]*(n+1)
Y=[0]*(n+1)
xsum,ysum=0,0
for i in range(m):
    a,b=map(int,sys.stdin.readline().split())
    X[a]+=1
    Y[b]+=1
    xsum+=a
    ysum+=b
a=987654321
ln,rn,lval,rval=0,m,0,xsum
for i in range(1,n+1):
    rval-=rn
    rn-=X[i]
    ln+=X[i-1]
    lval+=ln
    a=min(a,rval+lval)
ln,rn,lval,rval=0,m,0,ysum
b=987654321
for i in range(1,n+1):
    rval-=rn
    rn-=Y[i]
    ln+=Y[i-1]
    lval+=ln
    b=min(b,rval+lval)
print a+b