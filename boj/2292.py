n=int(input())
for i in range (10**9):
    if n<=3*i*i+3*i+1:break
print(i+1)
