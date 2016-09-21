s=raw_input()
l=[1,1,1,1,1,1,2,1,1]
a=[0]*10
ans=0
for c in s:
    i=ord(c)-48
    if i==9:a[6]+=1
    else:a[i]+=1
for i in range(9):ans=max(a[i]//l[i]+a[i]%l[i],ans)
print ans


