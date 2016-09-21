for _ in range(int(input())):
    n,d,a,b,f=map(float,input().split())
    print(int(n),"%.2f"%(f/((a+b)/d)))