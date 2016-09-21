a=[]
s=""
for i in input():a.append(i)
a.sort(reverse=True)
for i in a:s+=str(i)
print(s)