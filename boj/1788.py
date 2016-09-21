mod=1000000000
l=[-1]*1000009

l[0]=0
l[1]=1
n=input()

if n==0:ans=0
elif n>0:ans=1
elif abs(n)%2==1:ans=1
else:ans=-1
print(ans)

n=abs(n)

for i in range(2,n+1):
	l[i]=(l[i-1]+l[i-2])%mod

print(l[n])
