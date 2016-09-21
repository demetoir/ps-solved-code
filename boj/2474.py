m={0:0,1:1}
import sys
def f(n):
    if not n in m:m[n]=f(n-1)+f(n-2)
    return m[n]
a=int(sys.stdin.readline())
sys.stdout.write(str(f(a)))