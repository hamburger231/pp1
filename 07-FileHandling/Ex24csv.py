import csv
f = open("studentslist.txt","r")
x = csv.reader(f)
for i in x:
    if i[2] != "age"and int(i[2]) > 30:
        print(f'{i[0]}   {i[1]}     {i[4]}')
f.close()