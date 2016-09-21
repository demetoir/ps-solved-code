n=int(input())
a=list(zip(map(int,input().split()),range(n)))
p=[0]*n
b=sorted(a,key=lambda i:i[0])
for i in range(n):p[b[i][1]]=str(i)
print(" ".join(p))
