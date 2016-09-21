ans=0
n=input()
for B in range(1,501):
    for A in range(B,501):
        if A*A-B*B==n:
            ans+=1
print ans
