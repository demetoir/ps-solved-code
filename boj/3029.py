cur=list(map(int,raw_input().split(":")))
target=list(map(int,raw_input().split(":")))
a,b,c=0,0,0
c+= target[2]-cur[2]
if c<0:
	c+=60
	b-=1
b+=target[1]-cur[1]
if b<0:
	b+=60
	a-=1
a+=target[0]-cur[0]
if a<=0:
	a+=24

print "%s:%s:%s"%(str(a).zfill(2),str(b).zfill(2),str(c).zfill(2))


