
n=int(input())
l=list(map(int,input().split()))
s,m=0,0
for k in l:
    if s<0:s=k
    else: s+=k
    if m<s:m=s
print(m)
