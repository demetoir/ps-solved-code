n=input()
score=[(-1,-1)]*1001
country=[0]*1000
ans=0
for i in range(n):
    a,b,c=map(int,raw_input().split())
    score[c]=(a,b)
for i in range(1000,-1,-1):
    a,b=score[i]
    if (a,b)==(-1,-1):continue
    if country[a]<2:
        print a,b
        ans+=1
        country[a]+=1
    if ans==3:break