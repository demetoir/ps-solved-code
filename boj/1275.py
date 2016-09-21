import sys
import Queue
try:
	import testcase
	stream=testcase.stream()

except:
	stream=sys.stdin

Q=Queue.deque()
for line in stream:
    Q+=list(map(int,line.split()))

pop=Q.popleft
  
n,q=pop(),pop()
l=[]
for i in range(n):
    l+=[Q.popleft()]
  
 
m=2**17
  
  
class segtree:
    tree=[]
    def __init__(self,n,array):
  
        self.tree=[0]*(m*2+10)
        for i in range(n):
            self.update(i,array[i])
  
    def update(self,index,newval):
        return self.up(index,newval,1,0,m-1)
  
    def up(self,index,newval,node,L,R):
  
        if index<L or R<index:return self.tree[node]
  
        if L==R:
            self.tree[node]=newval
            return self.tree[node]
  
        mid=(L+R)//2
        self.tree[node]=self.up(index,newval,node*2,L,mid)+self.up(index,newval,node*2+1,mid+1,R)
        return self.tree[node]
  
  
  
    def query(self,a,b):
        return self.sum(a,b,1,0,m-1)
  
    def sum(self,a,b,node,L,R):
        if b<L or R<a:return 0
        if a<=L and R<=b :return self.tree[node]
  
        mid=(L+R)//2
        return self.sum(a,b,node*2,L,mid)+self.sum(a,b,node*2+1,mid+1,R)
  
  
  
  
seg=segtree(n,l)
  
  
for i in range(q):
  
    x,y,a,b=pop(),pop(),pop(),pop()
    if x>y:
        x,y=y,x
    print seg.query(x-1,y-1)
    seg.update(a-1,b)