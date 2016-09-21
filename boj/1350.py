
input()
l=map(int,raw_input().split())
k=input()

ans=0
for i in l:
    if i==0:
        continue
    ans+=i//k
    if i%k>0:ans+=1
print ans*k