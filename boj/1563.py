m=[]
N=int(input())
a,b,c=1,0,0
for i in range(N+1):m+=[a+b+c];x,y,z=a+b+c,a,b;a,b,c=x,y,z
r=m[N]
for i in range(N):r+=m[i]*m[N-1-i]
print(r%10**6)