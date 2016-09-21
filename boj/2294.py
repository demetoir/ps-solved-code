n,k=map(int,input().split())
coins=[int(input()) for i in range(n)]

coins.sort()

f=[10**6]*(k+1)

for coin in  coins:
    for i in range(coin,k+1,coin):
        f[i]=i//coin
def r(k):
    l=[f[k]]
    for coin in coins:
        if k<=coin:break
        l+=[f[k-coin]+f[coin]]
    f[k]=min(l)

def test():
    for i in range(1,k+1):
        r(i)
#print(f)
test()
print(-1 if f[k]==10**6 else f[k])
#print(f)