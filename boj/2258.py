l=[]
n,m=map(int,raw_input().split())
for i in range(n):
	w,c=map(int,raw_input().split())
	l+=[(c,w)]

l.sort(key=lambda a:a[0])

t=[l[0]]
ll=[]
for i in range(1,n):
	if l[i][0]>l[i-1][0]:
		ll+=[t]
		t=[]
	t+=[l[i]]

if len(t)>0:
	ll+=[t]

for i in range(len(ll)):
	l=ll[i]
	l.sort(key=lambda a:a[1])
	ll[i]=l[::-1]

ans=987654321987654321
sum=0

for l in ll:
	money=0
	for c,w in l:
		sum+=w
		money+=c
		if m<=sum:
			#print sum,money
			ans=min(money,ans)

if ans==987654321987654321:
	ans = -1

#for i in ll:print i

print ans