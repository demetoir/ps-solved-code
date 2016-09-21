a,b=map(int,raw_input().split())
def f(a):
	b=""
	for i in list(reversed(str(a))):b+=i
	return int(b)
print f(f(a)+f(b))

