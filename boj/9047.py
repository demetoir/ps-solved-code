out=[]
a=[str(i)*4 for  i in range(1,10) ]
for t in range(1000,10000):
    n=str(t)
    if n in a: continue
    #n=input()

    cnt=0

    while n!="6174":
        cnt+=1
        t=[]
        for i in n:t+=[i]
        t.sort()
        hi=int("".join(t[::-1]))
        lo=int("".join(t))
        n=str(hi-lo).zfill(4)

    print(cnt)
    out+=[str(cnt)]
#print("\n".join(out))
