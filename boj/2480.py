a,b,c=map(int,raw_input().split())
ans=0
if a==b and b==c and c==a:
	ans=10000+1000*a
elif a!=b and b!=c and c!=a:
	ans=100*max(a,b,c)
else:
	ans=1000+100*(sum([a,b,c])-max(a,b,c)-min(a,b,c))
print ans
