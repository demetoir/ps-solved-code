for T in range(input()):
    n=input()
    l=sum(map(int,raw_input().split()))
    
    for i in range(1,1234):
        if n<l:
            print i
            break
        l*=4
     