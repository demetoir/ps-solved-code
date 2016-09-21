n=int(input())
s=0
x=[]
y=[]
for i in range(n):
    a,b=map(int,input().split())
    x+=[a]
    y+=[b]
x+=[x[0]]
y+=[y[0]]
for i in range(n):s+=x[i]*y[i+1]-x[i+1]*y[i]
print(round(abs(s/2),1))
