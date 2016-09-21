n,r1,c1,r2,c2=map(int,input().split())
a,b=(2*n-1)//2,(2*n-1)//2

for i in range(r1,r2+1):
    s=""
    for j in range(c1,c2+1):
        y=i%(2*n-1)
        x=j%(2*n-1)
        alpha=(abs(a-x)+abs(b-y))
        if alpha<n:
            s+=chr(alpha%26+97)
        else:
            s+="."
    print(s)

