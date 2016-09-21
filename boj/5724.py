while 1:
    a=int(input())
    if a==0:break
    print(sum([i*i for i in range(a+1)]))