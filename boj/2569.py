
n=input()
a=[]
for i in range(n):a+=[int(raw_input())]

sortedlist=list(sorted(a))

l=[-1]*(n+1)
for i in range(n):
	for j in range(n):
		if a[i]==sortedlist[j]:
			l[i]=j



check=[0]*n
ans=0
for cur in range(n):
	chane=[]

	while 1:
		if check[cur]==1:break

		chane+=[cur]
		check[cur]=1
		cur=l[cur]

	if len(chane)<2:continue
	mini=min(a[i] for i in chane)
	sumi=sum(a[i] for i in chane)
	p=mini*(len(chane)-2) + sumi
	q=sumi+mini+ min(a)*(len(chane)+1)
	ans+=min(p,q)

print ans