f = open("studentslist.txt","r")
fr = f.readlines()
for i in fr:
    x = i.split(',')
    if x[2] != "age"and int(x[2]) > 30:
        print(f'{x[0]}   {x[1]}     {x[4]}',end="")
f.close()