import sys
for T in range(int(input())):
    m,n,x,y=map(int,sys.stdin.readline().split())
    while 1:
        if x<y:x+=m
        elif x>y:y+=n
        elif x==y:break
        elif x>m*n:x=-1;break
    print(x)