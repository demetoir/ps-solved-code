l=input()
l=list(map(int,raw_input().split()))
n=input()
ans=0
for a in range(1,1001):
	for b in range(a+1,1001):
		if n<a or n>b:continue
		t=1
		for c in l:
			if c>=a and c<=b:
				t=0
				break
		ans+=t
print(ans)