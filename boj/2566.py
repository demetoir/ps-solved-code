a=[]
for i in range(3):
    a.append(list(map(int ,input().split())))
top=x=y=0
for i in range(3):
    for j in range(3):
        if top<a[i][j]:
            top=a[i][j]
            x=i+1
            y=j+1
print(top)
print(x,y)
