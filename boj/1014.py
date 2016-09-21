l=[]
def make(n,a,k):
    global l
    if n==0:
        l+=[(a,k)]
        return
    make(n-1,a*2,k)
    if a%2==0:
        make(n-1,a*2+1,k+1)

def check(a,b):
    global M
    for i in range(M-1):
        if ((a|b)&3<<i)==3<<i:
            return False
    return True

for T in range(int(input())):
    N,M=map(int,input().split())
    Class=[]
    for i in range(N):
        a=0
        for c in input():
            if c==".":a=a*2
            else:a=a*2+1
        Class+=[a]
    l=[]
    make(M,0,0)
    memo=[l[:] for i in range(N)]
    #print(memo)

    for i in range(len(memo[0])):
            cur,cur_val=memo[0][i]
            if cur&Class[0]>0:
                memo[0][i]=(cur,0)


    for n in range(1,N):
        for i in range(len(memo[n])):
            cur,cur_val=memo[n][i]
            if cur&Class[n]>0:
                memo[n][i]=(cur,0)
                continue
            maxval=0

            for j in range(len(memo[n-1])):

                pre,pre_val=memo[n-1][j]

                if check(pre,cur)==True:
                    maxval=max(maxval,pre_val)

            memo[n][i]=(cur,maxval+cur_val)
    #for i in memo:print(i)
    print(max(memo[N-1],key=lambda a:a[1])[1])