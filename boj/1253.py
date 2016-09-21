n=input()
l=map(int,raw_input().split())
d={}
for i in range(n):
    if l[i] in d:
        d[l[i]][i]=i
    else:
        d[l[i]]={i:i}
#print d
#print d
ans={}
 
for i in range(n):
    for j in range(i+1,n):
 
        s=l[i]+l[j]
 
 
        if s in d:
            a=len(d[s])
            if i in d[s]:
                a-=1
            if j in d[s]:
                a-=1
            if a>0:
                ans[s]=len(d[s])
#print ans
#print len(ans)
a=0
for i in ans:
    a+=ans[i]
print a