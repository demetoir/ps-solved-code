import sys

def recursive(n):
    global line,memo,building
    if memo[n]>-1:return memo[n]
    l=0
    for i in line[n]:
        r=recursive(i)
        if r>l:l=r
    memo[n]=l+building[n]
    return memo[n]

N=1000
line=[[]for i in range(N+1)]
memo=[-1]*(N+1)
building=[0]+[[]for i in range(N+1)]

for _ in range(int(input())):
    N,K=map(int,input().split())
    line=[[]for i in range(N+1)]
    memo=[-1]*(N+1)
    building=[0]+list(map(int,input().split()))

    for _ in range(K):
        x,y=map(int,sys.stdin.readline().split())
        line[y]+=[x]

    w=int(input())
    print(recursive(w))

