import sys
n=input()
seive=[1]*(10**5+10)
pl=[]
for i in range(2,10**5):
	if seive[i]==0:continue
	pl+=[i]
	for j in range(i*i,10**5,i):
		seive[j]=0

def isprime(k):
	if k<2:return False
	for i in pl:
		if i*i>k:break
		if k%i==0:return False
	return True


for i in range(n):
	a=int(sys.stdin.readline())
	while 1:
		if isprime(a):
			ans=a
			break
		a+=1
	print a
