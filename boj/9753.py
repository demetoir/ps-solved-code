
import sys
import Queue
seive=[True]*100010
prime=[]
import re

for i in range(2,100000+1):
    if seive[i]==False:continue
    prime+=[i]
    for j in range(i+i,100000+1,i):
        seive[j]=False
 
l=[False]*123456

for i in range(len(prime)):
    for j in range(i+1,len(prime)):
        a=prime[i]*prime[j]
        if a>100010:break
        l[a]=True

file=open("out.txt","r")
data=[]
for line in file:
    data+=[int(line)]
print data
for T in range(10000):
    a=T+1
    for i in range(a,100010):
        if l[i]:
            if data[T]!=i:
                print a,data[T],i
                exit()
            #print T,i
            break
print "qswdqwd"        