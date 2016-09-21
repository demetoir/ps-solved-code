import sys
n,c=map(int,raw_input().split())
l=[]
for i in range(n):
    l+=[int(sys.stdin.readline())]
l.sort()

def f(x):
    ret = 9876543210
    start=l[0]
    number=1
    for i in range(1,n):
        if l[i] - start >= x:
            start = l[i]
            number+=1

    if number >= c:return c
    else: return -1

lo=0
hi=9876543210
ans=0
while lo<=hi:
    mid = (hi+lo)//2
    val = f(mid)
    #print lo,mid,hi,val
    if val > -1:
        ans = max(ans,mid)
        lo=mid+1
    else:
        hi=mid-1
print ans