cnt=0
n=input()
while len(n)>1:
    cnt+=1;t=0
    for i in n:t+=ord(i)
    n=str(t-len(n)*48)
print(cnt)
print("YES" if int(n)%3==0 else"NO")