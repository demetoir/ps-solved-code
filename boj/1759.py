l,c=map(int,raw_input().split())
char=list(raw_input().split())

char.sort()

moum=["a","e","i","o","u"]
def f(s,i,m,j):
	if i==c:
		if m>=1 and j>=2 and m+j==l:print s
		return
	if char[i] in moum:	f(s+char[i],i+1,m+1,j)
	else:f(s+char[i],i+1,m,j+1)
	f(s,i+1,m,j)

f("",0,0,0)
