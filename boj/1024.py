def bi(n,l):
	lo=0
	hi=1000000000
	while lo<=hi:
		mid=(lo+hi)//2
		s=int(mid*l + (l-1)*l/2)
		if s==n:
			return mid
		if s<n:
			lo=mid+1
		else:
			hi=mid-1
	return -1

n,l = map(int,raw_input().split())


for i in range(l,101):
	start=bi(n,i)
	if start>=0:
		print " ".join(str(i) for i in range(start,start+i))
		exit()
print -1
