import sys
while 1:
	n= input()
	if n==0: break
	ans=0
	for i in range(n):
		s=sys.stdin.readline()

		for j in range(ans,len(s)):
			if s[j]==" " or s[j]=="\n":
				ans=j
				break

	print ans+1