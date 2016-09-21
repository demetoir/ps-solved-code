def check(word,n):
    ret=0
    a=[0]*124
    b=[0]*124
    for i in range(len(word)):
        a[ord(s[n-len(word)+i])]+=1
        b[ord(word[i])]+=1
        if s[n-len(word)+i]!=word[i]:ret+=1
    if a!=b:return INF
    return ret

s=input()
INF=987654321
memo=[0]+[-1]*50
words=[input() for i in range(int(input()))]
def f(n):
    if memo[n]>-1:return memo[n]
    ret=INF
    for word in words:
        if len(word)<=n:ret=min(ret,check(word,n)+f(n-len(word)))
    memo[n]=ret
    return ret
if f(len(s))==INF:print(-1)
else:print(f(len(s)))

