a=0
n=int(input())
for i in range(1,2000):
    a=i*i*2-2*i+1+a
    if a>n:
        print(i-1)
        break