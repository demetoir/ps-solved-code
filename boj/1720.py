n=int(input())
m=[1]+[-1]*n
def f(n):
    if n<0:return 0
    if m[n]>-1:return m[n]
    m[n]=f(n-1)+2*f(n-2)
    return m[n]
o=f(n)
if n%2==1:o+=f(n//2)
else:o+=f(n//2+1)
print(o//2)