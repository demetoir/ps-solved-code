a,b=input().split()
m=51
for j in range(len(b)-len(a)+1):
    c=0
    for i in range(len(a)):
        if a[i]!=b[i+j]:c+=1
    m=min(m,c)
print(m)