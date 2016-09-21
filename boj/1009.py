s=[[10],[1],[6,2,4,8],[1,3,9,7],[6,4],[5],[6],[1,7,9,3],[6,8,4,2],[1,9]]
for i in range(int(input())):
    a,b=map(int,input().split())
    print(s[a%10][b%len(s[a%10])])
