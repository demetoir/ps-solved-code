def r(N,count):
    if N<4 :
        a[0]=min(a[0],count+N-1)
        return
    for i in range(2,60):
        f=int(pow(N,1/i))
        c=f+1
        if f==1:f=c
        if f**i>N*2:break
        if N-pow(f,i)>pow(c,i)-N:r(c,1+abs(-N+pow(c,i))+count)
        else:r(f,1+abs(N-pow(f,i))+count)
n=int(input())
a=[n]
r(n,0)
print(a[0])