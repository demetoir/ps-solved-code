import sys

class Node:
	def __init__(self,data,pre=None,post=None):
		self.data=data
		self.pre=pre
		self.post=post


cur=Node(None)

for c in raw_input():
	new=Node(c)
	cur.post=new
	new.pre=cur
	cur=new

for i in range(input()):
	a=sys.stdin.readline()

	if a[0]=="L" and cur.pre!=None:
		cur=cur.pre

	elif a[0]=="D" and cur.post!=None:
		cur=cur.post

	elif a[0]=="B" and cur.pre!=None:

		target=cur.post
		cur=cur.pre

		cur.post=target
		if target!=None:
			target.pre=cur

	elif a[0]=="P":
		a=a[2]
		new=Node(a)

		nextnode=cur.post
		new.pre=cur
		new.post=nextnode
		cur.post=new
		if nextnode!=None:
			nextnode.pre=new
		cur=new

	#print cur.data,id(cur),id(cur.post),id(cur.pre)



a=cur
while a.data!=None:
	a=a.pre

a=a.post
l=[]
while a:
	l+=[a.data]
	a=a.post
print "".join(l)
