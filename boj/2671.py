a=[[1,8,3,4,4,1,7,4,-1]]+[[2,0,8,8,5,6,6,0,-1]]
while 1:
    try:
        s=raw_input()
    except:break
    p=0
    for i in s:
        p=a[int(i)][p]
        if p==8:
            break
    if p==5 or p==6 or p==0:
        print("SUBMARINE")
    else:
        print("NOISE")

