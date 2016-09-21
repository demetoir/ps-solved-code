m=input()
k=input()

l=map(int,raw_input().split())
l.sort()
memo=[0]*(2000)
memo[0]=1

for n in range(2000):
    val=0
    for c in l:
        if n-c<0:continue
        val+=memo[n-c]
    if val == 0 :memo[n]=1
    else: memo[n]=0
 
start=0
lenght=0
for p in range(1,600):
    for i in range(1,50):
        if memo[i:i+p]==memo[i+p:i+p+p]:
            lenght=p
            start=i
            sample=memo[i:i+p]
            break

a=m-start+1

if m>=start:
    ans=sum(memo[1:start]) 
    ans+=(a//lenght)*sum(sample)
    if a%lenght >0:
        ans+=sum(sample[:a%lenght])   
    print ans
else:
    print sum( memo[1:m+1])
    