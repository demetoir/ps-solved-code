import Queue
q=Queue.Queue()
n,c=map(int,raw_input().split())
l=[str(i) for i in range(1,n+1)]
ans=[]
i=0
while l!=[]:
	i=(i+c-1)%len(l)
	a=l[i]
	ans+=[a]
	l.remove(a)
print "<"+", ".join(ans)+">"