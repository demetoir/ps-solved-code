import sys
n,k=map(int,input().split())
l=[]
for i in range(n):
    l+=[float(sys.stdin.readline())]
l.sort()
print("%0.2f"%(sum(l[k:n-k])/(n-2*k)+0.00000001))
print("%0.2f"%((sum(l[k:n-k])+k*(l[k]+l[n-k-1]))/n+ 0.00000001))
