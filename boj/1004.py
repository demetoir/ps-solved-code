t=lambda x,y:(cx-x)**2+(cy-y)**2-r**2
m=lambda:map(int,input().split())
for s in range(int(input())):
    x1,y1,x2,y2=m();c=0
    for i in range(int(input())):
        cx,cy,r=m()
        if t(x1,y1)*t(x2,y2)<0:c+=1
    print(c)