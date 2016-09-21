a=[0]*128
s=""
for i in range(int(input())):a[ord(input()[0])]+=1
for i in range(128):
    if a[i]>4:s+=chr(i)
if s=="":s="PREDAJA"
print(s)