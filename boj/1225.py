a,b=raw_input().split()
B=sum(int (i) for i in b)
print sum(int(i)*B for i in a)
