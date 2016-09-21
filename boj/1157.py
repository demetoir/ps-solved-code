l=[0]*99
for i in input():l[ord(i)&95]+=1
m=max(l);print("?"if l.count(m)>1 else"%c"%l.index(m))
