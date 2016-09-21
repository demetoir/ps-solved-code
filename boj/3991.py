__author__ = 'SLAVE2'
h,w,c=map(int,raw_input().split())
l=map(int,raw_input().split())
ans=""
for i in range(c):

    ans+=str(i+1)*l[i]
for j in range(h):
    if j%2==0:
        print ans[j*w:j*w+w]
    else:
        print ans[j*w+w-1:j*w-1:-1]
