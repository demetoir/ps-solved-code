for T in range(3):

    s=raw_input()
    last=s[0]
    cur=1
    ans=1
    for c in s[1:]:
        if last==c:
            cur+=1
        else:
            ans=max(ans,cur)
            cur=1
            last=c
    ans=max(ans,cur)
    print ans
