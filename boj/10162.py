t=input()

a=t//300
t-=(t//300)*300

b=t//60
t-=(t//60)*60

c=t//10
t-=(t//10)*10

if t>0:print -1
else:print a,b,c