m=2**19
class segtree:
	tree=[]
	def __init__(self,n):

		self.tree=[0]*(m*2+10)
		for i in range(n):
			self.update(i,1)

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



import sys
n=input()
l=[]
sort=[]
for i in range(n):
	a=int(sys.stdin.readline())
	l+=[a]
	sort+=[(a,i)]



sort.sort(key=lambda a:(a[0],a[1]))



seg=segtree(n)
ans =0
for val,index in sort:
	out=seg.query(0,index-1)
	#print val,index,out
	ans=max(out+1,ans)
	seg.update(index,0)
print ans







