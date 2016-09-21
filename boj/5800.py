k=input()
for c in range(k):
	l=list(map(int,raw_input().split()))
	n=l[0]
	l=l[1:]
	l.sort()
	ans=0
	for i in range(n-1):
		ans=max(ans,l[i+1]-l[i])
	print "Class %d"%(c+1)
	a=max(l)
	b=min(l)
	print "Max %d, Min %d, Largest gap %d"%(a,b,ans)
