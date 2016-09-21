m=[[-1]*31 for i in range(31)]
m[0][0]=1
def f(w,h):
    if w<0 or h<0: return 0
    if m[w][h]>-1:return m[w][h]
    m[w][h]=f(w-1,h+1)+f(w,h-1)
    return m[w][h]
while 1:
    a=int(input())
    if a==0:break
    print(f(a,0))