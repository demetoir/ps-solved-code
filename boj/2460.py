t=m=0
for i in range(10):
    a,b=map(int,input().split())
    t+=b-a
    if t>10000:t=10000
    if m<t:m=t
print(m)