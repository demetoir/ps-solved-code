b=[]
for i in range(7):
    a=int(input())
    if a%2==1:
       b.append(a)
if b:print(str(sum(b))+"\n"+str(min(b)))
else:print("-1")