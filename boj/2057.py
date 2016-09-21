### if n==0  answer is "NO"

fac=[1]
for i in range(1,25+1):
    fac+=[fac[i-1]*i]

def findfac(n,s,a):
    #print(s)

    if a==s:
        print("YES")
        exit()
    if fac[n]>a:
        return

    if s+fac[n]<=a:
       findfac(n+1,s+fac[n],a)
    if s<=a:
       findfac(n+1,s,a)


a=int(input())
if a>0:
	findfac(0,0,a)
print("NO")
