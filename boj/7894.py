import math
for T in range(int(input())):
    n=int(input())
    a=0
    for i in range(1,n+1):a+=math.log(i,10)
    print(int(a)+1)