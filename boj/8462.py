import time

p=lambda:map(int,input().split())
#n,t=p();e=p();
c={}
n=1000
t=10000


#input and make dictionary
target_array=list(p())
line=[]
line_diction={}
for i in range(t):
    L,R=p()
    if  (R-L) not in line_diction:
        line_diction[R-L]=[]
    line_diction[R-L].append([L-1,R-1,R-L,i,{},0,-1])

#dictionary sort
for i in line_diction:
    i.sort(key=lambda a:a[0])

#dictionary to list
line_list=[]
for i in line_diction:
    line_list+=i

#set child
for i in range(n-1,-1,-1):
    for j in range(i,-1,-1):
        if line_list[i][0] >= line_list[j][0] and line_list[i][1] <= line_list[i][1]:
            line_list[i][6]=j
            break
#calculate sum
for target in line_list:

    if target[6]==-1:
       content={}
       s=0
       seq=list(range(target[0],target[1]+1))
    else:
         child=target[6]
         s=child[5]
         content=child[4]
         seq=list(range(child[0],target[0]))+list(range(child[1]+1,target[1]))

    for j in seq:
        if target_array[j] not in content:
           content[target_array[j]]=1
        s+=(content[target_array[j]]*2+1)*target_array
        content[target_array[j]]+=1
    target[4]=content
    target[5]=s


