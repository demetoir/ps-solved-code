T=int(input())
tile={0:1,1:1}
def findN(n):
    if n in tile:
        return tile[n]

    ret=0

    if n-1>0:
        ret+=findN(n-1)

    if n-2>0:
        ret+=findN(n-2)*4

    for i in range(3,n):
        ret+=findN(n-i)*(3-i%2)
    tile[n]=ret
    return ret

while T:
    T-=1
    n=int(input())
    print(findN(n+1))
