a=input()
ans=0
for j in range(1000):
    for i in range(1,1234567):
        if i>a:break
        a-=i
        ans+=1

print ans
