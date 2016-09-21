m=int(input());n=int(input())
s=[0]*10001
for i in range(1,101):s[i*i]=i*i
s=[i for i in s[m:n+1] if i>0]
if s==[]:print(-1)
else:print(sum(s));print(s[0])