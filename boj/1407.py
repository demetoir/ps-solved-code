def f(n,a,b):
    if a>b:return 0
    return n*(b-b//2-a+(a+1)//2) + f(2*n,(a+1)//2,b//2)
a,b=map(int,input().split())
print(f(1,a,b))

