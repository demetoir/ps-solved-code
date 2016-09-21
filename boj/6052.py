n=0
while 1:
    n+=1
    data=raw_input()
    if data=="0":
        break
    r,w,l=map(int,data.split())
    if (2*r)**2 >= w*w + l*l:
        print "Pizza",n, "fits on the table."
    else:
        print "Pizza",n,"does not fit on the table."