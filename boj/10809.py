s=raw_input()
ans=[]
for i in range(26):
    if chr(97+i)in s:ans+=[s.index(chr(i+97))]
    else:ans+=[-1]
print " ".join(map(str,ans))