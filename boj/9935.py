
s=raw_input()
p=raw_input()
a=s
while 1:
    s=s.replace(p,"")
    if a==s:break
    a=s
if s=="":print "FRULA"
else:print s