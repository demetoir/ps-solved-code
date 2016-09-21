n=input()
m=input()
s=raw_input()

c=0
cur=0
state=0
l=[]
ans=0

for c in s:

	if state==0:
		if c=="O":state=0
		else:state=1
		#print c,cur,state
		continue

	if state==1:
		if c=="O":state=2
		else:
			l+=[cur]
			cur=0
		#print c,cur,state
		continue

	if state==2:
		if c=="O":
			state=0
			l+=[cur]
			cur=0
		else:
			cur+=1
			state=1
		#print c,cur,state
		continue
#print cur
l+=[cur]
#print l
for p in l:
	if n>p:continue
	ans+=p-n+1

print ans