ans=0
cur=0
for i in range(10):
    cur+=input()
    if abs(100-ans)> abs(100-cur):
        ans=cur
    elif abs(100-ans)== abs(100-cur):
        ans=max(cur,ans)
print ans