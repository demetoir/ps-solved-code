a=[int(input()) for i in range(5)]
b=0
for i in a:b+=int(i)
print(b//5)
a.sort()
print(a[2])