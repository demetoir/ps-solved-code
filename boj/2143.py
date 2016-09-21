T=input()
A=[0]
B=[0]

na=input()
for i in list(map(int,raw_input().split())):
	A+=[sum(A[-1:])+i]

nb=input()
for i in list(map(int,raw_input().split())):
	B+=[sum(B[-1:])+i]

DA={}
DB={}

for i in range(na+1):
	for j in range(i+1,na+1):

		s=A[j]-A[i]

		if s in DA: DA[s]+=1
		else:DA[s]=1


for i in range(nb+1):
	for j in range(i+1,nb+1):

		s=B[j]-B[i]

		if s in DB: DB[s]+=1
		else:DB[s]=1
ans=0
for a in DA:
	b=T-a
	if b in DB:
		ans+=DA[a]*DB[b]
print ans