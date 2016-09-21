memo=0
INF=98765432100000000
err=0
h,c=0,0

def get():
	for s in range(h):
		for e in range(s+2,h):
			for i in range(s+1,e):
				a=l[i]
				b=l[s]+float((l[e]-l[s]))*(i-s)/float((e-s))
				if a>b:err[s][e]+=a-b
				else:err[s][e]+=b-a

def f(n,p):

	if  p==1:
		memo[n][p]=err[0][n]
		return memo[n][p]
	ret=memo[n][p]
	if memo[n][p]<INF:
		return memo[n][p]
	ret-=1
	for i in range(0,n):
		a=err[i][n]+f(i,p-1)
		if ret>a:ret=a

	memo[n][p]=ret
	return ret


for t in range(input()):
	h,c=map(int,raw_input().split())
	l=list(map(int,raw_input().split()))

	memo=[[INF]*(c+1) for i in range(h+1)]
	err=[[0.0]*(h+1) for i in range(h+1)]

	get()
	ans=float(f(h-1,c-1))/float(h)
	print ("%0.4f"%(ans))


##recursive
"""
memo=0
INF=98765432100000000
err=0
h,c=0,0

def get():
    for s in range(h):
        for e in range(s+2,h):
            for i in range(s+1,e):
                a=l[i]
                b=l[s]+float((l[e]-l[s]))*(i-s)/float((e-s))
                if a>b:err[s][e]+=a-b
                else:err[s][e]+=b-a

def f():
    global h,c,memo

    for i in range(h):
        for j in range(c):
            if i==0:
                memo[i][j]=0
            else:
                memo[i][j]=INF
    for i in range(1,h):
        for j in range(2,c+1):
            for k in range(i):
                a=memo[k][j-1]+err[k][i]
                if a<memo[i][j]:
                    memo[i][j]=a



for t in range(input()):
    h,c=map(int,raw_input().split())
    l=list(map(int,raw_input().split()))

    memo=[[INF]*(c+1) for i in range(h+1)]
    err=[[0.0]*(h+1) for i in range(h+1)]

    get()
    f()

    ans=float(memo[h-1][c])/float(h)
    print ("%0.4f"%(ans))

"""