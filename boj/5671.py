while 1:
    try:n,m=map(int,raw_input().split())
    except:break
    ans=0
    for i in range(n,m+1):
        a=[]
        for c in str(i):
            a+=[c]
        if len(str(i))==len(set(a)):
            ans+=1
    print(ans)
