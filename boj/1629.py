a,b,c=map(int,raw_input().split())
mul=a
ans=1
while b!=0:
	if b%2==1:
		ans=(ans*mul)%c
	mul=(mul*mul)%c
	b=b//2
print ans