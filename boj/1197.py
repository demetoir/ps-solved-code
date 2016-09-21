import sys
sys.setrecursionlimit(10010)
"""
n=int(input())
m=int(input())
"""
n,m=map(int,input().split())

l=[]
for i in range(m):l+=[list(map(int,sys.stdin.readline().split()))]

l.sort(key=lambda a:a[2])

parent=[i for i in range(n+1)]
rank=[0]*(n+1)

def find(n):
    global parent
    if parent[n]==n:return n
    parent[n]=find(parent[n])
    return parent[n]



def merge(a,b):
    global parent,rank
    if rank[a]<rank[b]:parent[a]=b
    elif rank[a]>rank[b]:parent[b]=a
    else:
        parent[a]=b
        rank[a]+=1

def Kruscal(l,n,m):
    global parent
    s=[]
    count=0
    cost=0
    for a,b,c in l:
        if count==n-1:break
        A,B=find(a),find(b)
        if A==B:continue
        #merge(A,B)
        parent[A]=B
        cost+=c
        count+=1
    return cost

print(Kruscal(l,n,m))