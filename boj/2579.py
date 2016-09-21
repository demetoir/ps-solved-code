n=input()
l=[0]
for i in range(n):l+=[input()]

memo=[[-1]*(n+1) for i in range(3)]
memo[1][1]=l[1]
memo[2][1]=l[1]

def f(i,j):

	if i<0:return 0
	if memo[j][i]>-1:return memo[j][i]

	if j==1:memo[j][i]=l[i]+max(f(i-2,1),f(i-2,2))
	else:memo[j][i]=l[i]+f(i-1,1)
	return  memo[j][i]

print(max(f(n,1),f(n,2)))
