n=int(input());
s=list(map(int,input().split()))
s[3],s[4]=s[4],s[3]
a=min(s)
p=min(s[0],s[5])
m=s[1:5]
t=[]
for i in range(4):t+=[m[i]+m[(i+1)%4]]
c=min(t)+p
b=min(t+[min(m)+p])
if n==1:o=sum(s)-max(s)
elif n==2:o=c*4+b*4
else:o=(5*n-6)*(n-2)*a+b*(8*n-12)+c*4
print(o)