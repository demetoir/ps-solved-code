#print 8**10
s,n,k,r1,r2,c1,c2=map(int,raw_input().split())
l = [0]*((n-k)//2) + [1]*k + [0]*((n-k)//2)

for j in range(r1,r2+1):
    ansline=""
    for i in range(c1,c2+1):
        color="0"
        a,b=i,j
        for t in range(s,0,-1):
            d=n**(t-1)
            #print a,b,d,a//d,b//d
            if l[a//d]==1 and l[b//d]==1:
                color = "1"
                break
            a=a%d
            b=b%d
            
            
        ansline+=color
    print ansline
        


