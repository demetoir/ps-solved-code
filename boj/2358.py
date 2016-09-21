n=input()
X={}
Y={}
for i in range(n):
	x,y=map(int,raw_input().split())
	if x in X:X[x]+=1
	else:X[x]=1
	if y in Y:Y[y]+=1
	else:Y[y]=1
ans=0
for i in X:
	if X[i]>=2:ans+=1
for i in Y:
	if Y[i]>=2:ans+=1
print ans