n=input()
l=[]
for i in range(n):
    x,y=map(int,raw_input().split())
    l+=[(x,y,i+1)]
l.sort()
 
ans_d=-1
ans_a=0
ans_b=n
x,y=0,0
for i in range(n-1):
    x1,y1,a=l[i]
    x2,y2,b=l[i+1]
    d=abs(y2-y1)/float(abs(x1-x2))
     
    if a>b:
        a,b=b,a
        x1,y1=x2,y2

    if d>ans_d or (d==ans_d and a<ans_a):
        ans_d=d
        ans_a=a             
        x,y=x1,y1

for i in range(n):
    a,b,c=l[i]
    if c==ans_a:continue
    d=abs(y-b)/float(abs(x-a))
    if d<ans_d:continue
    if c<ans_b:ans_b=c   
        
   
print ans_a,ans_b