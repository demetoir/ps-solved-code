N,S=map(int,input().split())
l=list(map(int,input().split()))
l,r=l[:N//2],l[N//2:]
a,b={},{}

def f(n,setin,setout,val):
    if n==len(setin):
        if val not in setout:
            setout[val]=1
        else:
            setout[val]+=1
        return
    f(n+1,setin,setout,val+setin[n])
    f(n+1,setin,setout,val)
f(0,l,a,0)
f(0,r,b,0)

ans=0
if S==0:
    ans=-1
for i in a:
    if S-i in b:
        ans+=b[S-i]*a[i]

print(ans)
