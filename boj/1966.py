for T in range(int(input())):
    n,m=map(int,input().split())
    a= list(map(int,input().split()))
    b=[[i,a[i]]for i in range(n)]
    a.sort()
    a.reverse()
    i=0
    cnt=1

    for number in a:
        while 1:
            if b[i][1]==number:
                break
            i=(i+1)%n
        if b[i][0]==m:
            print(cnt)
            break
        cnt+=1
        i=(i+1)%n

