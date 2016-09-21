for T in range(input()):
    n=input()
    data=list(map(int,raw_input().split()))
    ans=987654321
    for i in range(100):
        l,r=i,i
        for x in data:
           if x<i:l=min(x,l)
           elif x>i:r=max(x,r)
        ans=min((r-l)*2,ans)
    print ans
