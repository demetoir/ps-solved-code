for i in range(int(input())):
    s=input()
    count=0
    total=0
    for i in s:
        if i=="O":
           count+=1
           total+=count
        else:count=0
    print(total)
