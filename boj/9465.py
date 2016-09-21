import sys
for T in range(int(input())):
    n=int(sys.stdin.readline())
    up=list(map(int,sys.stdin.readline().split()))
    down=list(map(int,sys.stdin.readline().split()))
    a=0
    b=down[0]
    c=up[0]
    for i in range(1,n):
       x,y,z=max(a,b,c),max(a,c)+down[i],max(a,b)+up[i]
       a,b,c=x,y,z
    sys.stdout.write(str(max(x,y,z))+"\n")

