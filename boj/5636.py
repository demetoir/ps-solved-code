seive=[0]+[0]+[1]*100009
for i in range(2,100000+1):
   if seive[i]==0:continue
   for i in range(i*i,100000+1,i):
       seive[i]=0
"""
print(list(range(100)))
print(seive[:100])
"""
while 1:
    s=raw_input()
    if s=="0":
        break
    ans=[]
    for i in range(len(s)):
        c=0
        for j in range(i,len(s)):
            c=c*10+int(s[j])
            #print(c)
            if c>100000:break
            if seive[c]==1:
                ans+=[c]

    print(max(ans))