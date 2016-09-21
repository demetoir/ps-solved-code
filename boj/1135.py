n,l=int(input()),list(map(int,input().split()))
def r(i):
 q=[]
 for k in range(n):
  if l[k]==i:q+=[r(k)]
 q.sort(reverse=1)
 for k in range(len(q)):q[k]+=k+1
 return max(q+[0])
print(r(0))