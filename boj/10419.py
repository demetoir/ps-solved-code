for T in range(input()):
    ans =0
    n=input()
    for i in range(1,50000):
        if i*(i+1)>n:break
        ans=i
    print ans