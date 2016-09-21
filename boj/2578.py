
b=[list(map(int,input().split())) for i in range(5)]
s=[]
for i in range(5):
    s+=list(map(int,input().split()))

def x(n):
    global b
    for i in range(5):
        for j in range(5):
            if b[i][j]==n:b[i][j]=0

def check():
    global b
    ret=0

    for i in range(5):
        v=0;h=0
        for j in range(5):v+=b[i][j];h+=b[j][i]
        if v==0:ret+=1
        if h==0:ret+=1

    l=0
    r=0
    for i in range(5):
        l+=b[i][i];r+=b[i][4-i]
    if l==0:ret+=1
    if r==0:ret+=1

    return ret


for i in range(25):
    x(s[i])
    if check()>2:
        break
print(i+1)

