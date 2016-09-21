N=int(input())
n=int(N**0.5)+1
seive=[1]*(N+1)
if N==1:
    print(0)
    exit()

seiveList=[]
for i in range(2,N+1):
    if seive[i]==0:continue
    seiveList+=[i]
    for j in range(2*i,N+1,i):
        seive[j]=0
 


 
#print(len(seiveList))
i=-1
j=0
s=seiveList[0]
count=0
#print(seiveList)
seiveList+=[0]
while 1:
    if j==len(seiveList)-1:break
    #print(s,i,j)
    if s==N:
        count+=1
        i+=1
        s-=seiveList[i]
 
    elif s<N:
        j+=1
        s+=seiveList[j]
 
    elif s>N:
        i+=1
        s-=seiveList[i]
 
print(count)