for i in range(int(input())):
 l=[1]*26;s=2015
 for j in input():s-=l[ord(j)-65]*ord(j);l[ord(j)-65]=0
 print(s)