memo=[[0]*20 for i in range(20)]
for i in range(20):
	memo[0][i]=i
	memo[i][1]=1
for i in range(1,15):
	for j in range(2,15):
		memo[i][j]=memo[i-1][j]+memo[i][j-1]
for T in range(input()):
	k=input()
	n=input()
	print memo[k][n]