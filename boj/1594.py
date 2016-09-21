l=""
"""
while 1:
	try:l+=raw_input()
	except:break
"""
l=raw_input()
n=len(l)
if n<=3:
	print l
	exit()

memo=[-1]*1234
trail=[-1]*1234

def check(s):
    a=[c for c in s]
    if len(s)==3:return 3-len(set(a))
    if len(set(a))==2:return 0
    return 2

memo[n]=0

memo[n-1]=-9999999

memo[n-2]=check(l[n-2:n])
trail[n-2]=l[n-2:n]

memo[n-3]=check(l[n-3:n])
trail[n-3]=l[n-3:n]


for i in range(n-4,-1,-1):
	ret=-1
	s=l[i:i+3]
		#print k,s

	if check(s)+memo[i+3]>memo[i]:
		memo[i]=check(s)+memo[i+3]
		trail[i]=s

	s=l[i:i+2]
	#print k,s

	if check(s)+memo[i+2]>=memo[i]:
		memo[i]=check(s)+memo[i+2]
		trail[i]=s

#print memo
#print trail

ans=[]
cur=0
while 1:
	ans+=[trail[cur]]
	cur+=len(trail[cur])
	if trail[cur]==-1:break

print "-".join(ans)


