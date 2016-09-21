N=input()

for i in range(2,N):
    if i*i>N:break
    if N%i==0:
        print N-N//i
        exit()
print N-1