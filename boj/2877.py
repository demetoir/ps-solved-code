
k=int(input())
n=1
while k>2**n:k-=2**n;n+=1
k-=1
s='{0:b}'.format(k).zfill(n)
s=s.replace("0","4")
s=s.replace("1","7")
print(s)