for i in range(input()):
	l=list(map(str,raw_input().split()))
	ans=[]
	for s in l:
		ans+=["".join(reversed(s))]
	print " ".join(ans)