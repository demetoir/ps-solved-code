n,p=map(int,input().split())
c=n
a=[]
while c not in a:
      a.append(c)
      c=(c*n)%p
print(len(a)-a.index(c))