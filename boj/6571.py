dp=[0,1,2]+[0]*500

import sys

def f(n):
    if dp[n]>0:return dp[n]
    dp[n]=f(n-1)+f(n-2)
    return  dp[n]

f(500)

#for i in dp[1:]:print(i)
while 1:
    a,b=map(int,sys.stdin.readline().split())
    if (a,b)==(0,0):break
    c=0
    for i in dp[1:]:
        if i>10**100:break
        if a<=i and i<=b:c+=1
    print(c)