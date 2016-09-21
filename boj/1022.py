a,b,c,d=map(int,input().split())
m=[]
B=0
def f(i,j):
 L=max(abs(i),abs(j))
 p=(L*2-1)**2+1+L-1
 if L==i and i!=j:c=p-j
 elif L==-j and j!=-i:c=p-i+2*L
 elif L==-i and i!=j:c=p+j+4*L
 elif L==j and j!=-i:c=p+i+6*L
 else:c=1
 return c
for j in range(a,c+1):
 l=[]
 for i in range(b,d+1):l.append(f(i,j))
 if max(l)>B:B=max(l)
 m.append(l)
s="%"+str(len(str(B)))+"d"
for j in m:
    for i in j:print(s% (i),end=" ")
    print()