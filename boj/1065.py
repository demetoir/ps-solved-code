k=int(input());s=0
for i in range(100,k+1):
    if 2*((i%100)//10)==i%10+i//100:s+=1
s=k if k<100 else s+99
print(s)