import re
x = []
f = open("meatandfish.txt","r")
f1 = f.readlines()
for i in f1:
    x.append(re.fullmatch("[a-zA-Z0-9]{6}",i))

print(x)
