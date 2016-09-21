n=int(input())
crane=list(map(int,input().split()))
m=int(input())
box=list(map(int,input().split()))
 
crane.sort()
box.sort()
 
time=0
while 1:
    movelist=[]
    for c in crane:
        carry=-1
        for b in box:
            if b>c:break
            carry=b
 
        if carry>-1:
            movelist+=[carry]
            box.remove(carry)
 
    if movelist==[]:break
    time+=1
 
 
if box==[]:print(time)
else:print(-1)