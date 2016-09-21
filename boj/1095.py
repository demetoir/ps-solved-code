
def getnumber(n,p):
    if n==0:return 0
    return  getnumber(n//p,p)+n//p

s,f,m=map(int,raw_input().split())

ans=-1
seive=[1]*123456
prime=[]
for i in range(2,100001):
    if seive[i]>1:continue
    prime+=[i]
    for j in range(i+i,100001,i):
        seive[j]=i
        
      
divider=[0]*123456     
for p in prime:    
    divider[p]=getnumber(s+f,p)-getnumber(s,p)-getnumber(f,p)
  
out=1   
for ans in range(m,1,-1):
    #print ans
    cur=ans
    factor=[]
    while 1:
        if seive[cur]==1:
            factor+=[cur]
            break
        factor+=[seive[cur]]
        cur=cur/seive[cur]
    #print "factor",factor
    factor_set={}
    
    
    
    for i in factor:
        if i in factor_set:
            factor_set[i]+=1
        else:
            factor_set[i]=1
    #print "factor_set",factor_set        
    ispossible=True        
    for i in factor_set:
        if factor_set[i]>divider[i]:
            ispossible=False
            break
        
    if ispossible:
        
        out =ans
        
        break
print out        
        
        


