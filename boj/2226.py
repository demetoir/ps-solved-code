n=input()
x,y=0,1
for i in range(2,n+1):
    x,y=x+y - i%2,x+y
print x
