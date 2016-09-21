a,b=1,1
for i in range(int(input())-1):x,y=a+b+b,a+b;a,b=x%9901,y%9901
print((a+b+b)%9901)

