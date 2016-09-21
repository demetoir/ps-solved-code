A=raw_input()
B=raw_input()

n=len(A)+1
m=len(B)+1
memo=[[0]*m for i in range(n)]


ans=0
#for i in range(n):	print memo[i]

#print
for i in range(1,n):
	for j in range(1,m):
		if A[i-1]==B[j-1]:
			memo[i][j]=memo[i-1][j-1]+1
		else:
			memo[i][j]=max(memo[i-1][j],memo[i][j-1])
		ans=max(ans,memo[i][j])

for i in range(n):	print memo[i]

print ans