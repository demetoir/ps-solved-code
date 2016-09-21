s=input()
a=[int(i) for i in s]+[0]*4
b=[0]*4+[int(i) for i in s]
c=0
o=""
for i in range(len(b)-1,-1,-1):
    c=c+a[i]+b[i]
    o=str(c%2)+o
    c=c//2
if c==1:
    o="1"+o
if o=="00000":
    print(0)
else:print(o)
"""
print(bin(int(s,2)*17)[2:])
"""




