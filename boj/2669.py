a=list(map(int,raw_input().split()))
b=list(map(int,raw_input().split()))
c=list(map(int,raw_input().split()))
d=list(map(int,raw_input().split()))
def f(s,p,q):
	a,b,x,y=s
	if a< p+0.5 <x and b< q+0.5 <y:return True
	return False

ans=0
for i in range(1,100):
	for j in range(1,100):
		if f(a,i,j) or f(b,i,j) or f(c,i,j) or f(d,i,j):ans+=1
print ans


