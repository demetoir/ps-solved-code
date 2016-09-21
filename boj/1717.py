import  sys

n,m=map(int,sys.stdin.readline().split())
p=[i for i in range(n+1)]
r=[0]*(n+1)
def find(n):
    if n==p[n]:return n
    p[n]=find(p[n])
    return p[n]
def merge(A,B):
    if A!=B:
        if r[A]>r[B]:p[B]=A
        elif r[A]<r[B]:p[A]=B
        else:p[A]=B;r[A]+=1
for i in range(m):
    c,a,b=map(int,sys.stdin.readline().split())
    A=find(a)
    B=find(b)
    if c==0:merge(A,B)
    else:
        if A==B:print("YES")
        else:print("NO")