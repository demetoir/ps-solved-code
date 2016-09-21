
d,k=map(int,raw_input().split())
memo={1:1,2:1}
def fib(n):
    if n in memo:
        return memo[n]
    memo[n]=fib(n-1)+fib(n-2)
    return memo[n]
for i in range(1,31):
    fib(i)
ansa=0
ansb=0
for a in range(1,100000+1):
    if memo[d-2]*a>k:break
    s=k-memo[d-2]*a
    
    if s%memo[d-1]==0 and s//memo[d-1]>=a:
        print a
        print s//memo[d-1]
        break