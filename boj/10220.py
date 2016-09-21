n=12
l=[0]*n
a=0
def f(k,s):
    global a
    #print k,s,l
    if s>n:
        return
    if k==n :
        if s==n:
            a+=1
            #print l
        return
    for i in range(n):
        l[k]=i
        f(k+1,s+i)
        l[k]=0
        
        

f(0,0)
print a
print "comp"