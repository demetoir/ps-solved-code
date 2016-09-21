import sys
a,b,c=0,0,0
A,B,C=0,0,0
for i in range(int(input())):
    x,y,z=map(int,sys.stdin.readline().split())
    a,b,c=min(a,b)+x,min(a,b,c)+y,min(b,c)+z
    A,B,C=max(A,B)+x,max(A,B,C)+y,max(B,C)+z
print(max(A,B,C),min(a,b,c))