n,k=map(int,input().split())
result=[]
for dummy in range(n):
    d=list(map(int,input().split()))
    if d[0]==k:target,x,y,z=d
    result+=[d]
out=0
for numer,a,b,c in result:
    if a>x or (a==x and b>y) or (a==x and b==y and c>z): out+=1
print(out+1)

