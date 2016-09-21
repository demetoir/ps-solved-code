s=[0]*1001;a=0
for i in range(10):c=int(input());a+=c;s[c]+=1
print(a//10);print(s.index(max(s)))