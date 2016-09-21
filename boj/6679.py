l=lambda n,d:n%d+l(n//d,d) if n>0 else 0
for i in range(1000,10000):
    if l(i,12)==l(i,16)==l(i,10):print(i)