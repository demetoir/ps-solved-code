def dfs(cur):
	global check
	if check[cur]==1:return False

	check[cur]=1
	for next in range(n):
		if G[cur][next]==0:continue

		if toleft[next]==-1 or dfs(toleft[next]):
			toleft[next]=cur
			return True
	return False

toleft=[-1]*1000

def matching():
	global check

	count=0

	for i in range(n):
		check=[0]*n
		if dfs(i):
			count+=1

		check=[0]*n
		if dfs(i):
			count+=1

	return count

n=input()
s=[]

for i in range(n):
	a,b,c=map(int,raw_input().split())
	s+=[(a,b,c)]

G=[[0]*1000 for i in range(1000)]

for j in range(n):
	for i in range(n):
		if i==j:continue
		a,b,c=s[i]
		x,y,z=s[j]
		if a<=x and  b<=y and c<=z :
			G[j][i]=1

for i in range(n):
	for j in range(i):
		if i==j:continue
		a,b,c=s[i]
		x,y,z=s[j]
		if a==x and b==y and c==z:
			G[j][i]=0




ans=matching()

print n-ans