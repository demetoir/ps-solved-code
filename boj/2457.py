import sys

c=[0,0,31,59,90,120,151,181,212,243,273,304,334]
l=[-1]*1000

for i in range(input()):
	a,b,x,y=map(int,sys.stdin.readline().split())
	start,end=c[a]+b,c[x]+y
	if start==end:continue
	l[start]=max(end,l[start])

memo=[-1]*900

for i in range(1,c[12]+30+1):
	s,e=i,l[i]
	for post in range(s+1,e+1):
		if l[post]>e and l[memo[i]]<l[post]:memo[i]=post

cur=0
for i in range(1,c[3]+1+1):
	if memo[i]>memo[cur]:cur=i

if memo[cur]<=c[3]+1:
	print 0
	exit()

cnt=1
while 1:
	if l[cur]>c[11]+30:break
	if memo[cur]==-1:
		cnt=0;break
	cur=memo[cur]
	cnt+=1

print cnt

