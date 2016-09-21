###must use c++
"""
memo=[[0]*(2**15+2)for i in range(5)]
memo[0][0]=1
square_list=[]
for i in range(1,2**15+1):
    if i*i>2**15:break
    square_list+=[i*i]
m=2**15
for square in square_list:
    for number in range(1,5):
        for i in range(square,m+1):
            memo[number][i]+=memo[number-1][i-square]
"""

def f(n):
    a=0
    for i in range(256+1):
        for j in range(i+1):
            for k in range(j+1):
                t=n-i*i-j*j-k*k
                if t<0:break
                root=int( t**0.5)
                if root>=i and root*root==t: a+=1
    return a




while 1 :
    n=int(input())
    if n==0:break
    """
    total=0

    for i in range(1,5):
        total+=memo[i][n]

    print(total)
    """
    print(f(n))


