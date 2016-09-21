while 1:
    n=int(input())-1
    if n==-1:break
    if n==0:print("{ }");continue
    a=1
    l=[]
    while n>0:
        if n%2==1:l+=[str(a)]
        n=n//2;a*=3
    print("{ "+", ".join(l)+" }")