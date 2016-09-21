def nextval(n):
    a=0
    while n>0:
        a+=(n%10)**2
        n=n//10
    return a

while 1:
    a,b=map(int,raw_input().split())
    if (a,b)==(0,0):
        break
    A=[a]
    B=[b]
    while 1:
        post=nextval(a)
        if post in A:
            break
        a=post
        A+=[a]


    while 1:
        post=nextval(b)
        if post in B:
            break
        b=post
        B+=[b]
    """
    print(A)
    print(B)
    """

    ans=987654321
    for i in A:
        if i in B:
            ans=min(ans,A.index(i)+B.index(i)+2)
    if ans==987654321:ans=0
    print A[0],B[0],ans
