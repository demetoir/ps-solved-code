n=input()
for t in range(n):
	a,b=raw_input().split("-")
	A=0
	for i in range(3):
		A+=(ord(a[2-i])-65)*(26**i)

	if abs(A-int(b))<=100:print "nice"
	else:print "not nice"