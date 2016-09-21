for T in range(input()):
	r,e,c=map(int,raw_input().split())
	if r<e-c:print "advertise"
	elif r==e-c:print "does not matter"
	else:print "do not advertise"