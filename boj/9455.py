for T in range(input()):
	Grid=[]
	m,n=map(int,raw_input().split())
	for i in range(m):
		Grid+=[list(map(int,raw_input().split()))]
	ans=0
	#print Grid
	for x in range(n):
		s=0
		for y in range(m-1,-1,-1):
			if Grid[y][x]==1:
				ans+=m-1-y-s
				s+=1
	print ans