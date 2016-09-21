n=input()
ans=0
a=n
k=0
while 1:
	if a<=10**(k+1)-10**k:
		ans+=(k+1)*a
		break
	ans+=(10**(k+1)-10**k)*(k+1)
	a-=10**(k+1)-10**k
	k+=1
print ans