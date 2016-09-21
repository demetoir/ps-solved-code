def f(a):
	ret=0
	for i in l:
		ret+=i//a
	return ret

def search():
	ret =-1
	lo=0
	hi=10**9
	while lo<=hi:
		mid =(lo+hi)//2
		if f(mid)>=n:
			lo=mid+1
			ret=max(mid,ret)
		else:
			hi=mid-1
	return ret

k,n=map(int,raw_input().split())
l=[]
for i in range(k):
	l+=[input()]



print search()