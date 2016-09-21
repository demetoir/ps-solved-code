a=lambda:int(input())
for i in range(a()):
    s=a()
for j in range(a()):
    p,q=map(int,input().split())
    s+=p*q
print(s)