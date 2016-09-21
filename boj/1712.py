a,b,c=map(int,raw_input().split())
if b>=c:
    print -1
    exit()
x=a//(c-b) + 1
print x

