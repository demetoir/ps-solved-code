a=[str(i) for i in range(1111,10000)if "0"not in str(i)]

d={}
def mini(s):
    t=[]
    for _ in range(4):
        s=s[1:]+s[0]
        t+=[int(s)]
    return(min(t))

for i in a:
    d[mini(i)]=0

a=list(d)
a.sort()

print(a.index(mini("".join(list(map(str,input().split())))))+1)