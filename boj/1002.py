#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      YUJUN
#
# Created:     24-02-2014
# Copyright:   (c) YUJUN 2014
# Licence:     <your licence>
'''
6
0 0 1 0 5 1
0 0 1 0 2 1
0 0 2 0 1 2
0 0 1 0 0 1
0 0 1 0 0 2
1 0 1 2 0 2

'''
#-------------------------------------------------------------------------------
import sys,math
def main():
    g=""
    for i in range(int(sys.stdin.readline())):
        x,y,r,a,b,c = map(int,sys.stdin.readline().split())
        s=math.sqrt((x-a)**2+(y-b)**2)
        if s==0:
            if r==c:g+="-1\n"
            else:g+="0\n"
        else:
            if max(r,c)>s:
                if s+ min(r,c)==max(r,c):g+="1\n"
                elif min(r,c)+s>max(r,c):g+="2\n"
                else:g+="0\n"
            else:
                if s>c+r:g+="0\n"
                elif s<c+r:g+="2\n"
                else:g+="1\n"
    print(g)
    pass
if __name__ == '__main__':
    main()
