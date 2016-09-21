n,m=map(int,raw_input().split())
ll=[]
for i in range(n):
    s=raw_input()
    l=[]
    for c in s:
        l+=[c]
    ll+=[l]
h=n
v=m

for i in range(n):    
    for j in range(m):
        if ll[i][j]=="X":
            h-=1
            break
   
    
for j in range(m):
    for i in range(n):
        if ll[i][j]=="X":
            v-=1
            break

print max(h,v)




         