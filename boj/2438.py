a=int(input())
a=27
l=[['*']*a]*a
c=["123456"]
print (c[0])
c[0]=0
print(c[0])
'''
for i in range(1,a):
    for j in range(a):
       if i%3==1 and j%3==1:
        l[i][j]=' '
'''
l[1][0]='0'
