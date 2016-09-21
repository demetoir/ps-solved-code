for T in range(input()):
    h,w,n=map(int,raw_input().split())
    ans=str((n-1)%h+1)
    if (n-1)//h+1<10:
        ans+="0"+str((n-1)//h+1)
    else:
        ans+=str((n-1)//h+1)
    print ans