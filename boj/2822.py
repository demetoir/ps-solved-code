import itertools
l=[]
for n in range(8):
    l+=[int(raw_input())]
ans1=-1
ans2=[]
for s in  itertools.combinations(range(8),5):
    score=0
    for i in s:
        score+=l[i]
    if ans1 < score:
        ans1=score
        ans2=list(s)
print ans1
print " ".join(str(i+1) for i in ans2)