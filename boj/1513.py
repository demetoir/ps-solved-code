N,M,K=map(int,input().split())
ans=[0]*51
memo=[[0]*(N+1) for i in range(M+1)]
l=[]
D={}
start=[0]*100
mid=[0]*100
end=[0]*100
s_e=0

for i in range(K):
    l+=[list(map(int,input().split()))]
    a,b=l[i]
    D[(a,b)]=i

def set(a,b,c,d):
    for i in range(a,c+1):
        for j in range(b,d+1):memo[j][i]=-1
    for x,y in l:memo[y][x]=0
    memo[b][a]=1
    memo[d][c]=-1

def f(x,y):
    if memo[y][x]>=0:return memo[y][x]
    memo[y][x]=(f(x-1,y)+f(x,y-1))%1000007

    return memo[y][x]


memo=[[0]*(N+1) for j in range(M+1)]
set(1,1,N,M)
memo[1][1]=1
end[i]=f(N,M)
s_e=f(N,M)

#start
for i in range(K):
    c,d=l[i]
    if (c,d)==(1,1):
        start=[0]*100
        start[i]=1
        s_e=0
        break
    memo=[[0]*(N+1) for j in range(M+1)]
    set(1,1,c,d)
    memo[1][1]=1
    start[i]=f(c,d)

#end
for i in range(K):
    a,b=l[i]
    if (a,b)==(N,M):
        end=[0]*100
        end[i]=1
        s_e=0
        break
    memo=[[0]*(N+1) for j in range(M+1)]
    set(a,b,N,M)
    memo[b][a]=1
    end[i]=f(N,M)
#mid
for i in range(1,K):
    a,b=l[i-1]
    c,d=l[i]
    memo=[[0]*(N+1) for j in range(M+1)]
    set(a,b,c,d)
    memo[b][a]=1
    mid[i]=f(c,d)
"""
print("start",start)
print("end",end)
print("mid",mid)
"""
ans[0]=s_e%1000007
for i in range(K):
    for j in range(K):
        if i>j:continue
        total=start[i]

        #print(i,j,total)
        for path in mid[i+1:j+1]:
            #print(path)
            total=(total*path)%1000007

        total=(total*end[j])%1000007
        ans[j-i+1]=(total+ans[j-i+1])%1000007


#print("ans",ans)
print(" ".join([str(i) for i in ans[:K+1]]))
"""
1 1 1
1 1

50 50 48
2 2
3 3
4 4
5 5
6 6
7 7
8 8
9 9
10 10
11 11
12 12
13 13
14 14
15 15
16 16
17 17
18 18
19 19
20 20
21 21
22 22
23 23
24 24
25 25
26 26
27 27
28 28
29 29
30 30
31 31
32 32
33 33
34 34
35 35
36 36
37 37
38 38
39 39
40 40
41 41
42 42
43 43
44 44
45 45
46 46
47 47
48 48
49 49


"""







