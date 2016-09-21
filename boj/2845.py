l,p=map(int,raw_input().split())
a=list(map(int,raw_input().split()))
b=[]
for i in a:b+=[i-l*p]
print " ".join(str(i)for i in b)