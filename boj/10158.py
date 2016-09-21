w,h=map(int,raw_input().split())
p,q=map(int,raw_input().split())
t=int(input())
hor=[i for i in range(w)]+[i for i in range(w,0,-1)]
ver=[i for i in range(h)]+[i for i in range(h,0,-1)]
print hor[(t+p)%(2*w)],ver[(t+q)%(2*h)]
