input()
d={}
c=0
for i in list(map(int,input().split())):
    if i in d:c+=1
    else:d[i]=0
print(c)