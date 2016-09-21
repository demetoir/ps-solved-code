
for T in range(input()):
    n,k,t,m=map(int,raw_input().split())
    score=[[0]*(k+1)for i in range(n+1)]
    lastsubmit=[0]*(n+1)
    submitnumber=[0]*(n+1)
    for log in range(m):
        i,j,s=map(int,raw_input().split())
        submitnumber[i]+=1
        lastsubmit[i]=log
        score[i][j]=max(s,score[i][j])
    ans=1
    for i in range(1,n+1):
        if i==t:continue
        if sum(score[i])>sum(score[t]):
            ans+=1
        elif sum(score[i])==sum(score[t]):            
            if submitnumber[i]<submitnumber[t]:
                ans+=1
            elif submitnumber[i]==submitnumber[t]:
                if lastsubmit[i]<lastsubmit[t]:
                    ans+=1
    print ans
                
                
                
                
                
                