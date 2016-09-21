n=input()

adj=[]
for i in range(n):
    l=[]
 
    for c in raw_input():
        if c=="Y":
            l+=[True]
        else:
            l+=[False]
    adj+=[l]

ans=0
for i in range(n):
    friend={}
    for f in range(n):
        if adj[i][f]:
            friend[f]=1
            for f2 in range(n):
                if adj[f][f2]:
                    friend[f2]=1
    if i in friend:
        ans=max(ans,len(friend)-1)
    else:
        ans=max(ans,len(friend))

print ans
        