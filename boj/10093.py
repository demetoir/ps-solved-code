a,b=map(int,input().split())
if a>b:a,b=b,a
l=[str(i) for i in range(a+1,b)]
print(len(l))
print(" ".join(l))