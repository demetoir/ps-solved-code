import profile
import sys
import threading

threading.stack_size(67108864) # 64MB stack
sys.setrecursionlimit(2 ** 20) # something real big
                               # you actually hit the 64MB limit first
                               # going by other answers, could just use 2**32-1

# only new threads get the redefined stack size
#thread = threading.Thread(target=main)

#thread.start()
#sys.setrecursionlimit(1000000)
l=[]

def make(n,c):
    global l
    l+=[n*10+4,n*10+7]
    if c==0:return
    make(n*10+4,c-1)
    make(n*10+7,c-1)
make(0,5)
l.sort()


l=list(reversed(l))


def f(n):
    global found,ans
    if n==0:
        found=True
        return True
    for i in l:
        if i<=n:
            f(n-i)
        if found==True:
            ans+=[i]
            return True
    return False



found=False
ans=[]
n=11
f(n)
print(n,sum(ans),len(ans),ans)