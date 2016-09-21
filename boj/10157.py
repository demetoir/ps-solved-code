c,r=map(int,raw_input().split())
k=input()

x,y=0,-1
if k>c*r:
    print 0
    exit()
cur=0
a,b=c-1,r
s=1    
while 1:
    for i in range(b):
        y+=1*s
        cur+=1        
        if cur==k:
            print x+1,y+1
            exit()
    b-=1
    for i in range(a):
        x+=1*s
        cur+=1
        if cur==k:
            print x+1,y+1
            exit()
    a-=1
    s=-1*s      
            
        