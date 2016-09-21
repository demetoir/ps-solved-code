import sys
sys.setrecursionlimit(100000)

"""
n=int(input())
s=list(map(int,input().split()))
"""
n=500
s=[i for i in range(n)]
cache=[[-1]*(n+1) for i in range(n+1)]
stack=[]
top= -1
def find3(l,r):
    global s
    if l>=r:
       return 0
    if cache[l][r]>-1:
       return cache[l][r]
    ret=10000
    while ((s[l]==s[r])and(l<r)):
          l+=1
          r-=1
    if l>=r:
       ret=0
    cache[l][r]=min(ret,find3(l+1,r)+1,find3(l,r-1)+1)
    return cache[l][r]

cache4=[[-1]*(n+1) for i in range(n+1)]
stack=[]
top= -1
def find4(l,r):


import profile
profile.run("print(find3(0,len(s)-1))")










