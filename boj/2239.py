vertical=[[False]*10for i in range(10)]
horizon=[[False]*10for i in range(10)]
mini=[[False]*10 for i in range(10)]

sudoku=[]
for j in range(9):
	s=raw_input()
	l=[]
	for i in range(9):
		val=int(s[i])
		l+=[val]
		if val>0:
			vertical[i][val]=True
			horizon[j][val]=True
			mini[(i//3)*3+(j//3)][val]=True
	sudoku+=[l]

end=False
def f(x,y):

	global end

	if end:return

	if y==9:
		end=True
		for line in sudoku:print "".join(str(i)for i in line)
		return


	if sudoku[y][x]>0:
		f((x+1)%9,y+(x+1)//9)
		return

	for i in range(1,10):
		if horizon[y][i]:continue
		if vertical[x][i]:continue
		if mini[(x//3)*3+(y//3)][i]:continue

		sudoku[y][x]=i
		horizon[y][i]=True
		vertical[x][i]=True
		mini[(x//3)*3+(y//3)][i]=True

		f((x+1)%9,y+(x+1)//9)

		sudoku[y][x]=0
		horizon[y][i]=False
		vertical[x][i]=False
		mini[(x//3)*3+(y//3)][i]=False

	return

f(0,0)
#print end

