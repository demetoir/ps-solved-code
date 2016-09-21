for t in range(int(input())):
    p,m=map(int,input().split())
    s=[0]*(m+1)
    a=0
    for i in range(p):
        j=int(input())
        if s[j]==0:s[j]=1
        else:a+=1
    print(a)
