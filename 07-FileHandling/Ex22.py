import random


f = open('randint.txt',"w")
for i in range(1,51):
    f.write(str(random.randint(100,1000))+"\n")