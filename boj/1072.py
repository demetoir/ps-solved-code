
import sys


total,wins,games,per=0,0,0,0
while 1:
 try:

    total,wins=map(int,sys.stdin.readline().split())
    per =int(wins/total*100);
    if per >= 99:
        print(-1)
    else :
        if(total*(per+1) - 100*wins)%(99 - per) == 0:
            games = (total*(per+1) - 100*wins)/(99 - per);
        else:
            games = (total*(per+1) - 100*wins)/(99 - per) + 1;
        print(int(games))
 except:
        break






