for i in range(int(input())):
    a,b=input(),input()
    n=0
    for i in range(len(a)):
        if a[i]!=b[i]:n+=1
    print("Hamming distance is %d."%n)