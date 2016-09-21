n=input()
l=[]
ans=""

def f(x,y,s):
    global ans
    total=0

    if s==0:return

    for i in range(x,x+s):
        for j in range(y,y+s):
            total+=l[j][i]

    if total== s*s:
        ans+="1"
        return
    elif total==0:
        ans+="0"
        return
    else:
        s=s//2
        ans+="("
        f(x,y,s)
        f(x+s,y,s)
        f(x,y+s,s)
        f(x+s,y+s,s)
        ans+=")"


for i in range(n):
    t=[]
    for c in raw_input():t+=[int(c)]
    l+=[t]

f(0,0,n)
print ans