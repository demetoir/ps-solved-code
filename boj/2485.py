from fractions import gcd;a=[int(input()) for i in range(int(input()))];s={}
for i in range(len(a)-1):s[a[i+1]-a[i]]=a[i+1]-a[i]
l=list(s.keys());g=l[0]
for i in l:g=gcd(i,g)
print((a[-1]-a[0])//g+1-len(a))