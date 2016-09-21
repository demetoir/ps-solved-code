
seive=[1]*1000009
l=[1]*1000009
for i in range(2,1000000):
    for j in range(i+i,1000000,i):
        seive[j]+=i
    l[i]=abs(i-seive[i])


test=0
while 1:
    start,stop,bad=map(int,raw_input().split(" "))
    if  (start,stop,bad)==(0,0,0):
        break
    ans=0
    for i in range(start,stop+1):
        if l[i]<=bad:ans+=1
    test+=1

    print("Test "+str(test)+": "+str(ans))
