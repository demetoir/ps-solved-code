m,n=map(int,raw_input().split())
raw_input()
ans=[0]*5
for M in range(m):
    l=[0]*n
    for N in range(4):
        a=raw_input()[1:-1].split("#")
        #print a
        for i in range(n):
            if a[i]=="****":
                l[i]+=1
    #print l
    for i in l:
        ans[i]+=1
    raw_input()
print " ".join(map(str,ans))