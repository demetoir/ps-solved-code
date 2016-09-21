n=int(raw_input())

a=[i for  i in range(0,150)]
for i in range (2,140):
    a[i]+=a[i-1]
for i in range (2,140):
    a[i]+=a[i-1]    
    
l=[]
for i in range(1,140):
    if a[i]<=300000:
        l+=[a[i]]
balls=l[::-1]

memo=[i for i in range(300000+1)]
for ball in balls:
    for i in range(ball,300000+1):
        if memo[i]> memo[i-ball]+1:
            memo[i]=memo[i-ball]+1
            
print memo[n]
