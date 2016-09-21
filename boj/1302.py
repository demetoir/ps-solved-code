a={}
for i in range(int(input())):s=input();a[s]=a[s]+1 if s in a else 1
print(sorted([i for i in a if a[i]==max(a.values())])[0])