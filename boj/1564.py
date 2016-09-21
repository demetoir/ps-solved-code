def f(n):
    l=[i for i in range(n+1)]
    k=5
    five=0
    while k<n:
          five+=n//k
          for i in range(k,n+1,k):
              l[i]=l[i]//5
          k*=5
    for i in range(2,2*five+1,2):
        l[i]=l[i]//2
    return l
def p(n):
    s=1
    l=f(n)[1:]
    a=1000
    for i in l:
        s*=i
        s=s%10**5
    print(s%10**5)
p(int(input()))

