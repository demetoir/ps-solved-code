n=input()
k=input()
mod=1000000003
memo=[[-1]*1001 for i in range(1001)]
if n<k*2:
	print 0
	exit()
def f(n,k):

	if k==0:return 1
	if n<k:return 0
	ret=memo[n][k]
	if ret>-1:return ret
	ret=0
	for i in range(1,n+1):
		ret+=f(i-2,k-1)
		ret%=mod
	memo[n][k]=ret

	return ret

ans=f(n-3,k-1)

for i in range(2,n+1):

	ans+=f(n-i-1,k-1)
	ans%=mod

print ans
