f = open("numbers.txt",'r')

sum = 0
for i in f:
    sum += int(i)
print(sum)
    