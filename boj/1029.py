INF=999

n=input()
G=[]
for i in range(n):



	G+=[[int(i) for i in raw_input()]]

memo=[[-1]*n for i in range(2**n)]
memo[1][0]=0

ans=0

def f(bit,cur):
	global ans

	if bit&1==0 or bit&(2**cur)==0:
		return INF

	if memo[bit][cur]>-1:
		return memo[bit][cur]

	ret=INF
	bitcount=0

	for i in range(n):
		if bit&(2**i):bitcount+=1

	pre=bit-2**cur

	for i in range(n):
		if (pre&(2**i)) and f(pre,i) <= G[i][cur]:
			ret = min( ret, G[i][cur] )

	memo[bit][cur]=ret

	if ans<bitcount and ret<INF:
		ans=bitcount
	return ret

for bit in range(2**n):
	for cur in range(n):
		f(bit,cur)
		#print bit,cur,f(bit,cur)
print ans