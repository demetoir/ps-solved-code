###this is can not solve to python
###use c or c++



import itertools
import math

index_set={}

for n in range(0,20+1,2):
    iset=list(itertools.combinations(range(n),n//2))
    index_set[n]=iset[:len(iset)//2]

out=[]
for testcast in range(int(input())):
    n=int(input())
    pair_list=[list(map(int,input().split())) for i in range(n)]

    x,y=0,0
    for i in range(n):
        x+=pair_list[i][0]
        y+=pair_list[i][1]
    total=[]
    for vectorset in index_set[n]:
        a,b=x,y
        for i in vectorset:
            a-=2*pair_list[i][0]
            b-=2*pair_list[i][1]
        total+=[math.sqrt(a*a+b*b)]

    out+=["%.6f"%round(min(total),6)]
print("\n".join(out))







