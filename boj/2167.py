m,n=map(int,input().split())
s=[0]
for i in range(m):s+=[[0]+list(map(int,input().split()))]
for k in range(int(input())):
 i,j,x,y=map(int,input().split());m=0
 for f in range(i,x+1):m+=sum(s[f][j:y+1])
 print(m)