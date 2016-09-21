n=input()
a=raw_input()
b=raw_input()
ans=a

if n%2==1:
	ans=""
	for c in a:
		if c=="0":ans+="1"
		else:ans+="0"

if ans == b:print "Deletion succeeded"
else:print "Deletion failed"
