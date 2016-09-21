import sys
n=1000000
sieve=[0,0]+[1]*n

for i in range(2,n):
    if sieve[i]==0:continue
    for j in range(i+i,n+1,i):
        sieve[j]=0

a,b=map(int,sys.stdin.readline().split())
line=[]

for i in range(a,b+1):
    if sieve[i]==1:
        line+=[str(i)]

print("\n".join(line)+"\n")