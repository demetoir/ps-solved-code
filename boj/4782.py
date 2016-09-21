import sys
import fractions

while 1:
    b,n=map(int,sys.stdin.readline().split())
    if (b,n)==(0,0):
        break
    l=[]
    step=n//fractions.gcd(b,n)

    for m in range(step,n*2+1,step):
        if m==n:continue
        a=float((2*n*m-m*m))*b/float(n*n)
        if a<0:break
        if a-int(a)==0:
            #print"##",m,a
            l+=[(a/m,int(a),m)]

    #print l
    l.sort()
    ans=""
    for v,a,m in l:
        ans+=str(a)+"/"+str(m)+" "
    sys.stdout.write(ans+"\n")
