from itertools import combinations
for i in combinations([int(input())for i in range(9)],7):
    if sum(i)==100:
       t=list(i);t.sort()
       for i in range(7):print(t[i])