try:
    while 1:
        n,k=map(int,input().split());a=n
        while n//k>0:a+=n//k;n=n//k+n%k
        print(a)
except:pass
