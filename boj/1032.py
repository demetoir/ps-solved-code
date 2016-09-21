import sys
a=[]
for i in range(int(sys.stdin.readline())):a.append(sys.stdin.readline())
line = ""
if len(a)!=0:
    for i in range(len(a[0])-1):
        c=a[0][i]
        for j in range (1,len(a)):
            if c!=a[j][i]:
               line+='?'
               c=-1
               break
        if c!=-1:
           line+=c
print(line)