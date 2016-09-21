n=input()
l=list(map(int,raw_input().split()))
ans=1
a=1
b=1
for i in range(1,n):
	if l[i-1]<=l[i]:
		a+=1
	else:
		ans=max(ans,a)
		a=1
ans=max(ans,a)

for i in range(1,n):
	if l[i-1]>=l[i]:
		b+=1
	else:
		ans=max(ans,b)
		b=1
ans=max(ans,b)

print ans