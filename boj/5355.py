n=input()


for i in range(n):
    l=raw_input().split()
    a=float(l[0])
    for d in l[1:]:
        if d=="#":
            a-=7
        elif d=="%":
            a+=5
        elif d=="@":
            a*=3

    print "%0.2f"%a