def r(x,y):
    n=[[list(range(-1,2))] for i in range(3)]
    global matrix,check,r_count
    check[y][x]=1
    que=[(x,y)]
    if matrix[y][x]==0:
        return 0
    while que!=[]:
        x,y=que.pop(0)
        for b in range(-1,2):
            for a in range(-1,2):
                if check[y+b][x+a]==0 and matrix[y+b][a+x]==1:
                    que+=[(x+a,y+b)]
                    check[y+b][x+a]=1
    return 1
r_count=0
def next_location(x,y):
    global check
    for b in range(1,2+y):
        for a in range(1,2+x):
            if check[b][a]==0:return(a,b)
    return -1

while 1:
    x,y=map(int,input().split())
    if x==0 and y==0:break
    check=[[0]*(x+2)]
    matrix=[[0]*(x+2)]
    for i in range(y):
        matrix+=[[0]+list(map(int,input().split()))+[0]]
        check+=[[0]*(x+2)]
    check+=[[0]*(x+2)]
    matrix+=[[0]*(x+2)]
    count=0
    while 1:
        next_loc=next_location(x,y)
        if next_loc==-1:
            break
        a,b=next_loc
        r_count=0
        if r(a,b)==1:count+=1
    print(count)