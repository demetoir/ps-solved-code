for T in range(input()):
    n,d=map(int,raw_input().split())
    ans=0
    for i in range(n):
        v,c,f=map(float,raw_input().split())
        #print v,c,f,v*(c/f),d
        if v*(c/f)>=d:ans+=1
    print ans