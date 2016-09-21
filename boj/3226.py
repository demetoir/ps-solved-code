ans=0
for n in range(input()):
    start,d=raw_input().split()
    h,m=start.split(":")
    h,m,d=map(int,[h,m,d])

    for i in range(d):
        hh=(h+(m+i)//60)%24
        mm=(m+i)%60
        if 7<=hh and hh<19:ans+=10            
        else:ans+=5

print ans