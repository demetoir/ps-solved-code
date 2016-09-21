n=int(input())
l=[list(map(int,input().split()))for i in range(n)]
for i in range(1,n):
 c=l[i];p=l[i-1]
 for j in range(3):c[j]+=min(p[(j+1)%3],p[(j+2)%3])
print(min(l[n-1]))