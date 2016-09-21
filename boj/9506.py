while 1:
    a=input()
    if a==-1:break
    ans=[]
    for i in range(1,a):
        if a%i==0:
            ans+=[i]
    if sum(ans)==a:
        print a,"="," + ".join(map(str,ans))
    else:
        print a,"is NOT perfect."
    
    
    