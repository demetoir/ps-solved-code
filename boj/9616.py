import sys
for j in range(1,10000+1):
    for k in range(1,10000+1):
        m,n=j,k
        #m,n=map(int,sys.stdin.readline().split())
        if (m,n)==(0,0):break


        if n>m: n,m=m,n
        x = (n - 1) // 2
        v = x*(x + 1)*(2 * x + 1) // 6
        r = -4 * v*(n + m - 1) + (x + 1) * (2 * x*x*(x + 1) + x*(n*m - n - m) + n*m);

        a=0
        for i in range(1,min(m,n)+1,2):a+=i*(n-i+1)*(m-i+1)
        if a!=int(r):
            print(m,n,a,r)
            exit()




