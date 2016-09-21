f=lambda k,n:0 if k==0 else k//n+f(k//n,n)
n,m=map(int,input().split())
print(min(f(n,2)-f(m,2)-f(n-m,2),f(n,5)-f(m,5)-f(n-m,5)))