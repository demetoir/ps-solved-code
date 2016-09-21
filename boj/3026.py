for T in range(input()):
    a=input()
    b=int(str(a)[::-1])
    c=str(a+b)
    rc=c[::-1]
    if rc==c:
        print "YES"
    else:
        print "NO"