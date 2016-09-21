seive=[False]*123456
seive[0]=True
seive[1]=True
prime=[]
for i in range(2,100001):
    if seive[i]:continue
    prime+=[i]
    for j in range(i*2,100001,i):
        seive[j]=True
for t in range(input()):
    n=input()


    for p in prime:
        if p>n:break
        if n%p>0:
            continue

        for i in range(1,100):
            d=p**i
            if n%d>0:
                print p,i-1
                break

