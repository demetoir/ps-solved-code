a,b,c= map(int, input().split())
d=int(input())
nc=(c+d)%60
d=(c+d)//60
nb=(b+d)%60
d=(b+d)//60
a=(a+d)%24
print(a,nb,nc)