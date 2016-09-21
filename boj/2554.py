d="6126444846";
w=lambda n:(int((int(d[n%10])*(1+5*(int(n//10!=0)))*w(n//5))*(2**(4*int((n//5)!=0)-(n//5)%4))))%10 if n>0 else 1
;print(a(int(input())))