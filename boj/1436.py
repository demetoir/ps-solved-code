l=[]
for i in range(10**8):
    a=str(i)
    if "666" in a:
        #print(i)
        l+=[i]
    if len(l)==10001:break
print(l[int(input())-1])