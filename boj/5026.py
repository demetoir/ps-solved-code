for T in range(input()):
    s=raw_input()
    if s=="P=NP":
        print "skipped"
    else:
        a,b=map(int,s.split("+"))
        print a+b