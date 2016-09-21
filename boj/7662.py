from heapq import *
import Queue
import sys 
check=[True]*1000001
for T in range(input()):
    n=input()
    
    maxQ=[]
    minQ=[]
    for i in range(n):
        a,b=sys.stdin.readline().split()
        b=int(b)
    
        if a=="I":
            heappush(maxQ, (-b,i))
            heappush(minQ, (b,i))
            check[i]=True
            
        else:
            

            while len(maxQ)>0:                
                val,index=maxQ[0]
                if check[index]:
                    break

                heappop(maxQ)

            while len(minQ)>0:
                val,index=minQ[0]
                if check[index]:
                    break
                heappop(minQ)

                
            if len(maxQ)==0:continue
            
            if b==1:
                val,index=heappop(maxQ)
                check[index]=False
            else:
                val,index=heappop(minQ)
                check[index]=False
 
    while len(maxQ)>0:                
        val,index=maxQ[0]
        if check[index]:break
        heappop(maxQ)
        
    while len(minQ)>0:
        val,index=minQ[0]
        if check[index]:break
        heappop(minQ)
 
    if len(maxQ)==0:print "EMPTY"
    else:
        a,b=-heappop(maxQ)[0],heappop(minQ)[0]
        print a,b
        
        