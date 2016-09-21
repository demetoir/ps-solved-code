
n=int(input())
l=[float(input()) for i in range(n)]
s,m=1.0,-1
for k in l:
    if s<1:s=k
    else:s*=k
    if m<s:m=s
print("%.3f"%m)
