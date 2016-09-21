def f(n,x,y):
    if n<1:return 0
    d=2**(n-1)
    s=((x//d)*2+y//d)*(d**2)
    return s+f(n-1,x%d,y%d)
while 1:
      try:
          n,x,y=map(int,input().split())
          print(f(n,x,y))
      except:
             break