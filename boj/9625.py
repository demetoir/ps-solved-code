s={0:0,1:1}
def l(n):
    if n not in s:s[n]=l(n-1)+l(n-2)
    return s[n]
c=int(input())
print(l(c-1),l(c))