k=0
def f(n,level):
    global l,i,maxlevel
    r=n
    maxlevel=max(maxlevel,level)

    while 1:
        i+=1
        a=l[i]
        if a==")":return bool(r)
        if a=="(":
            a=f(1-n,level+1)
            if n==0:r=r|a
            else:r=r&a
            continue

        if a=="T":a=True
        else:a=False

        if n==0:r=r|a
        else:r=r&a

while 1:
    k+=1
    s=input()
    if s=="()":break
    l=[i for i in s]
    maxlevel=0
    i=0
    ans=f(1,1)

    i=0
    b=f(0,1)

    if maxlevel%2==0:ans=b
    print(str(k)+".",str(ans).lower())
