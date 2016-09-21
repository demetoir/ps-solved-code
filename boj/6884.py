T=int(input())
#import time
#tstart=time.time()
for t in range(T):
    start,end=87654321,987654321
    l=map(int,raw_input().split())
    for i in range(1,len(l)):
        s=l[i]
        for j in range(i+1,len(l)):
            if j-i+1>=end-start+1:
                break
            s+=l[j]
            isprime=True
            if s<2:
                isprime=False
            for k in range(2,s):
                if k*k>s:break
                if s%k==0:
                    isprime=False
                    break
            if isprime:
                if j-i+1 < end-start+1:
                    start=i
                    end=j
                break
    #print start,end
    if (start,end)==(87654321,987654321):
        print "This sequence is anti-primed."
    else:
        print "Shortest primed subsequence is length "+str(end-start+1)+": "+" ".join(str(c)for c  in l[start:end+1])
#print time.time()-tstart