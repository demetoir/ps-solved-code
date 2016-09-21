import time
start =time.time()
Ttime= time.time()
count=0

def make_sangguen(n):
    s=0
    while n!=0:
        s+=(n%10)**2
        n=n//10
    if s>test_max:
       s=make_sangguen(s)
    return s

test_max=100000+1

test_min=10
line=[0]*test_max
line[1]=1
sline=[]
prime_number_list=[]
test=100000
for i in range(1,test + 1,2):
    o=i
    d={}
    if i%5==0:continue
    while 1:
          if i==1 or line[i]==1:
             #print(o,i,d)
             while d:
                   i,val=d.popitem()
                   line[i]= 1
                   sline+=[i]
             break
          if i in d or line[i]== -1:
             #print(o,i,d)
             while d:
                   line[d.popitem()[0]]= -1
             break
          d[i]=i
          i=make_sangguen(i)

print(time.time()-start)
start=time.time()
sline.sort()
for i in sline:

    #print(i,line[i])


    for div in [2]+list(range(3,int(i**0.5+1),2))+[int(i**0.5+1)]:
       if i%div==0:break
    if div==int(i**0.5+1):
      prime_number_list+=[i]
#print(prime_number_list)

print(time.time()-start)
print(len(sline))
print(len(prime_number_list))
prime_number_list.sort()
#print(prime_number_list)
#for i in prime_number_list:print(i)
print(time.time()-start)
print(time.time()-Ttime)



