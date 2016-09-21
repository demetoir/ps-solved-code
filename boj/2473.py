

n=input()
l=list(map(int,raw_input().split()))
l.sort()

INF=9876543210
ans=INF
def bi(lo,hi,val):

	ret=0
	c=INF
	while lo<=hi:
		mid=(lo+hi)//2

		t=l[mid]-val
		if t<0:	t = -t

		if t<c:
			c=t
			ret=mid

		if l[mid]>=val:
			hi=mid-1
		else:
			lo=mid+1

	return ret

a,b,c=0,0,0
for i in range(n):
	for j in range(i+1,n):
		v=l[i]+l[j]

		if i>0:

			k=bi(0,i-1,-v)
			p=abs(v+l[k])

			if ans>p:
				ans=p
				a,b,c=sorted([l[i],l[j],l[k]])

print a,b,c
