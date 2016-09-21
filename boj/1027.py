N=input()

l=map(int,raw_input().split())

ans=0

for n in range(N):
    val=0
    for i in range(N):
        if i==n:
            continue
        
        
        flag=True
        for j in range(i+1,n):#i j n
            if (l[j]-l[i])*(n-j)>= (l[n]-l[j])*(j-i):
                flag = False
                break
        for j in range(n+1,i): # n j i
            if (l[n]-l[j])*(j-i) >= (l[j]-l[i])*(n-j):
                flag=False
                break
            
        if flag:
            val+=1
            
    ans=max(ans,val)
print ans        
            
            
            
            
            
            
            
            
            
            
            
            
            
            
                
            
            