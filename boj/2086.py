mod=1000000000
memo={1:1,2:1}
def fib(n):
    if n in memo: return memo[n]    
    k = n//2
    a = fib(k + 1)
    b = fib(k)
    if n % 2 == 1:
        memo[n] = (a*a + b*b)%mod
    else:
        memo[n] = (b*(2*a - b))%mod
    return memo[n]

a,b=map(int,raw_input().split())
print (fib(b+2)-fib(a+1)+mod)%mod        