n=int(input())
a=3;s=5
l=["*","* *","*****"]
while a<n:l+=[l[i]+" "*(s-(2*i))+l[i]for i in range(a)];a*=2;s=s*2+1
for i in range(n):print(" "*(n-i-1)+l[i]+" "*(n-i-1))