import bisect
s=set()
l=set()
r=[]

for i in range(int(input())):s.add(int(input()))
s=sorted(list(s))
maxval=len(s)

for i in range(maxval):
    for j in range(maxval):
        l.add(s[i]+s[j])

l=sorted(list(l))

for i in range(maxval):
    for j in range(maxval):
        if s[i]-s[j]>0:
            r+=[ (s[i]-s[j], s[i]) ]

r.sort(key=lambda a:a[0])
rval=[i[0] for i in r]

ans=0
for i in l:
    bl=bisect.bisect_left(rval,i,0,len(r)-1)
    br=bisect.bisect_right(rval,i,0,len(r)-1)

    if bl==br:i=bl
    else:i=br-1

    if i==r[i][0]:ans=max(r[i][1],ans)

print(ans)


