k=int(input());n=1
while k>n:k,n=k-n,n+1
a,b=k,n-k+1
if n%2==1:a,b=b,a
print(str(a)+"/"+str(b))