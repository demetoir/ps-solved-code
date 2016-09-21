N,M=map(int,input().split())
l=[]
c=[0]*(1000+1)
for i in range(N):l+=[int(input(),2)]
k=int(input())
def f(s):
    a=0
    for i in l:a=a+1if(s^i)==(1<<M)-1 else a
    return a
def b(a):
    t=0
    while a>0:a&=(a-1);t+=1
    return t

for j in range(0,1000+1,2):c[j]=f(0)
for i in l:
    s=i^((1<<M)-1);n=b(s)
    for j in range(n,1000+1,2):c[j]=max(f(s),c[j])
print(c[k])