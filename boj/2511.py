A=list(map(int,raw_input().split()))
B=list(map(int,raw_input().split()))
a,b=0,0
last=-1
for i in range(10):
	if A[i]==B[i]:
		a+=1
		b+=1

	elif A[i]<B[i]:
		b+=3
		last="B"
	else:
		a+=3
		last="A"
print a,b
if a>b:
	print "A"
elif a==b:
	if last==-1:
		print "D"
	else:
		print last
else:
	print "B"