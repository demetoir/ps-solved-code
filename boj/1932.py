s=[];n=int(input())
for i in range(n):s+=[list(map(int,input().split()))]
for i in range(n-2,-1,-1):
 for j in range(len(s[i])):s[i][j]+=max(s[i+1][j:j+2])
print(s[0][0])