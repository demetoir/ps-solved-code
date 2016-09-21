while 1:
 s=list(reversed(input()));d=0;f=1;t=0
 if s==["0"]:break
 for i in s:t+=1;f*=t;d+=int(i)*f
 print(d)