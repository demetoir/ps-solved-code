
import sys
import Queue
data=Queue.deque()
#n=input()
#l=map(str,raw_input().split())
 
for line in sys.stdin:
    for token in line.split():
        data+=[token]
        
         
#print data
n=int(data.popleft())
l=[]
if len(data)!=n:
    print list(range(100000)) 
    
for i in range(n):
    l+=[data.popleft()]

 
 
#l.reverse()
#print l
ans="9"*1500
      
     
for i in range(n):
    if l[i][0]=="0":
        #print l[i]
        continue
    cur=[l[i]]
    #print i,cur
    for j in range(n):
        if i==j:continue
        tempval="9"*1500
        temp=[]
        for k in range(1,len(cur)+1):
            #print "##",cur[:k]+[l[j]]+cur[k:]
            tempstring="".join(cur[:k]+[l[j]]+cur[k:])
            if tempstring<tempval:
                tempval=tempstring
                temp=cur[:k]+[l[j]]+cur[k:] 
        cur=temp
        #print "#",j,cur
    ans=min(ans,"".join(cur))

if ans=="9"*1500:
    print "INVALID"
else:
    print ans