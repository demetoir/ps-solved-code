def f(n):
 if n<0:return 0
 if n==0:return 1
 return f(n-1)+f(n-2)+f(n-3)
for T in range(int(input())):print(f(int(input())))