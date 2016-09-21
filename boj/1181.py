d={}
for i in range(int(input())):
    s=input();d[s]=len(s)
s=[[]for i in range(51)]
for i in d:s[d[i]]+=[i]
for i in s:
 if i!=[]:
    i.sort();print("\n".join(i))
