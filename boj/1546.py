n=int(input())
l=list(map(int,input().split()))
m=max(l)
for i in range(n):
    l[i]=l[i]/m*100
print("%.2f"%(sum(l)/n))