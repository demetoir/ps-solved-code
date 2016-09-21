n,w,h=map(int,raw_input().split())
l=w*w+h*h
for i in range(n):
    k=input()
    if l>=k*k:
        print "DA"
    else:
        print "NE"
