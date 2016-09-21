l=[1,1,2,2,2,8]
a=list(map(int,raw_input().split()))
s=[]
for i in range(6):s+=[str(l[i]-a[i])]
print " ".join(s)