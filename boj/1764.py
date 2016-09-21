a,b=map(int,input().split())
la={};lb={};s=[]
for i in range(a):la[input()]=0
for i in range(b):lb[input()]=0
for i in la:
    if i in lb:s+=[i]
s.sort()
print(len(s))
for i in s:print(i)