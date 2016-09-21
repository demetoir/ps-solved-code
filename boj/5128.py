for T in range(input()):
    a,b=raw_input().split()
    ans=[]
    for i in range(len(a)):
        x,y=ord(a[i]),ord(b[i])
        if y>=x:ans+=[y-x]
        else:ans+=[y-x+26]
    print "Distances:"," ".join(map(str,ans))