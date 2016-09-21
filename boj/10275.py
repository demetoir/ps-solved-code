for t in  range(int(input())):
    n,a,b=map(int,input().split())
    a=max(a,b)
    print(n-bin(a)[::-1].index("1"))