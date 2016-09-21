for t in range(int(input())):
    s=0
    i=0

    n=int(input())
    l=[]
    for i in range(n//10):
        l+=list(map(int,input().split()))
    if n%10>0:
        l+=list(map(int,input().split()))


    while 1:
        cur = 0
        for i in range(i,n):
            cur+=l[i]
            if cur>s:break
            if cur ==s:cur=0
        if i==n-1 and cur==0:break
        s+=l[i]
        i+=1
    print(s)
"""
1
22
1 1 2 1 1 2 1 1 2 1
1 2 1 1 2 1 1 2 1 1
1 1
"""