n=int(raw_input())
ans=987654321
for i in range(10000):
    j=n-5*i
    if j<0 or j%3>0:continue
    ans=min(ans,i+j//3)
if ans==987654321:
    ans=-1
print ans
    