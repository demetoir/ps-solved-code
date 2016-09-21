
n=input()
l=list(map(int,raw_input().split()))
l.sort()

def bisearch(x,lo,hi):

	ret=l[(lo+hi)//2]
	d=987654321987

	while lo<hi:
		mid =(lo+hi)//2

		if d>abs(l[mid]+x):
			ret=l[mid]
			d=abs(l[mid]+x)

		if d>abs(l[mid+1]+x):
			ret=l[mid+1]
			d=abs(l[mid+1]+x)

		if l[mid]+x==0:return l[mid]
		if l[mid]<-x:
			lo=mid+1
		else:
			hi=mid-1
	return ret

diff=987654321987
ans=0

for i in range(n):
	x=l[i]

	if i-1>=0:
		a=bisearch(x,0,i-1)

		if abs(x+a)<diff:
			ans=[a,x]
			diff=abs(x+a)

	if i+1<=n-1:
		b=bisearch(x,i+1,n-1)

		if abs(x+b)<diff:
			ans=[b,x]
			diff=abs(x+b)

	#print x,a,b
ans.sort()
a,b=ans
print a,b