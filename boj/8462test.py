#import time
#import copy
#import numpy
import sys
"""
def bs(a,t,l,h):
    if h<l:return[h,-1]
    m=(h+l)//2
    if t<a[m]:return bs(a,t,l,m-1)
    elif t>a[m]:return bs(a,t,m+1,h)
    else:return[m,a[m]]
"""

p=lambda:map(int,sys.stdin.readline().split())
n,t=p()

c={}

#input and make dictionary

target_array=list(p())
line=[]
line_diction={}

#target_array=[4, 3, 1, 1, 1, 3, 1, 2]

line=[(2, 7),(1, 6),(3 ,8)]
line_diction={}
dicton_key=[]
"""
for i in range(t):
    line.append((0,9999))
"""

#start=time.time()
for i in range(t):

    L,R=line[i]
    L,R=L,R
    if  (R-L) not in line_diction:
        line_diction[R-L]=[]
    #[L,R,R-L+1,input_index,contents,sum,child_index]
    line_diction[R-L].append([L-1,R-1,R-L+1,i,{},0,n])

#dictionary sort
for i in line_diction:
    line_diction[i].sort(key=lambda a:a[0])
dicton_key=list(line_diction.keys())
dicton_key.sort()

#dictionary to list
line_list=[]
for i in dicton_key:
    line_list+=line_diction[i]
additional_child_list=[0]

#set child
for i in range(t-1,0,-1):
    #같은거 일떄
    if line_list[i][0]==line_list[i-1][0] and line_list[i][1]==line_list[i-1][1]:
       line_list[i][6]=i-1+10001
       continue
    #bust 일떄
    if line_list[i][0]-line_list[i-1][0]==1 and line_list[i][1]-line_list[i-1][1] and line_list[i][2]>1:
       line_list[i][6]=i-1
       continue
    #100밑에는 생략
    if line_list[i][2]<50:
       continue


    #child 가 있으면 생략
    if line_list[i][6]<n or line_list[i][6]<=0:
       continue

    bust_size=0
    child_index=-1
    for j in range(i-1,0,-1):
        max_bust=[]
        #1/3이상 겹치거나 포함 될때 까지만
        if line_list[i][2]-line_list[j][2]>50:
           break
        #또는 1000개 까지만
        if i-j>100:
            break

        #겹치는 부분 구함
        size=min(line_list[i][1],line_list[j][1])-max(line_list[i][0],line_list[j][0])+1

        if bust_size<size:
           bust_size=size
           child_index=j

    #겹치는 부분이 적을때
    if bust_size<100:
       continue
    #no chile
    if bust_size==0:
       continue
    #이미 co child 가 있을떄 이전것과 비교
    if line_list[i][6]<0:
       if bust_size > additional_child_list[line_list[i][6]][2] :
          line_list[i][6]=child_index
       continue

    #child 일떄
    if line_list[child_index][2]==bust_size:
       line_list[i][6]=child_index
    #co child 일때
    else:
         line_list[i][6]=-len(additional_child_list)
         line_list[child_index][6]=-len(additional_child_list)
         child=[max(line_list[i][0],line_list[j][0]),min(line_list[i][1],line_list[i][1]),bust_size,0,{},0,0 ]
         additional_child_list.append(child)

#additional_child_list구함
if len(additional_child_list)>1:
   for target in additional_child_list[1:]:
       content={}
       seq=list(range(additional_child_list[0],additional_child_list[1]+1))
       s=0
       for j in seq:
            if target_array[j] not in content:
               content[target_array[j]]=0
            s+=(content[target_array[j]]*2+1)*target_array[j]
            content[target_array[j]]+=1

       target_array[4]=content
       target_array[5]=s



#calculate sum
for target in line_list:
    #child 없을떄
    if target[6]==n:
       content={}
       s=0
       seq=list(range(target[0],target[1]+1))
    #co child 일때
    elif target[6]<0:
        child=additional_child_list[-target[6]]
        s=child[5]
        content=dict(child[4])
        seq=list(range(target[0],child[0]))+list(range(child[1]+1,target[1]))
    #같은거일떄
    elif target[6]>=10000:
        child=line_list[target[6]-10000]
        target[5]=child[5]
        target[4]=child[4]
        continue
    #child 있을떄
    else:
         child=line_list[target[6]]
         s=child[5]
         content=dict(child[4])
         seq=list(range(target[0],child[0]))+list(range(child[1]+1,target[1]+1))

    #배열의 힘 구함
    for j in seq:
        if target_array[j] not in content:
           content[target_array[j]]=0
        s+=(content[target_array[j]]*2+1)*target_array[j]
        content[target_array[j]]+=1

    if target[6]==n:
       target[4]=dict(content)
       target[5]=s
       continue
    #bust  처리
    if target[0]-child[0]==1 and target[1]-child[1] ==1:
        content[target_array[child[0]]]-=1
        s-=(content[target_array[child[0]]]*2+1)*target_array[child[0]]
        if content[target_array[child[0]]]==0:
            content.pop(target_array[child[0]])
    target[4]=dict(content)
    target[5]=s
#print(time.time()-start)


output=[0]*t
for i in line_list:
    output[i[3]]=i[5]
for i in output:
    print(i)

