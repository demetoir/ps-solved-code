n=input()
l=map(int,raw_input().split())
ans=[]
for i in range(n-1,-1,-1):ans=ans[:l[i]]+[i+1]+ans[l[i]:]
print " ".join(map(str,ans))