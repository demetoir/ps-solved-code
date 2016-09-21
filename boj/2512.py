n=input()
l=map(int,raw_input().split())
m=input()
hi=9876543210
low=0
ans=0
while low<=hi:
    mid=(low+hi)//2
    cur=0
    s=0
    
    for i in l:
        if i>mid:
            s+=mid
            cur=max(cur,mid)
        else:
            s+=i
            cur=max(cur,i)
            
    if s<=m:
        ans=max(cur,ans)
        low=mid+1    
    else:
        hi=mid-1
        
print ans
    
    
    
    
    
    