import Queue
 
for T in range(input()):
    s=raw_input()
    stack=Queue.deque()
    ans="YES"
    for i in range(len(s)):
        if s[i]=="(":
            stack.append("(")
        else:
            if len(stack)==0:
                ans="NO"
                break
            p=stack.pop()
            if p==")":
                ans="NO"
                break
    if len(stack)>0:
         ans="NO"
 
    print ans