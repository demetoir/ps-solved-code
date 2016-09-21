n=input()
l=map(int,raw_input().split())
 
ans=0
for i in range(n):
    for j in range(n):
        if l[i]-l[j]>=0:
            ans+=l[i]-l[j]
        else:
            ans-=l[i]-l[j]
print ans