n,k=map(int,raw_input().split())

length=0
a=n
p=0

while 1:
	if a<=(10**(p+1)-10**p):
		length+=(p+1)*a
		break
	length+=(10**(p+1)-10**p)*(p+1)
	a-=(10**(p+1)-10**p)
	p+=1


if length<k:
	print -1
else:

	a=k
	p=0
	while 1:
		if a<=(10**(p+1)-10**p)*(p+1):
			#print a,p
			#print a//(p+1),a%(p+1)
			s=str( (10**p-1+a//(p+1))%10)+str((10**p-1+a//(p+1))+1)
			#print s
			print s[a%(p+1)]
			break

		a-=(10**(p+1)-10**p)*(p+1)
		p+=1



