size=111
cur=[[0]*size for  i in range(size)]


mod=1000000007
N,R,L=map(int,raw_input().split())
cur[1][1]=1


for n in range(1,N):
	next=[[0]*size for  i in range(size)]

	for a in range(101):		
		for b in range(101):
			
			p=cur[a][b]
			if p==0:continue
			next[a][b+1]=(p+next[a][b+1])%mod
			next[a][b]=(p*(n-1)+next[a][b])%mod
			next[a+1][b]=(p+next[a+1][b])%mod
			
	cur=next[:]	

print cur[L][R]
