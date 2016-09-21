r,c=map(int,raw_input().split())
a,b=map(int,raw_input().split())

for R in range(r):
    l=""
    for C in range(c):
        if (R%2+C%2)==1:l+="."*b
        else:l+="X"*b

    for A in range(a):
        print l
