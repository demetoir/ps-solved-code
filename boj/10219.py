for T in range(input()):

    n,m=map(int,raw_input().split())
    ans=987654321
    l=[]
    for i in range(n):
        s=raw_input()
        t=""
        for c in s:
           t=c+t
        l+=[t]
    for i in l:
        print i

