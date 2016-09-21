n=input()
ans=0
for k in range(1,10**6):

	s=n-k*(k-1)/2
	if s<=0:break
	#print s,k,(n-k*(k-1)/2)%k
	if (n-k*(k-1)/2)%k==0:
		ans+=1

print ans
