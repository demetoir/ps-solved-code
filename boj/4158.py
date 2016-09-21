import sys
def f():
	i=0
	j=0
	ret=0
	while 1:
		if i>=n or j>=m:break
		if a[i]>b[j]:
			j+=1
		elif a[i]<b[j]:
			i+=1
		else:
			i+=1
			j+=1
			ret+=1
	return ret
while 1:
	n,m=map(int,sys.stdin.readline().split())
	if (n,m)==(0,0):break

	a=[]
	for i in range(n):
		a+=[int(sys.stdin.readline())]

	b=[]
	for i in range(m):
		b+=[int(sys.stdin.readline())]

	print f()
