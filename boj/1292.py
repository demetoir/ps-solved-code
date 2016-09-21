l=[]
for i in range(46):l+=[i]*i
a,b=map(int,input().split());print(sum(l[a-1:b]))