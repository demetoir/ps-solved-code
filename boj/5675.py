d=[0]*181
for i in range(720):
	a=(i//12)*6
	b=(i%60)*6
	s=abs(a-b)
	#print i,a,b
	if s>180:
		#print i,s-180
		d[s-180]=1
	else:
		#print i,s
		d[s]=1


while 1:
	try:n=input()
	except:break
	if d[n]==1:print "Y"
	else:print("N")