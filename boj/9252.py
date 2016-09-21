A=raw_input()
B=raw_input()

n=len(A)+1
m=len(B)+1
memo=[[0]*m for i in range(n)]
trail=[[(-1,-1)]*m for i in range(n)]

ans=0
#for i in range(n):	print memo[i]

#print
for i in range(1,n):
	for j in range(1,m):
		if A[i-1]==B[j-1]:
			memo[i][j]=memo[i-1][j-1]+1
			trail[i][j]=(i-1,j-1)
		else:
			if memo[i-1][j]>memo[i][j-1]:
				memo[i][j]=memo[i-1][j]
				trail[i][j]=(i-1,j)
			else:
				memo[i][j]=memo[i][j-1]
				trail[i][j]=(i,j-1)



ansList=[]
x,y=n-1,m-1

while 1:
	if x==0 or y==0:break

	if A[x-1]==B[y-1]:
		ansList+=[A[x-1]]

	x,y=trail[x][y]

ansList.reverse()
print memo[n-1][m-1]
print "".join(str(i) for i in ansList)