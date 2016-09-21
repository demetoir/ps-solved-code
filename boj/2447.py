a,l,b=int(input()),["*"*a+"\n" for i in range(a)],1
while b!=a:
 for i in range(b,a,b*3):
  x=i
  for j in range(b,a,b*3):
   y=j
   for c in range(x,x+b):l[c]=l[c][:y]+" "*b+l[c][y+b:]
 b*=3
print("".join(l))