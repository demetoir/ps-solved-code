a,b,c=1,0,0
for i in raw_input():
    if i=="A":
        a,b=b,a
    elif i=="B":
        b,c=c,b
    else:
        a,c=c,a

if a==1:
    print 1
elif b==1:
    print 2
else:
    print 3