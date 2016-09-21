d="6126444846"
def a(n):
    if n<1:return 1
    f=n//5
    return(int((int(d[n%10])*(1+5*(int(n//10!=0)))*a(f))*(2**(4*int(f!=0)-f%4))))%10

w=lambda n:(int((int(d[n%10])*(1+5*(int(n//10!=0)))*w(n//5))*(2**(4*int((n//5)!=0)-(n//5)%4))))%10 if n>0 else 1

##부르트
import time
start=time.time()
s=100
for i in range(1,s+1):
    t=a(i)
    b=w(i)
    print(i,t,b)
    if t!=b:
       print("no",i,t,b)
       input()
       break
print(time.time()-start)
print("comp")



def f(n):
    t,s=1,1
    for i in range(1,n+1):
        s=s*i
        d=i
        while d%5==0:t,d=t//2,d//5
        if d%10==0:d=10
        else:d=d%10
        if (t*d)%10==0:t=(t*d)//10
        else:t=(t*d)
    return t%10







