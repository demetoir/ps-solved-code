s=raw_input()
a,b=0,0
for i in range(len(s)-2):
    if s[i:i+3]=="JOI":a+=1
    if s[i:i+3]=="IOI":b+=1
print a
print b