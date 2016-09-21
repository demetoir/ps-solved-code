s=0
t=lambda:list(map(int,input().split()))
n=int(input())
a=t();b=t();a.sort();b.sort()
for i in range(n):s+=a[i]*b[n-i-1]
print(s)