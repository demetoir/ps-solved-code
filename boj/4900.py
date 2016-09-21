segtocode=["063","010","093","079","106","103","119","011","127","107"]
codetoseg={"063":0,"010":1,"093":2,"079":3,"106":4,"103":5,"119":6,"011":7,"127":8,"107":9}
while 1:
	s=raw_input()
	if s=="BYE":break
	index=0
	a=0

	while 1:
		if s[index]=="+":break
		a=a*10+codetoseg[s[index:index+3]]
		index+=3

	index+=1
	b=0

	while 1:
		if s[index]=="=":break
		b=b*10+codetoseg[s[index:index+3]]
		index+=3
	#print a,b
	c=a+b
	ans=""
	while 1:
		if c==0:
			break
		ans=segtocode[c%10]+ans
		c=c//10
	print s+ans

