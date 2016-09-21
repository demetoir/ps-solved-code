m={0:1,1:1}
def f(k):
 if k in m:return m[k]
 m[k]=f(k-1)+2*f(k-2)
 return m[k]
while 1:
 try:print(f(int(input())))
 except:break