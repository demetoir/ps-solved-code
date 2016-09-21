ans=input()
while 1:
    a=raw_input()
    if a=="+":
        b=input()
        ans+=b
    elif a=="*":
        b=input()
        ans*=b
    elif a=="-":
        b=input()
        ans-=b
    elif a=="/":
        b=input()
        ans/=b
    elif a=="=":break

print ans