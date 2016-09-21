l=["TTT","TTH","THT","THH","HTT","HTH","HHT","HHH"]
for T in range(input()):
    s=raw_input()
    ans=[0]*8
    for i in range(40-2):
        for j in range(8):
            p=l[j]
            if s[i:i+3]==p:
                ans[j]+=1
    print " ".join(map(str,ans))
