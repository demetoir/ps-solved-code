n= int(input())
l=[]
def r(n,s):
    global l
    if n==0:
        l+=[s]
        return
    last=s%10
    for i in range(last-1,-1,-1):
        r(n-1,s*10+i)
for i in range(10):
    for j in range(10):
        r(i,j)
l.sort()
#print(l)
#print(len(l))

if n>=len(l):
    print(-1)
else:
    print(l[n])

