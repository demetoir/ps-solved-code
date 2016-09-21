a,b=map(int,raw_input().split())
if (a+b)%2==1:
    print -1
    exit()
x=(a+b)//2
y=a-x
if x<0 or y<0:
    print -1
    exit()
print max(x,y),min(x,y)