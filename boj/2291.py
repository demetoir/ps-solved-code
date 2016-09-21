memo=[[[-1]*300 for j in range(300)]for i in range(12)]
N,M,k=map(int,raw_input().split())
l=[]
def f(n,m,cur):
    ret = memo[n][m][cur]
    if ret > -1:
        return ret
    if n==0 and m==0:
        return 1
 
    ret=0
    if cur > m :return 0
 
    for i in range(cur,m+1):
        ret += f(n-1,m-i,i)
    memo[n][m][cur]=ret
    return ret
 
#f(N,M,1)
n,m,cur=N,M,1
ans=1
start,end=1,0
for n in range(N,0,-1):
    cur=ans
    for i in range(cur,m+1):
        end += f(n-1,m-i,i)
        if start <= k <= end:
 
            ans = i
            start = end - f(n-1,m-i,i) +1
            end -= f(n-1,m-i,i)
            break
 
 
    l+=[ans]
    m-=ans
print " ".join(str(i) for i in l)