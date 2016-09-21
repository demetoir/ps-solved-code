n,f=map(int,raw_input().split())

l=[[1]]

for i in range(1,11):
	t=[1]

	for j in range(i-1):
		a= l[i-1][j]+l[i-1][j+1]
		t+=[a]
	t+=[1]
	l+=[t]
#for i in l:print(i)
mul=l[n-1]
#print mul
import itertools
for i in itertools.permutations(range(1,n+1)):
	s=0
	t=0

	for j in i:
		s+=mul[t]*j
		t+=1

	if s==f:
		print " ".join(str (j) for j in i)
		break
