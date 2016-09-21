s=raw_input()
ans=[-1]*26
for i in range(26):
    ans[i]=s.count(chr(i+97))
print " ".join(map(str,ans))