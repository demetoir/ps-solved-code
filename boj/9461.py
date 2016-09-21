memo=[0,1,1,1]+[0]*100
for i in range(4,101):
	memo[i]=memo[i-2]+memo[i-3]
for T in range(input()):
	print memo[input()]

