n=int(input())
import  sys
l=[int(sys.stdin.readline()) for i in range(n)]
l.sort()
ans=0
for i in range(n):ans=max(ans,l[i]*(n-i))
print(ans)