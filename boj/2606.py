def r(s):
    if c[s]==1:return
    c[s]=1
    for i in l[s]:r(i)
input()
s=int(input())
l=[[]*s for i in range(101)]
c=[0]*101
for i in range(s):
    a,b=map(int,input().split())
    l[a].append(b)
    l[b].append(a)
r(1)
s=0
for i in c:s+=i
print(s-1)