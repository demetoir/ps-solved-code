n=input()
l=[]
for i in range(n):
    l+=[input()]
ans=0
memo=[1]*n
for i in range(n-1,-1,-1):
    for j in range(i+1,n):
        if l[i]<l[j] and memo[i]<memo[j]+1:
            memo[i]=memo[j]+1

print n-max(memo)    