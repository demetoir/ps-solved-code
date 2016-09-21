N=(int(input())//100)*100
F=int(input())
for i in range(100):
    if (N+i)%F==0:break
print(str(i).zfill(2))