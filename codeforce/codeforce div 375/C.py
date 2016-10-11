true =  True
false = False


n,m = map(int, raw_input().split())
A = map(int, raw_input().split())
ans = 0
cnt = [0]*4321
level = n//m
for i in range(n):
    if A[i] <= m:
        cnt[A[i]]+=1

for i in range(1,m+1):
    while cnt[i] < level:
        index = -1
        val = -1
        for j in range(n):
            if A[j] > m:
                index = j
                break

            if cnt[A[j]] > val :
                val = cnt[A[j]]
                index = j
        if A[index] <= m:
            cnt[A[index]] -=1
        A[index] = i
        ans +=1
        cnt[i]+=1

print level, ans
print " ".join(map(str,A))

