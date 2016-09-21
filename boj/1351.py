n,p,q=map(int,input().split())
d={0:1}
def f(n):
    if n in d:return d[n]
    d[n]=f(n//p)+f(n//q)
    return d[n]
print(f(n))
