import itertools
l=[]
for i in range(9):l+=[input()]

for s in itertools.combinations(range(9),7):
	if sum(l[i] for i in s)==100:
		print "\n".join(str(l[i]) for i in s)