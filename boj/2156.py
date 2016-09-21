a,b,c=0,0,0
for i in range(int(input())):
    w=int(input())
    c,b,a=b+w,a+w,max(a,b,c)
print(max(a,b,c))