n=int(input());k=int(input());m=[[1]*(n+2)]
for i in range(n):m+=[[1]+[0]*n+[1]]
m+=[[1]*(n+2)];f=[0,1,0,-1];g=f[1:]+[0];d=0;c=n**2;x,y=1,1
for i in range(n**2):
 if m[y+g[d]][x+f[d]]!=0:d=(d+1)%4
 if c==k:a=x;b=y
 m[y][x]=c;y+=g[d];x+=f[d];c-=1
for i in m[1:-1]:print(" ".join(map(str,i[1:-1])))
print(b,a)