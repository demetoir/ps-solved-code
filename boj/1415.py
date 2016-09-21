memo=[[0]*500001 for i in range(51)]
n=input()
candy=[0]*10001

for i in range(n):
	candy[input()]+=1

seive=[0,0]+[1]*500001
for i in range(2,500001):
	if seive[i]==0:continue
	for j in range(i*i,500001,i):
		seive[j]=0


memo[0][0]=1+candy[0]
s=0
k=1
for w in range(1,10001):
	if candy[w]==0:continue

	for count in range(candy[w]+1):
		for j in range(s+1):
			memo[k][j+count*w]+=memo[k-1][j]
	#print w,memo[k][:100]
	k+=1
	s+=w*candy[w]


ans=0

for i in range(2,500001):
	if seive[i]==1:
		ans+=memo[k-1][i]

"""
print range(100)
print memo[k][:100]
"""
print ans