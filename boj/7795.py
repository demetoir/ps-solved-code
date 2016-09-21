for t in range(int(input())):
    a,b=map(int,input().split())
    A=list(map(int,input().split()))
    B=list(map(int,input().split()))
    A.sort()
    B.sort()
    i,j=0,0
    ans=0
    while 1:
        if i==a or j==b:break
        if A[i]>B[j]:
            j+=1
        else:
            i+=1
            ans+=j
    if i!=a:
        ans+=j*(a-i)

    print(ans)
