l=[]
for i in range(input()):
    l+=[raw_input()]
for s in l:
    r=""
    for c in s:
        r=c+r
    if r in l:
        print len(r),r[len(r)//2]
        exit()
        