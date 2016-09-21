m,n=map(int,input().split())
a=[0]
for i in range(m):a.append(input())
b=dict()
s=""
for i in range(1,len(a)):b[a[i]]=i
for i in range(n):
    t=input()
    if t[0]>='0'and t[0]<='9':s+=a[int(t)]+"\n"
    else:s+=str(b.get(t))+"\n"
print(s)