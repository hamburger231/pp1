f = open('countries.txt','r')
line = 0
for i in f:
    line += 1
    print(f'{line}. {i}',end="")
f.close()