a,b,c = map(int, raw_input().split())

ansval = 1234567
ans = 0
for i in range(1,101):
    # if(i == a or i == b or i == c): continue
    val = abs(a - i) + abs(b-i) + abs(c-i)
    if(val<ansval):
        ans = i
        ansval = val

print ansval