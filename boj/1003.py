m={0:1,1:1}
def f(n):
 if not n in m:m[n]=f(n-1)+f(n-2)
 return m[n]
print(f(int(input())))