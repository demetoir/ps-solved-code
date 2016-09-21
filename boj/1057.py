n,x,y=map(int,raw_input().split())
l=[0]+[0]*n
x-=1
y-=1
ans=1
while 1:
	x=x//2
	y=y//2
	if x==y:break
	ans+=1
print ans
