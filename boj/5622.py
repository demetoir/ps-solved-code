s=input()
t=0
a=["ABC","DEF","GHI","JKL","MNO","PQRS","TUV","WXYZ"]
for c in s:
    for i in range(8):
        if c in a[i]:break
    t+=i+3
print(t)


