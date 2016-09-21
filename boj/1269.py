a={}
b={}
raw_input()
for i in map(int,raw_input().split()):
    a[i]=0
for i in map(int,raw_input().split()):
    b[i]=0
ans=len(a)+len(b)
for i in a:
    if i in b:
        ans-=2
print ans