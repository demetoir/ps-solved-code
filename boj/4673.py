l=lambda n:n%10+l(n//10) if n>0 else 0
a=[1]*20002
for i in range(1,10000):a[l(i)+i]=0
for i in range(1,10000):
    if a[i]==1:print(i)