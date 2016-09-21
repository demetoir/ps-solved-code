

for T in range(input()):
	s=raw_input()
	lenght=len(s)

	alpa=[0]*128

	i=0
	ans="OK"
	while i<lenght:

		cur=ord(s[i])

		alpa[cur]+=1
		if alpa[cur]==3:
			alpa[cur]=0

			if  i+1>=lenght or s[i+1]!=s[i]:
				ans="FAKE"
				break
			i+=1
		i+=1
	print(ans)