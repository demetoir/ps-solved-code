import  sys

case=0
while 1:
    case+=1
    n=int(input())
    if n==0:break
    l=[[0,0,0]]
    for i in range(n):
        l+=[list(map(int,sys.stdin.readline().split()))]
    l[1]=[123456789,l[1][1],l[1][1]+l[1][2]]
    for i in range(2,n+1):
        a,b,c=l[i]
        x,y,z=l[i-1]
        a=min(x,y)+a
        b=min(x,y,z,a)+b
        c=min(y,z,b)+c
        l[i]=[a,b,c]
        print(a,b,c)
    print(str(case)+". "+str(l[n][1]) )