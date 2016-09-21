
number_list=[]
line_list=[6,2,5,5,4,5,6,3,7,5]
target=0

def high(s,cur,n):
    global number_list,target
    if n==0 and s>a:
        number_list+=[s]
        return 1
    for i in range(10):
        if cur + line_list[i] + (n-1)*2 > target:continue
        if cur + line_list[i] + (n-1)*7 < target:continue
        #print( (s*10+i)*10**(n-1) +10**(n-1)-1,a)

        if (s*10+i)*10**(n-1) +10**(n-1)-1< a:
            #print( (s*10+i)*10**(n-1),target)
            continue

        if high(s*10+i,cur+line_list[i],n-1)==1:
            return 1

def low(s,cur,n):
    global number_list,target,a
    if n==0 :
        number_list+=[s]
        return 1
    for i in range(10):
        if cur + line_list[i] + (n-1)*2 > target:continue
        if cur + line_list[i] + (n-1)*7 < target:continue


        if low(s*10+i,cur+line_list[i],n-1)==1:
            return 1

a=input()

target=0
for i in a:
    target+=line_list[int(i)]


n=len(a)
a=int(a)



low(0,0,n)
number_list+=[a]
high(0,0,n)


out=number_list[2%(len(number_list))]

#print(number_list)
if out>a:
    print(out-a)
elif out<a:
    print(10**n-a+out)
else:
    print(10**n)








