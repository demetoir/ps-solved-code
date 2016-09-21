import sys


n,m=map(int,raw_input().split())
size=2**20
tree=[0]*(size*2)
index,val=0,0

def set(a,b,node):
    
    if index<a or b<index:
        return tree[node]
    
    if a==b:

        tree[node]=val

        return  tree[node]
    mid=(a+b)//2
 
    tree[node]=set(a,mid,node*2)+set(mid+1,b,node*2+1)
    return tree[node]
 
l,r=0,0
def get(a,b,node):
    
    if r<a or b<l:
        return 0
    if l<=a and b<=r:
        return tree[node]
    mid=(a+b)/2
    return get(a,mid,node*2)+get(mid+1,b,node*2+1)


for i in range(m):
    p,q,r=map(int,sys.stdin.readline().split())
    
    if p==0:
        l,r=min(q,r)-1,max(q,r)-1
        sys.stdout.write( str(get(0,size-1,1))+"\n") 
    else:
        index,val=q-1,r
        set(0,size-1,1)

        
    