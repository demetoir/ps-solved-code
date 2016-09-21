
n=input()
while 1:
    a=input()
    if a==0:break
    if a%n==0:
        print a,"is a multiple of "+str(n)+"."
    else:
        print a,"is NOT a multiple of "+str(n)+"."
    