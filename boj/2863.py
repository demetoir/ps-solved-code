﻿s=input()+" "+input();a,b,c,d=map(int,s.split());t=[a/c+b/d,c/d+a/b,d/b+c/a,b/a+d/c];print(t.index(max(t)))