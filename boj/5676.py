import sys

index,val=0,0
def set(a,b,node):
    
    if index<a or b<index:return tree[node]
    
    if a==b:
        tree[node]=val
        return  val
    
    mid=(a+b)//2
 
    tree[node]=set(a,mid,node*2)*set(mid+1,b,node*2+1)
    return tree[node]
 
l,r=0,0
def get(a,b,node):
    
    if r<a or b<l:return 1
    
    if l<=a and b<=r:return tree[node]
    
    mid=(a+b)/2
    
    return get(a,mid,node*2)*get(mid+1,b,node*2+1)

while 1:    

    size=2**17
    tree=[1]*(size*2)
    index,val=0,0

    try:n,k=map(int,raw_input().split())
    except:break  
      
    l=list(map(int,raw_input().split()))  
    
    for i in range(n):
        index=i
        if l[i]>0:      val = 1
        elif l[i]<0:    val = -1
        else:           val = 0
        set(0,size-1,1)
        
  
    ans=""   
    for i in range(k):
        p,q,r=sys.stdin.readline().split()
        
        if p=="P":
            q,r=int(q),int(r)
            l,r=min(q,r)-1,max(q,r)-1
            
            t=get(0,size-1,1)
            if t>0:ans+="+"
            elif t<0:ans+="-"
            else:ans+="0"

        else:
            q,r=int(q),int(r)
            index=q-1            
            if r>0:      val = 1
            elif r<0:    val = -1
            else:        val = 0
            set(0,size-1,1)

    print ans
        
  