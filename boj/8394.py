d={0:1,1:1}
def f(n):
    if n in d:return d[n]
    d[n]=f(n-1)+f(n-2)
    return d[n]
print(f(int(input())%60)%10)