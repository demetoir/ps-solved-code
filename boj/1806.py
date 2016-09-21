N,S=map(int,input().split())
l=list(map(int,input().split()))
s=0
sl=[0]
r=N+1
for i in l:s+=i;sl+=[s]
i=0
j=0
while j<N:
    if S<=sl[j+1]-sl[i]:r=min(r,j-i+1);i+=1
    else:j+=1
if r==N+1:r=0
print(r)