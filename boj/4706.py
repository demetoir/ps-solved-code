while 1:
    a,b=map(float,raw_input().split())
    if (a,b)==(0,0):break
    x=(1-(b**2/a**2))**0.5
    print "%.3f"%x