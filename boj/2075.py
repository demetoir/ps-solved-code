n=input()

l=[]
for i in range(n):
    l+=map(int,raw_input().split())
l.sort()
print l[n*n-n]

