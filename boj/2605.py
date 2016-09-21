input();l=list(map(int,input().split()));a=[]
for i in range(len(l)):a.insert(l[i],str(i+1))
a.reverse();print(" ".join(a))