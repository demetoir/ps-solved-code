import sys
n=10**5+1
l=[0,1]+[0]*n
for i in range(1,n):
    a=i;m=1;q=[]
    while 1:
        q+=[a]
        if a<n and l[a]>0:m=l[a];break
        a=a//2 if a%2==0 else a*3+1
    for i in reversed(q):
        if i>m:m=i
        if i<n:l[i]=m
sys.stdout.write("\n".join([str(l[int(sys.stdin.readline())]) for t in range(int(input()))]))

