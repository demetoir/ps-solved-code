
total,n,s,a=[0]*10,0,"",int(input())
while 10**n<=a:
    for i in range(10):total[i]+=(a//10**(n+1))*(10**n)
    total[0]-=10**n
    last=((a%(10**(n+1)))//10**n)
    for i in range(last):total[i]+=10**n
    total[last]+=a%(10**n)+1
    n+=1
for i in total:s+=str(i)+" "
print(s)


"""
test_total=[0]*10
test_total_set=[]
test=[]
test_string=""
test_string_set=[]
test_n=1001
for i in range(1,test_n+1):
    test.append([j for j in range(1,i)])
for i in test:
    test_string=""
    for j in i:
        test_string+=str(j)
    test_string_set.append(test_string)
for i in test_string_set:
    test_total=[0]*10
    for j in i:
        test_total[int(j)]+=1
    test_total_set.append(test_total)

def f(a):
    total=[0]*10
    n=0
    #a=int(input())
    #if a==1:return [0,1]+[0]*8
    while 10**n<=a:
        for i in range(10):
            total[i]+=(a//10**(n+1))*(10**n)
        total[0]-=10**n
        last=((a%(10**(n+1)))//10**n)
        for i in range(last):
            total[i]+=10**n
        total[last]+=a%(10**n)+1
        n+=1
    return total


for i in range(1,test_n):
    f_total=f(i)
    flag=0
    print(i)
    for j in range(10):
        if  f_total[j]!=test_total_set[i][j]:
            print(i,"different")
            print("f_total",f_total)
            print("test_total",test_total_set[i])
            flag=1
            break
    if flag==1:
       break

"""
