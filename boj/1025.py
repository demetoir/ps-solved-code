def check(x,y):
    global n,m
    if x>=m or x<0:
        return False
    if y>=n or y<0:
        return False
    return True

def isSquare(n):
    if int(n**0.5)**2==n:
        return True
    return False
square_list=[]
n,m=map(int , input().split())
board=[]
for i in range(n):
    b=[]
    for j in input():
        b+=[int(j)]
        if isSquare(int(j))==True:square_list+=[int(j)]
    board+=[b]


for x in range(10):
    for y in range(10):
        for dx in range(-10,10):
            for dy in range(-10,10):
                number=0
                for i in range(10):
                    if check(x+dx*i,y+dy*i)==False:
                        break
                    number=number*10+ board[y+dy*i][x+dx*i]
                    if  isSquare(number)==True:
                        square_list+=[number]

#for s in square_list:  print(s)

if len(square_list)==0:
    print(-1)
else:
    print(max(square_list))


