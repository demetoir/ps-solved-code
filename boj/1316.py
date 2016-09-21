
n=input()
ans=n
for T in range(n):
	s=raw_input()
	d={}
	for i in range(len(s)):
		c=s[i]
		if c in d:
			d[c]+=[i]
		else:
			d[c]=[i]

	for key in d:
		l=d[key]
		if l[0]+len(l)-1!=l[len(l)-1]:
			ans-=1
			break


print ans
