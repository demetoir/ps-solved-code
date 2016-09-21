i,j=map(int,input().split())

if i>j:i,j=j,i
print(int((j+i)*(j-i+1)/2))