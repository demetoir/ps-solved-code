import bisect

n,c=map(int,raw_input().split())
l=[]
while 1:
	try:
		l+=list(map(int,raw_input().split()))
	except:
		break

def f(i,end,v,d):
	if i==end:
		d+=[v]
		return
	f(i+1,end,v+l[i],d)
	f(i+1,end,v,d)

A=[]
B=[]

f(0,n//2,0,A)
f(n//2,n,0,B)

B.sort()

ans=0


for i in A:
	index=bisect.bisect_right(B,c-i)
	ans+=index

print ans
