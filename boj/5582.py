A=raw_input()
B=raw_input()

memo=[[0 for i in range(len(A)+1)] for j in range(len(B))]

for i in range(len(A)):
    if A[i]==B[0]:
        memo[0][i]=1

for i in range(len(B)):
    if B[i]==A[0]:
        memo[i][0]=1

ans=0
for j in range(1,len(B)):
    for i in range(1,len(A)):
        if A[i]==B[j]:
            memo[j][i]=memo[j-1][i-1]+1
            if ans<memo[j][i]:ans=memo[j][i]
            
print ans