a=input()
b=input()
c=input()
if a+b+c!=180:print "Error"
else:
	if a==b and b==c and c==a:print "Equilateral"
	elif a!=b and b!=c and c!=a:print "Scalene"
	else:print "Isosceles"