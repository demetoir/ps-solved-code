board=[]
memo={}
def incode(inlist):
    a=0
    #print inlist
    for i in range(len(inlist)):
        a*=100
        x,y=inlist[i]
        a+=x*5+y
    return a



for i in range(5):
    s=raw_input()
    for j in range(5):
        if s[j]=="*":
            board+=[(i,j)]
n=len(board)
#print board
number=incode(board)

def istogether(B):
    check=[False]*n
    q=Queue.Queue()
    q.put(B[0])
    check[0]=True
    number=1

    while not q.empty():
        x,y=q.get()
        next=[]
        if x-1>=0:next+=[(x-1,y)]
        if x+1<5:next+=[(x+1,y)]
        if y-1>=0:next+=[(x,y-1)]
        if y+1<5:next+=[(x,y+1)]
        for a,b in next:
            if (a,b) in B:
                index=B.index((a,b))
                if check[index]==False:
                    check[index]=True
                    number+=1
                    q.put((a,b))

    if number==n: return True
    else:return False

import Queue
Q=Queue.Queue()
Q.put(board)
memo[number]=0
import sys
while not Q.empty():
    cur=Q.get()
    code=incode(cur)
    cost=memo[code]

    if istogether(cur):
        ans=cost
        print ans
        break
    for i in range(len(cur)):
        x,y=cur[i]
        can=[]

        if x-1>=0 and (x-1,y) not in cur:can+=[(x-1,y)]
        if x+1<5 and (x+1,y) not in cur:can+=[(x+1,y)]
        if y-1>=0 and (x,y-1) not in cur:can+=[(x,y-1)]
        if y+1<5 and (x,y+1) not in cur:can+=[(x,y+1)]

        for a,b in can:
            next=cur[:]
            next[i]=(a,b)
            nextcode=incode(next)
            if nextcode not in memo:
                memo[nextcode]=cost+1
                Q.put(next)




