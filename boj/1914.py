def f(k,a,b):
    if k==0:return
    mid=6-a-b
    f(k-1,a,mid)
    print a,b
    f(k-1,mid,b)
n=input()
print 2**n-1
if n<=20:
    f(n,1,3)