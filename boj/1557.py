import math,sys



def is_prime(n):
    if n % 2 == 0 and n > 2:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True
l=[]
recursive_list=[]

def recursive(count,index,mul):
    global recursive_list

    if count==0:
       recursive_list+=[mul]
       return
    for i in range(index,L_size):
        if mul*l[i]>k:
           return
        recursive(count-1,i+1,mul*l[i])




#k=int(input())
k=10**10+10
root_k=int(k**0.5)
#print("k,root_k",k,root_k)

for i in range(2,root_k+1):
    if is_prime(i):
       l+=[i**2]

L_size=len(l)
#print(len(l))
#print(l)
set_list=[]
import profile
recursive_list=[]
total=0
cur_list=[]

def make_set_list():
    global set_list
    global recursive_list
    global total
    for i in range(1,len(l)+1):
        mul_list=[]
        recursive_list=[]

        recursive(i,0,1)

        total+=len(recursive_list)
        #print(i,recursive_list)

        if recursive_list==[]:
           return
        recursive_list.sort()
        set_list+=[recursive_list]


def get_number(cur):
    global set_list
    global cur_list
    cur_list=[]
    for innerset in set_list:
        temp=[]
        for i in innerset:
            if cur<i:
               break
            temp+=[i]
        cur_list+=[temp]

    sign=1
    total=0
    for inner in cur_list:
        for i in inner:
            number=cur//i
            total+=sign*number
        sign*=-1

    return cur-total

def binsearch(target ,hi,lo):
    mid = (hi+lo)//2
    number=get_number(mid)

    if number==target:
        return mid
    if mid ==10**10:
        return
    if  number>target:
        return binsearch(target,hi,mid)
    else:
        return binsearch(target,mid,lo)

make_set_list()
data=int(input())
#data=13
#profile.run("make_set_list()")

b=binsearch(data,0,10**10+1)


for i in range(10,-1,-1):
    if data==get_number(b-i):
        print(b-i)
        break;



