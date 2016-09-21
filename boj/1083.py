while 1:
 try:
  a,l,s,p,t=int(input()),list(map(int,input().split())),int(input()),0,""
  while s!=0 and p!=a:
   e=s+p+1 if s<a else a;k=l.index(max(l[p:e]));l.insert(p,l.pop(k));s-=k-p;p+=1
  for i in l:t+=str(i)+" "
  print(t)
 except:break