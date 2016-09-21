a,b,n=map(int,raw_input().split())
 
def f(x):
    ret=0
    for k in range(2,x):
        d=x
        for i in range(n):
            d=d//k
            if d==0:break
        e=x//k
        ret+=e-d-1
    return ret
 
print f(a+b)-f(a-1)