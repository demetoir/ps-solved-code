import sys
def f(n):
    a=0
    for  i in range(2,n+1):
        t=n
        c=0
        while t%i==0:
            t=t//i
            c+=1

        a+=c
    return a
a=[]
for T in range(1001):
    a+=[f(T)]
for T in range(int(input())):
    sys.stdout.write(str(a[int(sys.stdin.readline())])+"\n")