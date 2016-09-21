from math import factorial as f

def nCr(n,r):return f(n)//(f(r)*f(n-r))

def r(k):
    global n,cache
    ret=cache[k]
    if ret>-1:
       return ret
    ret=(n+1)**(k+1)-1
    for i in range(2,k+2):
        ret-=r(k-i+1)*nCr(k+1,i)
    ret=ret//(k+1)
    cache[k]=ret
    return ret

n,k=map(int,input().split())
cache=[n]+[-1]*50
print(r(k)%1000000007)





