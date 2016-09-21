



cache=[1]+[0]*k
def f(k):
    if k<0:
       return 0
    if cache[k]>0:
       return cache[k]
    ret=0
    for i in l:
        ret+=f(k-i)
    cache[k]=ret
    return ret
cache2=[1]+[0]*k
def f2(k):
    for i in range(k+1):
        for j in l:
            cache2[i+j]+=1
    return cache2[k]

def e():
    dl=[[ 1 if i%l[0]==0 else 0 for i in range(k+1)]]
    dl+=[[0]*(k+1) for i in range(n+1)]
    for i in range(1,n+1):
        t=l[i]
        for j in range(k+1):
            m=j//t
            if m==0:
               dl[i][j]=dl[i-1][j]
               continue
            for x in range(m+1):
                dl[i][j]+=dl[i-1][j-t*x]
    return dl

"""
n,k=map(int,input().split())
l=[int(input()) for i in range(n)]
l.sort()
"""



n=2

k=8

n=1

l=[1,2,5,10,20,25]
dl=e()
print(dl[n][k])

n+=1

l=[1,2]
print(f2(k))
print(cache2)
