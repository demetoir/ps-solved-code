prime=[0,0]+[1]*3000

left=[]
right=[]

def bimatch(a,b):
	global check,n,left,right
	right=[-1]*n
	left=[-1]*n

	left[a]=b
	right[b]=a
	size=2

	for cur in range(n):

		check=[False]*n
		check[a]=True
		check[b]=True

		if dfs(cur):size+=1

	if size==n:return True
	else:return False

def dfs(cur):
	global check,left,right

	if check[cur]:return False
	check[cur]=True
	for post in G[cur]:
		if right[post]==-1 or dfs(right[post]):
			right[post]=cur
			return True

	return False

for i in range(2,3000 ):
	if prime[i]==0:continue
	for j in range(i*i,3000,i):
		prime[j]=0

G=[[]for i in range(50)]
n=input()
l=list(map(int,raw_input().split()))

for i in range(n):
	for j in range(i+1,n):
		if prime[l[i]+l[j]]==1:
			G[i]+=[j]
			G[j]+=[i]

#print G
ans=[]
for i in range(1,n):
	dodge=i
	if prime[l[0]+l[dodge]]==0:continue
	if bimatch(0,i):
		ans+=[l[i]]

ans=[str(i) for i in sorted(ans)]
if len(ans)==0:print -1
else:
	print " ".join(ans)