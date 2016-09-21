memo={0:0,1:1}
def f(n):
	if n in memo:
		return memo[n]
	memo[n]=f(n-1)+f(n-2)
	return memo[n]
print f(input())