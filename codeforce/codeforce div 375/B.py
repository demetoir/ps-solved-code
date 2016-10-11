raw_input()
s= raw_input()
c=""
ans1 = 0;
ans2 = 0;
flag = False
for i in range(len(s)):
    if flag == False :
        if s[i] == '(':
            flag = True
            ans1 = max(ans1,len(c))
            c=""
            continue
        if s[i] == '_':
            ans1 = max(ans1,len(c))
            c= ""
            continue

        c+=s[i]

    else:
        if s[i] == ')':
            flag = False
            if len(c):
                ans2+=1;
            c = ''
            continue
        if s[i] == '_':
            if len(c):
                ans2+=1;
            c = ''
            continue
        c+= s[i]

ans1 = max(ans1,len(c))
print ans1,ans2
