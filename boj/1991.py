d={}
for i in range(int(input())):
    s=input();d[s[0]]=s[2],s[4]
pre=""
cur=""
post=""
def r(n):
    global pre,cur,post,d
    if n==".":return
    pre+=n
    r(d[n][0])
    cur+=n
    r(d[n][1])
    post+=n
r("A")
print(pre)
print(cur)
print(post)