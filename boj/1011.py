for i in range(int(input())):
    m,n=map(int,input().split());
    m=n-m;
    n=0;
    count=0;
    while m>0:
        n+=1;
        if m>n:
            m=m-2*n;
            count+=2;
        else:
            count+=1
            m=0
    print(count)