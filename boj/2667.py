n=input()
IG=[]
for i in range(n):
	l=[]
	for c in raw_input():
		l+=[int(c)]
	IG+=[l]
check=[[False]*n for i in range(n)]

dx=[1,0,-1,0]
dy=[0,1,0,-1]

def dfs(x,y):
	check[y][x]=True
	ret=1
	for i in range(4):
		a=x+dx[i]
		b=y+dy[i]
		if a<0 or n<=a:continue
		if b<0 or n<=b:continue
		if IG[b][a]==0:continue
		if check[b][a]:continue

		ret+=dfs(a,b)

	return ret
l=[]
for x in range(n):
	for y in range(n):
		if check[y][x]==False and IG[y][x]==1:

			l+=[dfs(x,y)]
l.sort()
print len(l)
print "\n".join(str(i) for i in l)

