n=int(input())
a=0
for i in range(1,n-2):a+=i*(n-2-i)*n
print(a//4)