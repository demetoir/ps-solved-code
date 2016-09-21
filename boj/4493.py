for T in range(input()):
    n=input()
    A,B=0,0
    for N in range(n):
        a,b=raw_input().split()
        if a==b:continue
        if (a=="R" and b=="S" )or (a=="P"and b=="R") or (a=="S"and b=="P"):
            A+=1
        else:B+=1
    if A>B:print "Player 1"
    elif A<B:print "Player 2"
    else:print "TIE"