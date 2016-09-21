s=lambda:list(map(int,input().split()))
input()
a={}
for i in s():a[i]=0
input()
m=s()
for i in m:print(1 if i in a else 0)