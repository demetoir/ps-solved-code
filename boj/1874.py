import queue
import sys

target=[]
squence=[]
i=1

stack=queue.deque()
stack.append(-1)
for n in range(int(input())):
    target+=[int(sys.stdin.readline())]

for i in target:
    top=stack.pop()
    if i == top:
        squence+=["-"]
        continue

    stack.append(top)
    if i<i:
        squence=["NO"]
        break
    else:
        for c in range(i,i+1):
            stack.append(c)
            squence+=["+"]
        i=i+1
        stack.pop()
        squence+=["-"]

print("\n".join(squence))
