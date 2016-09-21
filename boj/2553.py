t=1
for i in range(1,int(input())+1):
 while i%5==0:t,i=t//2,i//5
 if (t*i)%10==0:t=(t*i)//10
 else:t=(t*i)
print(t%10)