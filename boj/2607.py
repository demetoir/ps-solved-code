n=int(input())
l=[0]*99
for c in input():l[ord(c)]+=1
a=0
for i in range(n-1):
    t=[0]*99;p=0;n=0
    for c in input():t[ord(c)]+=1
    for i in range(99):
        if l[i]-t[i]>0:p+=l[i]-t[i]
        if l[i]-t[i]<0:n+=l[i]-t[i]
    if p<2 and n>-2:a+=1
print(a)

