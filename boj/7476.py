
n=input()
A=[0]+list(map(int,raw_input().split()))
m=input()
B=[-1]+list(map(int,raw_input().split()))






trail=[[(-1,-1)]*(n+1) for i in range(m+1)]
memo=[[-1]*(n+1) for i in range(m+1)]
start=(-1,-1)
ansList=[]
ans=0
def f(a,b):
	global start,ans

	if memo[b][a]>-1:
		return memo[b][a]

	if a==0 or b==0:
		memo[b][a]=0
		return 0

	if A[a]!=B[b]:
		memo[b][a]=f(a,b-1)
		trail[b][a]=a,b-1
		return memo[b][a]

	ret=1

	for i in range(1,a):
		if A[i]<A[a] and f(i,b-1)+1>ret:
			#print i,b-1
			ret=f(i,b-1)+1
			trail[b][a]=(i,b-1)
			#print a,b, i,b-1
	if ans<ret:
		#print a,b,ret
		start=(a,b)
		ans=ret

	memo[b][a]=ret
	return  ret

for a in range(n+1):
	for b in range(m+1):

		#print a,b
		f(a,b)



"""
for i in memo:print i
print
for i in trail:print i
"""

x,y=start
#print start
while 1:
	#print x,y
	if (x,y)==(-1,-1):break
	if A[x]==B[y]:
		ansList+=[A[x]]
	x,y=trail[y][x]
ansList=list(reversed(ansList))
#print ansList
print ans
if ans>0:
	print " ".join(str(i)for i in ansList)