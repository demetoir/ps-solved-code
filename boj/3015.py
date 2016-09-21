import sys
n=input()
stack=[(input(),1)]
ans=0
for i in range(1,n):
    cur=int(sys.stdin.readline())
    #print stack
    while len(stack)>0:
        val,number=stack[len(stack)-1]
        if val>cur:break
        elif val==cur:
            ans+=number
            stack.pop()
            break
        stack.pop()
        ans+=number

    if len(stack)>0:
            ans+=1

    if cur == val:
        stack+=[(cur,number+1)]
    else:
        stack+=[(cur,1)]
    #print stack
    #print ans
    #print


print ans