memo={0:1,1:1,2:2,3:4}
def f(x):
    if x in memo:return memo[x]
    memo[x]=f(x-1)+f(x-2)+f(x-3)+f(x-4)
    return memo[x]
for T in range(input()):
    print f(input())
