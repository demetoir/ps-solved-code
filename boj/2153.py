s=raw_input()
n=0

for c in s:
    if ord(c)>=97:n+= ord(c)-96
    else:n+=(ord(c)-65)+27

ans=True

for i in range(2,n):
    if i*i>n:break
    if n%i==0:ans=False
        
if ans:print "It is a prime word."
else:print "It is not a prime word."
        