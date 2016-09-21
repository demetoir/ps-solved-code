n=input()

for i in range(n):
    a,b=raw_input().split()
    a=a.lower()
    b=b.lower()
    A={}
    B={}
    for c in a:
        if c not in A:
            A[c]=1
        else:
            A[c]+=1
            
    for c in b:
        if c not in B:
            B[c]=1
        else:
            B[c]+=1
    if A==B:
        print a+" & "+b+" are anagrams."
    else:
        print a+" & "+b+" are NOT anagrams."

    
