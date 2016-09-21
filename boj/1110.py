n=int(input())
a=n
c=1
n=(n//10+n%10)%10+(n%10)*10
while n!=a:
      n=(n//10+n%10)%10+(n%10)*10
      c+=1
print(c)