l,x,y=map(int,raw_input().split())
a=((l**2*x**2)/(x**2+y**2))**0.5
b=((l**2*y**2)/(x**2+y**2))**0.5
print int(a),int(b)