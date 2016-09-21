n=int(input());s=0
while n>0:s+=1;n-=s
print(s-1 if n<0 else s)