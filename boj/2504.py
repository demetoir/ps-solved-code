i=-1
s=input()

a,b=0,0
for c in s:
    if ord(c)<45: a+=1
    else:b+=1
def f(k):
    global i,s
    a=0
    while i<len(s)-1:
        i+=1;c=s[i]
        if c=="(":a+=f(2)
        elif c=="[":a+=f(3)
        elif c==")" and k==2:return 2 if a==0 else a*2
        elif c=="]" and k==3:return 3 if a==0 else a*3
        else:print(0);exit()
    return a

if a%2==0 and b%2==0:print(f(0))
else:print(0)