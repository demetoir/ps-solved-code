try:
 while 1:
  a=input();b=input();l=[]
  for i in a:
   if i in b:l+=[i];b=b.replace(i,"",1)
  l.sort();print("".join(l))
except:pass