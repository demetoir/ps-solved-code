s=raw_input()


stack=[]
cur=0
mul=1

for i in range(len(s)):
    if s[i].isdigit():
        cur+=1
    if s[i]=="(":
        cur-=1
        stack+=[(cur,mul)]
        cur=0
        mul=int(s[i-1])
    if s[i]==")":
        val,a=stack.pop()
        cur=val + mul*cur
        mul=a
    #print i,s[i],cur,mul
    #print stack

print cur