try:
 while(1):
  line=[0]*10;count=1;t=int(input());a=t
  while 1:
   for i in str(a):line[int(i)]=1
   if sum(line)==10:break
   count+=1;a=t*count
  print(count)
except:pass