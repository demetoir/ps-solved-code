for T in range(input()):
    
    l=list(map(int,raw_input().split()))
    l.sort()
    l=l[1:4]
    if l[2]-l[0]>=4:print "KIN"
    else:print sum(l)