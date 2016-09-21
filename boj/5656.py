T=0
while 1:
    T+=1
    a,c,b=raw_input().split()
    a,b=int(a),int(b)
    if c=="E":break
    if c==">":ans=(a>b)
    elif c==">=":ans=(a>=b)
    elif c=="<":ans=(a<b)
    elif c=="<=":ans=(a<=b)
    elif c=="==":ans=(a==b)
    elif c=="!=":ans=(a!=b)
    print "Case %d:"%T,str(ans).lower()
