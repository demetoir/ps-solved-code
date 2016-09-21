a,b=map(int,raw_input().split())

if a==0:
	print "-"
	exit()

a,b=a,b-a
ans="-1"

for i in range(1,61):

	if (2**i-1)%(a+b)==0:
		mul=(2**i-1)//(a+b)
		a*=mul
		b*=mul
		if a<b:
			ans=bin(b)[2:]

			ans=ans.replace("1","-")
			ans=ans.replace("0","*")
		else:
			ans=bin(a)[2:]
			ans=ans.replace("1","*")
			ans=ans.replace("0","-")
		break


print ans

