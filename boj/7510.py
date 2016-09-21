for T in range(input()):
    a,b,c=map(int,raw_input().split())
    a,b,c=a*a,b*b,c*c
    A=max(a,b,c)
    print "Scenario #%d:"%(T+1)
    if sum([a,b,c])-A==A:print "yes"
    else:print "no"
    print 
