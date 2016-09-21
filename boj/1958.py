A=raw_input()
B=raw_input()
C=raw_input()

n=len(A)+1
m=len(B)+1
l=len(C)+1

memo=[[[0]*l for j in range(m)] for i in range(n)]


ans=0

for i in range(1,n):
	for j in range(1,m):
		for k in range(1,l):
			if A[i-1]==B[j-1] and C[k-1]==A[i-1]:
				memo[i][j][k]=memo[i-1][j-1][k-1]+1
			else:
				memo[i][j][k]=max(memo[i-1][j][k],memo[i][j-1][k],memo[i][j][k-1])



print memo[n-1][m-1][l-1]