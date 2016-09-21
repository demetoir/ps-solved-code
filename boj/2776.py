for T in range(input()):
	n=input()
	d={}
	for i in map(int,raw_input().split()):d[i]=i
	m=input()
	l=[]
	for i in map(int,raw_input().split()):
		if i in d:l+=["1"]
		else:l+=["0"]
	print "\n".join(l)