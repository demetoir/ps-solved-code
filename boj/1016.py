import sys
a,b=map(int,sys.stdin.readline().split())
l=[0]*(b-a+1)
for n in range(2,int(pow(b,0.5))+1):
    for j in range((n**2-a%n**2)%n**2,b-a+1,n*n):l[j]=1
c=0
for i in l:
    if i==0:c+=1
print(c)