n,m,t,k=map(int,raw_input().split())
l=[]
ans=0
for a in range(t):
    x,y=map(int,raw_input().split())
    l+=[(x,y)]
a,b=0,0
for x,y in l:
    l2=[]
    for x1,y1 in l:
        if x<= x1 <= x+k and y-k <= y1 <= y+k:
            l2+=[y1]
    for y1 in l2:
        val=0
        for y2 in l2:
            if y1<= y2 <= y1+k:
                val+=1
        if val >= ans:
            ans = max(ans,val)
            a,b=x,y1+k
            #print a,b,ans
print a,b
print ans


