n=input()
a=1
t=1
ans=1
while 1:
	#print ans, a,t
	if ans>n:
		ans=-1
		break
	if a%n==0:break
	t=(t*10)%n
	a=(a+t)%n
	ans+=1
print ans

