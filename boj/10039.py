s=0
for i in range(5):
    a=int(input())
    s=s+a if a>40 else s+40
print(s//5)