for t in range(int(input())):
    word=[]
    for i in range(int(input())):
        word+=[input()]
    print("Scenario #"+str(t+1)+":")
    l=[]
    for i in range(int(input())):
        l=list(map(int,input().split()))
        s=""
        for j in l[1:]:s+=word[j]
        print(s)
    print()
