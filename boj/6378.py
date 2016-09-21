while 1:
    a= input()
    if a=="0":break
    while 1:
        if len(a)==1:break
        total=0
        for i in a:total+=int(i)
        a=str(total)
    print(a)
