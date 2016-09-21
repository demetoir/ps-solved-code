import sys

for t in range(3):
    s=0
    for i in range(int(input())):s+=int(sys.stdin.readline())
    if s>0:print("+")
    elif s<0:print("-")
    else:print(0)