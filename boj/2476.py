m=[]
for _ in range(int(input())):
    a,b,c=map(int,input().split())
    if a==b==c:m+=[10**4+1000*a]
    elif a!=b and b!=c and c!=a:m+=[100*max(a,b,c)]
    else:m+=[1000+100*sorted([a,b,c])[1]]
print(max(m))