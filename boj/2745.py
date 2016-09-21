n,x=raw_input().split()
x=int(x)
ans=0
for c in n:
    i=ord(c)
    if i>=65:ans=ans*x+ i-55
    else:ans=ans*x+i-48
print ans