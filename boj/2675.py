for T in range(int(raw_input())):
    r,s=raw_input().split()
    ans=""
    R=int(r)
    for c in s:
        ans+=c*R
    print ans