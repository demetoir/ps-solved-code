n,m=map(int,raw_input().split())
l=[]
for i in range(n):
    l+=[int(raw_input())]
l.sort()
j=0
ans=9876543210
for i in range(n):
    if j<i:j=i
    while j<n:
        if l[j]-l[i]>=m:
            ans=min(ans,l[j]-l[i])
            break
        j+=1
print ans
