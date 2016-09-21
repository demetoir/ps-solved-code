n=int(input())
p=[[] for i in range(n+1)]
c=0
for k in range(int(input())):
    l=list(map(int,input().split()))[1:]
    if 1 in l:
        c+=1
        for i in l:p[i]+=[n+c]
    else:
        s=[]
        for i in l:s+=p[i]
        for i in l:p[i]=list(set(s))
print(1)
for i in range(2,n+1):
    if len(p[i])==c:print(i)
