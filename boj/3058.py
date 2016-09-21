for T in range(input()):
	l=list(map(int,raw_input().split()))
	ans1,ans2=0,9876543210
	for i in l:
		if i%2==0:
			ans1+=i
			ans2=min(ans2,i)
	print ans1,ans2