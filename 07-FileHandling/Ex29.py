import re
f = open("grades.txt","r")
f1 = f.read()
x = re.findall("[0-9].{2}",f1)
c = 0
sum = 0
for i in x:
    sum += float(i)
    c += 1
print(sum/c)


    