while 1:
    a,b,c=map(int,raw_input().split())
    if (a,b,c)==(0,0,0):break
    if a+c==2*b:
        print "AP",c+b-a
    elif a*c==b*b:
        print "GP",c*(b/a)
