import sys
l=[]
for T in range(int(raw_input())):
    l+=[int(sys.stdin.readline())]
l.sort()
for i in l:
    sys.stdout.write(str(i)+"\n") 
    