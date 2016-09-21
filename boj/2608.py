t=[['M',1000],['CM',900],['D',500],['CD',400],['C',100],['XC',90],['L',50],['XL',40],['X',10],['IX',9],['V',5],['IV',4],['I',1]]
a=input()
b=input()
ans=0
for i in range(1,4000):
    s='';n=i
    for p in t:
        while i-p[1]>=0:i-=p[1];s+=p[0]
    if a==s:a=n
    if b==s:b=n
    if type(a) is int and type(b) is int:ans=a+b
    if ans==n:print(n);print(s)