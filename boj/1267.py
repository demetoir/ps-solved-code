n= input()
l=list(map(int,raw_input().split()))
Y=0
M=0
for i in l:
	Y+=(i//30 +1)*10
	M+=(i//60 +1)*15

if Y<M:
	print "Y",Y
elif Y>M:
	print "M",M
else:
	print "Y M",Y