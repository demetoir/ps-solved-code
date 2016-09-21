l=""
ans=""
while 1:
	a=raw_input()
	l+=" "+a
	if "E-N-D" in a: break
t=""

for c in l[:-5]:
	if c.isalpha() or c=="-":
		t+=c
	else:
		if len(t)>len(ans):
			ans=t
		t=""
if len(t)>len(ans):
			ans=t
print ans.lower()