n=input()
l=map(int,raw_input().split())
ans={}
if n==1:
    print "A"
    exit()
    
for a in range(-1000,1000+1,1):
    
    flag=True
    b=l[1]-l[0]*a
    for i in range(n-1):
        if l[i+1] != l[i]*a+b:
            flag=False
            break
    if flag:
        ans[l[n-1]*a+b]=0
        #print a,b,l[i]*a+b
if len(ans)==0:
    print "B"
elif len(ans)==1:
    for i in ans:
        print i
else:
    print "A"