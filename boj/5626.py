
n=input()
l=map(int,raw_input().split())

old=[0]*n
mod=1000000007
if l[0]>0:
    print 0
    exit()
old[0]=1
half=n//2
for i in range(1,n):
    new=[0]*n
    p=l[i]
    if p>-1:
        if (i<half and p>i) or (i>=half and p>n-i-1):
            print 0
            exit()
        
        if 0<=p+1<n:
            new[p]=(old[p+1]+new[p])%mod
        if 0<=p-1<n:
            new[p]=(old[p-1]+new[p])%mod 
        new[p]=(old[p]+new[p])%mod 
    else:
        for j in range(n):
            if 0<=j+1<n:
                new[j+1]=(old[j]+new[j+1])%mod
            if 0<=j-1<n:
                new[j-1]=(old[j]+new[j-1])%mod
            new[j]=(old[j]+new[j])%mod
    #print i
    #print old
    #print new        
    old=new[:]    
#print old
print old[0]        
        
        
        
        
        
            
             
