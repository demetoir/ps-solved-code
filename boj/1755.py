trans=[9,4,8,7,2,1,6,5,0,3]
m,n=map(int,input().split())
l=[]
for i in range(m,n+1):
    s=str(i)
    ord=""
    for c in s:
        ord+=str(trans[int(c)])
    l+=[[ord,s]]
l.sort(key=lambda a:a[0])
c=0
for a,b in l:
    c+=1
    print(b,end=" ")
    if c==10:
        c=0
        print()
