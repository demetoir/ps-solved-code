n=input()
A,B=100,100
for i in range(n):
    a,b=map(int,raw_input().split())
    if a>b:
        B-=a
    elif b>a:
        A-=b
print A
print B