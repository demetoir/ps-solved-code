n,m=map(int,input().split())
l=list(map(int,input().split()))
c=0
total=0
start=-1
end=-1
while 1:
    if total<m:
        end+=1
        if end==n:break
        total+=l[end]
    elif total==m:
        start+=1
        total-=l[start]
        c+=1
    elif total>m:
        start+=1
        total-=l[start]
print(c)

"""

n,m=map(int,input().split())
l=list(map(int,input().split()))
c=0
total=0
start=-1
end=-1
while 1:
    if total<m:
        end+=1
        if end==n:break
        total+=l[end]
        continue
    if total==m:
        start+=1
        total-=l[start]
        c+=1
        continue
    if total>m:
        start+=1
        total-=l[start]
        continue

print(c)
"""