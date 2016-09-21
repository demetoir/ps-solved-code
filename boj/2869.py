import math
a,b,V=map(float,raw_input().split())
n=math.ceil((V-a)/(a-b))

print int(n)+1